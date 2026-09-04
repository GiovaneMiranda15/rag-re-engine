# rag-re-advisor

Motor de recomendação **determinístico e baseado em regras** que sugere qual
arquitetura RAG (GraphRAG, Self-RAG, Corrective RAG, Adaptive RAG, RAPTOR ou Agentic
RAG) usar para cada atividade da Engenharia de Requisitos. É a Fase 1 do TCC
"Aplicação de Arquiteturas Retrieval-Augmented Generation (RAG) na Engenharia de
Requisitos" (Giovane Luna Miranda) — a Tabela 1 e a Tabela 2 da proposta,
operacionalizadas como ferramenta.

Todas as regras e citações usadas aqui vêm de `../docs/tabela-2-criterios-secundarios.md`,
onde cada critério foi verificado contra a fonte primária antes de virar código. Não é
um motor de RAG de verdade (não faz embeddings, não consulta vector store, não chama
LLM) — só decide *qual* arquitetura usar, com base nas características da tarefa.

## Instalação

Requer [uv](https://docs.astral.sh/uv/).

```bash
cd rag-re-advisor
uv sync
```

## Uso — CLI

```bash
uv run rag-re-advisor recommend --activity rastreabilidade --needs-traceability

uv run rag-re-advisor recommend --activity analise --audit-criticality alto --json
```

Atividades válidas: `elicitacao`, `analise`, `especificacao`, `validacao`,
`gerenciamento_mudancas`, `rastreabilidade`.

Sinais opcionais de refinamento: `--data-volume {baixo,medio,alto}`,
`--data-structure {nao_estruturado,semi_estruturado,relacional_grafo}`,
`--needs-traceability`/`--no-needs-traceability`,
`--needs-external-lookup`/`--no-needs-external-lookup`,
`--audit-criticality {baixo,medio,alto}`, `--latency-budget {baixo,medio,alto}`.

## Uso — servidor MCP

```bash
uv run rag-re-advisor-mcp
```

Expõe a tool `recommend_rag_architecture` via stdio. Para registrar no Claude Code:

```bash
claude mcp add rag-re-advisor -- uv run --project /caminho/para/rag-re-advisor rag-re-advisor-mcp
```

## Uso — Claude Skill

A Skill do projeto está em `../.claude/skills/rag-re-advisor/SKILL.md` — é carregada
automaticamente pelo Claude Code quando você trabalha nesta pasta.

## Testes

```bash
uv run pytest
```

Os testes verificam, entre outras coisas, que o motor reproduz exatamente o
mapeamento primário da Tabela 1 para as 6 atividades.
