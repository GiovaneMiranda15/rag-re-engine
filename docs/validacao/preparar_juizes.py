#!/usr/bin/env python3
"""Prepara a avaliação cega: copia as entregas sob letras sorteadas, sem nomes de método.

Uso: preparar_juizes.py <experimento> <rotulo> <caso_em_runs> <caso_selado> <condicoes separadas por vírgula>
O mapa condição → letra fica em sealed/juiz-map-<rotulo>.json. Abra-o só depois das notas.
"""
import json, pathlib, random, re, shutil, sys
E = pathlib.Path(sys.argv[1]); label, base, key = sys.argv[2:5]; conds = sys.argv[5].split(",")
out = E / "juizes" / label
if out.exists():
    shutil.rmtree(out)
out.mkdir(parents=True)
letters = ["A", "B", "C", "D"][: len(conds)]
random.SystemRandom().shuffle(letters)
mapping = dict(zip(conds, letters))
(E / "sealed" / f"juiz-map-{label}.json").write_text(json.dumps(mapping))
SCRUB = re.compile(r"re-?copilot|timovi|\.?product[- ]team|recop\.py|rag-re-engine|\.re/", re.I)
for cond, letter in mapping.items():
    target = out / letter
    target.mkdir()
    for f in (E / "runs" / base / cond / "entrega").iterdir():
        if f.is_file():
            (target / f.name).write_text(SCRUB.sub("[método]", f.read_text(errors="replace")))
first = E / "runs" / base / conds[0]
shutil.copytree(first / "fontes", out / "fontes")
shutil.copy(first / "escopo.md", out / "escopo.md")
shutil.copytree(E / "sealed" / key / "mudancas", out / "mudancas")
for name in ("gabarito.md", "oraculo.md"):
    shutil.copy(E / "sealed" / key / name, out / name)
print(sorted(p.name for p in out.iterdir()))
