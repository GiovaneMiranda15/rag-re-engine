# Perguntas aos stakeholders

Projeto: sistema único de compras e contratos de manutenção de equipamentos, Rede Hospitalar Aurora do Vale.
Data: 04/11/2026. Modo: entrevista delegada, resposta única. As perguntas estão ordenadas pelo que destravam.
Para cada uma há o que as fontes já dizem, a decisão pedida e a premissa adotada se não houver resposta.
Detalhes e citações completas: `01-diagnostico.md`.

## 1. (Q-001) Fronteira do sistema único

**Para:** Diretora Geral (patrocinadora).

**O que as fontes dizem:** o escopo pede sistema único para comprar, contratar, acompanhar e pagar, mas também diz que ele se relaciona com as OS e o inventário. O ERP é recortado pela categoria `MANUT_EQUIP`, e medicamentos, OPME e obras estão fora do projeto (`escopo.md`; `erp_suprimax_dump.sql`, cabeçalho).

**Decisão pedida:** na fase 1, o ERP e o ManutClin são substituídos ou continuam e se integram ao novo sistema?

**Premissa sem resposta:** a planilha é substituída; o novo sistema assume os contratos e compras de manutenção; o ERP segue para as demais categorias; o ManutClin segue como dono de OS e inventário, com integração.

## 2. (Q-002) Sucesso e mínimo da fase 1

**Para:** Diretora Geral, com o Comitê de Contratos.

**O que as fontes dizem:** a entrada em operação é até 30/06/2027 e o escopo lista oito etapas, de requisição a pagamento. Nenhuma fonte define meta. As linhas de base são: 38 dias de contratação, 21 dias em `AGUARDANDO_COMPRA`, cerca de 6 dias úteis de conferência, cerca de 140 títulos alterados por mês e R$ 0,00 de glosas em 2025 (`indicadores_manutencao_2025.md`; ata de 19/08/2026).

**Decisão pedida:** qual desses números, com qual meta, define que a fase 1 deu certo e, portanto, quais etapas são o mínimo se nem tudo couber no prazo?

**Premissa sem resposta:** prioridade Must para contrato único e alertas, regras de aprovação, OS para requisição e medição com ateste; custo por equipamento e fila de parecer como Should. Metas ficam "a definir".

## 3. (Q-003) Política contra parâmetros do ERP

**Para:** Diretor Financeiro, com a Gerente de Suprimentos.

**O que as fontes dizem:** a POL-SUP-004 rev. 3 difere do ERP em alçada de OC (R$ 50.000,00 x R$ 80.000), base da alçada de contrato (global x mensal), cotações (acima de R$ 5.000,00 e R$ 15.000,00 x a partir de R$ 25.000) e prazo de pagamento (padrão de 45 e mínimo de 30 dias x 15 a 30 dias). Há casos concretos, como OC-2026-00388, OC-2026-00440 e as OCs 00301 a 00303, que somam R$ 149.300,00.

**Decisão pedida:** a política vale integralmente no novo sistema, ou há alguma exceção aprovada que explique os parâmetros do ERP? Se houver, indique qual.

**Premissa sem resposta:** vale a política, sem exceções. Os casos passados são levados ao Comitê, sem regularização retroativa pelo projeto.

## 4. (Q-004) Onde o pagamento acontece

**Para:** Diretor Financeiro.

**O que as fontes dizem:** o Financeiro recebe títulos do ERP e altera o vencimento de cerca de 140 por mês (ata, item 6). As fontes não mostram tabela de títulos nem o sistema que paga. O limite do ERP de 15 a 30 dias é uma causa provável, mas não comprovada.

**Decisão pedida:** em qual sistema os títulos são pagos, e a fase 1 deve substituí-lo ou enviar dados para ele? Informe também o motivo mais comum das alterações.

**Premissa sem resposta:** o novo sistema aprova a medição e gera o título; a baixa continua no sistema financeiro atual, com integração. A causa fica registrada como hipótese.

## 5. (Q-005) Custo por equipamento

**Para:** Diretor Financeiro, com a Controladoria.

**O que as fontes dizem:** a Diretora Geral pediu o custo somando contrato, chamados e peças (ata, item 1). OCs não têm patrimônio, e 48,8% do gasto de 2025 está fora de contratos. O valor de R$ 1.550.440,00 bate exatamente com a planilha proporcional aos meses, o que sugere cálculo e não pagamentos.

**Decisão pedida:** como ratear o valor de um contrato entre seus equipamentos: igualmente, por valor do equipamento, por uso de OS ou por outro critério?

**Premissa sem resposta:** rateio igual entre os equipamentos cobertos, configurável, sobre valores pagos; chamados e peças entram diretamente pelo patrimônio.

## 6. (Q-006) Limite do parecer jurídico

