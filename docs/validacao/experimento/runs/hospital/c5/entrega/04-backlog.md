# Backlog ágil

**Projeto:** sistema único de compras e contratos de manutenção de equipamentos. **Data:** 04/11/2026, atualizado após `mudancas/`. **Baseline:** sem baseline.
**Tamanho:** 7 épicos, 17 features, 43 histórias. Sem estimativas: equipe e velocidade não constam nas fontes.
Ordem de prioridade definida pela Diretora Geral (Q-002). História com label `hipotese` depende de premissa ainda não confirmada; `conflito` depende de decisão sobre requisitos que se contradizem; `bloqueada_por` indica a pergunta. Status `revisar`: afetada por mudança (`08-mudancas.md`).

## Sequência de entrega proposta [H]

As datas são propostas e não foram avaliadas contra capacidade da equipe. Antes da onda 1, é preciso resolver Q-001, Q-018 e Q-016.

| Onda | Foco | Janela [H] | Histórias |
|---|---|---|---|
| 1 | Fundação e contratos | dez/2026 a jan/2027 | US-001, US-002, US-003, US-004, US-007, US-022, US-038 |
| 2 | Aprovações, renovação e equipamentos | fev a mar/2027 | US-005, US-006, US-008, US-009, US-011, US-013, US-014, US-015, US-016, US-017, US-019, US-021, US-023, US-028, US-029, US-039, US-040, US-043 |
| 3 | OS, medição, ateste, glosa e título | abr a mai/2027 | US-012, US-018, US-020, US-024, US-025, US-026, US-027, US-030, US-031, US-032, US-033, US-034 |
| 4 | Consolidação e transição | jun/2027 | US-010, US-035, US-036, US-041, US-042 |
| 5 | Fase 2 | Após 30/06/2027 | US-037 |

## Histórias afetadas por mudança

| História | Título | CR |
|---|---|---|
| US-011 | Exigir parecer acima de R$ 30.000,00 | CR-002 |
| US-032 | Calcular glosa por evento | CR-003 |
| US-035 | Ver visão consolidada da rede | CR-001 |
| US-040 | Sanear e migrar contratos | CR-001 |
| US-042 | Garantir capacidade, disponibilidade e recuperação | CR-001 |
| US-043 | Incorporar o Hospital Aurora Serra e seus contratos | CR-001 (nova) |

## Histórias bloqueadas por pergunta

| História | Título | Bloqueada por |
|---|---|---|
| US-006 | Bloquear medição de contrato vencido, com exceção | Q-007 |
| US-007 | Receber alerta de renovação | Q-008 |
| US-011 | Exigir parecer acima de R$ 30.000,00 | Q-019 |
| US-022 | Conectar aos sistemas mantidos com monitoramento | Q-001, Q-018 |
| US-023 | Receber inventário e calibração | Q-018 |
| US-024 | Criar requisição a partir da OS | Q-018 |
| US-033 | Aceitar ou justificar glosa no ateste e pausar relógio | Q-010 |
| US-034 | Gerar título com vencimento correto | Q-004 |
| US-036 | Acompanhar indicadores do processo | Q-002 |
| US-037 | Consultar custo por equipamento | Q-005 |
| US-038 | Excluir dados de paciente da integração | Q-016, Q-017 |
| US-042 | Garantir capacidade, disponibilidade e recuperação | Q-018 |
| US-043 | Incorporar o Hospital Aurora Serra e seus contratos | Q-020, Q-021 |

RN-024 (bloqueio no ManutClin) não tem história: depende de Q-013 e seria mudança no ManutClin.

## Dependências

