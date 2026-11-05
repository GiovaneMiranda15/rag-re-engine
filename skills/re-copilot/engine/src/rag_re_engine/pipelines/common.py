"""Funções compartilhadas pelos pipelines: conversão para evidência, fusão de rankings e decomposição."""

from __future__ import annotations

from rag_re_engine.llm import LLM, parse_json
from rag_re_engine.models import Evidence, PipelineOutput, ScoredChunk

DECOMPOSE_PROMPT = """Decomponha a consulta de Engenharia de Requisitos abaixo em até {n} subconsultas de busca
curtas e específicas (termos do domínio), uma por subtema. Se ela já for atômica, devolva só ela.

CONSULTA: {query}

Responda SOMENTE com JSON no formato {{"subqueries": ["...", "..."]}}."""


def to_evidence(hit: ScoredChunk, relevance: float | None = None, origin: str = "internal") -> Evidence:
    c = hit.chunk
    return Evidence(c.doc_id, c.chunk_id, c.text, hit.similarity, relevance, origin, c.sistema)


def rrf(rankings: list[list[ScoredChunk]], k: int, c: int = 60) -> list[ScoredChunk]:
    """Reciprocal Rank Fusion: combina rankings sem depender da escala das similaridades."""
    scores: dict[str, float] = {}
    best: dict[str, ScoredChunk] = {}
    for ranking in rankings:
        for pos, hit in enumerate(ranking, start=1):
            cid = hit.chunk.chunk_id
            scores[cid] = scores.get(cid, 0.0) + 1.0 / (c + pos)
            if cid not in best or hit.similarity > best[cid].similarity:
                best[cid] = hit
    return [best[cid] for cid in sorted(scores, key=lambda x: (-scores[x], x))[:k]]


def decompose(llm: LLM, query: str, out: PipelineOutput, max_sub: int = 4) -> list[str]:
    """Subconsultas via LLM; em qualquer falha, a consulta original (e o motivo no trace)."""
    try:
        out.llm_calls += 1
        payload = parse_json(llm.complete(DECOMPOSE_PROMPT.format(n=max_sub, query=query)))
        subs = payload.get("subqueries") if isinstance(payload, dict) else payload
        cleaned = [s.strip() for s in subs if isinstance(s, str) and s.strip()][:max_sub]
        return cleaned or [query]
    except (RuntimeError, ValueError, AttributeError, TypeError) as exc:
        out.trace.append(f"decomposição falhou ({exc}); usando a consulta original")
        return [query]
