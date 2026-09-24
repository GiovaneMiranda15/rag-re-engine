"""Baseline (naive RAG): top-k por similaridade, sem avaliação nem correção.

Referência de comparação para as arquiteturas avançadas na avaliação.
"""

from __future__ import annotations

from rag_re_engine.embeddings import Embedder
from rag_re_engine.models import Evidence, PipelineOutput
from rag_re_engine.store import SqliteStore


class BaselinePipeline:
    name = "baseline"

    def __init__(self, store: SqliteStore, embedder: Embedder, k: int = 5) -> None:
        self.store = store
        self.embedder = embedder
        self.k = k

    def run(self, query: str) -> PipelineOutput:
        hits = self.store.search(self.embedder.embed_query(query), self.k)
        evidence = [Evidence(h.chunk.doc_id, h.chunk.chunk_id, h.chunk.text, h.similarity) for h in hits]
        return PipelineOutput(evidence=evidence, trace=[f"retrieve: top-{self.k} por similaridade ({len(hits)} chunks)"])
