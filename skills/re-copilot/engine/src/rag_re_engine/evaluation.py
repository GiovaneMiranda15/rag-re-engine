"""Avaliação comparativa de estratégias sobre um conjunto de consultas anotadas.

Formato do dataset (JSONL, uma consulta por linha):
    {"id": "Q1", "activity": "analise", "query": "...", "relevant_doc_ids": ["doc.pdf"]}

A relevância é anotada no nível de documento (mais viável de anotar manualmente no PURE).
Métricas por consulta, depois agregadas por média:
- hit: 1 se alguma evidência vem de documento relevante;
- recall: fração dos documentos relevantes cobertos pelas evidências;
- precision: fração das evidências que vêm de documentos relevantes;
- mrr: 1/posição da primeira evidência relevante;
- context_chars: tamanho do contexto entregue ao agente (custo);
- llm_calls e latency_s: custo computacional.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from statistics import mean

from rag_re_engine.embeddings import Embedder
from rag_re_engine.engine import retrieve
from rag_re_engine.llm import LLM
from rag_re_engine.models import EvidencePackage
from rag_re_engine.store import SqliteStore

METRICS = ("hit", "recall", "precision", "mrr", "context_chars", "llm_calls", "latency_s", "degradada")
# Marcas no trace de que a estratégia não rodou de verdade (LLM indisponível, estrutura não construída).
DEGRADED_MARKS = ("falhou", "degradando", "heurística", "não construíd")


@dataclass(frozen=True, slots=True)
class Query:
    id: str
    activity: str
    query: str
    relevant_doc_ids: frozenset[str]


def load_dataset(path: Path) -> list[Query]:
    queries = []
    for n, line in enumerate(Path(path).read_text().splitlines(), start=1):
        if not line.strip():
            continue
        row = json.loads(line)
        missing = {"id", "activity", "query", "relevant_doc_ids"} - row.keys()
        if missing:
            raise ValueError(f"linha {n}: campos ausentes {sorted(missing)}")
        queries.append(Query(row["id"], row["activity"], row["query"], frozenset(row["relevant_doc_ids"])))
    return queries


def score(package: EvidencePackage, relevant: frozenset[str]) -> dict[str, float]:
    # Resumo RAPTOR vale pelos documentos que resume (`derived_from`), não pelo seu doc_id interno.
    per_evidence = [
        {cid.rsplit("#", 1)[0] for cid in e.derived_from} if e.derived_from else {e.doc_id} for e in package.evidence
    ]
    docs = [d for group in per_evidence for d in group]
    hits = [bool(group & relevant) for group in per_evidence]
    first = next((i for i, h in enumerate(hits, start=1) if h), None)
    return {
        "hit": float(any(hits)),
        "recall": len(relevant & set(docs)) / len(relevant) if relevant else 0.0,
        "precision": sum(hits) / len(hits) if hits else 0.0,
        "mrr": 1.0 / first if first else 0.0,
        "context_chars": float(sum(len(e.text) for e in package.evidence)),
        "llm_calls": float(package.llm_calls),
        "latency_s": package.latency_s,
        "degradada": float(any(m in t for t in package.trace for m in DEGRADED_MARKS)),
    }


def evaluate(
    queries: list[Query],
    strategies: list[str],
    store: SqliteStore,
    embedder: Embedder,
    llm: LLM | None,
    k: int = 5,
) -> dict:
    per_query: list[dict] = []
    for q in queries:
        for strategy in strategies:
            package = retrieve(q.query, q.activity, store, embedder, llm, k=k, strategy=strategy)
            per_query.append({"id": q.id, "strategy": strategy, **score(package, q.relevant_doc_ids), "trace": package.trace})
    summary = {
        s: {m: round(mean(r[m] for r in per_query if r["strategy"] == s), 4) for m in METRICS} for s in strategies
    }
    return {"k": k, "embedder": embedder.name, "llm": getattr(llm, "name", None), "n_queries": len(queries),
            "summary": summary, "per_query": per_query}


def to_markdown(report: dict) -> str:
    header = "| Estratégia | " + " | ".join(METRICS) + " |"
    lines = [
        f"# Avaliação — {report['n_queries']} consultas, k={report['k']}, embedder={report['embedder']}, llm={report['llm']}",
        "",
        header,
        "|" + "---|" * (len(METRICS) + 1),
    ]
    for strategy, metrics in report["summary"].items():
        lines.append(f"| {strategy} | " + " | ".join(f"{metrics[m]:g}" for m in METRICS) + " |")
    degraded = {s: m["degradada"] for s, m in report["summary"].items() if m.get("degradada")}
    if degraded:
        lines += ["", f"**ATENÇÃO: resultado não confiável.** Fração de consultas degradadas: {degraded}."]
    return "\n".join(lines) + "\n"
