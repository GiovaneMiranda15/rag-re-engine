"""Interface de linha de comando: `rag-re-engine index | retrieve | context | evaluate`."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from rag_re_advisor.models import Activity, TaskContext

from rag_re_engine.embeddings import get_embedder
from rag_re_engine.engine import PIPELINES, retrieve
from rag_re_engine.evaluation import evaluate, load_dataset, to_markdown
from rag_re_engine.ingest import chunk_text, load_documents
from rag_re_engine.llm import get_llm
from rag_re_engine.models import EvidencePackage
from rag_re_engine.store import SqliteStore


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="rag-re-engine",
        description="Executa a arquitetura RAG recomendada para uma atividade de Engenharia de Requisitos.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    idx = sub.add_parser("index", help="Indexa um diretório de documentos (txt, md, pdf).")
    idx.add_argument("corpus", type=Path)
    idx.add_argument("--db", type=Path, required=True)
    idx.add_argument("--embedder", default="fastembed", help="hash[:dim] | fastembed[:modelo] (default: fastembed)")
    idx.add_argument("--max-chars", type=int, default=1200)
    idx.add_argument("--overlap", type=int, default=200)

    ret = sub.add_parser("retrieve", help="Recupera evidências para uma consulta.")
    ret.add_argument("--db", type=Path, required=True)
    ret.add_argument("--activity", required=True, choices=[a.value for a in Activity])
    ret.add_argument("--query", required=True)
    ret.add_argument("--strategy", choices=sorted(PIPELINES), default=None, help="força uma estratégia (ignora o advisor)")
    ret.add_argument("--llm", default="claude", help="claude[:modelo] | none (default: claude)")
    ret.add_argument("-k", type=int, default=5)
    ret.add_argument("--json", action="store_true")

    ctx = sub.add_parser("context", help="Context provider do agent-system: Task Package no stdin, Evidence Package no stdout.")
    ctx.add_argument("--llm", default="claude")

    ev = sub.add_parser("evaluate", help="Compara estratégias sobre um dataset JSONL anotado.")
    ev.add_argument("--db", type=Path, required=True)
    ev.add_argument("--dataset", type=Path, required=True)
    ev.add_argument("--strategies", default="baseline,corrective_rag")
    ev.add_argument("--llm", default="claude")
    ev.add_argument("-k", type=int, default=5)
    ev.add_argument("--out", type=Path, default=None, help="prefixo dos relatórios (.json e .md)")
    return parser


def _open_store(db: Path) -> tuple[SqliteStore, object]:
    if not db.exists():
        raise SystemExit(f"índice não encontrado: {db} (rode `rag-re-engine index` antes)")
    store = SqliteStore(db)
    if not store.embedder_name:
        raise SystemExit(f"índice vazio: {db}")
    return store, get_embedder(store.embedder_name)


def _llm(spec: str):
    return None if spec == "none" else get_llm(spec)


def _format_human(package: EvidencePackage) -> str:
    lines = [
        f"Atividade: {package.activity} | recomendada: {package.recommended} | executada: {package.strategy}",
        *[f"Nota: {n}" for n in package.notes],
        "Trace:",
        *[f"  - {t}" for t in package.trace],
        f"Evidências ({len(package.evidence)}), {package.llm_calls} chamadas LLM, {package.latency_s:.1f}s:",
    ]
    for i, e in enumerate(package.evidence, start=1):
        rel = f" rel={e.relevance:.2f}" if e.relevance is not None else ""
        lines.append(f"  [{i}] {e.chunk_id} ({e.origin}, sim={e.similarity:.2f}{rel})")
        lines.append(f"      {e.text[:300]}")
    return "\n".join(lines)


def _cmd_index(args: argparse.Namespace) -> int:
    embedder = get_embedder(args.embedder)
    docs = load_documents(args.corpus)
    chunks = [c for doc_id, text in docs.items() for c in chunk_text(doc_id, text, args.max_chars, args.overlap)]
    if not chunks:
        print(f"nenhum documento suportado em {args.corpus}", file=sys.stderr)
        return 1
    store = SqliteStore(args.db)
    batch = 64
    for i in range(0, len(chunks), batch):
        part = chunks[i : i + batch]
        store.add(part, embedder.embed([c.text for c in part]), embedder.name)
    print(f"{len(docs)} documentos, {len(chunks)} chunks indexados em {args.db} ({embedder.name})")
    return 0


def _cmd_retrieve(args: argparse.Namespace) -> int:
    store, embedder = _open_store(args.db)
    package = retrieve(args.query, TaskContext(activity=Activity(args.activity)), store, embedder,
                       _llm(args.llm), k=args.k, strategy=args.strategy)
    print(json.dumps(package.to_dict(), ensure_ascii=False, indent=2) if args.json else _format_human(package))
    return 0


def _cmd_context(args: argparse.Namespace) -> int:
    """Lê `context_request` do Task Package: {activity, db, query?, strategy?, k?}."""
    task = json.load(sys.stdin)
    req = task.get("context_request") or {}
    for key in ("activity", "db"):
        if key not in req:
            print(f"context_request sem '{key}'", file=sys.stderr)
            return 2
    store, embedder = _open_store(Path(req["db"]).expanduser())
    package = retrieve(req.get("query") or task["objective"], TaskContext(activity=Activity(req["activity"])),
                       store, embedder, _llm(args.llm), k=int(req.get("k", 5)), strategy=req.get("strategy"))
    print(json.dumps(package.to_dict(), ensure_ascii=False))
    return 0


def _cmd_evaluate(args: argparse.Namespace) -> int:
    store, embedder = _open_store(args.db)
    strategies = [s.strip() for s in args.strategies.split(",") if s.strip()]
    report = evaluate(load_dataset(args.dataset), strategies, store, embedder, _llm(args.llm), k=args.k)
    markdown = to_markdown(report)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.with_suffix(".json").write_text(json.dumps(report, ensure_ascii=False, indent=2))
        args.out.with_suffix(".md").write_text(markdown)
    print(markdown)
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    handlers = {"index": _cmd_index, "retrieve": _cmd_retrieve, "context": _cmd_context, "evaluate": _cmd_evaluate}
    return handlers[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
