# re-copilot v2 — Desenho

> Status: **F1 a F4 implementadas (v3)** · 2026-11-04 · validação em `docs/validacao/` · decisões da seção 12 tomadas

## 1. Objetivo

Copiloto que ajuda engenheiro de software, scrum master ou PMO a **definir e manter** os
requisitos de qualquer projeto de qualquer área da empresa. Ele:

1. lê as fontes existentes (documentos, dumps de banco, ERDs, mapas de processo, exports);
2. atua nos perfis da empresa (técnicos e de negócio) para entrevistar o usuário;
3. diagnostica o cenário atual (divergências, gargalos, riscos, pontos de apoio, oportunidades);
4. produz documentação de negócio, documentação técnica e backlog ágil;
5. **acompanha e mantém** os requisitos: detecta informação nova, classifica (novo,
   existente, conflitante, complementar), analisa impacto e versiona. **Foco do TCC.**

Em cada etapa, a recuperação usa a arquitetura RAG que o framework do TCC (Tabela 1)
associa à atividade. O usuário não escolhe a arquitetura: a skill escolhe e registra.

**Caso de referência:** novo sistema de vendas unificado, que substitui um sistema atual
e vários sistemas isolados.

## 1.1 Independência

A skill é **autocontida**: tudo fica em `skills/re-copilot/` (referências, perfis,
`scripts/recop.py`, motor RAG em `engine/`, caso sintético em `exemplos/`). Ela não
depende dos arquivos do TCC nem do `rag-re-advisor`: o mapa atividade → arquitetura está
embutido em `engine/src/rag_re_engine/strategies.py`. O TCC usa a skill como estudo de
caso, mas a skill não depende do TCC.

## 2. Princípios (mantidos da v1)

- Nada vira `confirmado` sem resposta humana ou evidência citada; o resto é `hipótese`.
- Toda afirmação cita fonte: `[doc: <chunk_id>]`, `[sql: arquivo:objeto]`,
  `[entrevista: <perfil> Q-NNN]`.
- Acesso **somente leitura** às fontes. Na fase 1, nenhuma conexão direta a banco ou sistema.
- Persistir após cada passo relevante; tudo em `.re/`.
- Dados pessoais: nunca copiar linhas de dados de dumps; ler só a estrutura (DDL, procedures, triggers).

## 3. Fontes

### 3.1 Registro de fontes — `.re/fontes.json`

Cada fonte pertence a um **sistema** (ou "documentação geral"). É isso que permite
comparar o que o sistema A faz com o que o sistema B faz.

```json
{
  "sistemas": [
    {"id": "SIS-01", "nome": "ERP Vendas atual", "papel": "legado-principal"},
    {"id": "SIS-02", "nome": "Planilha de comissões", "papel": "satelite"}
  ],
  "fontes": [
    {"id": "F-001", "sistema": "SIS-01", "tipo": "ddl", "path": "fontes/erp/schema.sql",
     "sha256": "…", "indexado_em": "2026-11-03T10:00:00Z"}
  ]
}
```

`tipo` ∈ `documento | ddl | erd | processo | planilha | export | outro`.

### 3.2 Formatos na fase 1

| Formato | Como entra |
|---|---|
| txt, md, pdf | motor RAG (já suportado) |
| `.sql` (dump/backup) | extrator de **estrutura**: tabelas, colunas, PK/FK, constraints, procedures, triggers e views. Linhas `INSERT`/`COPY` são descartadas antes de indexar |
| ERD (png, jpg, pdf) | o Claude lê a imagem e transcreve entidades e relações para `.md`, que é indexado |
| drawio, bpmn (XML) | extração de texto (nomes de raias, tarefas, gateways) para `.md` |
| csv, xlsx | cabeçalhos e uma amostra mínima, sem dados pessoais; ou o usuário exporta para md |
| docx | conversão para texto (pandoc, se existir) |

Depois, fora da fase 1: conexão read-only a banco ou API via MCP.

### 3.3 Detecção de mudança

Ao reindexar (comando `atualizar fontes` ou ao ativar a skill), a skill compara o
`sha256` de cada fonte. Fonte nova ou alterada **dispara o modo manutenção** (seção 7)
apenas sobre o que mudou.

## 4. Perfis

Mantém os 9 atuais e adiciona estes:

