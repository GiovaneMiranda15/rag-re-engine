# TCC — RAG aplicado à Engenharia de Requisitos

Repositório do TCC de Giovane Luna Miranda: **"Aplicação de Arquiteturas
Retrieval-Augmented Generation (RAG) na Engenharia de Requisitos: Uma Proposta de
Framework para Apoio às Atividades do Processo de Requisitos"**.

## Conteúdo

- `Proposta De TCC.pdf` — proposta original, com a Tabela 1 (associação preliminar
  entre atividades de Engenharia de Requisitos e arquiteturas RAG).
- `docs/tabela-2-criterios-secundarios.md` — extensão da Tabela 1 com critérios
  secundários de refinamento, cada um fundamentado em fonte primária verificada.
  Inclui também correções a duas citações incorretas identificadas na proposta
  original (Adaptive RAG e RAPTOR).
- `*.pdf` — artigos de referência (Lewis et al. 2020; Gao et al. 2023; surveys de
  GraphRAG e Modular RAG).
- `rag-re-advisor/` — Fase 1 do projeto prático: motor de recomendação determinístico
  que operacionaliza as Tabelas 1 e 2 como ferramenta, exposto como CLI, servidor MCP
  e Claude Skill. Ver `rag-re-advisor/README.md`.
- `.claude/skills/rag-re-advisor/` — Skill de projeto que usa o motor acima.

## Fases do projeto prático

1. **Guia de decisão** (`rag-re-advisor/`, em andamento) — motor baseado em regras,
   auditável, sem implementar nenhum pipeline RAG de verdade.
2. **Orquestrador funcional parcial** (planejado) — validar 1-2 arquiteturas reais
   contra um estudo de caso, começando pela atividade de Análise.
3. **Cobertura completa do ciclo de vida** (ambição de longo prazo, fora do escopo
   obrigatório da defesa).

Prazo do TCC: junho de 2027.
