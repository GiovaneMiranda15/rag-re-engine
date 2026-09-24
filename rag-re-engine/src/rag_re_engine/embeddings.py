"""Geradores de embedding. Todos retornam vetores L2-normalizados (cosseno = produto interno)."""

from __future__ import annotations

import hashlib
import re
from typing import Protocol

import numpy as np

DEFAULT_FASTEMBED_MODEL = "BAAI/bge-small-en-v1.5"


class Embedder(Protocol):
    name: str

    def embed(self, texts: list[str]) -> np.ndarray: ...

    def embed_query(self, text: str) -> np.ndarray: ...


def _normalize(matrix: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    return matrix / norms


class HashEmbedder:
    """Bag-of-words com feature hashing. Determinístico e offline: usado em testes e como baseline lexical."""

    def __init__(self, dim: int = 512) -> None:
        self.dim = dim
        self.name = f"hash:{dim}"

    def embed(self, texts: list[str]) -> np.ndarray:
        matrix = np.zeros((len(texts), self.dim), dtype=np.float32)
        for row, text in enumerate(texts):
            for token in re.findall(r"\w+", text.lower()):
                bucket = int(hashlib.md5(token.encode()).hexdigest()[:8], 16) % self.dim
                matrix[row, bucket] += 1.0
        return _normalize(matrix)

    def embed_query(self, text: str) -> np.ndarray:
        return self.embed([text])[0]


class FastEmbedEmbedder:
    """Embeddings semânticos locais via fastembed (ONNX). Requer o extra `embeddings`."""

    def __init__(self, model_name: str = DEFAULT_FASTEMBED_MODEL) -> None:
        try:
            from fastembed import TextEmbedding
        except ImportError as exc:  # pragma: no cover - depende do extra instalado
            raise RuntimeError("fastembed não instalado: rode `uv sync --extra embeddings`.") from exc
        self._model = TextEmbedding(model_name=model_name)
        self.name = f"fastembed:{model_name}"

    def embed(self, texts: list[str]) -> np.ndarray:
        return _normalize(np.array(list(self._model.passage_embed(texts)), dtype=np.float32))

    def embed_query(self, text: str) -> np.ndarray:
        return _normalize(np.array(list(self._model.query_embed([text])), dtype=np.float32))[0]


def get_embedder(spec: str) -> Embedder:
    """`hash`, `hash:<dim>`, `fastembed` ou `fastembed:<modelo>`."""
    kind, _, arg = spec.partition(":")
    if kind == "hash":
        return HashEmbedder(int(arg) if arg else 512)
    if kind == "fastembed":
        return FastEmbedEmbedder(arg or DEFAULT_FASTEMBED_MODEL)
    raise ValueError(f"embedder desconhecido: {spec}")
