"""GraphRAG — Edge et al., 2024, adaptado: grafo de entidades extraído dos documentos.

`build_graph` extrai entidades e relações com o LLM (só de chunks ainda não processados), agrupa em
comunidades e resume cada uma. Na consulta: liga a consulta a entidades (nome + embedding) e a comunidades,
expande no grafo por `hops` e ranqueia os chunks que mencionam as entidades alcançadas.

Adaptações (declarar na metodologia): comunidades por propagação de rótulos em vez de Leiden, sem hierarquia;
a busca entrega evidências (não uma resposta map-reduce). O grafo de **requisitos** do projeto é outro: fica
no modelo da skill e é percorrido por `recop.py impacto`.
"""

from __future__ import annotations

import re
from collections import defaultdict, deque
from concurrent.futures import ThreadPoolExecutor

import numpy as np

from rag_re_engine.embeddings import Embedder
from rag_re_engine.llm import LLM, parse_json
from rag_re_engine.models import Chunk, PipelineOutput, ScoredChunk
from rag_re_engine.pipelines.common import to_evidence
from rag_re_engine.store import SqliteStore

EXTRACT_PROMPT = """Extraia um grafo de conhecimento dos trechos de documentos de um projeto.
Entidades: sistemas, atores, papéis, processos, regras, documentos de negócio, entidades de dados, tabelas e
integrações. Relações: use verbos curtos (aprova, calcula, integra_com, armazena, depende_de...).
Use o nome canônico mais simples e repita-o igual em toda a resposta. Não invente nada.

TRECHOS:
{items}

Responda SOMENTE com JSON:
{{"entidades": [{{"nome": "...", "tipo": "...", "descricao": "...", "trechos": [0]}}],
 "relacoes": [{{"de": "...", "para": "...", "rotulo": "...", "trecho": 0}}]}}"""

COMMUNITY_PROMPT = """Resuma em 2 ou 3 frases o que une as entidades e relações abaixo, em um projeto de software.
Não acrescente nada.

{items}

Responda só com o resumo."""


def _norm(name: str) -> str:
    return " ".join(str(name).strip().lower().split())


def _entity_id(store: SqliteStore, name: str, tipo: str = "", desc: str = "") -> int:
    conn = store.conn
    conn.execute("INSERT OR IGNORE INTO entities (name, type, description) VALUES (?, ?, ?)", (_norm(name), tipo, desc))
    return conn.execute("SELECT id FROM entities WHERE name = ?", (_norm(name),)).fetchone()[0]


def label_propagation(nodes: list[int], edges: list[tuple[int, int]], iterations: int = 10) -> dict[int, int]:
    """Determinística: cada nó adota o rótulo mais frequente entre os vizinhos (empate: menor rótulo)."""
    adj: dict[int, list[int]] = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    labels = {n: n for n in nodes}
    for _ in range(iterations):
        changed = False
        for n in sorted(nodes):
            if not adj[n]:
                continue
            counts: dict[int, int] = defaultdict(int)
            for m in adj[n]:
                counts[labels[m]] += 1
            best = min(counts, key=lambda lb: (-counts[lb], lb))
            if best != labels[n]:
                labels[n], changed = best, True
        if not changed:
            break
    return labels