| História | Depende de |
|---|---|
| US-002 | US-001 |
| US-003 | US-002 |
| US-004 | US-002 |
| US-005 | US-002 |
| US-006 | US-004 |
| US-007 | US-004 |
| US-008 | US-007 |
| US-009 | US-002 |
| US-010 | US-002 |
| US-011 | US-002 |
| US-012 | US-011 |
| US-013 | US-001 |
| US-014 | US-013 |
| US-015 | US-002, US-003 |
| US-016 | US-014 |
| US-017 | US-014 |
| US-018 | US-014 |
| US-019 | US-014 |
| US-020 | US-014 |
| US-021 | US-013 |
| US-023 | US-022 |
| US-024 | US-013, US-023 |
| US-025 | US-004, US-023 |
| US-026 | US-025 |
| US-027 | US-023 |
| US-028 | US-023 |
| US-029 | US-023 |
| US-030 | US-023 |
| US-031 | US-002, US-023 |
| US-032 | US-031, US-025 |
| US-033 | US-032, US-026 |
| US-034 | US-014 |
| US-035 | US-002, US-003 |
| US-036 | US-035 |
| US-037 | US-024, US-035 |
| US-038 | US-022 |
| US-039 | US-001 |
| US-040 | US-002 |
| US-041 | US-040 |
| US-043 | US-002, US-040 |

## Épicos, features e histórias

## EP-001 — Cadastro único de contratos [proposto]

Prioridade 1 da Diretora Geral: vigência, valor, SLA e alertas de renovação.

Prioridade: Must

### FT-001 — Cadastro e vigência [proposto]

Contrato único, com moeda, índice, SLA e status calculado.

Prioridade: Must

#### US-002 — Cadastrar contrato com vigência, valor e SLA [proposto]

Como advogada do Jurídico, quero cadastrar o contrato em um único lugar, para que todas as áreas vejam a mesma informação sem pedir por e-mail.

Prioridade: Must · Requisitos: RF-001, RN-009, RN-011

- Dado contrato completo, quando salvo, então guarda número, unidade, fornecedor, início, fim, valor, moeda, índice, SLA de atendimento e de solução e preventiva.
- Dado contrato sem fim de vigência, quando salvo, então o sistema recusa.
- Dado número já cadastrado, quando salvo, então o sistema recusa a duplicidade.

#### US-003 — Validar índice e moeda do contrato [proposto]

Como analista do Financeiro, quero que índice e câmbio sigam a política, para evitar reajuste errado e soma de moedas.

Prioridade: Must · Requisitos: RN-007, RN-019

- Dado contrato em BRL assinado em 01/01/2024 ou depois, quando salvo com IGP-M, então o sistema recusa.
- Dado contrato assinado até 31/12/2023, quando salvo com IGP-M, então o sistema aceita.
- Dado contrato em USD, quando salvo, então exige câmbio de referência e não aceita índice de reajuste.

#### US-004 — Calcular status da vigência [proposto]

Como advogada do Jurídico, quero status calculado pelas datas, para que um contrato vencido não apareça como ativo.

Prioridade: Must · Requisitos: RF-001

- Dado contrato com fim futuro, quando consultado, então aparece vigente.
- Dado CT-2022-0055 com fim em 31/08/2025, quando consultado depois disso, então aparece vigência encerrada, mesmo com renovação em andamento.
- Dado contrato no último dia da vigência, quando consultado, então ainda aparece vigente.

#### US-005 — Impedir pagamento de contrato não registrado [proposto]

Como analista do Financeiro, quero impedir o primeiro pagamento sem registro, para cumprir a política.

Prioridade: Must · Requisitos: RN-021

- Dado contrato registrado, quando a medição é liberada, então o sistema aceita.
- Dada cobrança sem contrato registrado, quando enviada a pagamento, então o sistema recusa.
- Dado contrato registrado depois do primeiro pedido, quando o pedido é reenviado, então o sistema aceita.

#### US-006 — Bloquear medição de contrato vencido, com exceção [proposto]

Como Diretor Financeiro, quero bloquear a medição de contrato vencido, salvo exceção justificada, para reduzir pagamentos sem cobertura.

Prioridade: Must · Requisitos: RN-008