| Perfil | Ótica |
|---|---|
| `gestao-pmo` | prazos, custo, dependências, riscos de projeto, governança |
| `comercial` | funil, propostas, preços, descontos, comissões, metas |
| `marketing` | campanhas, segmentação, canais, LGPD de marketing |
| `financeiro` | faturamento, fiscal, conciliação, inadimplência |
| `juridico-compliance` | contratos, regulação setorial, LGPD, auditoria |
| `operacoes` | processo do dia a dia, exceções, gargalos manuais |
| `suporte` | chamados, reclamações, SLA de atendimento |
| `dados-bi` | indicadores, relatórios, fonte da verdade dos números |

O **perfil sob demanda** (`entrevistar como <qualquer área>`) é gerado a partir de
`roles/_template.md` e salvo em `.re/perfis/` do projeto.

## 5. Modelo de dados: o grafo de requisitos

Hoje `requisitos.md` é a fonte da verdade. Para a manutenção e o GraphRAG funcionarem,
o modelo passa a ser **estruturado**, e os `.md` passam a ser gerados a partir dele.

```
.re/modelo/
├── requisitos.json   RF, RNF, RN (com versões)
├── elementos.json    processos, entidades de dados, atores, integrações, regras existentes
├── achados.json      divergências, gargalos, riscos, apoio, oportunidades
├── perguntas.json    lacunas com responsável
├── backlog.json      épicos, features, histórias
└── mudancas.json     CR-NNN (pedidos de mudança)
```

As arestas ficam **embutidas** em cada item (campo `rel` + campos de referência como
`pai`, `requisitos`, `sistemas`), em vez de um `links.json` separado: um só lugar para
editar. `scripts/recop.py` monta o grafo, valida (`check`), gera as visões (`render`) e
percorre o impacto (`impacto`). Formato completo em `skills/re-copilot/references/modelo.md`.

Arestas: `deriva_de` (req → fonte), `implementado_em` (regra → sistema),
`depende_de`, `conflita_com`, `complementa`, `substitui`, `detalha` (história → req),
`afeta` (CR → req/história), `responsavel` (req → perfil).

Requisito:

```json
{"id": "RN-004", "versao": 3, "tipo": "regra", "enunciado": "…", "status": "confirmado",
 "prioridade": "Must", "criterios_aceite": ["…"], "fontes": ["doc:politica.pdf#3"],
 "historico": [{"versao": 2, "data": "…", "mudanca": "CR-007", "antes": "…"}]}
```

Status: `hipótese | confirmado | conflito | validado | alterado | obsoleto | descartado`.

**Baseline:** foto versionada do conjunto validado (`.re/baselines/B-001.json`). As
mudanças são medidas contra a baseline vigente.

## 6. Fluxo principal

| Fase | O que faz | Arquitetura (Tabela 1) |
|---|---|---|
| `escopo` | reformula o escopo e o glossário; cria o `state.json` **logo no início** | — |
| `fontes` | registra os sistemas e as fontes, extrai e indexa | — |
| `diagnostico` | relatório do cenário atual (seção 6.1) | Agentic RAG (decomposição) + CRAG (checagem de divergências); RAPTOR para resumir sistemas grandes |
| `elicitacao` | entrevistas por perfil, consultando as fontes antes de cada pergunta | Agentic RAG |
| `analise` | qualidade (ISO/IEC/IEEE 29148), conflitos, duplicidades, lacunas | Self-RAG / CRAG |
| `especificacao` | gera os entregáveis (seção 8) | RAPTOR |
| `validacao` | revisão com o usuário e checagem contra normas e documentos | CRAG |
| `baseline` | congela a versão validada | — |
| `manutencao` | modo contínuo (seção 7) | Adaptive RAG + GraphRAG |

O usuário pode pular ou voltar fases. A `manutencao` fica ativa a partir da primeira baseline.

### 6.1 Diagnóstico — `.re/diagnostico.md`

Para cada processo (ex.: pedido → faturamento → comissão):

- **Mapa:** sistemas envolvidos, entidades e regras de cada um, com citações.
- **Divergências:** tabela regra × sistema (ex.: o desconto máximo é 10% no SIS-01 e 15% no SIS-02).
- **Gargalos:** passos manuais, redigitação, integração por planilha, dado duplicado.
- **Riscos:** probabilidade × impacto, com origem.
- **Pontos de apoio:** o que já funciona bem e deve ser preservado ou reaproveitado.
- **Oportunidades:** o que o sistema unificado resolve ou habilita.

