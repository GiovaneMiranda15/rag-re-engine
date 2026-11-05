# Rodada 01 — re-copilot × IA comum × timovi

Executada em 2026-11-03 e 2026-11-04. Protocolo em `../README.md`. Dados em `../experimento/`.

## Conclusão

**Até aqui, não há evidência de que a re-copilot seja melhor que as alternativas.**

- No diagnóstico, as três condições praticamente empatam (95% a 99% de cobertura). A IA comum já
  encontra quase tudo nos casos testados.
- A **timovi foi a melhor no conjunto**, sobretudo em documentação técnica e rastreabilidade.
- A re-copilot v1 teve as melhores perguntas e o maior volume de citações, mas ficou atrás em backlog e
  técnico. A v2 corrigiu esses dois pontos, e perdeu em honestidade e negócio.
- A re-copilot foi a mais lenta nas duas execuções, e o RAG real dobrou o tempo sem aumentar a cobertura.
- Os testes favoreceram pouco o maior diferencial previsto, a **manutenção ao longo do tempo**: eles
  ocorreram numa única sessão, com o contexto inteiro em memória.

## Cobertura e confiabilidade

Média de 2 juízes cegos. Concordância item a item: vendas 100% (kappa 1,00), RH 98% (kappa 0,85). Os
juízes são o mesmo modelo, então a concordância alta não prova correção.

| Métrica | Vendas c1 | Vendas c2 | Vendas c3 | RH c1 | RH c2 | RH c3 |
|---|---|---|---|---|---|---|
| Cobertura total | 0,95 | 0,95 | 0,95 | 0,965 | **0,986** | 0,951 |
| Divergências | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 |
| Riscos | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 | 0,94 |
| Oportunidades | 1,00 | 1,00 | 1,00 | 0,96 | 1,00 | 0,88 |
| Armadilhas caídas | — | — | — | 1 de 7 | 1 de 7 | **2 de 7** |
| Adicionais falsos ou sem suporte (de 10) | 1,5 | 3,5 | 1,0 | 3,0 | 2,0 | 2,0 |
| Citações corretas (de 10) | 10 | 9 | 10 | 10 | 9 | 10 |
| Classificação de mudanças | 0,90 | 0,90 | 0,90 | 0,80 | 0,80 | **0,90** |
| Impacto de mudanças | 1,00 | 1,00 | 0,90 | 0,95 | 0,95 | 0,95 |

`c1` = IA comum, `c2` = timovi, `c3` = re-copilot v1.

## Qualidade (1 a 5)

| Dimensão | Vendas c1 | Vendas c2 | Vendas c3 | RH c1 | RH c2 | RH c3 |
|---|---|---|---|---|---|---|
| Negócio | 4,5 | 4,5 | 4,0 | 4,0 | **5,0** | 4,0 |
| Técnico | 4,5 | **5,0** | 3,0 | 4,0 | **5,0** | 3,0 |
| Backlog | 4,0 | **5,0** | 2,5 | 3,5 | **4,0** | 3,5 |
| Rastreabilidade | 4,0 | **5,0** | 4,0 | 4,0 | **5,0** | 4,5 |
| Manutenção | **5,0** | 4,5 | 4,0 | 4,0 | **5,0** | **5,0** |
| Honestidade | **5,0** | 4,0 | **5,0** | 4,5 | 4,5 | 4,5 |
| Perguntas | 4,0 | 4,0 | **5,0** | **5,0** | 4,0 | 4,5 |
| **Média** | 4,43 | **4,57** | 3,93 | 4,14 | **4,64** | 4,14 |

## Custo

| Execução | Duração somada | Ferramentas | Contexto final |
|---|---|---|---|
| Vendas c1 | 28,8 min | 46 | 178 mil |
| Vendas c2 | 30,4 min | 33 | 230 mil |
| Vendas c3 | 30,5 min | 34 | 255 mil |
| RH c1 | 11,7 min (\*) | 18 | 194 mil |
| RH c2 | 25,4 min (\*) | 46 | 266 mil |
| RH c3 | 22,7 min (\*) | 35 | 305 mil |
| RH c4 | 57,5 min | 49 | 324 mil |

(\*) Execuções de RH c1, c2 e c3 foram interrompidas por limite de uso; há trechos sem medida. Não
compare os tempos delas entre si com precisão.

## Skill v2 (c4) contra v1 e timovi

Caso RH, 1 juiz cego na mesma rodada (`rh-v2.json`). Com só um juiz, diferenças de 1 ponto são fracas.

