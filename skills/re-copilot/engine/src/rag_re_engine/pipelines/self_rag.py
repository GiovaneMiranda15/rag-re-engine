"""Self-RAG — Asai et al., 2024, adaptado.

Ciclo: recupera → julga relevância (ISREL) → redige afirmações a partir das evidências → julga se cada
afirmação é sustentada (ISSUP) → se houver lacunas, refaz a busca e repete.

Adaptações (declarar na metodologia): o original treina um gerador com "reflection tokens"; aqui a
reflexão é feita por prompts separados a um LLM genérico, e a decisão "preciso recuperar?" (Retrieve) é
substituída por sempre recuperar na 1ª iteração. Como o motor entrega evidências, não respostas, o produto
final são as evidências que sustentaram alguma afirmação.
"""

from __future__ import annotations

from dataclasses import dataclass

from rag_re_engine.embeddings import Embedder
from rag_re_engine.llm import LLM, parse_json
from rag_re_engine.models import PipelineOutput, ScoredChunk
from rag_re_engine.pipelines.common import to_evidence
from rag_re_engine.pipelines.corrective import GRADE_PROMPT
from rag_re_engine.store import SqliteStore

CLAIMS_PROMPT = """A partir SOMENTE dos TRECHOS, liste as afirmações que respondem à CONSULTA. Para cada afirmação,
indique os índices dos trechos que a sustentam e avalie o suporte: "total", "parcial" ou "nenhum".
Se algo necessário para responder não estiver nos trechos, descreva em "faltando".

CONSULTA: {query}

TRECHOS:
{items}

Responda SOMENTE com JSON: {{"afirmacoes": [{{"texto": "...", "trechos": [0], "suporte": "total"}}], "faltando": "<consulta de busca ou vazio>"}}."""


@dataclass(frozen=True, slots=True)
class SelfRagConfig:
    k: int = 5
    relevance: float = 0.5
    max_iter: int = 2


class SelfRagPipeline:
    name = "self_rag"

    def __init__(self, store: SqliteStore, embedder: Embedder, llm: LLM, config: SelfRagConfig | None = None) -> None:
        self.store = store
        self.embedder = embedder
        self.llm = llm
        self.config = config or SelfRagConfig()

    def _isrel(self, query: str, hits: list[ScoredChunk], out: PipelineOutput) -> list[float]:
        items = "\n\n".join(f"[{i}] {h.chunk.text}" for i, h in enumerate(hits))
        out.llm_calls += 1
        payload = parse_json(self.llm.complete(GRADE_PROMPT.format(query=query, items=items, n=len(hits))))
        scores = payload.get("scores") if isinstance(payload, dict) else payload
        if not isinstance(scores, list) or len(scores) != len(hits):
            raise ValueError("ISREL com número de notas diferente do número de trechos")
        return [float(s) for s in scores]

    def run(self, query: str) -> PipelineOutput:
        cfg = self.config
        out = PipelineOutput(evidence=[])
        current, seen = query, set()
        kept: list[tuple[ScoredChunk, float]] = []
        for iteration in range(1, cfg.max_iter + 1):
            hits = self.store.search(self.embedder.embed_query(current), cfg.k, exclude=seen)
            seen |= {h.chunk.chunk_id for h in hits}
            out.trace.append(f"iter {iteration}: retrieve '{current[:80]}' -> {len(hits)} chunks")
            if not hits:
                break
            try:
                scores = self._isrel(query, hits, out)
            except (RuntimeError, ValueError, TypeError) as exc:
                out.trace.append(f"ISREL falhou ({exc}); degradando para ranking por similaridade")
                out.evidence = [to_evidence(h) for h, _ in kept] + [to_evidence(h) for h in hits]
                return out
            kept += [(h, s) for h, s in zip(hits, scores) if s >= cfg.relevance]
            out.trace.append(f"iter {iteration}: ISREL {[round(s, 2) for s in scores]}; acumulados {len(kept)}")
            if not kept:
                continue
            try:
                out.llm_calls += 1
                items = "\n\n".join(f"[{i}] {h.chunk.text}" for i, (h, _) in enumerate(kept))
                payload = parse_json(self.llm.complete(CLAIMS_PROMPT.format(query=query, items=items)))
                claims = payload.get("afirmacoes", [])
                supported = {int(i) for c in claims if c.get("suporte") in ("total", "parcial")
                             for i in c.get("trechos", []) if 0 <= int(i) < len(kept)}
                weak = sum(1 for c in claims if c.get("suporte") != "total")
                missing = str(payload.get("faltando") or "").strip()
                out.trace.append(f"iter {iteration}: ISSUP {len(claims)} afirmações, {weak} sem suporte total")
                out.evidence = [to_evidence(kept[i][0], relevance=kept[i][1]) for i in sorted(supported)]
                if not missing and weak == 0:
                    break
                current = missing or current
            except (RuntimeError, ValueError, TypeError, AttributeError) as exc:
                out.trace.append(f"ISSUP falhou ({exc}); usando as evidências relevantes")
                out.evidence = [to_evidence(h, relevance=s) for h, s in kept]
                break
        else:
            out.trace.append("limite de iterações atingido")
        if not out.evidence and kept:
            out.evidence = [to_evidence(h, relevance=s) for h, s in kept]
        out.evidence.sort(key=lambda e: -(e.relevance or 0.0))
        return out
