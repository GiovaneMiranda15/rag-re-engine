"""Índice em SQLite com busca vetorial exata (força bruta em numpy).

Para o tamanho do corpus do TCC (PURE: 79 documentos) a busca exata é rápida e elimina
aproximação de ANN como variável na avaliação.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import numpy as np

from rag_re_engine.models import Chunk, ScoredChunk

SCHEMA = """
CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS chunks (
    chunk_id TEXT PRIMARY KEY,
    doc_id TEXT NOT NULL,
    position INTEGER NOT NULL,
    text TEXT NOT NULL,
    embedding BLOB NOT NULL
);
"""


class SqliteStore:
    def __init__(self, path: Path | str) -> None:
        self.path = str(path)
        self._conn = sqlite3.connect(self.path)
        self._conn.executescript(SCHEMA)
        self._matrix: np.ndarray | None = None
        self._chunks: list[Chunk] = []

    @property
    def embedder_name(self) -> str | None:
        row = self._conn.execute("SELECT value FROM meta WHERE key = 'embedder'").fetchone()
        return row[0] if row else None

    def add(self, chunks: list[Chunk], vectors: np.ndarray, embedder_name: str) -> None:
        current = self.embedder_name
        if current and current != embedder_name:
            raise ValueError(f"índice criado com '{current}', não é possível adicionar com '{embedder_name}'")
        with self._conn:
            self._conn.execute("INSERT OR REPLACE INTO meta VALUES ('embedder', ?)", (embedder_name,))
            self._conn.executemany(
                "INSERT OR REPLACE INTO chunks VALUES (?, ?, ?, ?, ?)",
                [
                    (c.chunk_id, c.doc_id, c.position, c.text, v.astype(np.float32).tobytes())
                    for c, v in zip(chunks, vectors, strict=True)
                ],
            )
        self._matrix = None

    def count(self) -> int:
        return self._conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]

    def _load(self) -> None:
        rows = self._conn.execute("SELECT chunk_id, doc_id, position, text, embedding FROM chunks ORDER BY chunk_id").fetchall()
        self._chunks = [Chunk(r[0], r[1], r[2], r[3]) for r in rows]
        self._matrix = np.vstack([np.frombuffer(r[4], dtype=np.float32) for r in rows]) if rows else np.zeros((0, 1))

    def search(self, query_vector: np.ndarray, k: int, exclude: set[str] | None = None) -> list[ScoredChunk]:
        if self._matrix is None:
            self._load()
        if not self._chunks or k <= 0:
            return []
        scores = self._matrix @ query_vector.astype(np.float32)
        order = np.argsort(-scores, kind="stable")
        results: list[ScoredChunk] = []
        for idx in order:
            chunk = self._chunks[idx]
            if exclude and chunk.chunk_id in exclude:
                continue
            results.append(ScoredChunk(chunk, float(scores[idx])))
            if len(results) == k:
                break
        return results

    def close(self) -> None:
        self._conn.close()
