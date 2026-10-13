# re-copilot — Copiloto de Engenharia de Requisitos para Claude Code

Skill do Claude Code que conduz as atividades de Engenharia de Requisitos de um projeto
(escopo → contexto → entrevistas por perfil → análise → especificação → validação →
rastreabilidade). Ela consulta documentos via RAG (opcional) e o código do projeto, e
entrevista você assumindo cada perfil: negócio, UX, frontend, backend, DBA, arquiteto,
segurança, QA e DevOps.

Tudo fica salvo em `.re/` dentro do projeto analisado, então dá para parar e retomar
depois.

Base teórica: TCC "Aplicação de Arquiteturas RAG na Engenharia de Requisitos"
(Giovane Luna Miranda).

## Modos de uso

| Modo | Requisitos | O que funciona |
|---|---|---|
| **Sem RAG** | só o Claude Code | entrevistas por perfil, leitura do código, requisitos e rastreabilidade em `.re/` |
| **Com RAG** | + `rag-re-engine` | também indexa documentos (txt/md/pdf) e cita evidências `[doc: arquivo#n]` |

A skill detecta sozinha se o motor está disponível; sem ele, avisa e segue sem RAG.

## Instalação

### 1. Skill (obrigatório)

```bash
git clone https://github.com/GiovaneMiranda15/rag-re-engine.git
cd rag-re-engine/skills/re-copilot
./install.sh            # ou ./install.sh --engine para já instalar o motor RAG
```

O script copia esta pasta para `~/.claude/skills/re-copilot` (ou para
`$CLAUDE_SKILLS_DIR/re-copilot`). Alternativas manuais:

- **cópia**: `cp -r re-copilot ~/.claude/skills/`
- **só em um projeto**: copie para `<projeto>/.claude/skills/re-copilot`
- **symlink** (para quem mantém a skill): `ln -s "$PWD" ~/.claude/skills/re-copilot`

Reinicie o Claude Code depois de instalar.

### 2. Motor RAG (opcional)

Pré-requisitos: [uv](https://docs.astral.sh/uv/) e Python ≥ 3.12.

**Opção A — instalar do GitHub (recomendado, não precisa de clone):**

```bash
uv tool install "rag-re-engine[embeddings] @ git+https://github.com/GiovaneMiranda15/rag-re-engine.git#subdirectory=rag-re-engine"
# ou: ./install.sh --engine            (do GitHub)
#     ./install.sh --engine <clone>    (de um clone local)
```

O executável `rag-re-engine` vai para o `PATH` (`~/.local/bin`). Para atualizar, rode
`uv tool upgrade rag-re-engine`.

**Opção B — usar direto de um clone (para desenvolvimento):**

```bash
export RAG_RE_HOME=/caminho/do/clone   # coloque no ~/.bashrc ou ~/.zshrc
```

Dependências opcionais do motor:

- `pdftotext` (pacote `poppler-utils`) para indexar PDFs;
- `claude` CLI no `PATH` para o Corrective RAG (fases `analise`/`validacao`). Sem ele,
  use consultas com `--llm none`;
- na 1ª indexação, o modelo de embeddings multilíngue (~220 MB) é baixado.

Verificação:

```bash
rag-re-engine --help                                  # opção A
uv run --project "$RAG_RE_HOME/rag-re-engine" rag-re-engine --help   # opção B
```

## Uso

Abra o Claude Code no diretório do projeto a analisar e digite `re-copilot` (ou peça
"levantar requisitos de <escopo>"). Na primeira execução, a skill confirma o diretório
e cria `.re/`.

Comandos que você pode dar a qualquer momento:

| Você diz | Ação |
|---|---|
| `status` | painel com fase, perfis e pendências |
| `entrevistar backend` / `agora como DBA` | entrevista na ótica do perfil |
| `próximo` | encerra o perfil atual com resumo |
| `indexar docs/` | indexa documentos no RAG |
| `buscar <assunto>` | consulta o RAG e mostra evidências |
| `analisar` / `especificar` / `validar` / `rastreabilidade` | executa a fase |
| `requisito RF-003` | mostra o requisito com fontes e histórico |

## Arquivos gerados no projeto (`.re/`)

- `state.json`: fase atual, perfis e índice
- `escopo.md`: escopo reformulado e glossário
- `contexto.md`: achados do RAG e do código, com citações
- `requisitos.md`: fonte da verdade dos requisitos (status `hipótese`, `confirmado`,
  `conflito`, `validado` ou `descartado`, com fontes)
- `perguntas-abertas.md`: lacunas com responsável
- `entrevistas/<perfil>.md`: resumo das perguntas e respostas de cada perfil
- `especificacao.md` e `rastreabilidade.md`: documentos das fases finais
- `index.db`: índice RAG (se usado). Coloque no `.gitignore`
- `log-rag.jsonl`: log das consultas RAG

Formato completo em `references/artefatos.md`. Os `.md` podem conter trechos de
documentos internos: confira antes de versionar em repositório público.

## Estrutura da skill

```
re-copilot/
├── SKILL.md            # ponto de entrada (lido pelo Claude Code)
├── README.md           # este arquivo
├── install.sh          # instalador
├── references/         # workflow, entrevista, RAG, formato dos artefatos
└── roles/              # ótica e perguntas-semente de cada perfil
```
