---
name: rag-re-advisor
description: Recomenda qual arquitetura RAG (GraphRAG, Self-RAG, Corrective RAG, Adaptive RAG, RAPTOR ou Agentic RAG) usar para uma atividade de Engenharia de Requisitos, com base no framework do TCC "Aplicação de Arquiteturas RAG na Engenharia de Requisitos", e opcionalmente executa a recomendação sobre um corpus indexado. Use quando o usuário perguntar qual RAG usar para elicitação, análise, especificação, validação, gerenciamento de mudanças ou rastreabilidade de requisitos.
---

# rag-re-advisor

Esta Skill não decide nada por conta própria — ela só invoca o motor de recomendação
determinístico do pacote `rag-re-advisor` (em `rag-re-advisor/` na raiz deste
repositório) e apresenta o resultado. A fonte da verdade é sempre a saída do comando;
nunca raciocine sobre qual arquitetura recomendar por conta própria nem invente
critérios que não estejam no motor.

## Passos

1. **Atividade** (obrigatória) — uma de: `elicitacao`, `analise`, `especificacao`,
   `validacao`, `gerenciamento_mudancas`, `rastreabilidade`. Se não estiver clara,
   pergunte (uma pergunta só, listando as opções).

2. **Sinais de refinamento** (opcionais) — inclua apenas os que o usuário mencionar
   explícita ou implicitamente; nunca invente valores. Não interrogue o usuário sobre
   todos: só os valores abaixo alteram o resultado, os demais são aceitos mas neutros.

   | O usuário diz algo como… | Flag | Efeito no motor |
   |---|---|---|
   | "base extensa", "muitos documentos" | `--data-volume alto` | +2 RAPTOR |
   | "requisitos ligados a testes/código", "grafo", "rastrear dependências" | `--data-structure relacional_grafo` e/ou `--needs-traceability` | +2 GraphRAG (critério único, não soma duas vezes) |
   | "base incompleta/desatualizada", "consultar normas externas" | `--needs-external-lookup` | +2 Corrective RAG |
   | "não pode alucinar", "auditoria", "regulatório", "crítico" | `--audit-criticality alto` | +2 Self-RAG e +2 Corrective RAG |
   | "precisa ser rápido/barato", "poucos recursos" | `--latency-budget baixo` | +2 Adaptive RAG; **veta** Agentic RAG |
   | "tempo/recursos de sobra" | `--latency-budget alto` | +2 Agentic RAG |

3. Rode, a partir da raiz do repositório:

   ```
   uv run --project rag-re-advisor rag-re-advisor recommend --activity <atividade> [sinais] --json
   ```

4. Apresente, de forma concisa:
   - `top`: arquitetura recomendada, pontuação e justificativas (já vêm com citação);
   - se `tie` não estiver vazio: diga explicitamente que há empate entre as arquiteturas
     listadas e que a ordem entre elas é arbitrária — não escolha uma. Para `analise`,
     informe que o único sinal que desempata é a necessidade de busca externa (favorece
     o Corrective RAG);
   - alternativas com `score > 0` e `viable: true`;
   - alternativas com `viable: false`: diga que foram descartadas e cite o `blockers`
     (ex.: Agentic RAG com orçamento de latência baixo), mesmo que a pontuação seja maior.
   - se o `top` tiver pontuação baixa e nenhuma afinidade primária (ex.: após um veto),
     diga isso ao usuário em vez de apresentar como recomendação forte.

5. **Execução (opcional, Fase 2)** — se o usuário quiser aplicar a recomendação sobre um
   corpus, ofereça o `rag-re-engine` (só `corrective_rag` e `baseline` estão
   implementados; outras arquiteturas caem no baseline com aviso em `notes`):

   ```
   uv run --project rag-re-engine rag-re-engine index <pasta-do-corpus> --db <arquivo.db>
   uv run --project rag-re-engine rag-re-engine retrieve --db <arquivo.db> --activity <atividade> --query "<consulta>"
   ```

   Não rode `index` sem confirmar a pasta do corpus com o usuário.

## Semântica da pontuação (para responder perguntas sobre o resultado)

- Afinidade primária (Tabela 1) vale 5; cada critério secundário (Tabela 2) vale 2.
- Os critérios secundários **refinam dentro da atividade**: desempatam e ordenam
  alternativas, mas não trocam a arquitetura primária — exceto quando uma
  **pré-condição de viabilidade** é violada (hoje, só Agentic RAG com latência baixa),
  caso em que a arquitetura é vetada.

## Contexto para embasar a conversa

O motor implementa a Tabela 1 e a Tabela 2 do TCC de Giovane Luna Miranda
(`Proposta De TCC.pdf` e `docs/tabela-2-criterios-secundarios.md`, ambos na raiz do
repositório). Toda citação usada nas justificativas foi verificada contra a fonte
primária — se o usuário pedir mais detalhes sobre uma citação, esses dois documentos
têm o texto completo.