Cada item gera uma hipótese de requisito ou uma pergunta para o perfil responsável.

## 7. Manutenção (foco do TCC)

### 7.1 Gatilhos

1. **Manual:** "chegou esta mudança: …", ou um documento ou ata colado na conversa.
2. **Fonte nova ou alterada:** detectada pelo hash (3.3).
3. **Durante qualquer fase:** toda informação nova (resposta de entrevista, trecho de
   documento) passa pelo classificador. Assim a manutenção não é uma fase separada:
   está embutida no fluxo inteiro.

### 7.2 Classificador

| Classe | Critério | Ação |
|---|---|---|
| `novo` | nenhum requisito equivalente | cria como hipótese ou confirmado, conforme a fonte |
| `existente` | equivalente a REQ-X | acrescenta a fonte em REQ-X (reforça) |
| `conflitante` | contradiz REQ-X ou outra fonte | marca `conflito`, abre CR e pergunta ao responsável |
| `complementar` | detalha ou estende REQ-X | propõe nova versão de REQ-X ou um requisito filho (`complementa`) |
| `fora_escopo` | — | registra em escopo › fora do escopo |

Mecânica: busca dos candidatos no modelo (similaridade sobre os enunciados) mais uma
decisão do LLM, com justificativa e fontes.

### 7.3 Análise de impacto

1. O **Adaptive RAG** classifica a mudança:
   - **simples:** afeta 1 requisito, sem dependências; consulta direta.
   - **moderada:** várias fontes; CRAG.
   - **complexa:** cruza sistemas, regras e backlog; GraphRAG multi-hop.
2. O **GraphRAG** percorre o grafo do modelo (`recop.py impacto`) a partir dos nós afetados e chega a requisitos
   dependentes, regras, sistemas, histórias do backlog, critérios de aceite e perfis
   responsáveis.
3. Gera o **CR-NNN** em `mudancas.json` e `.re/mudancas/CR-NNN.md` com: descrição,
   origem, classe, itens afetados (diretos e indiretos), risco, esforço relativo, perfis
   a consultar e recomendação.
4. O usuário **aprova, ajusta ou rejeita**. Se aprovar: nova versão dos requisitos,
   histórias afetadas marcadas `revisar`, entregáveis regenerados, log atualizado.

### 7.4 Métricas para o TCC

`.re/log-rag.jsonl` ganha estes campos: `gatilho`, `classe`, `complexidade` (Adaptive),
`n_afetados`, `hops` (GraphRAG), `decisao_usuario`. Com eles dá para medir a precisão do
classificador (decisão do usuário vs. classe proposta), a cobertura de impacto e o custo
por estratégia.

## 8. Entregáveis — `.re/entregaveis/`

| Documento | Conteúdo |
|---|---|
| `negocio/brd.md` | objetivo, problema, stakeholders, processos atual e futuro, regras de negócio, indicadores de sucesso, glossário |
| `negocio/processos.md` | fluxos atual e futuro (Mermaid), gargalos resolvidos |
| `negocio/diagnostico.md` | relatório da seção 6.1 |
| `tecnico/srs.md` | SRS no padrão ISO/IEC/IEEE 29148: RF, RNF (ISO/IEC 25010), interfaces, restrições |
| `tecnico/dados.md` | modelo conceitual unificado (ER em Mermaid), de-para dos sistemas legados, migração |
| `tecnico/integracoes.md` | sistemas, direção, contratos, tratamento de falha |
| `tecnico/rastreabilidade.md` | matriz requisito × fonte × sistema × história × teste |
| `backlog/backlog.md` | épicos → features → histórias (Como/Quero/Para), critérios Dado/Quando/Então, prioridade, dependências, requisito de origem |
| `backlog/jira.csv` | formato de importação CSV do Jira |
| `backlog/azure-devops.csv` | formato de importação CSV do Azure Boards (hierarquia por colunas Title 1/2/3) |
| `mudancas.md` | changelog por baseline e CRs |

Os mapeamentos de campos de Jira e Azure DevOps ficam em `references/backlog-export.md`.
Toda história carrega o ID do requisito de origem (label ou tag), para manter a
rastreabilidade depois da importação.

## 9. Mudanças no motor (`rag-re-engine`)

