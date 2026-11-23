#!/usr/bin/env python3
"""Agrega as avaliações dos juízes cegos e mede a concordância entre eles.

Uso: agregar_juizes.py <juiz-1.json> <juiz-2.json> --mapa mapa.json --saida resultado.json
`mapa.json`: {"c1": "A", ...} (condição → letra). Só é usado aqui, depois da avaliação.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from statistics import mean

CATEGORIES = {"D": "divergencias", "G": "gargalos", "R": "riscos", "P": "apoio", "O": "oportunidades"}


def categoria(item: str) -> str | None:
    match = re.match(r"([A-Z])\d+$", item)
    return CATEGORIES.get(match.group(1)) if match else None


def summarize(method: dict) -> dict:
    out: dict = {}
    per_cat: dict[str, list[float]] = {}
    for item, value in method.get("itens", {}).items():
        cat = categoria(item)
        if cat:
            per_cat.setdefault(cat, []).append(float(value.get("nota", 0)))
    for cat, notes in per_cat.items():
        out[cat] = round(sum(notes) / (2 * len(notes)), 3)
    notes = [n for v in per_cat.values() for n in v]
    out["cobertura_total"] = round(sum(notes) / (2 * len(notes)), 3) if notes else 0.0
    out["itens_avaliados"] = len(notes)
    traps = method.get("armadilhas", {}) or {}
    out["armadilhas_caidas"] = sum(1 for t in traps.values() if t.get("caiu"))
    out["armadilhas_total"] = len(traps)
    changes = method.get("mudancas", [])
    out["classificacao_mudancas"] = round(mean(float(c.get("acerto", 0)) for c in changes), 3) if changes else 0.0
    out["impacto_mudancas"] = round(mean(float(c.get("impacto", 0)) for c in changes) / 2, 3) if changes else 0.0
    extras = method.get("adicionais", [])
    verdict = [str(e.get("veredito", "")) for e in extras]
    out["adicionais_sustentados"] = verdict.count("sustentado")
    out["adicionais_triviais"] = verdict.count("trivial")
    out["adicionais_sem_suporte"] = verdict.count("sem_suporte")
    out["adicionais_falsos"] = verdict.count("falso")
    cit = method.get("citacoes", {}) or {}
    out["citacoes_verificadas"] = cit.get("verificadas", 0)
    out["citacoes_corretas"] = cit.get("corretas", 0)
    quality = method.get("qualidade", {}) or {}
    for key, value in quality.items():
        out[f"q_{key}"] = value.get("nota") if isinstance(value, dict) else value
    return out


def agreement(a: dict, b: dict) -> dict:
    """Concordância item a item: exata (mesma nota) e kappa de Cohen ponderado linearmente (notas 0, 1, 2)."""
    pairs = []
    for letter in a["metodos"]:
        items_a = a["metodos"][letter].get("itens", {})
        items_b = b["metodos"].get(letter, {}).get("itens", {})
        pairs += [(float(items_a[i].get("nota", 0)), float(items_b[i].get("nota", 0))) for i in items_a if i in items_b]
    if not pairs:
        return {}
    observed = mean(1 - abs(x - y) / 2 for x, y in pairs)
    xs, ys = [p[0] for p in pairs], [p[1] for p in pairs]
    expected = mean(1 - abs(x - y) / 2 for x in xs for y in ys)
    kappa = (observed - expected) / (1 - expected) if expected < 1 else 1.0
    return {"pares": len(pairs), "concordancia_exata": round(mean(x == y for x, y in pairs), 3),
            "kappa_ponderado": round(kappa, 3)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("juizes", nargs="+", type=Path)
    parser.add_argument("--mapa", type=Path, required=True)
    parser.add_argument("--saida", type=Path)
    args = parser.parse_args()
    judges = [json.loads(p.read_text()) for p in args.juizes]
    mapping = json.loads(args.mapa.read_text())
    result: dict = {"condicoes": {}}
    for condition, letter in sorted(mapping.items()):
        each = [summarize(j["metodos"][letter]) for j in judges]
        keys = {k for e in each for k in e}
        avg = {k: round(mean(float(e[k]) for e in each if isinstance(e.get(k), (int, float))), 3)
               for k in sorted(keys) if any(isinstance(e.get(k), (int, float)) for e in each)}
        result["condicoes"][condition] = {"letra": letter, "media": avg, "por_juiz": each}
    if len(judges) >= 2:
        result["concordancia"] = agreement(judges[0], judges[1])
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.saida:
        args.saida.parent.mkdir(parents=True, exist_ok=True)
        args.saida.write_text(text + "\n")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
