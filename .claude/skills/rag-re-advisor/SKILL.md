---
name: rag-re-advisor
description: Recomenda qual arquitetura RAG (GraphRAG, Self-RAG, Corrective RAG, Adaptive RAG, RAPTOR ou Agentic RAG) usar para uma atividade de Engenharia de Requisitos, com base no framework do TCC "Aplicação de Arquiteturas RAG na Engenharia de Requisitos". Use quando o usuário perguntar qual RAG usar para elicitação, análise, especificação, validação, gerenciamento de mudanças ou rastreabilidade de requisitos.
---

# rag-re-advisor

Esta Skill não decide nada por conta própria — ela só invoca o motor de recomendação
determinístico do pacote `rag-re-advisor` (em `rag-re-advisor/` na raiz deste
repositório) e apresenta o resultado. A fonte da verdade é sempre a saída do comando;
nunca raciocine sobre qual arquitetura recomendar por conta própria nem invente
critérios que não estejam no motor.

## Passos

1. Identifique a atividade de Engenharia de Requisitos que o usuário quer (uma de:
   `elicitacao`, `analise`, `especificacao`, `validacao`, `gerenciamento_mudancas`,
   `rastreabilidade`). Se não estiver claro, pergunte.
2. Opcionalmente, colete sinais de refinamento — só inclua os que o usuário mencionar
   explícita ou implicitamente, nunca invente valores:
   - `--data-volume` (`baixo`/`medio`/`alto`)
   - `--data-structure` (`nao_estruturado`/`semi_estruturado`/`relacional_grafo`)
   - `--needs-traceability` / `--no-needs-traceability`
   - `--needs-external-lookup` / `--no-needs-external-lookup`
   - `--audit-criticality` (`baixo`/`medio`/`alto`)
   - `--latency-budget` (`baixo`/`medio`/`alto`)
3. Rode, a partir da raiz do repositório:

   ```
   uv run --project rag-re-advisor rag-re-advisor recommend --activity <atividade> [sinais opcionais] --json
   ```

4. Apresente ao usuário: a arquitetura recomendada, a pontuação, as justificativas com
   citação (elas já vêm formatadas no JSON), e as alternativas relevantes (pontuação >
   0). Se houver empate no topo (ex.: Self-RAG e Corrective RAG para `analise` sem
   sinais adicionais), diga isso explicitamente em vez de escolher uma arbitrariamente.

## Contexto para embasar a conversa

O motor implementa a Tabela 1 e a Tabela 2 do TCC de Giovane Luna Miranda
(`Proposta De TCC.pdf` e `docs/tabela-2-criterios-secundarios.md`, ambos na raiz do
repositório). Toda citação usada nas justificativas foi verificada contra a fonte
primária — se o usuário pedir mais detalhes sobre uma citação, esses dois documentos
têm o texto completo.
