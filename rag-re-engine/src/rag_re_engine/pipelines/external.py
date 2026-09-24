"""Fontes de "conhecimento externo" acionadas pelo CRAG quando a recuperação é Incorrect/Ambiguous.

No artigo original (Yan et al., 2024) a ação corretiva é uma busca web. Aqui a fonte é
plugável; a implementação padrão (`LocalRequery`) é uma ADAPTAÇÃO: busca de novo no mesmo
corpus com a consulta reescrita, excluindo chunks já avaliados. Isso deve ser declarado
como limitação na metodologia.
"""

from __future__ import annotations

from typing import Protocol

from rag_re_engine.embeddings import Embedder
from rag_re_engine.models import ScoredChunk
from rag_re_engine.store import SqliteStore


class ExternalSource(Protocol):
    name: str

    def search(self, query: str, k: int, exclude: set[str]) -> list[ScoredChunk]: ...


class LocalRequery:
    name = "local_requery"

    def __init__(self, store: SqliteStore, embedder: Embedder) -> None:
        self.store = store
        self.embedder = embedder

    def search(self, query: str, k: int, exclude: set[str]) -> list[ScoredChunk]:
        return self.store.search(self.embedder.embed_query(query), k, exclude=exclude)
