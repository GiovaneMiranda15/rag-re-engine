# re-copilot: Copiloto de Engenharia de Requisitos para Claude Code

Skill do Claude Code que ajuda engenheiros de software, scrum masters e PMOs a **definir e
manter** os requisitos de qualquer projeto, de qualquer área da empresa:

1. **Lê as fontes que já existem**, organizadas por sistema: documentos, dumps SQL
   (estrutura, triggers, procedures), ERDs, mapas de processo e planilhas.
2. **Diagnostica o cenário atual**: divergências entre sistemas, gargalos, riscos, pontos
   de apoio e oportunidades, sempre com a fonte citada.
3. **Entrevista você na pele de cada perfil**: negócio, gestão/PMO, comercial, marketing,
   financeiro, jurídico/compliance, operações, suporte, dados/BI, UX, arquitetura,
   backend, frontend, DBA, segurança, QA e DevOps. Também cria perfis sob demanda.
4. **Gera os entregáveis**: documentação de negócio (BRD, processos, diagnóstico),
   documentação técnica (SRS, dados, integrações, rastreabilidade) e backlog ágil
   (épicos, features e histórias, com CSV para Jira e Azure DevOps).
5. **Acompanha e mantém os requisitos**: classifica cada informação nova (novo,
   existente, conflitante, complementar), analisa o impacto pelo grafo de requisitos,
   abre pedidos de mudança (CR) e versiona por baseline.

Cada etapa usa a arquitetura RAG mais adequada à atividade de Engenharia de Requisitos
(Agentic, Corrective, RAPTOR, Adaptive, GraphRAG), executada pelo motor que vem junto.

Tudo fica em `.re/` dentro do projeto analisado, então dá para parar e retomar.

## Autocontida

Tudo de que a skill precisa está nesta pasta:

```
re-copilot/
├── SKILL.md            ponto de entrada
├── references/         workflow, modelo, fontes, diagnóstico, entrevista, manutenção, entregáveis, backlog, RAG
├── roles/              17 perfis + _template.md
├── scripts/recop.py    utilitário (só Python padrão): check, render, status, fontes, impacto
├── engine/             motor RAG opcional (Python + uv)
├── exemplos/           casos sintéticos vendas-unificado, rh-admissao e hospital-compras, com gabarito
└── install.sh
```

## Modos de uso

| Modo | Precisa de | O que funciona |
|---|---|---|
| **Sem RAG** | Claude Code + `python3` | tudo, lendo as fontes direto (Read/Grep): bom para poucos documentos |
| **Com RAG** | + [uv](https://docs.astral.sh/uv/) | indexação por sistema, busca semântica, Corrective RAG, métricas de recuperação |

A skill detecta sozinha se o motor está disponível.

## Instalação

```bash
git clone <este repositório> && cd <repo>/skills/re-copilot
./install.sh              # só a skill → ~/.claude/skills/re-copilot
./install.sh --engine     # skill + motor RAG (comando rag-re-engine no PATH)
./install.sh --force      # atualiza uma cópia já instalada
```

Alternativas: copiar a pasta para `<projeto>/.claude/skills/re-copilot` (só aquele
projeto) ou criar um symlink, para quem mantém a skill
(`ln -s "$PWD" ~/.claude/skills/re-copilot`). Reinicie o Claude Code depois de instalar.

Sem `--engine`, a skill ainda consegue usar o motor direto da pasta com
`uv run --project <skill>/engine --extra embeddings`, se o `uv` estiver instalado.

Dependências opcionais do motor:

- `pdftotext` (poppler-utils), para PDFs;
- `claude` CLI no PATH, para o Corrective RAG (análise e validação);
- o modelo de embeddings multilíngue (~220 MB), baixado na primeira indexação.

## Uso

Abra o Claude Code no diretório do projeto e digite `re-copilot` (ou "levantar requisitos
de <escopo>"). Comandos úteis a qualquer momento: `status`, `diagnóstico`,
`entrevistar financeiro`, `buscar desconto em SIS-01`, `mudança: <texto>`,
`impacto RN-004`, `baseline`, `entregáveis`. A lista completa está em `SKILL.md`.

Para experimentar com o caso sintético, siga `exemplos/vendas-unificado/README.md`.

## Arquivos gerados no projeto

`.re/modelo/*.json` é a fonte da verdade (requisitos, elementos, achados, perguntas,
backlog, mudanças). Os `.md` de visão e os entregáveis em `.re/entregaveis/` são gerados a
partir dele. Formato completo em `references/modelo.md`.

Coloque `.re/index.db` no `.gitignore`. Os demais arquivos podem conter trechos de
documentos internos: confira antes de versionar em repositório público.

## Testes

```bash
cd engine && uv run pytest              # motor
uv run --project engine pytest tests    # utilitário recop.py (a partir da pasta da skill)
```