| Item | Para quê | Prioridade |
|---|---|---|
| Metadados no chunk (`sistema`, `tipo`, `fonte_id`) e filtro `--sistema` no retrieve | divergências entre sistemas | F1 |
| Ingest de `.sql` (só estrutura) e de `.md` gerados de ERD/BPMN | fontes de banco e processo | F1 |
| Adaptive RAG | gerenciamento de mudanças | F2 |
| GraphRAG sobre o grafo do modelo + entidades extraídas das fontes | impacto e rastreabilidade | F3 |
| RAPTOR | especificação e resumo de sistemas grandes | F4 |
| Self-RAG, Agentic RAG formal | análise e elicitação (hoje o agente faz a decomposição) | F5 |

## 10. Estrutura da skill

```
re-copilot/
├── SKILL.md                    roteador: ativação, comandos, regras
├── README.md
├── install.sh
├── references/
│   ├── workflow.md             fases e painel
│   ├── fontes.md               registro, extração, detecção de mudança
│   ├── diagnostico.md
│   ├── entrevista.md
│   ├── manutencao.md           gatilhos, classificador, impacto, CR, baseline
│   ├── modelo.md               esquemas JSON do .re/modelo
│   ├── entregaveis.md          templates dos documentos
│   ├── backlog-export.md       Jira / Azure DevOps
│   └── rag.md                  motor, estratégias por fase, log
├── roles/                      17 perfis + _template.md
├── scripts/recop.py            check, render, status, fontes, impacto (Python padrão)
├── engine/                     motor RAG opcional (uv)
├── exemplos/vendas-unificado/  caso sintético + gabarito
└── tests/                      testes do recop.py
```

## 11. Roadmap

| Fase | Entrega | Pronto quando |
|---|---|---|
| **F1** base | escopo com state imediato, registro de sistemas e fontes, extração de `.sql`/ERD/BPMN, metadados no motor, 17 perfis, modelo estruturado, diagnóstico; correção dos bugs da v1 (`ENGINE` entre chamadas, `install.sh --engine`) | caso exemplo com 2 sistemas gera um diagnóstico com divergências citadas |
| **F2** manutenção | classificador, CR, baseline/versões, gatilho por hash, Adaptive RAG | mudança injetada no caso exemplo gera CR com os afetados corretos |
| **F3** entregáveis + grafo | BRD, SRS, dados, backlog md/csv, GraphRAG | CSVs importam no Jira e no Azure DevOps; impacto multi-hop funciona |
| **F4** RAPTOR | especificação sobre bases grandes | avaliação baseline × RAPTOR |
| **F5** estudo de caso | rodar no caso real de vendas e coletar métricas | dados para o capítulo de resultados |

## 12. Decisões (2026-11-03)

1. **Modelo JSON é a fonte da verdade**; os `.md` são gerados por `recop.py render`.
2. **Caso sintético** em `skills/re-copilot/exemplos/vendas-unificado/` (3 sistemas +
   documentação geral, mudanças M-01/M-02 e `gabarito.md` para avaliar diagnóstico e
   classificação).
3. **Nome mantido** (`re-copilot`), com a skill **autocontida** (seção 1.1).

## 13. Estado

Implementado:

- **Motor:** embutido na skill, com todas as arquiteturas (baseline, Corrective, Adaptive, Self-RAG, Agentic,
  RAPTOR, GraphRAG, cada uma com adaptações declaradas no módulo), metadados por sistema e leitura de `.sql` só
  com a estrutura.
- **`recop.py`:** check, lint, verificar, render, status, fontes, impacto, candidatos, baseline, diff e exportar (Jira, Azure).
- **Skill:** modelo estruturado, 17 perfis + template, referências de fontes, diagnóstico, manutenção,
  entregáveis e backlog.
- **Casos:** `vendas-unificado` e `rh-admissao` (independente, com armadilhas).

Validado: testes automáticos (mecânica) e duas rodadas em `docs/validacao/resultados/`. A v1 não superou as
alternativas. A v3, em caso novo, teve a melhor documentação (4,86, contra 4,00), com cobertura um pouco menor
(92%, contra 99% e 96%). No primeiro projeto real (`rodada-03-caso-real.md`), foi útil e fiel às notas, mas com status
`confirmado` inflado. Falta a avaliação humana.

Pendente: teste de manutenção entre sessões, repetições da avaliação, importação real no Jira e no Azure,
conexão direta a bancos (fora da fase 1) e avaliação com engenheiros.