- Dada medição com competência dentro da vigência, quando liberada, então o sistema aceita.
- Dada medição após o fim da vigência sem exceção, quando liberada, então o sistema recusa.
- Dada exceção aprovada com justificativa, quando liberada, então o sistema aceita e registra na trilha.

### FT-002 — Renovação e aditivos [proposto]

Alertas, fluxo de renovação e histórico de aditivos.

Prioridade: Must

#### US-007 — Receber alerta de renovação [proposto]

Como responsável pelo contrato, quero alerta de vencimento, para iniciar a renovação a tempo.

Prioridade: Must · Requisitos: RF-008, RN-006

- Dado CT-2025-0064 com fim em 31/01/2027, quando chega 03/10/2026 (120 dias), então os responsáveis recebem o alerta.
- Dado contrato com 121 dias para o fim, quando processada a rotina, então não há alerta.
- Dado alerta sem renovação aberta depois de 30 dias, quando processada a rotina, então o aviso é repetido.

#### US-008 — Acompanhar a renovação [proposto]

Como advogada do Jurídico, quero acompanhar etapas e responsável, para que a renovação não fique parada.

Prioridade: Should · Requisitos: RF-015

- Dada renovação aberta, quando há minuta em discussão, então aparece a etapa e o responsável.
- Dada renovação concluída, quando assinada, então a vigência é atualizada por aditivo ou novo contrato.
- Dado contrato vencido, quando em renovação, então os dois estados aparecem juntos.

#### US-009 — Registrar aditivo com histórico [proposto]

Como advogada do Jurídico, quero registrar aditivos com os valores anteriores, para evitar casos como CT-2023-0088.

Prioridade: Must · Requisitos: RF-018

- Dado aditivo que muda o fim, quando salvo, então a vigência muda e o valor anterior fica no histórico.
- Dado aditivo salvo por outra área, quando concluído, então o Jurídico recebe aviso.
- Dado aditivo sem documento de referência, quando salvo, então o sistema recusa.

#### US-010 — Importar renovações do legado [proposto]

Como advogada do Jurídico, quero levar para o novo sistema as renovações feitas durante a transição, para não perder vigências.

Prioridade: Must · Requisitos: RF-014

- Dada renovação concluída no legado, quando importada, então o contrato mostra a nova vigência.
- Dado número inexistente, quando importado, então a linha é rejeitada com motivo.
- Dada a mesma renovação importada de novo, quando processada, então não há duplicidade.

### FT-003 — Parecer jurídico [proposto]

Exigência de parecer e fila.

Prioridade: Must

#### US-011 — Exigir parecer acima de R$ 30.000,00 [revisar]

Como advogada do Jurídico, quero exigir parecer pelo valor global, para cumprir a política. Limite em conflito (DIV-019): vale R$ 30.000,00 até a decisão de Q-019.

Prioridade: Must · Requisitos: RN-005, RN-028

- Dado contrato de R$ 58.800,00 sem parecer, quando enviado à aprovação, então o sistema recusa.
- Dado contrato de R$ 30.000,00, quando enviado, então não exige parecer.
- Dado contrato de R$ 30.000,01, quando enviado, então exige parecer.

#### US-012 — Ver fila de pareceres [proposto]

Como advogada do Jurídico, quero ver a fila por dias de espera e fim de vigência, para priorizar.

Prioridade: Should · Requisitos: RF-003

- Dado parecer em aberto, quando abro a fila, então vejo dias de espera e fim de vigência.
- Dado parecer concluído, quando abro a fila, então ele sai da fila e entra na medição do ciclo.

## EP-002 — Compras e aprovações conforme a Política [proposto]

Prioridade 2: requisição, cotação e alçadas com trilha de auditoria.

Prioridade: Must

### FT-004 — Requisição e cotação [proposto]

Registro e validação pela política.

Prioridade: Must

#### US-013 — Registrar requisição com cotações [proposto]

