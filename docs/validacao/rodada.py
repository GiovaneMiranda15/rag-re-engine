#!/usr/bin/env python3
"""Passos mecânicos de uma rodada de validação. Idempotente: dá para repetir e retomar depois de uma interrupção.

Uso: python3 -I docs/validacao/rodada.py <comando> [--rodada r04] [--condicoes c1,c2,c6]

    preparar     congela as skills e confere o ambiente
    selar        separa gabarito/oráculo/mudanças do caso e cria os diretórios de execução
    status       mostra em que etapa cada condição está e o próximo passo
    oraculo      anonimiza as perguntas das condições para o oráculo
    respostas    entrega as respostas do oráculo a cada condição
    mudancas     tira a foto da etapa 2 e entrega as mudanças a quem terminou a etapa 2
    juizes       prepara a avaliação cega
    resultado    calcula as medidas objetivas e agrega os juízes
"""

from __future__ import annotations

import argparse
import os
import json
import random
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
VALID = REPO / "docs" / "validacao"
# skill no repositório próprio (github.com/GiovaneMiranda15/re-copilot); RE_COPILOT sobrepõe
SKILL = Path(os.environ.get("RE_COPILOT", REPO.parent / "re-copilot")).expanduser()
TIMOVI = Path.home() / "workspace" / ".agents" / "skills" / "timovi"
ENTREGAS = ("01-diagnostico.md", "02-negocio.md", "03-tecnico.md", "04-backlog.md", "05-jira.csv", "06-azure-devops.csv",
            "07-rastreabilidade.md", "08-mudancas.md")
EXCLUIR = {".venv", "__pycache__", ".pytest_cache", "exemplos", "tests", "install.sh"}


def base(args) -> Path:
    return VALID / "experimento" / args.rodada


def congela(origem: Path, destino: Path) -> None:
    if destino.exists():
        return
    shutil.copytree(origem, destino, ignore=lambda _, names: [n for n in names if n in EXCLUIR or n.endswith(".db")])


def cmd_preparar(args) -> int:
    root = base(args)
    root.mkdir(parents=True, exist_ok=True)
    problemas = []
    testes = subprocess.run(["uv", "run", "--project", "engine", "pytest", "tests", "engine/tests", "-q"], cwd=SKILL,
                            capture_output=True, text=True)
    print("testes:", testes.stdout.strip().splitlines()[-1] if testes.stdout.strip() else testes.stderr[-200:])
    if testes.returncode:
        problemas.append("testes da skill falhando")
    congela(SKILL, root / "skills" / "re-copilot")
    if TIMOVI.exists():
        congela(TIMOVI, root / "skills" / "timovi")
    else:
        problemas.append(f"timovi não encontrada em {TIMOVI}")
    if (root / "skills" / "re-copilot" / "exemplos").exists():
        problemas.append("cópia da skill contém os casos de exemplo")
    shutil.copy(VALID / "briefing-comum.md", root / "briefing-comum.md")
    print("skills congeladas em", root / "skills")
    print("PROBLEMAS:" if problemas else "ambiente ok", *problemas)
    return 1 if problemas else 0


def cmd_selar(args) -> int:
    root = base(args)
    caso = root / "caso"
    selado = root / "sealed"
    selado.mkdir(parents=True, exist_ok=True)
    for nome in ("gabarito.md", "oraculo.md", "mudancas"):
        origem, destino = caso / nome, selado / nome
        if origem.exists() and not destino.exists():
            shutil.move(str(origem), destino)
    faltam = [n for n in ("gabarito.md", "oraculo.md", "mudancas") if not (selado / n).exists()]
    if faltam or not (caso / "fontes").exists():
        print("caso incompleto:", faltam or "sem fontes", file=sys.stderr)
        return 1
    rotulos = [p for p in caso.rglob("*") if p.is_file() and re.search(r"gabarito|armadilha", p.read_text(errors="replace"), re.I)]
    if rotulos:
        print("ATENÇÃO, fontes com rótulo de gabarito:", rotulos)
        return 1
    for cond in args.condicoes:
        run = root / "runs" / cond
        (run / "entrega").mkdir(parents=True, exist_ok=True)
        if not (run / "fontes").exists():
            shutil.copytree(caso / "fontes", run / "fontes")
        shutil.copy(caso / "escopo.md", run / "escopo.md")
        shutil.copy(root / "briefing-comum.md", run / "BRIEFING.md")
    print("execuções criadas:", ", ".join(args.condicoes))
    return 0


def etapa(run: Path) -> str:
    e = run / "entrega"
    if (e / "08-mudancas.md").exists():
        return "concluída"
    if (run / "mudancas").exists():
        return "fazendo etapa 3"
    if all((e / n).exists() for n in ENTREGAS[:7]):
        return "etapa 2 pronta: rodar `mudancas` e liberar a etapa 3"
    if (e / "respostas.md").exists():
        return "fazendo etapa 2"
    if (e / "perguntas.md").exists() and (e / "01-diagnostico.md").exists():
        return "etapa 1 pronta: aguardando respostas"
    return "fazendo etapa 1" if (run / "BRIEFING.md").exists() else "não criada"


