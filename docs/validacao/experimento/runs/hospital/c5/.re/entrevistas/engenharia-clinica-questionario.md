# Questionário delegado — engenharia-clinica

Rodada 1, 2026-11-04. Aguardando respostas.

## 10. (Q-010) Apuração de SLA e glosa

**Para:** Engenharia Clínica, com Financeiro e Jurídico.

**O que as fontes dizem:** a política prevê glosa de 2% do valor mensal por evento, mas não houve glosa em 2025. Na OS 88170, o atendimento levou 14,2 horas em contrato com SLA de 4 ou 8 horas, e a medição tem glosa 0 (R$ 220,80 pela regra). A OS 88190 ficou 533,7 horas aberta aguardando compra de peça, contra solução de 72 horas. O prestador pode editar a hora de atendimento.

**Decisão pedida:** o relógio do SLA pausa em `AGUARDANDO_COMPRA` e `AGUARDANDO_PECA`, e a glosa deve ser só proposta pelo sistema, dependendo de aceite humano, ou aplicada automaticamente?

**Premissa sem resposta:** o relógio pausa só em espera de item não coberto; o sistema propõe a glosa, e a Engenharia Clínica aceita ou justifica no ateste; cada OS fora do SLA é um evento.


## 11. (Q-011) Escala de criticidade

**Para:** Engenharia Clínica.

**O que as fontes dizem:** há quatro níveis na política (§6.2), A/B/C por equipamento no ManutClin e Crítico/Não crítico por contrato na planilha, sem tabela de equivalência.

**Decisão pedida:** qual é a equivalência entre A/B/C e os quatro níveis da política?

**Premissa sem resposta:** a escala oficial é a de quatro níveis; nenhuma equivalência é presumida, e os equipamentos são reclassificados pela Engenharia Clínica antes da carga. O contrato herda o maior nível dos itens cobertos.


## 12. (Q-012) Preventiva de ventiladores

**Para:** Engenharia Clínica.

**O que as fontes dizem:** o `plano_preventivo` tem 365 dias para ventiladores na Central; CT-2023-0019 aparece como Semestral na planilha. O dump do plano também não traz desfibriladores da Central e do Litoral nem a unidade Sul, mas não informa se é amostra.

**Decisão pedida:** qual periodicidade vale para ventiladores da Central: 365 dias ou semestral?

**Premissa sem resposta:** vale a semestral do contrato, por ser a mais conservadora e estar contratada. O sistema apenas sinaliza as diferenças e o plano segue no ManutClin.


## 13. (Q-013) Calibração vencida e liberação ausente

**Para:** Gerente de Engenharia Clínica, com o Diretor Técnico.

**O que as fontes dizem:** PAT-004512 está `EM_USO` com calibração vencida em 31/03/2026. A OS 88213 foi fechada sem teste e sem liberação, contra a regra do fluxo, e o gatilho do ManutClin não confere isso. A política §6.3 diz "não deve permanecer em uso".

**Decisão pedida:** o tratamento desses casos deve ser só alerta e relatório, ou também bloqueio operacional no ManutClin?

**Premissa sem resposta:** alerta e relatório no novo sistema; bloqueio é mudança a pedir ao ManutClin. A verificação do caso atual é recomendada de imediato, fora do cronograma do projeto.