Como analista de Compras, quero registrar requisição e cotações, com patrimônio quando houver, para compor a compra e o custo futuro.

Prioridade: Must · Requisitos: RF-017, RN-003

- Dada compra de R$ 5.000,00 sem cotação, quando enviada, então o sistema aceita.
- Dada compra de R$ 5.000,01 com uma cotação, quando enviada, então o sistema recusa; com duas, aceita.
- Dada compra de R$ 15.000,01 com duas cotações, quando enviada, então o sistema recusa; com três, aceita.

### FT-005 — Alçadas e controles [proposto]

Aprovação de OC e contrato, segregação, soma por requisição, trilha.

Prioridade: Must

#### US-014 — Aprovar OC pela alçada [proposto]

Como aprovador, quero receber só as OCs de minha alçada, para cumprir a política.

Prioridade: Must · Requisitos: RF-016, RN-001

- Dada OC de R$ 50.000,00, quando submetida, então vai ao Gerente de Suprimentos.
- Dada OC de R$ 72.500,00, quando o Gerente de Suprimentos tenta aprovar, então o sistema recusa e encaminha ao Diretor Financeiro.
- Dada OC de R$ 250.000,01, quando submetida, então vai à Diretora Geral.

#### US-015 — Aprovar contrato pelo valor global [proposto]

Como Diretor Financeiro, quero que a alçada de contrato use o valor global, para evitar aprovação em nível insuficiente.

Prioridade: Must · Requisitos: RF-016, RN-002, RN-020

- Dado contrato assinado desde 01/01/2025 de R$ 6.800,00/mês por 24 meses, quando submetido, então a base é R$ 163.200,00 e vai ao Diretor Financeiro.
- Dado contrato de R$ 22.000,00/mês por 24 meses, quando submetido, então vai à Diretora Geral.
- Dado contrato em USD, quando submetido, então a base usa o câmbio de referência e aditivos somam ao global.

#### US-016 — Impedir autoaprovação [proposto]

Como auditor interno, quero que o solicitante não aprove a própria compra, para garantir segregação.

Prioridade: Must · Requisitos: RN-014

- Dada OC solicitada por X, quando X tenta aprovar, então o sistema recusa.
- Dada OC solicitada por X, quando Y com alçada aprova, então o sistema aceita.
- Dado único aprovador na faixa sendo o solicitante, quando submetida, então a OC sobe ao nível seguinte.

#### US-017 — Somar ordens da mesma requisição [proposto]

Como Diretor Financeiro, quero somar ordens da mesma requisição, para impedir fracionamento.

Prioridade: Must · Requisitos: RN-016

- Dadas três OCs de uma requisição somando R$ 149.300,00, quando a terceira é aprovada, então a alçada é a do Diretor Financeiro.
- Dada OC única de R$ 49.800,00, quando submetida, então a alçada é do Gerente de Suprimentos.
- Dada a soma exatamente em R$ 50.000,00, quando submetida, então a alçada não muda.

#### US-018 — Alertar compras recorrentes sem contrato [proposto]

Como Gerente de Suprimentos, quero alerta de OCs recorrentes sem contrato, para identificar casos como o das autoclaves.

Prioridade: Should · Requisitos: RN-025

- Dadas três OCs mensais do mesmo fornecedor e unidade sem contrato, quando emitida a terceira, então recebo alerta.
- Dadas OCs vinculadas a contrato, quando emitidas, então não há alerta.

#### US-019 — Registrar trilha das aprovações [proposto]

Como auditor interno, quero a trilha de cada aprovação, para provar quem aprovou o quê.

Prioridade: Must · Requisitos: RNF-002

- Dada aprovação concluída, quando consultada, então mostra usuário, data, valor anterior e valor novo.
- Dada recusa, quando consultada, então mostra usuário, data e motivo.
- Dado registro de trilha, quando há tentativa de alteração, então o sistema recusa.

