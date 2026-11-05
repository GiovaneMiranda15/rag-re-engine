"""Agentic RAG — agente iterativo que planeja buscas, avalia suficiência e busca o que falta.

Adaptação (declarar na metodologia): o laço é fixo (planejar → buscar → avaliar) com uma só ferramenta
(busca no índice), em vez de um agente ReAct com ferramentas abertas. No uso pela skill, o próprio Claude
Code atua como agente de nível superior (decompõe por sistema e chama o motor).
"""

from __future__ import annotations

from rag_re_engine.embeddings import Embedder
from rag_re_engine.llm import LLM, parse_json
from rag_re_engine.models import PipelineOutput, ScoredChunk
from rag_re_engine.pipelines.common import decompose, rrf, to_evidence
from rag_re_engine.store import SqliteStore

SUFFICIENCY_PROMPT = """Você está levantando requisitos. Os TRECHOS são suficientes para responder à CONSULTA?
Se não, liste até 3 novas buscas para o que falta (atores, regras, dados, integrações, exceções...).

CONSULTA: {query}

TRECHOS:
{items}

Responda SOMENTE com JSON: {{"suficiente": true, "buscas": []}}."""


class AgenticRagPipeline:
    name = "agentic_rag"

    def __init__(self, store: SqliteStore, embedder: Embedder, llm: LLM, k: int = 5, max_rounds: int = 3) -> None:
        self.store = store
        self.embedder = embedder
        self.llm = llm
        self.k = k
        self.max_rounds = max_rounds

    def run(self, query: str) -> PipelineOutput:
        out = PipelineOutput(evidence=[])
        rankings: list[list[ScoredChunk]] = []
        pending = decompose(self.llm, query, out)
        done: set[str] = set()
        for round_no in range(1, self.max_rounds + 1):
            pending = [q for q in pending if q not in done]
            if not pending:
                out.trace.append(f"rodada {round_no}: nada novo a buscar")
                break
            out.trace.append(f"rodada {round_no}: buscas {pending}")
            for sub in pending:
                rankings.append(self.store.search(self.embedder.embed_query(sub), self.k))
                done.add(sub)
            merged = rrf(rankings, self.k * 2)
            if round_no == self.max_rounds or not merged:
                break
            try:
                out.llm_calls += 1
                items = "\n\n".join(f"[{i}] {h.chunk.text}" for i, h in enumerate(merged))
                payload = parse_json(self.llm.complete(SUFFICIENCY_PROMPT.format(query=query, items=items)))
                if payload.get("suficiente"):
                    out.trace.append(f"rodada {round_no}: suficiente")
                    break
                pending = [str(b) for b in payload.get("buscas", [])][:3]
            except (RuntimeError, ValueError, AttributeError) as exc:
                out.trace.append(f"avaliação de suficiência falhou ({exc}); encerrando")
                break
        out.evidence = [to_evidence(h) for h in rrf(rankings, self.k * 2)]
        out.trace.append(f"fusão RRF: {len(out.evidence)} evidências")
        return out