def build_graph(
    store: SqliteStore, embedder: Embedder, llm: LLM, batch: int = 4, communities: bool = True, workers: int = 4
) -> dict:
    conn = store.conn
    done = {r[0] for r in conn.execute("SELECT chunk_id FROM graph_done")}
    pending = [c for c in store.leaves() if c.chunk_id not in done]
    failures = 0
    parts = [pending[i : i + batch] for i in range(0, len(pending), batch)]

    def extract(part: list[Chunk]) -> dict:
        items = "\n\n".join(f"[{j}] ({c.doc_id}) {c.text}" for j, c in enumerate(part))
        return parse_json(llm.complete(EXTRACT_PROMPT.format(items=items)))

    # O LLM roda em paralelo; o SQLite só é tocado nesta thread.
    with ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
        futures = [pool.submit(extract, part) for part in parts]
    for part, future in zip(parts, futures):
        try:
            payload = future.result()
            with conn:
                for ent in payload.get("entidades", []):
                    eid = _entity_id(store, ent["nome"], str(ent.get("tipo", "")), str(ent.get("descricao", "")))
                    for j in ent.get("trechos", []):
                        if 0 <= int(j) < len(part):
                            conn.execute("INSERT OR IGNORE INTO mentions VALUES (?, ?)", (eid, part[int(j)].chunk_id))
                for rel in payload.get("relacoes", []):
                    j = int(rel.get("trecho", 0))
                    if not 0 <= j < len(part):
                        continue
                    src, dst = _entity_id(store, rel["de"]), _entity_id(store, rel["para"])
                    conn.execute("INSERT OR IGNORE INTO relations VALUES (?, ?, ?, ?)",
                                 (src, dst, str(rel.get("rotulo", "")), part[j].chunk_id))
                    for eid in (src, dst):
                        conn.execute("INSERT OR IGNORE INTO mentions VALUES (?, ?)", (eid, part[j].chunk_id))
                conn.executemany("INSERT OR IGNORE INTO graph_done VALUES (?)", [(c.chunk_id,) for c in part])
        except (RuntimeError, ValueError, KeyError, TypeError, AttributeError):
            failures += 1

    rows = conn.execute("SELECT id, name, description FROM entities WHERE embedding IS NULL").fetchall()
    if rows:
        vectors = embedder.embed([f"{r[1]}: {r[2]}" for r in rows])
        with conn:
            conn.executemany("UPDATE entities SET embedding = ? WHERE id = ?",
                             [(v.astype(np.float32).tobytes(), r[0]) for v, r in zip(vectors, rows)])

    n_communities = _build_communities(store, embedder, llm) if communities else 0
    store.set_meta("graph_failures", str(failures))
    if not failures:
        store.set_meta("derivados_desatualizados", "0")
    return {
        "entidades": conn.execute("SELECT COUNT(*) FROM entities").fetchone()[0],
        "relacoes": conn.execute("SELECT COUNT(*) FROM relations").fetchone()[0],
        "comunidades": n_communities,
        "lotes_com_falha": failures,
        "chunks_processados": len(pending),
    }


def _build_communities(store: SqliteStore, embedder: Embedder, llm: LLM) -> int:
    conn = store.conn
    nodes = [r[0] for r in conn.execute("SELECT id FROM entities")]
    edges = [(r[0], r[1]) for r in conn.execute("SELECT DISTINCT src, dst FROM relations")]
    labels = label_propagation(nodes, edges)
    groups: dict[int, list[int]] = defaultdict(list)
    for node, label in labels.items():
        groups[label].append(node)
    with conn:
        conn.execute("DELETE FROM communities")
        conn.executemany("UPDATE entities SET community = ? WHERE id = ?", [(lb, n) for n, lb in labels.items()])
    names = dict(conn.execute("SELECT id, name FROM entities").fetchall())
    count = 0
    for label, members in groups.items():
        if len(members) < 2:
            continue
        rels = [f"{names[a]} {lb} {names[b]}" for a, lb, b in conn.execute(
            f"SELECT src, label, dst FROM relations WHERE src IN ({','.join('?' * len(members))})", members)]
        text = "Entidades: " + ", ".join(names[m] for m in members) + "\nRelações: " + "; ".join(rels[:40])
        try:
            summary = llm.complete(COMMUNITY_PROMPT.format(items=text)).strip()
        except RuntimeError:
            continue
        vector = embedder.embed([summary or text])[0]
        with conn:
            conn.execute("INSERT OR REPLACE INTO communities VALUES (?, ?, ?)",
                         (label, summary or text, vector.astype(np.float32).tobytes()))
        count += 1
    return count