#### US-020 — Manter limites como parâmetros com vigência [proposto]

Como Gerente de Suprimentos, quero parametrizar limites com vigência, para que nova revisão da política não exija mudança no software.

Prioridade: Should · Requisitos: RNF-006

- Dado limite com vigência futura, quando chega a data, então passa a valer.
- Dada compra anterior à vigência, quando consultada, então mantém o limite da época.

### FT-006 — Compra emergencial [proposto]

Regras da Portaria DG-017/2025.

Prioridade: Must

#### US-021 — Registrar compra emergencial [proposto]

Como analista de Compras, quero registrar a emergencial pela Portaria, para atender rápido e com controle.

Prioridade: Must · Requisitos: RF-020, RN-018

- Dada emergencial de R$ 92.000,00 com uma proposta, quando emitida, então o sistema aceita.
- Dada emergencial de R$ 100.000,01, quando emitida, então o sistema recusa como emergencial.
- Dada emergencial emitida, quando decorrerem 72 horas sem aprovação do Diretor Técnico, então o sistema alerta; emergenciais do período aparecem na lista do Comitê.

## EP-003 — Ligação entre OS, requisição e medição [proposto]

Prioridade 3: elimina redigitação e leva o ateste para o sistema.

Prioridade: Must

### FT-007 — OS e inventário [proposto]

Recebimento de dados do ManutClin e requisição a partir da OS.

Prioridade: Must

#### US-023 — Receber inventário e calibração [proposto]

Como engenheira clínica, quero ver no sistema os equipamentos com patrimônio, unidade, status, nível e calibração, para relacioná-los aos contratos.

Prioridade: Must · Requisitos: RF-007

- Dado patrimônio no ManutClin, quando sincronizado, então aparece com os dados atuais.
- Dado patrimônio sem contrato, quando consultado, então aparece sem cobertura contratual.
- Dada alteração de validade, quando sincronizada em até 24 horas, então o valor é atualizado.

#### US-024 — Criar requisição a partir da OS [proposto]

Como analista da Engenharia Clínica, quero gerar a requisição a partir da OS, para não redigitar.

Prioridade: Must · Requisitos: RF-004

- Dada OS em AGUARDANDO_COMPRA, quando gero a requisição, então ela recebe OS, patrimônio e unidade.
- Dada OS já com requisição, quando tento gerar outra, então o sistema alerta.
- Dada OS fechada, quando tento gerar, então o sistema recusa.

### FT-008 — Medição e ateste [proposto]

Conferência assistida e bloqueio sem ateste.

Prioridade: Must

#### US-025 — Conferir medição contra OS [proposto]

Como analista da Engenharia Clínica, quero ver as OS do contrato e os eventos fora do SLA na medição, para reduzir a conferência à mão.

Prioridade: Must · Requisitos: RF-005

- Dada medição de um contrato, quando aberta, então aparecem as OS da competência.
- Dada OS sem contrato ligado, quando conferida, então aparece como divergência.
- Dada OS de 31/08 fechada em 01/09, quando conferida, então entra pela regra de competência definida.

#### US-026 — Atestar medição no sistema [proposto]

Como engenheira clínica, quero atestar no sistema, para que nada seja pago sem ateste.

Prioridade: Must · Requisitos: RF-005, RN-013

- Dada medição conferida, quando atestada, então registra usuário e data e libera o pagamento.
- Dada medição sem ateste, quando enviada a pagamento, então o sistema recusa.
- Dada medição atestada e depois alterada, quando salva, então o ateste é invalidado.

### FT-009 — Segurança do equipamento [proposto]

Irregularidades de liberação, calibração, criticidade e preventiva.

Prioridade: Must

#### US-027 — Listar OS corretivas sem teste ou liberação [proposto]

Como engenheira clínica, quero a lista de OS irregulares, para agir sobre retorno ao uso sem liberação.

Prioridade: Must · Requisitos: RN-012

