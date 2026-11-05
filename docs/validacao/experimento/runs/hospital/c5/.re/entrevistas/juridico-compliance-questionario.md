# Questionário delegado — juridico-compliance

Rodada 1, 2026-11-04. Aguardando respostas.

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


## 9. (Q-009) SLA de CT-2024-0117

**Para:** Jurídico.

**O que as fontes dizem:** a planilha informa 4 horas e o ManutClin, 8 horas, para início de atendimento. Os outros contratos coincidem, e o contrato original não está nas fontes.

**Decisão pedida:** qual valor consta no contrato vigente, considerando aditivos?

**Premissa sem resposta:** o valor é tratado como pendente. A migração bloqueia a apuração automática de glosa desse contrato até a conferência.


## 14. (Q-014) Dados de paciente e evento adverso

**Para:** Jurídico (ou encarregado de dados, se houver), com o Diretor Técnico.

**O que as fontes dizem:** OS tem campos de nome e prontuário de paciente, e o usuário `prestador_portal` tem `SELECT` em toda a tabela. O prontuário está fora do escopo. As fontes não tratam de LGPD, de guarda de registros nem de notificação de evento adverso.

**Decisão pedida:** o novo sistema deve excluir totalmente a identificação de paciente e receber das OS só o indicador de evento adverso, mantendo o tratamento e a notificação fora do projeto?

**Premissa sem resposta:** sim. Nenhum dado de paciente é importado, o histórico é migrado sem esses campos, e a retenção de registros fica "a definir" com o Jurídico.