class GraphRagPipeline:
    name = "graph_rag"

    def __init__(self, store: SqliteStore, embedder: Embedder, k: int = 5, seeds: int = 5, hops: int = 2) -> None:
        self.store = store
        self.embedder = embedder
        self.k = k
        self.seeds = seeds
        self.hops = hops

    def _seed_entities(self, query: str, qv: np.ndarray, out: PipelineOutput) -> dict[int, float]:
        conn = self.store.conn
        rows = conn.execute("SELECT id, name, embedding, community FROM entities WHERE embedding IS NOT NULL").fetchall()
        if not rows:
            return {}
        matrix = np.vstack([np.frombuffer(r[2], dtype=np.float32) for r in rows])
        sims = matrix @ qv.astype(np.float32)
        lowered = _norm(query)
        seeds: dict[int, float] = {}
        for idx in np.argsort(-sims, kind="stable")[: self.seeds]:
            seeds[rows[idx][0]] = float(sims[idx])
        for r, s in zip(rows, sims):
            if len(r[1]) > 2 and re.search(rf"\b{re.escape(r[1])}\b", lowered):
                seeds[r[0]] = max(seeds.get(r[0], 0.0), float(s), 0.9)
        comm = conn.execute("SELECT id, summary, embedding FROM communities").fetchall()
        if comm:
            cm = np.vstack([np.frombuffer(c[2], dtype=np.float32) for c in comm])
            best = int(np.argmax(cm @ qv.astype(np.float32)))
            out.trace.append(f"comunidade mais próxima: {comm[best][1][:120]}")
            for r, s in zip(rows, sims):
                if r[3] == comm[best][0]:
                    seeds.setdefault(r[0], float(s))
        names = {r[0]: r[1] for r in rows}
        out.trace.append("entidades-semente: " + ", ".join(names[e] for e in list(seeds)[:8]))
        return seeds

    def run(self, query: str) -> PipelineOutput:
        out = PipelineOutput(evidence=[])
        conn = self.store.conn
        qv = self.embedder.embed_query(query)
        seeds = self._seed_entities(query, qv, out)
        if not seeds:
            out.trace.append("grafo não construído (rode `build --what graph`); usando similaridade")
            out.evidence = [to_evidence(h) for h in self.store.search(qv, self.k)]
            return out
        if self.store.get_meta("derivados_desatualizados") == "1":
            out.trace.append("atenção: fontes reindexadas depois do último `build`; grafo pode estar desatualizado")

        adj: dict[int, set[int]] = defaultdict(set)
        for a, b in conn.execute("SELECT DISTINCT src, dst FROM relations"):
            adj[a].add(b)
            adj[b].add(a)
        dist = {e: 0 for e in seeds}
        queue = deque(seeds)
        while queue:
            cur = queue.popleft()
            if dist[cur] < self.hops:
                for nxt in adj[cur]:
                    if nxt not in dist:
                        dist[nxt] = dist[cur] + 1
                        queue.append(nxt)
        scores: dict[str, float] = defaultdict(float)
        for eid, d in dist.items():
            weight = max(seeds.get(eid, 0.3), 0.1) / (d + 1)
            for (cid,) in conn.execute("SELECT chunk_id FROM mentions WHERE entity_id = ?", (eid,)):
                scores[cid] += weight
        out.trace.append(f"expansão: {len(dist)} entidades em até {self.hops} saltos; {len(scores)} chunks candidatos")
        ranked = sorted(scores, key=lambda c: (-scores[c], c))
        chunks: list[Chunk] = self.store.get_chunks(ranked[: self.k * 3])[: self.k]
        out.evidence = [to_evidence(ScoredChunk(c, float(scores[c.chunk_id]))) for c in chunks]
        if len(out.evidence) < self.k:  # entidades pouco conectadas: completa com similaridade
            have = {e.chunk_id for e in out.evidence}
            extra = self.store.search(qv, self.k - len(out.evidence), exclude=have)
            out.evidence += [to_evidence(h) for h in extra]
            out.trace.append(f"completado com {len(extra)} chunks por similaridade")
        return out