| Métrica | c2 timovi | c3 v1 | c4 v2 |
|---|---|---|---|
| Cobertura total | **0,986** | 0,958 | 0,958 |
| Classificação de mudanças | 0,80 | 0,90 | **1,00** |
| Armadilhas caídas | 1 | 1 | 1 |
| Adicionais sem suporte ou falsos | 3 | 1 | 3 |
| Negócio | **5** | 4 | 3 |
| Técnico | 4 | 3 | **5** |
| Backlog | **4** | 3 | **4** |
| Honestidade | 4 | **5** | 3 |
| Perguntas | **5** | 4 | 4 |

- **O que melhorou:** o técnico foi de 3 a 5 e o backlog de 3 a 4. As histórias passaram a ter
  critérios suficientes, e a v2 executou de fato as arquiteturas RAG.
- **O que piorou:** a honestidade foi de 5 a 3. Para cumprir a completude, a v2 trouxe números sem fonte
  (ex.: 99,5% de disponibilidade e 3 s no p95). Foi efeito colateral da regra nova.
- **Variação do juiz:** T1 foi marcada para c3 em uma avaliação e não em outra. Na rodada da v2, T2 foi
  marcada para os três métodos.

## Arquiteturas RAG

Recall por atividade; k=3, LLM Haiku, sem consultas degradadas. Em negrito, a melhor de cada linha.
Cada célula tem de 1 a 3 consultas por caso, e os dois corpora são pequenos (27 e 39 trechos). **Não
sustenta conclusão**: serve para testar o método e levantar hipóteses.

| Atividade (arquitetura da Tabela 1) | Caso | baseline | Indicada | Melhor |
|---|---|---|---|---|
| Elicitação (Agentic) | vendas | 0,41 | **0,69** | Agentic |
| Elicitação (Agentic) | RH | **0,72** | 0,61 | baseline |
| Análise (CRAG / Self-RAG) | vendas | 0,50 | 0,50 / 0,50 | Agentic, 0,75 |
| Análise (CRAG / Self-RAG) | RH | 0,61 | 0,39 / 0,47 | Agentic, 0,69 |
| Especificação (RAPTOR) | vendas | 0,17 | **0,67** | RAPTOR |
| Especificação (RAPTOR) | RH | 0,17 | 0,42 | Adaptive, 0,58 |
| Validação (CRAG) | vendas | 0,17 | 0,17 | GraphRAG, 0,83 |
| Validação (CRAG) | RH | **0,88** | **0,88** | empate |
| Mudanças (Adaptive) | vendas | 0,50 | 0,50 | Agentic, 0,83 |
| Mudanças (Adaptive) | RH | 0,42 | 0,58 | Agentic, 0,83 |
| Rastreabilidade (GraphRAG) | vendas | 0,42 | 0,42 | Agentic, 0,58 |
| Rastreabilidade (GraphRAG) | RH | 0,00 | 0,17 | Agentic, 0,42 |

Resultados gerais (detalhes em `../rag/`):

| Estratégia | Recall vendas / RH | Precisão vendas / RH | Contexto (caracteres) | Latência |
|---|---|---|---|---|
| baseline | 0,37 / 0,49 | 0,38 / 0,64 | 1,2 mil | ~0 s |
| Corrective | 0,32 / 0,48 | **0,71** / **0,83** | **0,3 mil** | 15 s |
| Adaptive | 0,40 / 0,54 | 0,68 / 0,80 | 0,8 mil | 20 s |
| Self-RAG | 0,53 / 0,50 | **0,83** / 0,82 | 0,9 mil | 35 s |
| Agentic | 0,58 / 0,61 | 0,44 / 0,52 | 2,3 mil | 23 s |
| RAPTOR (\*\*) | **0,62** / **0,67** | 0,69 / 0,76 | 4,0 / 2,5 mil | ~0 s |
| GraphRAG | 0,48 / 0,40 | 0,55 / 0,48 | 1,4 mil | ~0 s |

(\*\*) A nota do RAPTOR inclui correção da métrica: um resumo vale pelos documentos que resume. Isso o
favorece, já que um único resumo cobre vários documentos; note o contexto maior. Agora ele é medido em
`*-avaliacao-sem-llm.md`.

Hipóteses para o TCC, a testar em corpora maiores:

- A associação preliminar da Tabela 1 **não se confirmou de forma consistente** nestes dados. RAPTOR em
  Especificação foi a associação mais favorável.