- Dada OS 88213, fechada sem teste e liberação, quando recebida, então entra na lista.
- Dada OS corretiva com teste APROVADO e liberação, quando recebida, então não entra.
- Dada OS com teste REPROVADO, quando recebida, então entra na lista.

#### US-028 — Alertar calibração vencida [proposto]

Como engenheira clínica, quero alerta de equipamento em uso com calibração vencida, para retirar de uso.

Prioridade: Must · Requisitos: RN-015

- Dado PAT-004512 EM_USO com validade em 31/03/2026, quando processada a carga, então há alerta.
- Dado equipamento com validade hoje, quando processada, então não há alerta de vencido.
- Dado equipamento sem validade, quando processado, então aparece como sem informação, não como conforme.

#### US-029 — Classificar equipamentos em quatro níveis [proposto]

Como engenheira clínica, quero classificar pelos níveis da política, para ter uma só escala.

Prioridade: Must · Requisitos: RN-010, RN-023, RN-022

- Dado equipamento A, quando carregado, então recebe nível 1.
- Dado equipamento C, quando carregado, então recebe nível 4.
- Dado equipamento B, quando carregado, então fica pendente até eu escolher nível 2 ou 3.
- Dado contrato com itens de vários níveis, quando consultado, então mostra o maior nível (premissa de RN-022).

#### US-030 — Conciliar preventiva do contrato e do plano [proposto]

Como engenheira clínica, quero ver diferenças entre contrato e plano, para corrigir casos como os ventiladores da Central.

Prioridade: Should · Requisitos: RF-013

- Dado contrato Semestral e plano de 365 dias, quando conciliados, então a diferença é sinalizada.
- Dado contrato Trimestral e plano de 90 dias, quando conciliados, então não há diferença.

## EP-004 — Glosa por SLA [proposto]

Prioridade 4: apuração de SLA e cálculo de glosa.

Prioridade: Must

### FT-010 — Apuração e glosa [proposto]

Tempos por OS, eventos fora do SLA e cálculo de 2%.

Prioridade: Must

#### US-031 — Apurar tempos de SLA por OS [proposto]

Como analista da Engenharia Clínica, quero o tempo de atendimento e solução de cada OS contra o contrato, para identificar eventos.

Prioridade: Must · Requisitos: RN-009

- Dada OS 88170, com 14,2 horas até o atendimento em contrato de 4 horas, quando apurada, então é evento fora do SLA.
- Dada OS 88213, com 3,4 horas em contrato de 4 horas, quando apurada, então está dentro.
- Dado atendimento exatamente no limite do SLA, quando apurado, então está dentro.

#### US-032 — Calcular glosa por evento [revisar]

Como analista do Financeiro, quero o valor da glosa calculado, para que ela apareça na medição.

Prioridade: Must · Requisitos: RN-017

- Dado um evento em contrato de R$ 11.040,00/mês, quando calculado, então a glosa é R$ 220,80.
- Dados dois eventos no mês, quando calculado, então a glosa é R$ 441,60.
- Dado mês sem evento, quando calculado, então a glosa é R$ 0,00.
- Dados 5 eventos em contrato de R$ 11.040,00/mês, quando calculada a competência, então a glosa é R$ 1.104,00.
- Dados 6 eventos no mesmo contrato e competência, quando calculada, então a glosa continua R$ 1.104,00.

#### US-033 — Aceitar ou justificar glosa no ateste e pausar relógio [proposto]

Como engenheira clínica, quero aceitar ou justificar a glosa e descontar esperas válidas, para apurar de forma justa.

Prioridade: Should · Requisitos: RN-026

- Dada glosa proposta, quando aceita, então desconta da medição.
- Dada glosa recusada, quando salva, então exige justificativa.
- Dada OS em espera de item não coberto, quando apurada a solução, então o período é excluído.

## EP-005 — Pagamento [proposto]

