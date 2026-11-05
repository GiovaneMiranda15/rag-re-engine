#!/usr/bin/env python3
"""Utilitário do re-copilot (só biblioteca padrão): valida o modelo, gera as visões .md,
detecta mudanças nas fontes, mostra o painel e calcula o impacto pelo grafo.

Uso (a partir da raiz do projeto analisado):
    python3 <skill>/scripts/recop.py check            # integridade do modelo
    python3 <skill>/scripts/recop.py render           # gera .re/*.md a partir de .re/modelo/*.json
    python3 <skill>/scripts/recop.py lint             # lacunas de completude
    python3 <skill>/scripts/recop.py verificar [--docs entrega]  # números sem fonte, citações e IDs inválidos
    python3 <skill>/scripts/recop.py status           # números do painel (JSON)
    python3 <skill>/scripts/recop.py fontes [--update] # novas/alteradas/removidas vs .re/fontes.json
    python3 <skill>/scripts/recop.py impacto RN-004 [RF-002 ...] [--depth 3]
    python3 <skill>/scripts/recop.py candidatos "texto da afirmação nova" [-n 8]
    python3 <skill>/scripts/recop.py baseline --nota "v1 validada"
    python3 <skill>/scripts/recop.py diff [B-001]       # o que mudou desde a baseline
    python3 <skill>/scripts/recop.py exportar jira|azure [--processo agile|scrum|basic] [--delta] [--saida arq.csv]
Opção global: --re <dir> (default: .re)
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re as regex
import sys
import unicodedata
from collections import deque
from datetime import datetime, timezone
from pathlib import Path

COLLECTIONS = ("requisitos", "elementos", "achados", "perguntas", "backlog", "mudancas")
PREFIXES = {
    "requisitos": ("RF-", "RNF-", "RN-"),
    "elementos": ("EL-",),
    "achados": ("DIV-", "GAR-", "RIS-", "APO-", "OPO-"),
    "perguntas": ("Q-",),
    "backlog": ("EP-", "FT-", "US-"),
    "mudancas": ("CR-",),
}
STATUS = {
    "requisitos": {"hipótese", "confirmado", "conflito", "validado", "alterado", "obsoleto", "descartado"},
    "achados": {"aberto", "tratado", "descartado"},
    "perguntas": {"aberta", "respondida", "cancelada"},
    "backlog": {"proposto", "pronto", "revisar", "descartado"},
    "mudancas": {"proposta", "aprovada", "rejeitada", "aplicada"},
}
REL_TYPES = {"deriva_de", "depende_de", "conflita_com", "complementa", "substitui", "detalha", "afeta", "implementado_em"}
# Campos que também são arestas do grafo (além de `rel`).
EDGE_FIELDS = {"pai": "detalha", "requisitos": "detalha", "relacionados": "afeta", "afetados": "afeta",
               "sistemas": "implementado_em", "gera": "afeta", "bloqueada_por": "depende_de", "dependencias": "depende_de"}


# ---------------------------------------------------------------- carga

def load(re_dir: Path) -> dict:
    model = {}
    for name in COLLECTIONS:
        path = re_dir / "modelo" / f"{name}.json"
        model[name] = json.loads(path.read_text())["itens"] if path.exists() else []
    fontes = re_dir / "fontes.json"
    model["fontes"] = json.loads(fontes.read_text()) if fontes.exists() else {"sistemas": [], "fontes": []}
    return model


def nodes(model: dict) -> dict[str, dict]:
    out = {item["id"]: item for name in COLLECTIONS for item in model[name]}
    out.update({s["id"]: s for s in model["fontes"].get("sistemas", [])})
    out.update({f["id"]: f for f in model["fontes"].get("fontes", [])})
    return out


def edges(model: dict) -> list[tuple[str, str, str]]:
    """(origem, tipo, destino) a partir de `rel` e dos campos de referência."""
    result = []
    for name in COLLECTIONS:
        for item in model[name]:
            for rel_type, targets in (item.get("rel") or {}).items():
                result += [(item["id"], rel_type, t) for t in targets]
            for field, rel_type in EDGE_FIELDS.items():
                value = item.get(field)
                for t in [value] if isinstance(value, str) else (value or []):
                    result.append((item["id"], rel_type, t))
            for t in item.get("fontes_id") or []:
                result.append((item["id"], "deriva_de", t))
    return result


# ---------------------------------------------------------------- check

def check(model: dict) -> list[str]:
    errors = []
    all_nodes = nodes(model)
    seen: set[str] = set()
    for name in COLLECTIONS:
        for item in model[name]:
            iid = item.get("id", "")
            if iid in seen:
                errors.append(f"{iid}: ID duplicado")
            seen.add(iid)
            if not iid.startswith(PREFIXES[name]):
                errors.append(f"{iid}: prefixo inválido para {name} (esperado {PREFIXES[name]})")
            status = item.get("status")
            if name in STATUS and status not in STATUS[name]:
                errors.append(f"{iid}: status '{status}' inválido (válidos: {sorted(STATUS[name])})")
            if name == "requisitos":
                if status in {"confirmado", "validado"} and not (item.get("fontes") or item.get("fontes_id")):
                    errors.append(f"{iid}: {status} sem fonte")
                if not item.get("enunciado"):
                    errors.append(f"{iid}: sem enunciado")
            for rel_type in (item.get("rel") or {}):
                if rel_type not in REL_TYPES:
                    errors.append(f"{iid}: tipo de relação desconhecido '{rel_type}'")
    for src, rel_type, dst in edges(model):
        if dst not in all_nodes:
            errors.append(f"{src}: {rel_type} → {dst} não existe")
    return errors


# ---------------------------------------------------------------- lint

TEMAS_TRANSVERSAIS = {
    "migração": ("migra", "carga inicial", "de-para", "legado"),
    "auditoria": ("auditoria", "trilha", "historico de alter"),
    "permissões": ("permiss", "perfil de acesso", "papeis", "autoriza"),
    "monitoramento": ("monitor", "alerta", "observab"),
    "falha de integração": ("falha", "reprocess", "indisponib", "retry"),
    "indicadores": ("indicador", "kpi", "painel", "dashboard", "relatorio"),
    "LGPD": ("lgpd", "dados pessoais", "consentimento", "privacidade"),
    "treinamento/transição": ("treinamento", "transicao", "convivencia", "capacita"),
}


def _plain(text: str) -> str:
    return "".join(ch for ch in unicodedata.normalize("NFKD", str(text).lower()) if not unicodedata.combining(ch))


def lint(model: dict) -> dict:
    """Lacunas que `check` não pega: o modelo é coerente, mas o conteúdo está incompleto ou defasado."""
    ativos = {"hipótese", "confirmado", "validado", "alterado"}
    reqs = [r for r in model["requisitos"] if r.get("status") in ativos]
    stories = [b for b in model["backlog"] if b["id"].startswith("US-") and b.get("status") != "descartado"]
    covered = {r for s in stories for r in s.get("requisitos") or []}
    edge = [(a, t, b) for a, t, b in edges(model)]
    linked_to_reqs = {a for a, _, b in edge if b.startswith(("RF-", "RNF-", "RN-"))} | \
                     {b for a, _, b in edge if a.startswith(("RF-", "RNF-", "RN-"))}
    achados_sem = [a["id"] for a in model["achados"]
                   if a.get("status") == "aberto" and not a["id"].startswith("APO-")
                   and not a.get("gera") and a["id"] not in linked_to_reqs]
    changed = {i for c in model["mudancas"] if c.get("status") == "aplicada" for i in c.get("afetados") or []}
    bag = _plain(" ".join(str(i.get(k, "")) for name in ("requisitos", "backlog") for i in model[name]
                          for k in ("titulo", "enunciado", "descricao")))
    rnf_sem_numero = [r["id"] for r in reqs if r["id"].startswith("RNF-")
                      and not regex.search(r"\d", str(r.get("enunciado", "")))]
    confirmados_sem_prova = [r["id"] for r in reqs if r.get("status") in {"confirmado", "validado"}
                             and all(str(f).startswith("hipótese") for f in (r.get("fontes") or ["hipótese"]))
                             and not r.get("fontes_id")]
    return {
        "historias_com_menos_de_2_criterios": [s["id"] for s in stories if len(s.get("criterios_aceite") or []) < 2],
        "historias_must_com_menos_de_3_criterios": [s["id"] for s in stories if s.get("prioridade") == "Must"
                                                    and len(s.get("criterios_aceite") or []) == 2],
        "historias_sem_requisito": [s["id"] for s in stories if not s.get("requisitos")],
        "requisitos_sem_historia": [r["id"] for r in reqs if r["id"] not in covered and not r["id"].startswith("RN-")],
        "requisitos_sem_criterio": [r["id"] for r in reqs if not r.get("criterios_aceite")],
        "rnf_sem_metrica": rnf_sem_numero,
        "historias_que_sao_decisao": [s["id"] for s in stories
                                      if regex.match(r"(?:decidir|definir|levantar|validar com|alinhar)\b", _plain(s.get("titulo", "")))],
        "confirmados_apoiados_so_em_hipotese": confirmados_sem_prova,
        "achados_abertos_sem_tratamento": achados_sem,
        "perguntas_abertas_ligadas_a_mudanca": [q["id"] for q in model["perguntas"] if q.get("status") == "aberta"
                                                 and set(q.get("relacionados") or []) & changed],
        "temas_transversais_ausentes": [t for t, marks in TEMAS_TRANSVERSAIS.items() if not any(m in bag for m in marks)],
    }


# ---------------------------------------------------------------- verificar

NUM_UNIT = regex.compile(
    r"(?:R\$\s*)?\d+(?:[.,]\d+)*\s*(?:%|ms\b|s\b|seg\w*|min\w*|h\b|horas?\b|dias?\b|semanas?\b|meses\b|m[eê]s\b|anos?\b)"
    r"|R\$\s*\d+(?:[.,]\d+)*|\b\d{3,}(?:[.,]\d+)*\b",
    regex.I,
)
CODE = regex.compile(r"\b[A-Za-z]{1,6}[-_]\d+\b")
MODEL_ID = regex.compile(r"\b(?:RF|RNF|RN|EL|DIV|GAR|RIS|APO|OPO|Q|EP|FT|US|CR)-\d{1,4}\b")
FILE_REF = regex.compile(r"(?<![\w*-])[\w./][\w./-]*\.(?:sql|csv|pdf|txt|docx|xlsx|drawio|bpmn)\b")


def _number(value: str) -> str:
    """Forma canônica: `1.820,00` e `1820` viram `1820`; `99,5` vira `99.5`."""
    digits = value.strip()
    if "," in digits and "." in digits:
        digits = digits.replace(".", "").replace(",", ".")
    elif "," in digits:
        digits = digits.replace(",", ".")
    elif regex.fullmatch(r"\d{1,3}(?:\.\d{3})+", digits):
        digits = digits.replace(".", "")
    return digits[:-3] if digits.endswith(".00") else digits.rstrip("0").rstrip(".") if "." in digits else digits


def _unit(fragment: str) -> str:
    """Classe da unidade de um valor: número sem unidade não confirma valor com unidade."""
    low = fragment.lower()
    if "%" in low:
        return "%"
    if "r$" in low:
        return "R$"
    for pattern, name in ((r"\d\s*ms\b", "ms"), (r"\d\s*(?:s\b|seg)", "s"), (r"\d\s*min", "min"), (r"\d\s*(?:h\b|hora)", "h"),
                          (r"\d\s*dia", "dia"), (r"\d\s*semana", "semana"), (r"\d\s*m[eê]s|\d\s*meses", "mes"), (r"\d\s*ano", "ano")):
        if regex.search(pattern, low):
            return name
    return ""


def _values_in(text: str) -> set[tuple[str, str]]:
    """Pares (número, unidade) do texto; números de 3 ou mais dígitos valem também sem unidade."""
    clean = CODE.sub(" ", text)
    values = set()
    for match in NUM_UNIT.finditer(clean):
        fragment = match.group(0)
        number = _number(regex.search(r"\d+(?:[.,]\d+)*", fragment).group(0))
        values.add((number, _unit(fragment)))
        if len(number.split(".")[0]) >= 3:
            values.add((number, ""))
    return values


def _evidence_text(re_dir: Path, model: dict) -> str:
    """Tudo o que conta como evidência: fontes, transcrições, entrevistas e o escopo. Entregáveis não contam."""
    root = re_dir.parent
    paths = [root / f["path"] for f in model["fontes"].get("fontes", []) if f.get("path") and not f.get("removido_em")]
    for sistema in model["fontes"].get("sistemas", []):
        for folder in sistema.get("pastas", []):
            base = root / folder
            if base.is_dir():
                paths += [p for p in base.rglob("*") if p.is_file()]
    for extra in ("entrevistas", "extraidos"):
        if (re_dir / extra).is_dir():
            paths += [p for p in (re_dir / extra).rglob("*") if p.is_file()]
    paths.append(re_dir / "escopo.md")
    chunks = []
    for path in set(paths):
        if path.is_file() and path.suffix.lower() in {".md", ".txt", ".sql", ".csv", ".xml", ".bpmn", ".drawio", ".json"}:
            chunks.append(path.read_text(errors="replace"))
    answers = [str(q.get("resposta")) for q in model["perguntas"] if q.get("resposta")]
    return "\n".join(chunks + answers)


def verificar(re_dir: Path, model: dict, docs: Path | None = None) -> dict:
    """Checagens objetivas contra as fontes. O modelo pode errar; estas regras não se convencem."""
    evidence = _evidence_text(re_dir, model)
    known_values = _values_in(evidence)
    known_files = {"escopo.md"}
    root = re_dir.parent
    for extra in ("extraidos", "entrevistas"):
        if (re_dir / extra).is_dir():
            known_files |= {p.name for p in (re_dir / extra).rglob("*") if p.is_file()}
    for f in model["fontes"].get("fontes", []):
        if f.get("path"):
            known_files.add(Path(f["path"]).name)
    for sistema in model["fontes"].get("sistemas", []):
        for folder in sistema.get("pastas", []):
            if (root / folder).is_dir():
                known_files |= {p.name for p in (root / folder).rglob("*") if p.is_file()}
    numeros, citacoes = [], []
    ids_perguntas = {q["id"] for q in model["perguntas"]}
    confirmed = {"confirmado", "validado", "alterado"}
    for r in model["requisitos"]:
        if r.get("status") in confirmed:
            text = CODE.sub(" ", str(r.get("enunciado", "")))
            for match in NUM_UNIT.finditer(text):
                hit = match.group(0)
                number = _number(regex.search(r"\d+(?:[.,]\d+)*", hit).group(0))
                if (number, _unit(hit)) not in known_values:
                    numeros.append({"id": r["id"], "valor": hit.strip()})
            if "[hipótese" in str(r.get("enunciado", "")).lower():
                numeros.append({"id": r["id"], "valor": "enunciado com hipótese em item confirmado"})
    for name in ("requisitos", "achados", "elementos"):
        for item in model[name]:
            for c in item.get("fontes") or []:
                c = str(c)
                f = _citation_file(c)
                if f and Path(f).name not in known_files:
                    citacoes.append({"id": item["id"], "citacao": c, "problema": "arquivo não registrado"})
                sql = regex.match(r"sql:\s*([^:\s]+):\s*(\S+)", c)
                if sql and Path(sql.group(1)).name in known_files and sql.group(2).rsplit(".", 1)[-1] not in evidence:
                    citacoes.append({"id": item["id"], "citacao": c, "problema": "objeto não encontrado"})
                ent = regex.match(r"entrevista:\s*\S+\s+(Q-\d+)", c)
                if ent and ent.group(1) not in ids_perguntas:
                    citacoes.append({"id": item["id"], "citacao": c, "problema": "pergunta inexistente"})
    reqs = {r["id"]: r for r in model["requisitos"]}
    historias_hipotese = [
        b["id"] for b in model["backlog"]
        if b["id"].startswith("US-") and b.get("status") != "descartado"
        and any(reqs.get(r, {}).get("status") == "hipótese" for r in b.get("requisitos") or [])
        and "hipotese" not in (b.get("labels") or [])
    ]
    div_sem_checagem = [a["id"] for a in model["achados"] if a["id"].startswith("DIV-") and a.get("status") != "descartado"
                        and not all((a.get("checagem") or {}).get(k) for k in ("vigencia", "abrangencia", "definicao"))]
    report = {
        "numeros_sem_fonte_em_confirmados": numeros,
        "citacoes_invalidas": citacoes,
        "historias_de_hipotese_sem_label": historias_hipotese,
        "divergencias_sem_checagem_de_falso_positivo": div_sem_checagem,
    }
    if docs is not None:
        all_ids = set(nodes(model))
        ids_ruins, arquivos_ruins = {}, {}
        for path in sorted(docs.rglob("*")):
            if not path.is_file() or path.suffix.lower() not in {".md", ".csv"} or path.name in {"respostas.md"}:
                continue
            text = path.read_text(errors="replace")
            bad = sorted(set(MODEL_ID.findall(text)) - all_ids)
            if bad:
                ids_ruins[path.name] = bad
            refs = sorted(r for r in {m.rsplit("/", 1)[-1] for m in FILE_REF.findall(text)} - known_files
                          - {p.name for p in docs.rglob("*") if p.is_file()} if not r.endswith("-delta.csv"))
            if refs:
                arquivos_ruins[path.name] = refs
        report["ids_inexistentes_nos_documentos"] = ids_ruins
        report["arquivos_inexistentes_nos_documentos"] = arquivos_ruins
    return report


# ---------------------------------------------------------------- render

def _cell(value) -> str:
    if isinstance(value, list):
        value = ", ".join(map(str, value))
    return str(value if value not in (None, "") else "—").replace("|", "\\|").replace("\n", " ")


def _table(headers: list[str], rows: list[list]) -> str:
    lines = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    lines += ["| " + " | ".join(_cell(c) for c in row) + " |" for row in rows]
    return "\n".join(lines)


def render_requisitos(model: dict) -> str:
    groups = (("RF-", "Requisitos funcionais"), ("RNF-", "Requisitos não funcionais"), ("RN-", "Regras de negócio"))
    out = ["# Requisitos", "", "> Gerado por `recop.py render` a partir de `.re/modelo/requisitos.json`. Não edite à mão.", ""]
    for prefix, title in groups:
        items = [r for r in model["requisitos"] if r["id"].startswith(prefix)]
        out += [f"## {title}", ""]
        for r in items:
            out += [f"### {r['id']} — {r.get('titulo', '')} (v{r.get('versao', 1)})", "",
                    f"- **Enunciado:** {r.get('enunciado', '')}"]
            for label, key in (("Categoria", "categoria"), ("Prioridade", "prioridade"), ("Status", "status"),
                               ("Fontes", "fontes"), ("Perfis", "perfis")):
                if r.get(key):
                    out.append(f"- **{label}:** {_cell(r[key])}")
            for rel_type, targets in (r.get("rel") or {}).items():
                out.append(f"- **{rel_type.replace('_', ' ')}:** {', '.join(targets)}")
            if r.get("criterios_aceite"):
                out.append("- **Critérios de aceite:**")
                out += [f"  - {c}" for c in r["criterios_aceite"]]
            if r.get("historico"):
                out.append("- **Histórico:** " + "; ".join(
                    f"v{h.get('versao', '?')} {h.get('data', '')} {h.get('mudanca', '')} {h.get('nota', '')}".strip()
                    for h in r["historico"]))
            out.append("")
        if not items:
            out += ["_Nenhum._", ""]
    return "\n".join(out)


def render_perguntas(model: dict) -> str:
    rows = [[q["id"], q.get("pergunta"), q.get("responsavel"), q.get("origem"), q.get("relacionados"), q.get("status")]
            for q in model["perguntas"] if q.get("status") == "aberta"]
    return "# Perguntas abertas\n\n" + _table(["ID", "Pergunta", "Responsável", "Origem", "Relacionado", "Status"], rows) + "\n"


def render_achados(model: dict) -> str:
    out = ["# Achados do diagnóstico", ""]
    for prefix, title in (("DIV-", "Divergências"), ("GAR-", "Gargalos"), ("RIS-", "Riscos"),
                          ("APO-", "Pontos de apoio"), ("OPO-", "Oportunidades")):
        rows = [[a["id"], a.get("titulo"), a.get("sistemas"), a.get("severidade"), a.get("fontes"), a.get("status"),
                 a.get("gera")] for a in model["achados"] if a["id"].startswith(prefix)]
        out += [f"## {title}", "", _table(["ID", "Achado", "Sistemas", "Severidade", "Fontes", "Status", "Gera"], rows), ""]
    return "\n".join(out)


def render_backlog(model: dict) -> str:
    by_parent: dict[str | None, list[dict]] = {}
    for item in model["backlog"]:
        by_parent.setdefault(item.get("pai"), []).append(item)
    out = ["# Backlog", ""]

    def walk(parent: str | None, depth: int) -> None:
        for item in by_parent.get(parent, []):
            out.append(f"{'#' * min(depth + 2, 4)} {item['id']} — {item.get('titulo', '')} [{item.get('status')}]")
            out.append("")
            if item.get("descricao"):
                out.extend([item["descricao"], ""])
            meta = [f"Prioridade: {item['prioridade']}" if item.get("prioridade") else None,
                    f"Requisitos: {', '.join(item['requisitos'])}" if item.get("requisitos") else None,
                    f"Estimativa: {item['estimativa']}" if item.get("estimativa") else None]
            if any(meta):
                out.extend([" · ".join(m for m in meta if m), ""])
            if item.get("criterios_aceite"):
                out.extend([f"- {c}" for c in item["criterios_aceite"]] + [""])
            walk(item["id"], depth + 1)

    walk(None, 0)
    return "\n".join(out)


def _citation_file(citation: str) -> str | None:
    """Arquivo de uma citação `doc:SIS-01/a.md#2` ou `sql:SIS-01/a.sql:objeto` (None para outros tipos)."""
    match = regex.match(r"(?:doc|sql):\s*([^#:\s]+)", str(citation))
    return match.group(1) if match else None


def render_rastreabilidade(model: dict) -> str:
    """Matrizes geradas do modelo: sempre coerentes entre si, sem depender de redação manual."""
    all_edges = edges(model)
    achado_prefix = {"DIV", "GAR", "RIS", "APO", "OPO"}
    stories = [b for b in model["backlog"] if b["id"].startswith("US-") and b.get("status") != "descartado"]
    by_req: dict[str, list[str]] = {}
    for story in stories:
        for r in story.get("requisitos") or []:
            by_req.setdefault(r, []).append(story["id"])
    ids_req = {r["id"] for r in model["requisitos"]}
    def achados_de(rid: str) -> list[str]:
        return sorted({d for a, _, d in all_edges if a == rid and d.split("-")[0] in achado_prefix}
                      | {a for a, _, d in all_edges if d == rid and a.split("-")[0] in achado_prefix})

    out = ["# Matriz de rastreabilidade", "", "> Gerado por `recop.py render`. Não edite à mão.", ""]
    rows = [[r["id"], r.get("status"), (r.get("fontes") or []) + (r.get("fontes_id") or []), r.get("sistemas"),
             achados_de(r["id"]), sorted(by_req.get(r["id"], [])), r.get("perfis"), (r.get("rel") or {}).get("depende_de")]
            for r in model["requisitos"]]
    out += ["## 1. Requisito → fontes → backlog", "",
            _table(["Requisito", "Status", "Fontes", "Sistemas", "Achados", "Histórias", "Perfis", "Depende de"], rows), ""]
    rows = [[s_["id"], s_.get("titulo"), s_.get("requisitos"), s_.get("pai"), s_.get("bloqueada_por"), s_.get("status")] for s_ in stories]
    out += ["## 2. História → requisito → pendência", "",
            _table(["História", "Título", "Requisitos", "Pai", "Bloqueada por", "Status"], rows), ""]
    per_file: dict[str, list[str]] = {}
    for r in model["requisitos"]:
        for c in r.get("fontes") or []:
            f = _citation_file(c)
            if f:
                per_file.setdefault(f, []).append(r["id"])
    rows = [[f, sorted(set(v))] for f, v in sorted(per_file.items())]
    cited = {f.rsplit("/", 1)[-1] for f in per_file}
    sem_uso = [f.get("path") for f in model["fontes"].get("fontes", []) if Path(str(f.get("path"))).name not in cited
               and not f.get("removido_em")]
    out += ["## 3. Fonte → requisitos", "", _table(["Fonte", "Requisitos"], rows), "",
            f"**Fontes sem nenhum requisito:** {', '.join(map(str, sem_uso)) or 'nenhuma'}", ""]
    def tratamento(a: dict) -> list[str]:
        linked = {d for x, _, d in all_edges if x == a["id"]} | {x for x, _, d in all_edges if d == a["id"]}
        return sorted(i for i in linked if not i.startswith(("SIS-", "F-", "EL-")))
    rows = [[a["id"], a.get("titulo"), a.get("sistemas"), a.get("status"), tratamento(a)]
            for a in model["achados"] if a["id"].startswith("DIV-")]
    out += ["## 4. Divergência → tratamento", "", _table(["Divergência", "Título", "Sistemas", "Status", "Tratamento"], rows), ""]
    rows = []
    for a in model["achados"]:
        if a["id"].startswith("RIS-"):
            reqs = [i for i in tratamento(a) if i in ids_req]
            hist = sorted({h for r in reqs for h in by_req.get(r, [])})
            rows.append([a["id"], a.get("titulo"), a.get("severidade"), reqs, hist])
    out += ["## 5. Risco → requisitos → histórias", "", _table(["Risco", "Título", "Severidade", "Requisitos", "Histórias"], rows), ""]
    gerados = {q["id"]: sorted({x for x, _, d in all_edges if d == q["id"]}) for q in model["perguntas"]}
    rows = [[q["id"], q.get("pergunta"), q.get("responsavel"), q.get("status"), q.get("resposta"),
             sorted(set(q.get("relacionados") or []) | set(gerados.get(q["id"], [])))] for q in model["perguntas"]]
    out += ["## 6. Pergunta → resposta → itens", "", _table(["Pergunta", "Texto", "Responsável", "Status", "Resposta", "Itens"], rows), ""]
    abertas = [q for q in model["perguntas"] if q.get("status") == "aberta"]
    rows = [[q["id"], q.get("pergunta"), q.get("responsavel"),
             sorted(s_["id"] for s_ in stories if q["id"] in (s_.get("bloqueada_por") or []))] for q in abertas]
    out += ["## 7. Pendência → histórias bloqueadas", "", _table(["Pergunta", "Texto", "Responsável", "Histórias"], rows), ""]
    rows = [[c["id"], c.get("titulo"), c.get("classe"), c.get("status"), c.get("afetados")] for c in model["mudancas"]]
    out += ["## 8. Mudança → impacto", "", _table(["CR", "Título", "Classe", "Status", "Itens afetados"], rows), ""]
    orphans = [r["id"] for r in model["requisitos"] if not (r.get("fontes") or r.get("fontes_id"))
               and r.get("status") not in {"descartado", "obsoleto"}]
    no_story = [r["id"] for r in model["requisitos"] if r.get("status") in {"confirmado", "validado"}
                and r["id"] not in by_req]
    out += [f"**Sem fonte (órfãos):** {', '.join(orphans) or 'nenhum'}", "",
            f"**Confirmados/validados sem história direta:** {', '.join(no_story) or 'nenhum'}", ""]
    return "\n".join(out)


def render_cenarios(model: dict) -> str:
    """Catálogo de cenários de teste a partir dos critérios de aceite do backlog e dos requisitos."""
    rows = []
    for item in model["backlog"] + model["requisitos"]:
        if item.get("status") in {"descartado", "obsoleto"}:
            continue
        for n, criterion in enumerate(item.get("criterios_aceite") or [], start=1):
            rows.append([f"{item['id']}.{n}", item.get("titulo"), criterion, item.get("requisitos") or item["id"]])
    return "# Cenários de teste\n\n> Gerado dos critérios de aceite por `recop.py render`.\n\n" + \
        _table(["Cenário", "Item", "Critério", "Requisitos"], rows) + "\n"


def render(re_dir: Path, model: dict) -> list[Path]:
    views = {"requisitos.md": render_requisitos, "perguntas-abertas.md": render_perguntas,
             "achados.md": render_achados, "backlog.md": render_backlog, "rastreabilidade.md": render_rastreabilidade,
             "cenarios.md": render_cenarios}
    written = []
    for filename, fn in views.items():
        path = re_dir / filename
        path.write_text(fn(model))
        written.append(path)
    return written


# ---------------------------------------------------------------- status

def status(re_dir: Path, model: dict) -> dict:
    def count(items, key="status"):
        out: dict[str, int] = {}
        for i in items:
            out[i.get(key)] = out.get(i.get(key), 0) + 1
        return out

    state_path = re_dir / "state.json"
    state = json.loads(state_path.read_text()) if state_path.exists() else {}
    return {
        "projeto": state.get("projeto"), "fase": state.get("fase"), "baseline": state.get("baseline"),
        "requisitos": count(model["requisitos"]), "achados": count(model["achados"]),
        "perguntas_abertas": sum(1 for q in model["perguntas"] if q.get("status") == "aberta"),
        "backlog": count(model["backlog"]), "mudancas": count(model["mudancas"]),
        "sistemas": len(model["fontes"].get("sistemas", [])), "fontes": len(model["fontes"].get("fontes", [])),
        "perfis": state.get("perfis", {}),
    }


# ---------------------------------------------------------------- fontes

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1 << 16), b""):
            h.update(block)
    return h.hexdigest()


def scan_fontes(re_dir: Path, update: bool) -> dict:
    """Compara os arquivos sob as pastas de cada sistema (`sistemas[].pastas`) com `fontes[]`."""
    path = re_dir / "fontes.json"
    data = json.loads(path.read_text()) if path.exists() else {"sistemas": [], "fontes": []}
    root = re_dir.parent
    known = {f["path"]: f for f in data["fontes"]}
    found: dict[str, tuple[str, str]] = {}
    for sistema in data["sistemas"]:
        for folder in sistema.get("pastas", []):
            base = root / folder
            files = [base] if base.is_file() else sorted(p for p in base.rglob("*") if p.is_file())
            for f in files:
                found[str(f.relative_to(root))] = (sistema["id"], sha256(f))
    novas = sorted(p for p in found if p not in known)
    alteradas = sorted(p for p in found if p in known and known[p].get("sha256") != found[p][1])
    removidas = sorted(p for p in known if p not in found)
    if update:
        now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        next_n = max([int(f["id"].split("-")[1]) for f in data["fontes"]] or [0]) + 1
        for p in novas:
            data["fontes"].append({"id": f"F-{next_n:03d}", "sistema": found[p][0], "path": p, "tipo": _tipo(p),
                                   "sha256": found[p][1], "registrado_em": now})
            next_n += 1
        for f in data["fontes"]:
            if f["path"] in alteradas:
                f["sha256"] = found[f["path"]][1]
                f["alterado_em"] = now
            if f["path"] in removidas:
                f["removido_em"] = now
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    tamanho = sum((root / p).stat().st_size for p in found) // 1024
    return {"novas": novas, "alteradas": alteradas, "removidas": removidas, "atualizado": update, "tamanho_kb": tamanho}


def _tipo(path: str) -> str:
    suffix = Path(path).suffix.lower()
    return {".sql": "ddl", ".bpmn": "processo", ".drawio": "processo", ".csv": "planilha", ".xlsx": "planilha",
            ".png": "erd", ".jpg": "erd", ".jpeg": "erd"}.get(suffix, "documento")


# ---------------------------------------------------------------- impacto

def impacto(model: dict, start: str, depth: int) -> dict:
    """Busca em largura nas duas direções do grafo; devolve os nós alcançados por distância.

    Sistemas (SIS-) e fontes (F-) entram no resultado mas não são expandidos: são hubs que
    ligariam tudo a tudo.
    """
    all_nodes = nodes(model)
    if start not in all_nodes:
        raise SystemExit(f"{start} não existe no modelo")
    adj: dict[str, list[tuple[str, str]]] = {}
    for src, rel_type, dst in edges(model):
        adj.setdefault(src, []).append((dst, rel_type))
        adj.setdefault(dst, []).append((src, f"{rel_type}⁻¹"))
    dist = {start: 0}
    via: dict[str, str] = {}
    queue = deque([start])
    while queue:
        cur = queue.popleft()
        if dist[cur] >= depth or (cur != start and cur.startswith(("SIS-", "F-"))):
            continue
        for nxt, rel_type in adj.get(cur, []):
            if nxt not in dist:
                dist[nxt] = dist[cur] + 1
                via[nxt] = f"{cur} —{rel_type}→ {nxt}"
                queue.append(nxt)
    afetados = [{"id": n, "distancia": d, "via": via[n],
                 "titulo": all_nodes.get(n, {}).get("titulo") or all_nodes.get(n, {}).get("nome") or all_nodes.get(n, {}).get("path"),
                 "status": all_nodes.get(n, {}).get("status")}
                for n, d in sorted(dist.items(), key=lambda kv: (kv[1], kv[0])) if n != start]
    return {"origem": start, "profundidade": depth, "afetados": afetados}


def impacto_multi(model: dict, starts: list[str], depth: int) -> dict:
    """União do impacto de vários itens: mantém a menor distância de cada nó alcançado."""
    best: dict[str, dict] = {}
    for start in starts:
        for item in impacto(model, start, depth)["afetados"]:
            if item["id"] not in starts and (item["id"] not in best or item["distancia"] < best[item["id"]]["distancia"]):
                best[item["id"]] = item
    afetados = sorted(best.values(), key=lambda a: (a["distancia"], a["id"]))
    return {"origem": starts, "profundidade": depth, "afetados": afetados}


# ---------------------------------------------------------------- candidatos

STOPWORDS = set("""a o as os um uma de da do das dos em no na nos nas para por com sem que e ou se ao aos à às é ser
sistema deve deverá pode foi são como mais menos sobre entre quando qual quais este esta esse essa isso já não""".split())


def _tokens(text: str) -> set[str]:
    plain = unicodedata.normalize("NFKD", str(text).lower())
    plain = "".join(ch for ch in plain if not unicodedata.combining(ch))
    return {t for t in regex.findall(r"[a-z0-9%]+", plain) if len(t) > 1 and t not in STOPWORDS}


def candidatos(model: dict, texto: str, n: int = 8) -> list[dict]:
    """Itens do modelo mais parecidos com uma afirmação nova (entrada do classificador).

    Só ordena por sobreposição de termos; decidir a classe é papel do agente, que lê os itens.
    """
    query = _tokens(texto)
    scored = []
    for name in ("requisitos", "elementos", "achados", "perguntas", "backlog"):
        for item in model[name]:
            if item.get("status") in {"descartado", "cancelada"}:
                continue
            fields = [item.get(k) for k in ("titulo", "nome", "enunciado", "descricao", "pergunta", "resposta")]
            bag = _tokens(" ".join(str(f) for f in fields if f) + " " + " ".join(item.get("criterios_aceite") or []))
            common = query & bag
            if common:
                scored.append({"id": item["id"], "titulo": item.get("titulo") or item.get("nome") or item.get("pergunta"),
                               "status": item.get("status"), "pontos": round(len(common) / max(len(query), 1), 3),
                               "termos": sorted(common)})
    return sorted(scored, key=lambda x: (-x["pontos"], x["id"]))[:n]


# ---------------------------------------------------------------- baseline

def _load_state(re_dir: Path) -> dict:
    path = re_dir / "state.json"
    return json.loads(path.read_text()) if path.exists() else {}


def criar_baseline(re_dir: Path, model: dict, nota: str) -> dict:
    """Congela requisitos e backlog. Recusa se o modelo estiver inconsistente ou houver conflito aberto."""
    errors = check(model)
    if errors:
        raise SystemExit("baseline recusada: modelo com problemas de integridade (rode `check`)")
    conflitos = [r["id"] for r in model["requisitos"] if r.get("status") == "conflito"]
    if conflitos:
        raise SystemExit(f"baseline recusada: requisitos em conflito: {', '.join(conflitos)}")
    folder = re_dir / "baselines"
    folder.mkdir(exist_ok=True)
    numbers = [int(m.group(1)) for f in folder.glob("B-*.json") if (m := regex.fullmatch(r"B-(\d+)\.json", f.name))]
    bid = f"B-{max(numbers, default=0) + 1:03d}"
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    snapshot = {"id": bid, "data": now, "nota": nota, "requisitos": model["requisitos"], "backlog": model["backlog"]}
    (folder / f"{bid}.json").write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n")
    state = _load_state(re_dir)
    state["baseline"] = bid
    state["atualizado_em"] = now
    (re_dir / "state.json").write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
    return {"baseline": bid, "requisitos": len(model["requisitos"]), "backlog": len(model["backlog"])}


def diff_baseline(re_dir: Path, model: dict, bid: str | None) -> dict:
    bid = bid or _load_state(re_dir).get("baseline")
    if not bid:
        raise SystemExit("nenhuma baseline: rode `baseline` antes")
    path = re_dir / "baselines" / f"{bid}.json"
    if not path.exists():
        raise SystemExit(f"{path} não existe")
    old = json.loads(path.read_text())
    report: dict = {"baseline": bid}
    for name in ("requisitos", "backlog"):
        before = {i["id"]: i for i in old.get(name, [])}
        after = {i["id"]: i for i in model[name]}
        report[name] = {
            "criados": sorted(set(after) - set(before)),
            "removidos": sorted(set(before) - set(after)),
            "alterados": sorted(i for i in before.keys() & after.keys() if before[i] != after[i]),
        }
    return report


# ---------------------------------------------------------------- exportação do backlog

JIRA_PRIORITY = {"Must": "Highest", "Should": "High", "Could": "Medium", "Won't": "Low"}
AZURE_PRIORITY = {"Must": "1", "Should": "2", "Could": "3", "Won't": "4"}
AZURE_STORY = {"agile": "User Story", "scrum": "Product Backlog Item", "basic": "Issue"}


def _labels(item: dict) -> list[str]:
    return list(item.get("labels") or []) + [f"req-{r}" for r in item.get("requisitos") or []] + [item["id"]]


def _body(item: dict, with_criteria: bool) -> str:
    parts = [item.get("descricao") or ""]
    if with_criteria and item.get("criterios_aceite"):
        parts.append("Critérios de aceite:\n" + "\n".join(f"- {c}" for c in item["criterios_aceite"]))
    if item.get("requisitos"):
        parts.append("Requisitos: " + ", ".join(item["requisitos"]))
    return "\n\n".join(p for p in parts if p)


def _ordered(model: dict) -> tuple[list[dict], list[dict]]:
    """Épicos e demais itens válidos; `pai` ausente em item que não é épico é erro de modelo."""
    items = [i for i in model["backlog"] if i.get("status") != "descartado"]
    known = {i["id"] for i in items}
    orphans = [i["id"] for i in items if not i["id"].startswith("EP-") and i.get("pai") not in known]
    if orphans:
        raise SystemExit(f"itens sem pai válido: {', '.join(orphans)}")
    return [i for i in items if i["id"].startswith("EP-")], items


def _children(items: list[dict], parent: str) -> list[dict]:
    return [i for i in items if i.get("pai") == parent]


def _keep(item: dict, delta: bool, items: list[dict]) -> bool:
    """No modo delta, fica o que está em `revisar` e os pais necessários para a hierarquia."""
    if not delta or item.get("status") == "revisar":
        return True
    return any(_keep(c, True, items) for c in _children(items, item["id"]))


def export_jira(model: dict, delta: bool = False) -> str:
    """Épico → história. Jira padrão não tem Feature: vira o label `feature-<ID>` nas histórias."""
    epics, items = _ordered(model)
    rows: list[tuple[str, str, str, str, str, str, list[str]]] = []
    next_id = 1

    def story_rows(parent_row: str, story: dict, extra: list[str]) -> None:
        nonlocal next_id
        if not _keep(story, delta, items):
            return
        rows.append((str(next_id), parent_row, "Story", story.get("titulo", ""), _body(story, True),
                     JIRA_PRIORITY.get(story.get("prioridade"), ""), _labels(story) + extra))
        next_id += 1

    for epic in epics:
        if not _keep(epic, delta, items):
            continue
        epic_row = str(next_id)
        rows.append((epic_row, "", "Epic", epic.get("titulo", ""), _body(epic, False),
                     JIRA_PRIORITY.get(epic.get("prioridade"), ""), _labels(epic)))
        next_id += 1
        for child in _children(items, epic["id"]):
            if child["id"].startswith("FT-"):
                for story in _children(items, child["id"]):
                    story_rows(epic_row, story, [f"feature-{child['id']}"])
            else:
                story_rows(epic_row, child, [])
    width = max((len(r[6]) for r in rows), default=1)
    out = io.StringIO()
    writer = csv.writer(out, quoting=csv.QUOTE_ALL, lineterminator="\n")
    writer.writerow(["Issue Id", "Parent Id", "Issue Type", "Summary", "Description", "Priority"] + ["Labels"] * width)
    for r in rows:
        # Jira não aceita espaço em label.
        labels = [str(lb).replace(" ", "-") for lb in r[6]]
        writer.writerow(list(r[:6]) + labels + [""] * (width - len(labels)))
    return out.getvalue()


def export_azure(model: dict, processo: str = "agile", delta: bool = False) -> str:
    """Hierarquia por colunas Title N. Processo Basic não tem Feature: Epic → Issue, com tag da feature."""
    if processo not in AZURE_STORY:
        raise SystemExit(f"processo inválido: {processo} (agile, scrum, basic)")
    epics, items = _ordered(model)
    levels = 2 if processo == "basic" else 3
    out = io.StringIO()
    writer = csv.writer(out, quoting=csv.QUOTE_ALL, lineterminator="\n")
    writer.writerow(["Work Item Type"] + [f"Title {n}" for n in range(1, levels + 1)]
                    + ["Description", "Acceptance Criteria", "Priority", "Tags"])

    def line(kind: str, level: int, item: dict, extra: list[str] | None = None) -> None:
        titles = [""] * levels
        titles[level] = item.get("titulo", "")
        writer.writerow([kind] + titles + [_body(item, False), "\n".join(item.get("criterios_aceite") or []),
                                           AZURE_PRIORITY.get(item.get("prioridade"), ""),
                                           "; ".join(_labels(item) + (extra or []))])

    story_type = AZURE_STORY[processo]
    for epic in epics:
        if not _keep(epic, delta, items):
            continue
        line("Epic", 0, epic)
        for child in _children(items, epic["id"]):
            if not _keep(child, delta, items):
                continue
            if not child["id"].startswith("FT-"):
                line(story_type, levels - 1, child)
            elif processo == "basic":
                for story in _children(items, child["id"]):
                    if _keep(story, delta, items):
                        line(story_type, 1, story, [f"feature-{child['id']}"])
            else:
                line("Feature", 1, child)
                for story in _children(items, child["id"]):
                    if _keep(story, delta, items):
                        line(story_type, 2, story)
    return out.getvalue()


# ---------------------------------------------------------------- CLI

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="recop.py", description=__doc__.splitlines()[0])
    parser.add_argument("--re", type=Path, default=Path(".re"))
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check")
    sub.add_parser("render")
    sub.add_parser("lint")
    vf = sub.add_parser("verificar")
    vf.add_argument("--docs", type=Path, help="pasta de entregáveis a conferir")
    sub.add_parser("status")
    f = sub.add_parser("fontes")
    f.add_argument("--update", action="store_true")
    i = sub.add_parser("impacto")
    i.add_argument("id", nargs="+")
    i.add_argument("--depth", type=int, default=3)
    c = sub.add_parser("candidatos")
    c.add_argument("texto")
    c.add_argument("-n", type=int, default=8)
    b = sub.add_parser("baseline")
    b.add_argument("--nota", default="")
    d = sub.add_parser("diff")
    d.add_argument("baseline", nargs="?")
    e = sub.add_parser("exportar")
    e.add_argument("destino", choices=["jira", "azure"])
    e.add_argument("--processo", default="agile")
    e.add_argument("--delta", action="store_true", help="só itens em `revisar` e seus pais")
    e.add_argument("--saida", type=Path)
    args = parser.parse_args(argv)

    if not args.re.is_dir():
        print(f"{args.re} não existe", file=sys.stderr)
        return 2
    if args.cmd == "fontes":
        print(json.dumps(scan_fontes(args.re, args.update), ensure_ascii=False, indent=2))
        return 0
    model = load(args.re)
    if args.cmd == "check":
        errors = check(model)
        print("\n".join(errors) if errors else "ok")
        return 1 if errors else 0
    if args.cmd == "render":
        errors = check(model)
        for path in render(args.re, model):
            print(f"gerado {path}")
        if errors:
            print(f"atenção: {len(errors)} problema(s) de integridade — rode `check`", file=sys.stderr)
        return 0
    if args.cmd == "verificar":
        report = verificar(args.re, model, args.docs)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 1 if any(report.values()) else 0
    if args.cmd == "lint":
        report = lint(model)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 1 if any(report.values()) else 0
    if args.cmd == "status":
        print(json.dumps(status(args.re, model), ensure_ascii=False, indent=2))
        return 0
    if args.cmd == "impacto":
        print(json.dumps(impacto_multi(model, args.id, args.depth), ensure_ascii=False, indent=2))
        return 0
    if args.cmd == "candidatos":
        print(json.dumps(candidatos(model, args.texto, args.n), ensure_ascii=False, indent=2))
        return 0
    if args.cmd == "baseline":
        print(json.dumps(criar_baseline(args.re, model, args.nota), ensure_ascii=False, indent=2))
        return 0
    if args.cmd == "diff":
        print(json.dumps(diff_baseline(args.re, model, args.baseline), ensure_ascii=False, indent=2))
        return 0
    if args.cmd == "exportar":
        text = export_jira(model, args.delta) if args.destino == "jira" else export_azure(model, args.processo, args.delta)
        if args.saida:
            args.saida.parent.mkdir(parents=True, exist_ok=True)
            args.saida.write_text(text)
            print(f"gerado {args.saida}")
        else:
            print(text, end="")
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
