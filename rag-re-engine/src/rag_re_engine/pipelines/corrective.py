"""Corrective RAG (CRAG) — Yan et al., 2024, adaptado.

Fluxo:
1. recupera top-k;
2. retrieval evaluator dá uma confiança [0,1] a cada chunk;
3. decide a ação:
   - Correct   (algum chunk >= upper): refina os chunks internos relevantes;
   - Incorrect (todos < lower): descarta e busca na fonte externa com consulta reescrita;
   - Ambiguous (demais casos): combina internos relevantes + fonte externa;
4. knowledge refinement: divide em strips, avalia cada strip e recompõe só o relevante.

Adaptações em relação ao original (declarar na metodologia):
- o evaluator original é um T5-large ajustado; aqui é um LLM via prompt;
- a ação corretiva original é busca web; aqui é a `ExternalSource` configurada.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from enum import Enum

from rag_re_engine.embeddings import Embedder
from rag_re_engine.ingest import split_strips
from rag_re_engine.llm import LLM, parse_json
from rag_re_engine.models import Evidence, PipelineOutput, ScoredChunk
from rag_re_engine.pipelines.external import ExternalSource
from rag_re_engine.store import SqliteStore


class Action(str, Enum):
    CORRECT = "correct"
    INCORRECT = "incorrect"
    AMBIGUOUS = "ambiguous"


@dataclass(frozen=True, slots=True)
class CragConfig:
    k: int = 5
    upper: float = 0.6
    lower: float = 0.3
    strip_threshold: float = 0.5
    max_strips: int = 40


def decide_action(scores: list[float], upper: float, lower: float) -> Action:
    """Regra de decisão do CRAG sobre as confianças do evaluator."""
    if any(s >= upper for s in scores):
        return Action.CORRECT
    if all(s < lower for s in scores):
        return Action.INCORRECT
    return Action.AMBIGUOUS


GRADE_PROMPT = """Você é um avaliador de recuperação para Engenharia de Requisitos.
Para a CONSULTA abaixo, atribua a cada TRECHO uma confiança entre 0 e 1 de que ele contém
informação útil para respondê-la (1 = diretamente relevante, 0 = irrelevante).

CONSULTA: {query}

TRECHOS:
{items}

Responda SOMENTE com JSON no formato {{"scores": [<float>, ...]}} com exatamente {n} valores, na ordem dos trechos."""

REWRITE_PROMPT = """Reescreva a consulta abaixo como uma consulta de busca curta e específica
(palavras-chave e termos técnicos de requisitos), preservando a intenção.

CONSULTA: {query}

Responda SOMENTE com JSON no formato {{"query": "<consulta reescrita>"}}."""


class CorrectiveRagPipeline:
    name = "corrective_rag"

    def __init__(
        self,
        store: SqliteStore,
        embedder: Embedder,
        llm: LLM,
        external: ExternalSource,
        config: CragConfig | None = None,
    ) -> None:
        self.store = store
        self.embedder = embedder
        self.llm = llm
        self.external = external
        self.config = config or CragConfig()

    def run(self, query: str) -> PipelineOutput:
        cfg = self.config
        out = PipelineOutput(evidence=[])
        hits = self.store.search(self.embedder.embed_query(query), cfg.k)
        out.trace.append(f"retrieve: top-{cfg.k} ({len(hits)} chunks)")
        if not hits:
            out.trace.append("índice vazio: nada a avaliar")
            return out

        try:
            scores = self._grade(query, [h.chunk.text for h in hits], out)
        except (RuntimeError, ValueError) as exc:
            # Degradação: sem evaluator, devolve o ranking por similaridade (equivale ao baseline).
            out.trace.append(f"evaluator falhou ({exc}); degradando para ranking por similaridade")
            out.evidence = [Evidence(h.chunk.doc_id, h.chunk.chunk_id, h.chunk.text, h.similarity) for h in hits]
            return out

        action = decide_action(scores, cfg.upper, cfg.lower)
        out.trace.append(f"evaluate: scores={[round(s, 2) for s in scores]} -> {action.value}")

        candidates: list[tuple[ScoredChunk, float | None, str]] = []
        if action in (Action.CORRECT, Action.AMBIGUOUS):
            kept = [(h, s, "internal") for h, s in zip(hits, scores) if s >= cfg.lower]
            candidates += kept
            out.trace.append(f"internal: {len(kept)} chunks mantidos (>= {cfg.lower})")
        if action in (Action.INCORRECT, Action.AMBIGUOUS):
            rewritten = self._rewrite(query, out)
            seen = {h.chunk.chunk_id for h in hits}
            external = self.external.search(rewritten, cfg.k, exclude=seen)
            candidates += [(h, None, "external") for h in external]
            out.trace.append(f"external[{self.external.name}]: '{rewritten}' -> {len(external)} chunks")

        out.evidence = self._refine(query, candidates, out)
        out.trace.append(f"refine: {len(out.evidence)} evidências após filtragem de strips")
        return out

    def _grade(self, query: str, texts: list[str], out: PipelineOutput) -> list[float]:
        items = "\n\n".join(f"[{i}] {t}" for i, t in enumerate(texts))
        out.llm_calls += 1
        payload = parse_json(self.llm.complete(GRADE_PROMPT.format(query=query, items=items, n=len(texts))))
        scores = payload.get("scores") if isinstance(payload, dict) else payload
        if not isinstance(scores, list) or len(scores) != len(texts):
            raise ValueError(f"evaluator devolveu {json.dumps(scores)[:100]} para {len(texts)} trechos")
        return [min(1.0, max(0.0, float(s))) for s in scores]

    def _rewrite(self, query: str, out: PipelineOutput) -> str:
        try:
            out.llm_calls += 1
            payload = parse_json(self.llm.complete(REWRITE_PROMPT.format(query=query)))
            rewritten = payload.get("query") if isinstance(payload, dict) else None
            return rewritten.strip() if isinstance(rewritten, str) and rewritten.strip() else query
        except (RuntimeError, ValueError):
            out.trace.append("rewrite falhou; usando a consulta original")
            return query

    def _refine(
        self, query: str, candidates: list[tuple[ScoredChunk, float | None, str]], out: PipelineOutput
    ) -> list[Evidence]:
        """Decompose-then-recompose: mantém só as strips relevantes de cada chunk candidato."""
        cfg = self.config
        strips: list[tuple[int, str]] = []
        for idx, (hit, _, _) in enumerate(candidates):
            strips += [(idx, s) for s in split_strips(hit.chunk.text)]
        strips = strips[: cfg.max_strips]
        if not strips:
            return []
        try:
            strip_scores = self._grade(query, [s for _, s in strips], out)
        except (RuntimeError, ValueError) as exc:
            out.trace.append(f"refine falhou ({exc}); mantendo chunks inteiros")
            return [
                Evidence(h.chunk.doc_id, h.chunk.chunk_id, h.chunk.text, h.similarity, grade, origin)
                for h, grade, origin in candidates
            ]

        evidence: list[Evidence] = []
        for idx, (hit, grade, origin) in enumerate(candidates):
            kept = [(s, sc) for (i, s), sc in zip(strips, strip_scores) if i == idx and sc >= cfg.strip_threshold]
            if not kept:
                continue
            relevance = grade if grade is not None else max(sc for _, sc in kept)
            evidence.append(
                Evidence(hit.chunk.doc_id, hit.chunk.chunk_id, " ".join(s for s, _ in kept), hit.similarity, relevance, origin)
            )
        evidence.sort(key=lambda e: -(e.relevance or 0.0))
        return evidence
