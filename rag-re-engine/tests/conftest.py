"""Fixtures compartilhadas: índice do corpus de exemplo (HashEmbedder) e LLM falso determinístico."""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

from rag_re_engine.embeddings import HashEmbedder
from rag_re_engine.ingest import chunk_text, load_documents
from rag_re_engine.store import SqliteStore

FIXTURES = Path(__file__).parent / "fixtures"


class FakeLLM:
    """Pontua cada trecho `[i] ...` do prompt pela presença de palavras-chave; reescreve consultas de forma fixa."""

    name = "fake"

    def __init__(self, keywords: set[str], rewrite_to: str = "invoice billing", fail: bool = False) -> None:
        self.keywords = keywords
        self.rewrite_to = rewrite_to
        self.fail = fail
        self.calls = 0

    def complete(self, prompt: str) -> str:
        self.calls += 1
        if self.fail:
            raise RuntimeError("LLM indisponível")
        if prompt.startswith("Reescreva"):
            return json.dumps({"query": self.rewrite_to})
        items = re.findall(r"^\[\d+\] (.*)$", prompt, re.M)
        scores = [0.9 if any(k in item.lower() for k in self.keywords) else 0.1 for item in items]
        return f"```json\n{json.dumps({'scores': scores})}\n```"


@pytest.fixture
def embedder() -> HashEmbedder:
    return HashEmbedder()


@pytest.fixture
def store(tmp_path: Path, embedder: HashEmbedder) -> SqliteStore:
    s = SqliteStore(tmp_path / "idx.db")
    docs = load_documents(FIXTURES / "corpus")
    chunks = [c for doc_id, text in docs.items() for c in chunk_text(doc_id, text, max_chars=300, overlap=50)]
    s.add(chunks, embedder.embed([c.text for c in chunks]), embedder.name)
    yield s
    s.close()
