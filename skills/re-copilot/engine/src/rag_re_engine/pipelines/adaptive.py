"""Adaptive RAG — profundidade da recuperação de acordo com a complexidade da consulta.

Adaptação (declarar na metodologia): a literatura usa classificadores treinados; aqui o roteador é um
LLM via prompt, com heurística determinística se ele falhar. Rotas:
- simples: top-k por similaridade, sem custo de LLM adicional;
- moderada: Corrective RAG (avalia e corrige a recuperação);
- complexa: decomposição em subconsultas, fusão por RRF e filtro do evaluator.
"""

from __future__ import annotations

import re

from rag_re_engine.embeddings import Embedder
from rag_re_engine.llm import LLM, parse_json
from rag_re_engine.models import PipelineOutput
from rag_re_engine.pipelines import Pipeline
from rag_re_engine.pipelines.common import decompose, rrf, to_evidence
from rag_re_engine.pipelines.corrective import GRADE_PROMPT
from rag_re_engine.store import SqliteStore

ROUTES = ("simples", "moderada", "complexa")

CLASSIFY_PROMPT = """Classifique o esforço de recuperação necessário para avaliar a mudança ou consulta de
requisitos abaixo:
- simples: fato pontual, um só item, uma só fonte;
- moderada: precisa conferir mais de uma fonte, mas um só tema;
- complexa: cruza vários temas, sistemas, regras ou tem efeito em cascata.

CONSULTA: {query}

Responda SOMENTE com JSON no formato {{"complexidade": "simples|moderada|complexa", "motivo": "..."}}."""


def heuristic_route(query: str) -> str:
    """Contagem de sinais de múltiplos temas; usada quando o LLM não responde."""
    words = len(re.findall(r"\w+", query))
    connectors = len(re.findall(r"\b(e|ou|além|também|impacto|afeta|todos|entre|sistemas?)\b", query.lower()))
    if words > 30 or connectors >= 4:
        return "complexa"
    if words > 12 or connectors >= 2:
        return "moderada"
    return "simples"


class AdaptiveRagPipeline:
    name = "adaptive_rag"

    def __init__(self, store: SqliteStore, embedder: Embedder, llm: LLM, moderate: Pipeline, k: int = 5) -> None:
        self.store = store
        self.embedder = embedder
        self.llm = llm
        self.moderate = moderate
        self.k = k

    def _route(self, query: str, out: PipelineOutput) -> str:
        try:
            out.llm_calls += 1
            payload = parse_json(self.llm.complete(CLASSIFY_PROMPT.format(query=query)))
            route = str(payload.get("complexidade", "")).strip().lower()
            if route not in ROUTES:
                raise ValueError(f"rota inválida: {route!r}")
            out.trace.append(f"route: {route} ({str(payload.get('motivo', ''))[:120]})")
            return route
        except (RuntimeError, ValueError, AttributeError) as exc:
            route = heuristic_route(query)
            out.trace.append(f"route: {route} (heurística; roteador falhou: {exc})")
            return route

    def run(self, query: str) -> PipelineOutput:
        out = PipelineOutput(evidence=[])
        route = self._route(query, out)
        if route == "simples":
            hits = self.store.search(self.embedder.embed_query(query), self.k)
            out.evidence = [to_evidence(h) for h in hits]
            out.trace.append(f"retrieve: top-{self.k} ({len(hits)} chunks)")
            return out
        if route == "moderada":
            inner = self.moderate.run(query)
            out.evidence, out.llm_calls = inner.evidence, out.llm_calls + inner.llm_calls
            out.trace += inner.trace
            return out

        subs = decompose(self.llm, query, out)
        out.trace.append(f"decompose: {subs}")
        merged = rrf([self.store.search(self.embedder.embed_query(s), self.k) for s in subs], self.k * 2)
        out.evidence = [to_evidence(h) for h in merged]
        if not merged:
            return out
        try:
            out.llm_calls += 1
            items = "\n\n".join(f"[{i}] {h.chunk.text}" for i, h in enumerate(merged))
            payload = parse_json(self.llm.complete(GRADE_PROMPT.format(query=query, items=items, n=len(merged))))
            scores = payload.get("scores") if isinstance(payload, dict) else payload
            if not isinstance(scores, list) or len(scores) != len(merged):
                raise ValueError("número de notas diferente do número de trechos")
            kept = sorted(((h, float(s)) for h, s in zip(merged, scores) if float(s) >= 0.3), key=lambda x: -x[1])
            out.evidence = [to_evidence(h, relevance=s) for h, s in kept]
            out.trace.append(f"filter: {len(kept)}/{len(merged)} mantidos (>= 0.3)")
        except (RuntimeError, ValueError, TypeError) as exc:
            out.trace.append(f"filtro falhou ({exc}); mantendo a fusão por RRF")
        return out