- Agentic e RAPTOR ampliam o que se encontra (recall). CRAG e Self-RAG tornam o contexto mais preciso,
  mas custam mais e o CRAG pode perder recall. É um compromisso, não uma vitória única.
- O CRAG reduz o contexto em cerca de 2/3 sem grande perda de recall em RH, o que pode valer em bases grandes.

## Defeitos encontrados e corrigidos na skill

| Defeito | Origem | Correção |
|---|---|---|
| Exemplos da skill continham as respostas do caso de vendas | revisão antes do teste | exemplos trocados por outro domínio |
| Comando do motor sem `--extra embeddings`, caindo no embedder lexical | c3 vendas | comando corrigido |
| `--llm none` em todas as consultas: as arquiteturas nem rodavam na v1 | c3 vendas e RH | estratégia real por padrão |
| `rag-re-engine` antigo no PATH preferido ao da skill | c4 | motor da skill tem prioridade |
| Backlog magro: um critério por história, sem migração nem auditoria | juízes | mínimo de 2 critérios, cobertura transversal, `recop.py lint` |
| Técnico magro: sem estados nem dicionário | juízes | ciclo de vida, campos e ADRs obrigatórios |
| Perguntas defasadas depois de um CR | juízes | revisão obrigatória, apontada pelo `lint` |
| Falso positivo: trecho revogado e total × subconjunto vistos como divergência | juízes | checagem de vigência, abrangência e definição |
| Citação a transcrição interna como se fosse fonte | juízes | entregáveis citam o arquivo original |
| Números inventados para cumprir a completude | juiz da v2 | proposta só com `[hipótese]`; `lint` aponta confirmados sem prova |
| BRD sem síntese para decisão, com riscos só em título | juiz da v2 | seção de síntese e riscos completos |
| Métrica não dava crédito aos resumos do RAPTOR | revisão dos resultados | `score` usa `derived_from` |

**Os quatro últimos e a regra de falsos positivos ainda não foram retestados** (versão atual, v3).

## Limitações

- **Uma execução por condição:** sem repetição, não dá para medir a variação do próprio modelo.
- **Autoria:** o caso de vendas é do mesmo autor da skill, e tem efeito teto. O de RH foi feito por um
  agente independente, mas de mesma origem. Todos são sintéticos e pequenos.
- **Sem pessoas:** o oráculo e os juízes são IA. A entrevista interativa, um ponto central da skill, foi
  testada só no modo delegado, com uma rodada de 15 perguntas.
- **Cegamento parcial:** os nomes foram removidos, mas o estilo das citações pode revelar o método.
- **timovi fora de seu uso:** foi feita para o ciclo de feature, não para esse levantamento. A IA comum e
  ela seguiram o mesmo briefing, que já pede explicitamente as entregas certas. Isso reduz a vantagem
  de um método que estrutura o trabalho.
- **Não testado:** importação real no Jira e no Azure DevOps (só o formato do CSV); projetos grandes;
  retomada entre sessões.
- **Métrica de citação do script:** só detecta nome de arquivo com extensão, e por isso subestima c1 e c2.
  O script de vazamento de dados marca termos como "São Paulo"; na conferência manual dos alertas, os
  termos eram nomes de empresa, curso e cidade, e não dados pessoais.
- **Incidentes:** limites de uso interromperam as execuções, e um reinício apagou o `/tmp`. Os dados foram
  reconstruídos a partir dos transcripts:
  - RH c1, c2 e c3 retomaram a partir desse estado reconstruído, e c3 passou a ter scripts mais novos à
    disposição nas etapas 2 e 3, embora tivesse lido as instruções da v1;
  - os CSVs de vendas c3 não foram recuperados. Os números deles foram medidos antes da perda (55 linhas
    em cada CSV, ambos válidos);
  - o juiz 1 de vendas não leu os CSVs e escolheu a amostra de citações sem sorteio;
  - o mapa cego de vendas foi recuperado por similaridade de texto (1,0 / 0,99 / 0,99).

## Próximos passos sugeridos

1. **Testar a manutenção entre sessões**, o ponto em que a skill pode de fato se diferenciar: novas
   comunicações em uma sessão nova, sem o contexto anterior, medindo o acerto do impacto e o custo.
2. Retestar a v3, com 3 repetições por condição, em ao menos 1 caso novo maior.
3. Avaliar se o custo do RAG compensa: com poucos documentos, ler direto parece bastar. Definir um limiar.
4. Considerar ler da timovi o que funcionou: 30 cenários de teste e várias matrizes de rastreabilidade.
5. Rodar a avaliação com engenheiros (`../README.md`).