Título com prazo correto. Fronteira pendente em Q-004.

Prioridade: Should

### FT-011 — Títulos [proposto]

Vencimento calculado e alteração com motivo.

Prioridade: Should

#### US-034 — Gerar título com vencimento correto [proposto]

Como analista do Financeiro, quero título com vencimento pela regra, para não ajustar à mão.

Prioridade: Must · Requisitos: RF-006, RN-004

- Dada nota de 01/03/2027 em OC regular, quando gerado o título, então o vencimento é 45 dias depois.
- Dada OC regular com prazo de 29 dias, quando salva, então o sistema recusa; com 30, aceita.
- Dada OC emergencial com 15 dias, quando salva, então o sistema aceita.

## EP-006 — Visão consolidada e custos [proposto]

Visão da rede e, na segunda fase, custo por equipamento.

Prioridade: Should

### FT-012 — Painéis [proposto]

Consolidação por contrato, fornecedor, equipamento e unidade; indicadores.

Prioridade: Should

#### US-035 — Ver visão consolidada da rede [revisar]

Como Diretora Geral, quero consolidar por contrato, fornecedor, equipamento e unidade, para decidir sobre a rede.

Prioridade: Should · Requisitos: RF-009

- Dado filtro por unidade, quando aplicado, então os valores somam só a unidade.
- Dado contrato em USD, quando consolidado, então usa o câmbio de referência e mostra a moeda original.
- Dado fornecedor com dois nomes e um CNPJ, quando consolidado, então aparece uma só linha.
- Dado o Hospital Aurora Serra cadastrado, quando aberta a visão da rede, então ele aparece como unidade própria.

#### US-036 — Acompanhar indicadores do processo [proposto]

Como Diretora Geral, quero os indicadores contra a linha de base de 2025, para avaliar a fase 1.

Prioridade: Should · Requisitos: RF-019

- Dado mês encerrado, quando aberto o relatório, então mostra ciclo de contratação, espera de compra, títulos alterados e glosas.
- Dado indicador sem dado, quando aberto, então aparece como sem informação, não como zero.

### FT-013 — Custo por equipamento (fase 2) [proposto]

Contrato, chamados e peças por patrimônio.

Prioridade: Could

#### US-037 — Consultar custo por equipamento [proposto]

Como Diretora Geral, quero somar contrato, chamados e peças por equipamento, para decidir entre manter e substituir.

Prioridade: Could · Requisitos: RF-010, RN-027

- Dado equipamento com contrato e peça, quando consultado, então mostra os três componentes.
- Dado contrato de R$ 1.000,00 com 2 equipamentos, quando rateado, então cada um recebe R$ 500,00 (premissa de RN-027).

## EP-007 — Fundação, migração e transição [proposto]

Permissões, auditoria, dados, integração, carga, convivência e treinamento.

Prioridade: Must

### FT-014 — Segurança e dados pessoais [proposto]

Permissões, trilha e exclusão de dados de paciente.

Prioridade: Must

#### US-001 — Controlar acesso por papel e unidade [proposto]

Como administrador do sistema, quero conceder acesso por papel e unidade, para que cada área só aja no que lhe cabe.

Prioridade: Must · Requisitos: RNF-004

- Dado usuário de Suprimentos, quando abre um contrato, então pode ver e não pode aprovar acima de sua alçada.
- Dado usuário sem papel na unidade, quando tenta abrir uma medição, então o acesso é negado e registrado.
- Dado usuário com papel removido hoje, quando faz nova ação, então a permissão antiga já não vale.

#### US-038 — Excluir dados de paciente da integração [proposto]

Como encarregado de dados, quero que identificadores de paciente não entrem no sistema, para reduzir exposição.

Prioridade: Must · Requisitos: RNF-001

- Dada OS com nome de paciente, quando integrada, então o dado não é armazenado.
- Dada migração histórica, quando concluída, então uma busca nos campos importados não acha nome ou prontuário.
- Dada OS com evento adverso, quando integrada, então chega só o indicador, sem paciente (premissa de Q-017).