def cmd_status(args) -> int:
    root = base(args)
    print("skills:", "ok" if (root / "skills" / "re-copilot").exists() else "falta `preparar`")
    print("caso:", "selado" if (root / "sealed" / "gabarito.md").exists() else "pendente")
    for cond in args.condicoes:
        print(f"  {cond}: {etapa(root / 'runs' / cond)}")
    print("oráculo:", sorted(p.name for p in (root / "oraculo").glob("respostas-*.md")) or "sem respostas")
    print("juízes:", sorted(p.name for p in (root / "juizes").glob("juiz-*.json")) or "nenhum")
    return 0


def cmd_oraculo(args) -> int:
    root = base(args)
    destino = root / "oraculo"
    destino.mkdir(exist_ok=True)
    mapa_path = root / "sealed" / "oraculo-map.json"
    if mapa_path.exists():
        mapa = json.loads(mapa_path.read_text())
    else:
        letras = list("xyzw")[: len(args.condicoes)]
        random.SystemRandom().shuffle(letras)
        mapa = dict(zip(args.condicoes, letras))
        mapa_path.write_text(json.dumps(mapa))
    for cond, letra in mapa.items():
        shutil.copy(root / "runs" / cond / "entrega" / "perguntas.md", destino / f"perguntas-{letra}.md")
    shutil.copy(root / "sealed" / "oraculo.md", destino / "oraculo.md")
    print("pronto para o oráculo em", destino)
    return 0


def cmd_respostas(args) -> int:
    root = base(args)
    mapa = json.loads((root / "sealed" / "oraculo-map.json").read_text())
    for cond, letra in mapa.items():
        origem = root / "oraculo" / f"respostas-{letra}.md"
        shutil.copy(origem, root / "runs" / cond / "entrega" / "respostas.md")
        texto = origem.read_text()
        print(cond, "palavras:", len(texto.split()), "não sei:", len(re.findall(r"N[ãa]o sei", texto)))
    return 0


def cmd_mudancas(args) -> int:
    root = base(args)
    for cond in args.condicoes:
        run = root / "runs" / cond
        if not all((run / "entrega" / n).exists() for n in ENTREGAS[:7]) or (run / "mudancas").exists():
            continue
        foto = root / "sealed" / f"etapa2-{cond}"
        if not foto.exists():
            shutil.copytree(run / "entrega", foto)
        shutil.copytree(root / "sealed" / "mudancas", run / "mudancas")
        print("mudanças entregues a", cond)
    return 0


def cmd_juizes(args) -> int:
    root = base(args)
    saida = root / "juizes"
    if (root / "sealed" / "juiz-map.json").exists():
        print("já preparado; o mapa cego foi mantido")
        return 0
    letras = list("ABCD")[: len(args.condicoes)]
    random.SystemRandom().shuffle(letras)
    mapa = dict(zip(args.condicoes, letras))
    (root / "sealed" / "juiz-map.json").write_text(json.dumps(mapa))
    nomes = re.compile(r"re-?copilot|timovi|\.?product[- ]team|recop\.py|rag-re-engine|\.re/", re.I)
    for cond, letra in mapa.items():
        pasta = saida / letra
        pasta.mkdir(parents=True, exist_ok=True)
        for f in (root / "runs" / cond / "entrega").iterdir():
            if f.is_file():
                (pasta / f.name).write_text(nomes.sub("[método]", f.read_text(errors="replace")))
    shutil.copytree(root / "caso" / "fontes", saida / "fontes", dirs_exist_ok=True)
    shutil.copy(root / "caso" / "escopo.md", saida / "escopo.md")
    shutil.copytree(root / "sealed" / "mudancas", saida / "mudancas", dirs_exist_ok=True)
    for nome in ("gabarito.md", "oraculo.md"):
        shutil.copy(root / "sealed" / nome, saida / nome)
    print("juízes prontos em", saida, "letras:", sorted(mapa.values()))
    return 0


def cmd_resultado(args) -> int:
    root = base(args)
    res = VALID / "resultados"
    runs = [str(root / "runs" / c) for c in args.condicoes]
    subprocess.run([sys.executable, "-I", str(VALID / "avaliar_entregas.py"), *runs, "--json", str(res / f"{args.rodada}-objetivas.json")],
                   check=True, capture_output=True)
    juizes = sorted((root / "juizes").glob("juiz-*.json"))
    if not juizes:
        print("sem avaliações de juiz ainda")
        return 1
    out = subprocess.run([sys.executable, "-I", str(VALID / "agregar_juizes.py"), *map(str, juizes),
                          "--mapa", str(root / "sealed" / "juiz-map.json"), "--saida", str(res / f"{args.rodada}.json")],
                         check=True, capture_output=True, text=True).stdout
    dados = json.loads(out)
    print("concordância:", dados.get("concordancia"))
    chaves = sorted({k for c in dados["condicoes"].values() for k in c["media"]})
    print("métrica".ljust(26), *[c.ljust(7) for c in args.condicoes])
    for k in chaves:
        print(k.ljust(26), *[str(dados["condicoes"][c]["media"].get(k, "-")).ljust(7) for c in args.condicoes])
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("comando", choices=["preparar", "selar", "status", "oraculo", "respostas", "mudancas", "juizes", "resultado"])
    parser.add_argument("--rodada", default="r04")
    parser.add_argument("--condicoes", default="c1,c2,c6", type=lambda s: s.split(","))
    args = parser.parse_args()
    return globals()[f"cmd_{args.comando}"](args)


if __name__ == "__main__":
    raise SystemExit(main())
