"""Interface de linha de comando: `rag-re-advisor recommend ...`."""

from __future__ import annotations

import argparse
import json
import sys

from rag_re_advisor.engine import recommend
from rag_re_advisor.models import Activity, Criticality, DataStructure, DataVolume, Recommendation, TaskContext


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="rag-re-advisor",
        description="Recomenda a arquitetura RAG mais adequada para uma atividade de Engenharia de Requisitos.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    rec = sub.add_parser("recommend", help="Recomenda uma arquitetura RAG para o contexto informado.")
    rec.add_argument("--activity", required=True, choices=[a.value for a in Activity])
    rec.add_argument("--data-volume", choices=[v.value for v in DataVolume], default=None)
    rec.add_argument("--data-structure", choices=[s.value for s in DataStructure], default=None)
    rec.add_argument("--needs-traceability", action=argparse.BooleanOptionalAction, default=None)
    rec.add_argument("--needs-external-lookup", action=argparse.BooleanOptionalAction, default=None)
    rec.add_argument("--audit-criticality", choices=[c.value for c in Criticality], default=None)
    rec.add_argument("--latency-budget", choices=[c.value for c in Criticality], default=None)
    rec.add_argument("--json", action="store_true", help="Imprime o resultado como JSON em vez de texto.")

    return parser


def _context_from_args(args: argparse.Namespace) -> TaskContext:
    return TaskContext(
        activity=Activity(args.activity),
        data_volume=DataVolume(args.data_volume) if args.data_volume else None,
        data_structure=DataStructure(args.data_structure) if args.data_structure else None,
        needs_traceability=args.needs_traceability,
        needs_external_lookup=args.needs_external_lookup,
        audit_criticality=Criticality(args.audit_criticality) if args.audit_criticality else None,
        latency_budget=Criticality(args.latency_budget) if args.latency_budget else None,
    )


def _format_human(result: Recommendation) -> str:
    lines = [f"Atividade: {result.context.activity.value}", ""]

    def format_scored(label: str, scored) -> list[str]:
        block = [f"{label}: {scored.architecture.value} (pontuação: {scored.score:g})"]
        for reason in scored.reasons:
            block.append(f"  - {reason}")
        for blocker in scored.blockers:
            block.append(f"  - [inviável] {blocker}")
        if not scored.reasons and not scored.blockers:
            block.append("  - (nenhuma afinidade primária ou sinal secundário aplicável)")
        return block

    lines += format_scored("Recomendação principal", result.top)
    if len(result.tied) > 1:
        names = ", ".join(scored.architecture.value for scored in result.tied)
        lines.append(f"Empate no topo: {names} — a ordem entre elas é arbitrária.")
    if result.alternatives:
        lines.append("")
        lines.append("Alternativas:")
        for alt in result.alternatives:
            lines += ["  " + line for line in format_scored("Arquitetura", alt)]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "recommend":
        context = _context_from_args(args)
        result = recommend(context)
        if args.json:
            print(json.dumps(result.to_dict(), ensure_ascii=False, indent=2))
        else:
            print(_format_human(result))
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
