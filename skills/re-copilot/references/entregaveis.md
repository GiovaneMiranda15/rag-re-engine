# Entregáveis — `.re/entregaveis/`

Todos são gerados a partir do modelo. **Hipótese não é motivo para omitir:** um documento
magro não serve para planejar. Entra no corpo tudo o que o projeto precisa, com o status
visível: requisitos `confirmado` ou `validado` sem marca, e os `hipótese` com a marca
`[hipótese]` e a pergunta que os confirma. Conflitos e perguntas abertas também vão para a
seção "Pendências".

**Marque a natureza de cada afirmação relevante:** `[F]` fato com fonte, `[I]` inferência sua a
partir de fatos (diga de quais), `[H]` hipótese ou proposta. Inferência marcada como fato é o erro
mais grave de um documento de requisitos.

**Completude não autoriza inventar.** Número, prazo, meta ou nome sem fonte só entra como proposta
explícita: `[hipótese] 99,5% de disponibilidade (valor proposto; confirmar com <perfil>)`, nunca como
fato nem como requisito `confirmado`. Um requisito confirmado que dependa de um valor proposto deve
ser dividido: o comportamento fica `confirmado` e o valor vira um requisito `hipótese`. Na dúvida,
escreva "a definir" e abra a pergunta. Antes de entregar, `recop.py verificar --docs <pasta>` precisa
sair limpo; o que restar deve ser explicado no documento.

**Cobertura mínima:** cada achado `aberto` e cada tema abaixo precisa de um requisito, uma
história ou uma exclusão justificada em "fora do escopo":
migração de dados e convivência com o legado; auditoria e trilha de alterações; permissões;
monitoramento e alertas de integração; tratamento de falha; relatórios e indicadores de
sucesso; LGPD; treinamento e transição. Rode `recop.py lint` antes de entregar.

Cada documento começa com: projeto, data, baseline (ou "sem baseline") e lista de fontes.
Cite IDs (`RN-004`) em vez de repetir enunciados longos. Diagramas em Mermaid.

**Nos entregáveis, cite o arquivo original** que o leitor consegue abrir (ex.:
`fontes/SIS-01/schema.sql`, objeto `ck_limite`; `politica.md` §3). `chunk_id` e transcrições de
`.re/extraidos/` são internos: servem ao modelo e à rastreabilidade, não como fonte final.
Antes de afirmar uma regra derivada, confira os limites com o texto (ex.: "até 30 dias" inclui
o dia zero?).

Gere sob demanda (`gerar brd`, `gerar srs`…) ou todos (`entregáveis`). Depois de um CR
aplicado, regenere só os documentos afetados.

## Negócio — `negocio/`

| Arquivo | Seções |
|---|---|
| `brd.md` | 1 **Resumo executivo** (meia página: situação, proposta, os 3 maiores riscos e o que precisa ser decidido agora) · 2 Problema e objetivos, com indicador, valor atual, meta e fonte · 3 Escopo (dentro/fora, com o motivo) · 4 Partes interessadas (RACI) · 5 **O que foi decidido × o que é premissa**, em tabela: item, decisão, por quem, fonte · 6 Processo atual → futuro · 7 Regras de negócio com exemplo · 8 Requisitos por área · 9 **Pendências:** decisão, responsável, prazo, o que trava e o efeito se não houver resposta · 10 **Riscos para o patrocinador:** causa, efeito, probabilidade, impacto, mitigação, responsável · 11 **Validação por área:** o que cada área precisa confirmar neste documento · 12 Glossário · 13 Histórico de mudanças |
| `processos.md` | por processo: fluxo atual e futuro (`flowchart`), gargalos eliminados (`GAR`), papéis, regras aplicadas, indicadores |
| `diagnostico.md` | relatório da fase de diagnóstico (`diagnostico.md`) |

## Técnica — `tecnico/`

| Arquivo | Seções (base ISO/IEC/IEEE 29148) |
|---|---|
| `srs.md` | 1 Introdução (propósito, escopo, definições) · 2 Visão geral (contexto do sistema, atores, premissas, restrições) · 3 RF por módulo/processo (enunciado, prioridade, critérios de aceite) · 4 **Ciclo de vida** de cada entidade central: estados, transições, quem dispara, regras (`stateDiagram-v2`) · 5 RNF por categoria ISO/IEC 25010, **cada um com métrica ou um valor proposto `[hipótese]`** · 6 Interfaces externas · 7 Regras de negócio com cálculo, exemplo numérico e limites (o limite é inclusive?) · 8 **Mudanças necessárias nos sistemas atuais, por objeto** (trigger, constraint, coluna, permissão), com o motivo e a fonte · 9 **Matriz de acesso** (papel × dado × ação), sobretudo para dados pessoais · 10 **Cenários de teste de referência:** ao menos 20, derivados de casos reais das fontes e de `.re/cenarios.md`, sem dados pessoais · 11 Migração e transição · 12 Decisões técnicas candidatas a ADR (contexto, opção, consequência) · 13 Pendências |
| `dados.md` | modelo conceitual unificado (`erDiagram`), dicionário das entidades principais **com campos, tipos e chaves**, **de-para** dos sistemas legados (entidade/campo de origem → destino, transformação, conflitos), estratégia e riscos de migração, dados pessoais (LGPD: finalidade, base legal, retenção) |
| `integracoes.md` | por integração: sistemas, direção, meio (API, arquivo, evento), frequência, contrato, volume, tratamento de falha, monitoramento, responsável |
| `rastreabilidade.md` | cópia de `.re/rastreabilidade.md` (8 matrizes geradas por `recop.py render`; **não reescreva à mão**), mais uma análise curta: fontes sem requisito, achados sem tratamento, histórias bloqueadas |
| `arquitetura-contexto.md` | (opcional) diagrama de contexto (C4 nível 1 em Mermaid), restrições tecnológicas, decisões candidatas a ADR |

## Ágil — `backlog/`

Ver `backlog-export.md`: `backlog.md` (gerado por `recop.py render`), `jira.csv`,
`azure-devops.csv`.

## Mudanças — `mudancas.md`

Changelog por baseline: CRs aplicados e rejeitados (com motivo), requisitos criados,
alterados (antes → depois) e obsoletos, itens de backlog marcados `revisar`. Para cada mudança: o que
muda e **por quê**, a alternativa considerada, o efeito em um caso concreto e quem precisa ser avisado.
