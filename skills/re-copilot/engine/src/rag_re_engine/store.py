"""Índice em SQLite com busca vetorial exata (força bruta em numpy).

Para corpora de projeto (dezenas a poucos milhares de documentos) a busca exata é rápida e elimina
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
    embedding BLOB NOT NULL,
    sistema TEXT NOT NULL DEFAULT '',
    tipo TEXT NOT NULL DEFAULT '',
    nivel INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS raptor_children (parent_id TEXT NOT NULL, child_id TEXT NOT NULL, PRIMARY KEY (parent_id, child_id));
CREATE TABLE IF NOT EXISTS entities (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    type TEXT NOT NULL DEFAULT '',
    description TEXT NOT NULL DEFAULT '',
    community INTEGER,
    embedding BLOB
);
CREATE TABLE IF NOT EXISTS relations (src INTEGER NOT NULL, dst INTEGER NOT NULL, label TEXT NOT NULL, chunk_id TEXT NOT NULL, PRIMARY KEY (src, dst, label, chunk_id));
CREATE TABLE IF NOT EXISTS mentions (entity_id INTEGER NOT NULL, chunk_id TEXT NOT NULL, PRIMARY KEY (entity_id, chunk_id));
CREATE TABLE IF NOT EXISTS graph_done (chunk_id TEXT PRIMARY KEY);
CREATE TABLE IF NOT EXISTS communities (id INTEGER PRIMARY KEY, summary TEXT NOT NULL, embedding BLOB NOT NULL);
"""