#### US-039 — Registrar trilha de contrato, medição e título [proposto]

Como auditor interno, quero histórico das alterações, para saber quem mudou o quê.

Prioridade: Must · Requisitos: RNF-007

- Dada alteração de contrato, quando salva, então registra usuário, data, valores anteriores e novos.
- Dada alteração de vencimento, quando salva, então exige motivo e registra.
- Dado registro de trilha, quando há tentativa de alteração, então o sistema recusa.

### FT-015 — Integração [proposto]

Conexão com sistemas mantidos, monitoramento e reprocessamento.

Prioridade: Must

#### US-022 — Conectar aos sistemas mantidos com monitoramento [proposto]

Como coordenador de TI, quero monitorar integrações e reprocessar falhas, para não perder dados.

Prioridade: Must · Requisitos: RF-011, RNF-003, RNF-011

- Dada carga normal, quando concluída, então o registro de execução mostra lidos, aceitos e rejeitados.
- Dada falha de integração, quando detectada, então o alerta sai em até 15 min.
- Dado reprocessamento, quando executado, então não duplica registros.

### FT-016 — Migração e transição [proposto]

De-para, saneamento, carga, convivência e treinamento.

Prioridade: Must

#### US-040 — Sanear e migrar contratos [revisar]

Como advogada do Jurídico, quero migrar contratos conferidos, para começar sem as divergências atuais.

Prioridade: Must · Requisitos: RF-002

- Dados os oito contratos, quando migrados, então cada um tem vigência, valor e SLA conferidos com o documento assinado.
- Dado CT-2026-0021, ausente no ERP, quando migrado, então entra com origem na planilha e pendência de regularização.
- Dado fornecedor com mesmo CNPJ e dois nomes, quando migrado, então resulta em um só cadastro.
- Dados os dois contratos do Hospital Aurora Serra, quando recebidos, então entram na mesma conferência e carga.

#### US-041 — Conduzir convivência e treinamento [proposto]

Como PMO, quero plano de transição e treinamento por área, para entrar em operação até 30/06/2027.

Prioridade: Should · Requisitos: RF-012

- Dada área em entrada em operação, quando inicia o uso, então seus usuários concluíram o treinamento.
- Dada a entrada em operação, quando concluída, então a planilha fica somente leitura.
- Dado contrato renovado na convivência, quando importado, então aparece nos dois controles até o desligamento.

#### US-043 — Incorporar o Hospital Aurora Serra e seus contratos [revisar]

Como Gerente de Suprimentos, quero cadastrar a nova unidade e seus dois contratos, para que ela entre no controle da rede.

Prioridade: Must · Requisitos: RF-021

- Dada a unidade cadastrada, quando aberto o cadastro de contrato, então ela pode ser selecionada, com de-para próprio.
- Dado contrato da unidade sem vigência, valor ou SLA, quando carregado, então a linha é rejeitada com motivo.
- Dados os dois contratos carregados, quando aberta a visão da rede, então aparecem filtrados pela unidade.

### FT-017 — Qualidade operacional [proposto]

Capacidade, disponibilidade, desempenho e recuperação.

Prioridade: Should

#### US-042 — Garantir capacidade, disponibilidade e recuperação [revisar]

Como coordenador de TI, quero metas operacionais verificadas, para sustentar a operação.

Prioridade: Should · Requisitos: RNF-005, RNF-008, RNF-009, RNF-010

- Dada carga de 4.812 equipamentos, 640 OS/mês e 1.460 OCs/ano, quando processada, então não há perda de registros.
- Dada medição mensal, quando calculada, então a disponibilidade é de pelo menos 99,5% e consultas abrem em até 3 s em 95% dos casos (valores propostos).
- Dado teste de restauração, quando executado, então conclui em até 8 horas (valor proposto).
