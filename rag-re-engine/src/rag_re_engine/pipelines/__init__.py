"""Pipelines RAG. Cada um implementa `Pipeline.run(query) -> PipelineOutput`.

Seguindo a ideia de Modular RAG (Gao et al., 2024), os pipelines compõem os mesmos módulos
(store, embedder, LLM, busca externa) em fluxos diferentes.
"""

from __future__ import annotations

from typing import Protocol

from rag_re_engine.models import PipelineOutput


class Pipeline(Protocol):
    name: str

    def run(self, query: str) -> PipelineOutput: ...