**Para:** Jurídico.

**O que as fontes dizem:** a POL-SUP-004 §4.5 exige parecer acima de R$ 30.000,00; o fluxo de junho de 2025 usa acima de R$ 100.000. O parecer já consome 23 dos 38 dias de contratação. CT-2026-0021 (R$ 58.800,00) está entre os dois limites.

**Decisão pedida:** qual limite vale, R$ 30.000,00 ou R$ 100.000?

**Premissa sem resposta:** R$ 30.000,00, por ser a regra formal aprovada pela Diretoria, e o fluxo precisa ser corrigido. O risco de aumentar a fila fica registrado.

## 7. (Q-007) Pagamento fora de contrato vigente e registrado

**Para:** Jurídico, com o Diretor Financeiro.

**O que as fontes dizem:** CT-2022-0055 acabou em 31/08/2025, consta como ATIVO no ERP e segue em pagamento, com minuta em discussão. CT-2026-0021 não está no ERP e parece ser pago por OCs avulsas mensais de R$ 4.900,00. CT-2023-0088 consta como vencido na planilha, mas tem fim em 31/12/2026 no ERP, com aditivo.

**Decisão pedida:** o sistema deve bloquear a liberação de medição nesses casos e, se houver exceção por continuidade assistencial, quem a autoriza?

**Premissa sem resposta:** bloqueio com exceção justificada, aprovada pelo Diretor Financeiro e informada ao Comitê. O ERP é tratado como fonte da vigência de CT-2023-0088, a conferir no documento.

## 8. (Q-008) Renovação: prazo e responsável

**Para:** Gerente de Suprimentos, com Engenharia Clínica e Jurídico.

**O que as fontes dizem:** a política determina 120 dias, com a área gestora e o Jurídico; o fluxo, 90 dias, com Suprimentos; a planilha avisa a 60 dias ou menos. A "área gestora" não é definida.

**Decisão pedida:** quem é o responsável por iniciar a renovação (a "área gestora") nos 120 dias da política?

**Premissa sem resposta:** 120 dias, com a Engenharia Clínica como área gestora, responsável por iniciar, o Jurídico como corresponsável e Suprimentos acionado para cotar.

## 9. (Q-009) SLA de CT-2024-0117

**Para:** Jurídico.

**O que as fontes dizem:** a planilha informa 4 horas e o ManutClin, 8 horas, para início de atendimento. Os outros contratos coincidem, e o contrato original não está nas fontes.

**Decisão pedida:** qual valor consta no contrato vigente, considerando aditivos?

**Premissa sem resposta:** o valor é tratado como pendente. A migração bloqueia a apuração automática de glosa desse contrato até a conferência.

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

## 14. (Q-014) Dados de paciente e evento adverso

**Para:** Jurídico (ou encarregado de dados, se houver), com o Diretor Técnico.

**O que as fontes dizem:** OS tem campos de nome e prontuário de paciente, e o usuário `prestador_portal` tem `SELECT` em toda a tabela. O prontuário está fora do escopo. As fontes não tratam de LGPD, de guarda de registros nem de notificação de evento adverso.

**Decisão pedida:** o novo sistema deve excluir totalmente a identificação de paciente e receber das OS só o indicador de evento adverso, mantendo o tratamento e a notificação fora do projeto?

**Premissa sem resposta:** sim. Nenhum dado de paciente é importado, o histórico é migrado sem esses campos, e a retenção de registros fica "a definir" com o Jurídico.

## 15. (Q-015) Meios de integração e migração

**Para:** TI ou responsável técnico pelos sistemas, por meio do PMO. O escopo não cita a área de TI.

**O que as fontes dizem:** só há dumps de 30/09/2026, sem APIs nem rotinas de integração. Os sistemas não conversam (ata, item 5).

**Decisão pedida:** quais meios podem ser usados para ler e gravar no ERP e no ManutClin (API, tabela intermediária, arquivo) e quem responde por eles?

**Premissa sem resposta:** carga periódica por extração controlada, somente leitura no ManutClin, com monitoramento e reprocessamento. A atualização máxima fica "a definir".

---

## Decisões assumidas sem pergunta (podem ser contestadas nas respostas)

- CNPJ é a chave do fornecedor; MTS (ERP) e BioVolt são tratados como a mesma empresa.
- Patrimônio, número de contrato e de-para de unidades são as chaves da integração.
- CT-2025-0064 segue IPCA, conforme a POL-SUP-004 §4.3; o IGP-M do ERP é tratado como erro de cadastro.
- Capítulos 4 e 5 do manual de 2019 são ignorados por estarem revogados.
- Reajuste é tratado com a data-base de cada contrato, já que a periodicidade não consta nas fontes.
- Não há orçamento nem equipe nas fontes; esses itens ficam "a definir" e não são estimados.