class SqliteStore:
    def __init__(self, path: Path | str, sistemas: set[str] | None = None) -> None:
        """`sistemas` restringe a busca aos chunks desses sistemas (None = todos)."""
        self.path = str(path)
        self.sistemas = sistemas
        self._conn = sqlite3.connect(self.path)
        self._conn.executescript(SCHEMA)
        cols = {r[1] for r in self._conn.execute("PRAGMA table_info(chunks)")}
        for col in ("sistema", "tipo"):  # índices criados antes dos metadados
            if col not in cols:
                self._conn.execute(f"ALTER TABLE chunks ADD COLUMN {col} TEXT NOT NULL DEFAULT ''")
        if "nivel" not in cols:
            self._conn.execute("ALTER TABLE chunks ADD COLUMN nivel INTEGER NOT NULL DEFAULT 0")
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
                "INSERT OR REPLACE INTO chunks (chunk_id, doc_id, position, text, embedding, sistema, tipo, nivel) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                [
                    (c.chunk_id, c.doc_id, c.position, c.text, v.astype(np.float32).tobytes(), c.sistema, c.tipo, c.nivel)
                    for c, v in zip(chunks, vectors, strict=True)
                ],
            )
        self._matrix = None

    def delete_docs(self, doc_ids: list[str]) -> None:
        """Remove os chunks desses documentos (reindexação sem deixar chunks antigos).

        Resumos e grafo derivados deles ficam desatualizados; o aviso sai no trace até o `build`.
        """
        if not doc_ids:
            return
        with self._conn:
            for doc in doc_ids:
                ids = [(r[0],) for r in self._conn.execute("SELECT chunk_id FROM chunks WHERE doc_id = ?", (doc,))]
                self._conn.executemany("DELETE FROM mentions WHERE chunk_id = ?", ids)
                self._conn.executemany("DELETE FROM relations WHERE chunk_id = ?", ids)
                self._conn.executemany("DELETE FROM graph_done WHERE chunk_id = ?", ids)
                if ids:
                    self.set_meta("derivados_desatualizados", "1")
                self._conn.execute("DELETE FROM chunks WHERE doc_id = ?", (doc,))
        self._matrix = None

    def get_meta(self, key: str) -> str | None:
        row = self._conn.execute("SELECT value FROM meta WHERE key = ?", (key,)).fetchone()
        return row[0] if row else None

    def set_meta(self, key: str, value: str) -> None:
        self._conn.execute("INSERT OR REPLACE INTO meta VALUES (?, ?)", (key, value))

    @property
    def conn(self) -> sqlite3.Connection:
        """Acesso às tabelas derivadas (grafo, hierarquia), usado pelos builders."""
        return self._conn

    def leaves(self) -> list[Chunk]:
        rows = self._conn.execute(
            "SELECT chunk_id, doc_id, position, text, sistema, tipo, nivel FROM chunks WHERE nivel = 0 ORDER BY chunk_id"
        ).fetchall()
        return [Chunk(r[0], r[1], r[2], r[3], r[4], r[5], r[6]) for r in rows]

    def level_vectors(self, nivel: int) -> tuple[list[Chunk], np.ndarray]:
        rows = self._conn.execute(
            "SELECT chunk_id, doc_id, position, text, sistema, tipo, nivel, embedding FROM chunks WHERE nivel = ? ORDER BY chunk_id",
            (nivel,),
        ).fetchall()
        chunks = [Chunk(r[0], r[1], r[2], r[3], r[4], r[5], r[6]) for r in rows]
        matrix = np.vstack([np.frombuffer(r[7], dtype=np.float32) for r in rows]) if rows else np.zeros((0, 1))
        return chunks, matrix

    def clear_summaries(self) -> None:
        with self._conn:
            self._conn.execute("DELETE FROM chunks WHERE nivel > 0")
            self._conn.execute("DELETE FROM raptor_children")
        self._matrix = None

    def has_summaries(self) -> bool:
        return self._conn.execute("SELECT 1 FROM chunks WHERE nivel > 0 LIMIT 1").fetchone() is not None

    def children_of(self, chunk_id: str) -> tuple[str, ...]:
        """Trechos originais (nível 0) sob um resumo, descendo a árvore."""
        leaves: list[str] = []
        stack = [chunk_id]
        while stack:
            for (child,) in self._conn.execute("SELECT child_id FROM raptor_children WHERE parent_id = ?", (stack.pop(),)):
                if child.startswith("raptor/"):
                    stack.append(child)
                else:
                    leaves.append(child)
        return tuple(sorted(leaves))

    def get_chunks(self, chunk_ids: list[str]) -> list[Chunk]:
        out = []
        for cid in chunk_ids:
            r = self._conn.execute(
                "SELECT chunk_id, doc_id, position, text, sistema, tipo, nivel FROM chunks WHERE chunk_id = ?", (cid,)
            ).fetchone()
            if r and (self.sistemas is None or r[4] in self.sistemas):
                out.append(Chunk(r[0], r[1], r[2], r[3], r[4], r[5], r[6]))
        return out

    def count(self) -> int:
        return self._conn.execute("SELECT COUNT(*) FROM chunks WHERE nivel = 0").fetchone()[0]

    def _load(self) -> None:
        rows = self._conn.execute(
            "SELECT chunk_id, doc_id, position, text, embedding, sistema, tipo, nivel FROM chunks ORDER BY chunk_id"
        ).fetchall()
        if self.sistemas is not None:
            rows = [r for r in rows if r[5] in self.sistemas]
        self._chunks = [Chunk(r[0], r[1], r[2], r[3], r[5], r[6], r[7]) for r in rows]
        self._matrix = np.vstack([np.frombuffer(r[4], dtype=np.float32) for r in rows]) if rows else np.zeros((0, 1))

    def search(
        self, query_vector: np.ndarray, k: int, exclude: set[str] | None = None, all_levels: bool = False
    ) -> list[ScoredChunk]:
        """Busca exata. Por padrão só em trechos originais; `all_levels` inclui resumos (collapsed tree)."""
        if self._matrix is None:
            self._load()
        if not self._chunks or k <= 0:
            return []
        scores = self._matrix @ query_vector.astype(np.float32)
        order = np.argsort(-scores, kind="stable")
        results: list[ScoredChunk] = []
        for idx in order:
            chunk = self._chunks[idx]
            if (exclude and chunk.chunk_id in exclude) or (chunk.nivel > 0 and not all_levels):
                continue
            results.append(ScoredChunk(chunk, float(scores[idx])))
            if len(results) == k:
                break
        return results

    def close(self) -> None:
        self._conn.close()
