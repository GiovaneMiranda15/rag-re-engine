"""RAPTOR — Sarthi et al., 2024, adaptado: árvore de resumos e busca "collapsed tree".

`build_raptor` agrupa os chunks de um nível, resume cada grupo com o LLM e repete sobre os resumos. Na
consulta, a busca é feita sobre todos os níveis juntos. Resumos trazem `derived_from`, os trechos originais,
pois é neles que a citação deve se apoiar.

Adaptação (declarar na metodologia): o original usa UMAP + GMM com pertinência suave; aqui é k-means
determinístico (cada chunk em um só grupo), para não acrescentar dependências.
"""

from __future__ import annotations

import math
from concurrent.futures import ThreadPoolExecutor

import numpy as np

from rag_re_engine.embeddings import Embedder
from rag_re_engine.llm import LLM
from rag_re_engine.models import Chunk, Evidence, PipelineOutput
from rag_re_engine.store import SqliteStore

SUMMARY_PROMPT = """Resuma os trechos abaixo de documentos de um projeto em um parágrafo fiel, preservando regras,
valores, atores, sistemas e nomes. Não acrescente nada que não esteja nos trechos.

TRECHOS:
{items}

Responda só com o resumo."""


def kmeans(matrix: np.ndarray, k: int, iterations: int = 20) -> np.ndarray:
    """K-means esférico com inicialização determinística (farthest-first a partir do 1º ponto)."""
    centers = [matrix[0]]
    while len(centers) < k:
        dist = 1 - (matrix @ np.vstack(centers).T).max(axis=1)
        centers.append(matrix[int(np.argmax(dist))])
    c = np.vstack(centers)
    labels = np.zeros(len(matrix), dtype=int)
    for _ in range(iterations):
        new = np.argmax(matrix @ c.T, axis=1)
        if np.array_equal(new, labels) and _ > 0:
            break
        labels = new
        for i in range(k):
            members = matrix[labels == i]
            if len(members):
                center = members.mean(axis=0)
                norm = np.linalg.norm(center)
                c[i] = center / norm if norm else center
    return labels


def build_raptor(
    store: SqliteStore, embedder: Embedder, llm: LLM, cluster_size: int = 5, max_levels: int = 3, max_chars: int = 6000,
    workers: int = 4,
) -> dict:
    """(Re)constrói a árvore. Devolve {nivel: número de resumos}. Um grupo que falha é pulado e contado."""
    store.clear_summaries()
    built: dict[int, int] = {}
    failures = 0
    for level in range(1, max_levels + 1):
        chunks, matrix = store.level_vectors(level - 1)
        if len(chunks) < 2:
            break
        k = max(1, math.ceil(len(chunks) / cluster_size))
        labels = kmeans(matrix, k) if k > 1 else np.zeros(len(chunks), dtype=int)
        new_chunks: list[Chunk] = []
        children: list[tuple[str, str]] = []
        groups = [[c for c, lb in zip(chunks, labels) if lb == label] for label in sorted(set(labels.tolist()))]
        groups = [g for g in groups if len(g) >= 2 or level == 1]

        def summarize(members: list[Chunk]) -> str:
            items = "\n\n".join(f"[{m.doc_id}] {m.text}" for m in members)[:max_chars]
            return llm.complete(SUMMARY_PROMPT.format(items=items)).strip()

        with ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
            futures = [pool.submit(summarize, g) for g in groups]
        for members, future in zip(groups, futures):
            try:
                summary = future.result()
            except RuntimeError:
                failures += 1
                continue
            if not summary:
                failures += 1
                continue
            sistemas = {m.sistema for m in members}
            cid = f"raptor/L{level}/{len(new_chunks)}"
            new_chunks.append(Chunk(cid, f"raptor/L{level}", len(new_chunks), summary,
                                    sistemas.pop() if len(sistemas) == 1 else "", "resumo", level))
            children += [(cid, m.chunk_id) for m in members]
        if not new_chunks:
            break
        store.add(new_chunks, embedder.embed([c.text for c in new_chunks]), embedder.name)
        with store.conn:
            store.conn.executemany("INSERT OR REPLACE INTO raptor_children VALUES (?, ?)", children)
        built[level] = len(new_chunks)
        if len(new_chunks) == 1:
            break
    store.set_meta("raptor_failures", str(failures))
    return {"niveis": built, "falhas": failures}


class RaptorPipeline:
    name = "raptor"

    def __init__(self, store: SqliteStore, embedder: Embedder, k: int = 5) -> None:
        self.store = store
        self.embedder = embedder
        self.k = k

    def run(self, query: str) -> PipelineOutput:
        out = PipelineOutput(evidence=[])
        built = self.store.has_summaries()
        if not built:
            out.trace.append("árvore não construída (rode `build --what raptor`); buscando só nos trechos originais")
        elif self.store.get_meta("derivados_desatualizados") == "1":
            out.trace.append("atenção: fontes reindexadas depois do último `build`; resumos podem estar desatualizados")
        hits = self.store.search(self.embedder.embed_query(query), self.k, all_levels=True)
        for h in hits:
            c = h.chunk
            derived = self.store.children_of(c.chunk_id) if c.nivel > 0 else ()
            out.evidence.append(Evidence(c.doc_id, c.chunk_id, c.text, h.similarity, None,
                                         "summary" if c.nivel > 0 else "internal", c.sistema, derived))
        levels = sorted({h.chunk.nivel for h in hits})
        out.trace.append(f"collapsed tree: top-{self.k}, níveis {levels}")
        return out
