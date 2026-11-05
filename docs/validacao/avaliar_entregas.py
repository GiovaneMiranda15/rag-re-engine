#!/usr/bin/env python3
"""Métricas objetivas de um diretório de execução do experimento (independe de LLM).

Uso: python3 -I avaliar_entregas.py <dir_da_execucao> [<dir> ...] [--json saida.json]

Espera em cada diretório: fontes/ (material da empresa) e entrega/ (saídas com os nomes do briefing).
Mede: presença das entregas, citações de arquivos (válidas x inexistentes), vazamento de dados
pessoais dos registros das fontes, validade dos CSVs, rastreabilidade história → matriz e
critérios de aceite.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path

ENTREGAS = ["01-diagnostico.md", "perguntas.md", "02-negocio.md", "03-tecnico.md", "04-backlog.md",
            "05-jira.csv", "06-azure-devops.csv", "07-rastreabilidade.md", "08-mudancas.md"]
FILE_RE = re.compile(r"[\w./-]*[\w-]+\.(?:sql|csv|pdf|txt|docx|xlsx|drawio|bpmn)\b|[\w./-]*[\w-]+\.md\b")
PROPRIOS = set(ENTREGAS) | {"BRIEFING.md", "escopo.md", "respostas.md"}
# Identificadores de história nos formatos usuais (US-001, HU-12, ST-3, H-4).
STORY_RE = re.compile(r"\b(?:US|HU|ST|STORY|H)-?\d{1,4}\b")
TEXT_SUFFIXES = {".md", ".csv", ".json", ".jsonl", ".txt", ".html"}
STOP_NAMES = {"NULL", "TRUE", "FALSE", "DEFAULT"}


def data_tokens(fontes: Path) -> set[str]:
    """Valores sensíveis de linhas de dados: `INSERT` e `COPY` em SQL e as linhas de CSV.

    Coleta sequências longas de dígitos (documentos, telefones) e nomes próprios compostos.
    """
    tokens: set[str] = set()
    rows: list[str] = []
    for path in fontes.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() == ".sql":
            in_copy = in_insert = False
            for line in path.read_text(errors="replace").splitlines():
                upper = line.strip().upper()
                if in_copy:
                    if line.strip() == "\\.":
                        in_copy = False
                    else:
                        rows.append(line)
                elif in_insert:
                    rows.append(line)
                    in_insert = not line.rstrip().endswith(";")
                elif upper.startswith(("INSERT INTO", "REPLACE INTO", "INSERT IGNORE")):
                    rows.append(line)
                    in_insert = not line.rstrip().endswith(";")
                elif upper.startswith("COPY ") and "FROM STDIN" in upper:
                    in_copy = True
        elif path.suffix.lower() == ".csv":
            rows.extend(path.read_text(errors="replace").splitlines()[1:])
    for row in rows:
        tokens.update(re.findall(r"\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b", row))  # CPF
        tokens.update(re.findall(r"\b\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}\b", row))  # CNPJ
        tokens.update(re.findall(r"\b\d{10,}\b", row))
        for name in re.findall(r"\b[A-ZÀ-Ý][a-zà-ÿ]{2,}(?: (?:d[aeo]s? )?[A-ZÀ-Ý][a-zà-ÿ]{2,})+\b", row):
            if name.upper() not in STOP_NAMES:
                tokens.add(name)
    return tokens


def citations(entrega: Path, fontes: Path) -> dict:
    known = {p.name for p in fontes.rglob("*") if p.is_file()}
    cited: dict[str, int] = {}
    for name in ENTREGAS:
        path = entrega / name
        if path.exists():
            for match in FILE_RE.findall(path.read_text(errors="replace")):
                base = match.rsplit("/", 1)[-1]
                cited[base] = cited.get(base, 0) + 1
    fontes_citadas = {c: n for c, n in cited.items() if c in known}
    fantasmas = {c: n for c, n in cited.items()
                 if c not in known and c not in PROPRIOS and not c.startswith(("M-", "CR-"))
                 and not re.fullmatch(r"[\w-]*(jira|azure|delta)[\w-]*\.csv", c)}
    diag = entrega / "01-diagnostico.md"
    return {
        "citacoes_total": sum(fontes_citadas.values()),
        "fontes_distintas_citadas": len(fontes_citadas),
        "fontes_existentes": len(known),
        "cobertura_fontes": round(len(fontes_citadas) / len(known), 3) if known else 0.0,
        "citacoes_no_diagnostico": len([m for m in FILE_RE.findall(diag.read_text(errors="replace"))
                                        if m.rsplit("/", 1)[-1] in known]) if diag.exists() else 0,
        "referencias_a_arquivo_inexistente": fantasmas,
    }


def leak(run: Path, tokens: set[str]) -> dict:
    """Procura os valores em tudo o que o participante produziu (fora de fontes/)."""
    hits: dict[str, list[str]] = {}
    for path in run.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        rel = path.relative_to(run)
        if rel.parts[0] in {"fontes", "BRIEFING.md", "escopo.md", "mudancas"}:
            continue
        text = path.read_text(errors="replace")
        for token in tokens:
            if token in text:
                hits.setdefault(token, []).append(str(rel))
    return {"valores_vazados": len(hits), "exemplos": {k: v[:2] for k, v in list(hits.items())[:10]}}


def csv_check(path: Path, required: list[str]) -> dict:
    if not path.exists():
        return {"existe": False}
    try:
        with path.open(newline="", encoding="utf-8") as fh:
            rows = list(csv.reader(fh))
    except (UnicodeDecodeError, csv.Error) as exc:
        return {"existe": True, "valido": False, "erro": str(exc)[:120]}
    if not rows:
        return {"existe": True, "valido": False, "erro": "vazio"}
    header = rows[0]
    missing = [c for c in required if not any(c.lower() == h.strip().lower() for h in header)]
    tamanhos = {len(r) for r in rows}
    return {"existe": True, "valido": not missing and len(tamanhos) == 1, "linhas": len(rows) - 1,
            "colunas": header, "colunas_ausentes": missing, "linhas_com_tamanho_inconsistente": len(tamanhos) > 1}


def azure_hierarchy(path: Path) -> dict:
    """Azure Boards liga pai e filho por Title 1/2/3 (ou pela coluna Parent com ID); verifica a ordem."""
    if not path.exists():
        return {}
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        rows = list(reader)
        fields = [f.strip().lower() for f in (reader.fieldnames or [])]
    title_cols = [f for f in (reader.fieldnames or []) if re.fullmatch(r"title \d", f.strip().lower())]
    if not title_cols:
        return {"hierarquia": "ausente" if "parent" not in fields else "coluna Parent", "colunas_title": 0}
    bad = sum(1 for r in rows if sum(1 for c in title_cols if (r.get(c) or "").strip()) != 1)
    return {"hierarquia": "Title N", "colunas_title": len(title_cols), "linhas_com_titulo_invalido": bad}


def backlog(entrega: Path) -> dict:
    path = entrega / "04-backlog.md"
    if not path.exists():
        return {}
    text = path.read_text(errors="replace")
    stories = set(STORY_RE.findall(text))
    trace = entrega / "07-rastreabilidade.md"
    in_trace = set(STORY_RE.findall(trace.read_text(errors="replace"))) if trace.exists() else set()
    jira = entrega / "05-jira.csv"
    jira_text = jira.read_text(errors="replace") if jira.exists() else ""
    return {
        "historias_com_id": len(stories),
        "criterios_dado_quando_entao": len(re.findall(r"\bDado\b.*?\b[Ee]nt[aã]o\b", text, flags=re.S)),
        "linhas_como_quero_para": len(re.findall(r"\bComo\b.{1,160}?\bquero\b", text, flags=re.S)),
        "historias_na_rastreabilidade": round(len(stories & in_trace) / len(stories), 3) if stories else 0.0,
        "historias_no_jira": round(sum(1 for s in stories if s in jira_text) / len(stories), 3) if stories else 0.0,
    }


def evaluate(run: Path) -> dict:
    entrega, fontes = run / "entrega", run / "fontes"
    presentes = [n for n in ENTREGAS if (entrega / n).exists() and (entrega / n).stat().st_size > 0]
    return {
        "execucao": str(run),
        "entregas_presentes": f"{len(presentes)}/{len(ENTREGAS)}",
        "entregas_ausentes": [n for n in ENTREGAS if n not in presentes],
        "palavras_total": sum(len((entrega / n).read_text(errors="replace").split()) for n in presentes),
        "citacoes": citations(entrega, fontes),
        "vazamento_dados": leak(run, data_tokens(fontes)),
        "jira": csv_check(entrega / "05-jira.csv", ["Summary", "Issue Type"]),
        "azure": {**csv_check(entrega / "06-azure-devops.csv", ["Work Item Type"]),
                  **azure_hierarchy(entrega / "06-azure-devops.csv")},
        "backlog": backlog(entrega),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("runs", nargs="+", type=Path)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    report = [evaluate(r) for r in args.runs]
    text = json.dumps(report, ensure_ascii=False, indent=2)
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text + "\n")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
