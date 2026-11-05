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
- `skills/re-copilot/` — Skill **autocontida** de Engenharia de Requisitos para qualquer
  projeto e área: lê as fontes por sistema (docs, dumps SQL, ERDs), diagnostica o cenário
  atual, entrevista por perfil (17 perfis técnicos e de negócio), gera documentação de
  negócio, técnica e backlog (Jira/Azure DevOps) e **acompanha e mantém** os requisitos
  (classificador, impacto pelo grafo, CRs, baselines). Persiste em `.re/` no projeto alvo.
  Desenho em `docs/re-copilot-design.md`. Instalação:

  ```bash
  skills/re-copilot/install.sh --engine   # skill + motor RAG
  ```
- `skills/re-copilot/engine/` — motor RAG (Fase 2), embutido na skill: executa a
  arquitetura indicada para cada atividade (Corrective RAG + baseline implementados), com
  avaliação comparativa e *context provider*. Não depende do `rag-re-advisor`: o mapa
  atividade → arquitetura (Tabela 1) está embutido em `strategies.py`.

  Detalhes e uso sem RAG em `skills/re-copilot/README.md`.

  Uso: em qualquer projeto, `claude` → "re-copilot: escopo é <...>" ou `/re-copilot`.

## Fases do projeto prático

1. **Guia de decisão** (`rag-re-advisor/`, em andamento) — motor baseado em regras,
   auditável, sem implementar nenhum pipeline RAG de verdade.
2. **Orquestrador funcional parcial** (`skills/re-copilot/engine/`, em andamento: Corrective RAG + baseline para Análise) — validar 1-2 arquiteturas reais
   contra um estudo de caso, começando pela atividade de Análise.
3. **Cobertura completa do ciclo de vida** (ambição de longo prazo, fora do escopo
   obrigatório da defesa).

Prazo do TCC: junho de 2027.
