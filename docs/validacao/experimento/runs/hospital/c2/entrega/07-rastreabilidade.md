# Rastreabilidade

Liga requisitos, fontes e backlog. POL = POL-SUP-004 rev. 3; R*n* = resposta *n* de `respostas.md`; P*n* = pergunta *n*. Cada US-*n* implementa o RF-*n*.

## 1. Requisitos, fontes e backlog

| Requisito | Descrição | Fase | Regras | RNF | Fontes | História | Feature / Épico | Prior. | Pendências |
|---|---|---|---|---|---|---|---|---|---|
| RF-01 | Cadastro único de contrato: número, unidade, fornecedor, objeto, vigência, valor, índice, SLA de atendimento e solução, preventiva, documento | F1 | RN-08, RN-18 | - | Escopo; R2; R6; R13; planilha; ERP; ManutClin | US-01 | F-01 / EP-01 | 1 | DP-08 |
| RF-02 | Fornecedor único por CNPJ, com nomes alternativos | F1 | - | - | ERP; ManutClin; planilha | US-02 | F-01 / EP-01 | 1 | - |
| RF-03 | Vínculo entre contrato, equipamentos (um equipamento pode ter vários contratos) e unidades | F1 | - | - | ERP; ManutClin; planilha; escopo | US-03 | F-01 / EP-01 | 1 | - |
| RF-04 | Contrato em moeda estrangeira, com câmbio de referência | F1 | RN-11 | RNF-09 | POL 4.4; R12; planilha | US-04 | F-01 / EP-01 | 1 | DP-14 |
| RF-05 | Status de vigência calculado por data, separado do andamento da renovação | F1 | RN-09 | - | POL 4.2; R5; R6; ata | US-05 | F-02 / EP-01 | 1 | - |
| RF-06 | Alertas de renovação a partir de 120 dias | F1 | RN-09 | - | POL 4.2; R2; R5 | US-06 | F-02 / EP-01 | 1 | DP-07 |
| RF-07 | Fluxo de renovação com etapas e responsáveis | F1 | RN-09, RN-07 | - | POL 4.2, 4.5; R5; fluxo | US-07 | F-02 / EP-01 | 1 | DP-06, DP-07, DP-19 |
| RF-08 | Aditivos numerados com histórico, notificando o Jurídico | F1 | RN-19, RN-07 | - | R6; ERP; planilha; escopo | US-08 | F-03 / EP-01 | 1 | DP-06, DP-08, DP-19 |
| RF-09 | Registro e agenda de reajuste por contrato | F1 | RN-10 | - | POL 4.3; R6; ERP; planilha | US-09 | F-03 / EP-01 | 2 | DP-07 |
| RF-10 | Carga dos contratos saneados contra o documento assinado | F1 | RN-08 | RNF-06 | R6; R8; 03-tecnico seção 7 | US-10 | F-04 / EP-01 | 1 | DP-04, DP-05, DP-08 |
| RF-11 | Levantamento de contratos não registrados e de OCs avulsas recorrentes | F1 | RN-08 | - | R8; ERP | US-11 | F-04 / EP-01 | 1 | DP-10 |
| RF-12 | Requisição com área demandante, unidade, patrimônio e origem | F1 | RN-03 | - | Escopo; ata; ERP | US-12 | F-05 / EP-02 | 2 | DP-11 |
| RF-13 | Cotações exigidas conforme a faixa de valor | F1 | RN-04 | - | POL 3; R3; ERP | US-13 | F-05 / EP-02 | 2 | - |
| RF-14 | Limites da Política como parâmetros com data de vigência | F1 | RN-01, RN-02, RN-04, RN-06, RN-07, RN-09, RN-12, RN-14 | - | POL; Portaria; R3; M-02 | US-14 | F-06 / EP-02 | 2 | DP-05, DP-19 |
| RF-15 | Aprovação de OC por alçada | F1 | RN-01, RN-22 | - | POL 2, 2.1; R3; R2; ERP | US-15 | F-06 / EP-02 | 2 | DP-05, DP-10 |
| RF-16 | Impedimento de autoaprovação | F1 | RN-03 | - | POL 2.3; ERP | US-16 | F-06 / EP-02 | 2 | DP-11 |
| RF-17 | Aprovação de contrato por valor global, com parecer jurídico | F1 | RN-02, RN-07, RN-22 | - | POL 2.2, 4.5; R3; R4; ERP; M-02 | US-17 | F-06 / EP-02 | 2 | DP-05, DP-06, DP-19 |
| RF-18 | Detecção de possível fracionamento | F1 | RN-05 | - | POL 3.1; ERP | US-18 | F-06 / EP-02 | 2 | DP-11 |
| RF-19 | Compra emergencial conforme a Portaria | F1 | RN-06 | - | Portaria DG-017/2025; ata | US-19 | F-07 / EP-02 | 2 | - |
| RF-20 | Trilha de auditoria de aprovações e alterações de contrato | F1 | RN-22 | RNF-01, RNF-02, RNF-08 | R2; R15 | US-20 | F-08 / EP-02 | 2 | DP-18 |
| RF-21 | Perfis de acesso por função e unidade | F1 | RN-21 | RNF-03 | R15; grants do ManutClin | US-21 | F-08 / EP-02 | 2 | DP-18 |
| RF-22 | Consulta a OS e inventário do ManutClin, sem dados de paciente | F1 | RN-21 | RNF-02, RNF-04, RNF-05, RNF-06 | Escopo; ManutClin; R15 | US-22 | F-09 / EP-03 | 3 | DP-01, DP-17, DP-18 |
| RF-23 | Abertura de requisição a partir da OS, com vínculo estruturado | F1 | - | - | Ata; fluxo; ManutClin; ERP | US-23 | F-09 / EP-03 | 3 | DP-01 |
| RF-24 | Medição mensal única por contrato e competência | F1 | RN-13 | RNF-09 | POL 4.1, 5.2; ERP | US-24 | F-10 / EP-03 | 3 | - |
| RF-25 | Conferência da medição com as OS da competência | F1 | RN-13, RN-14 | RNF-04 | Ata; POL 5; ManutClin | US-25 | F-10 / EP-03 | 3 | DP-13 |
| RF-26 | Ateste no sistema pela Engenharia Clínica | F1 | RN-13, RN-22 | - | POL 5.2; R2; ERP | US-26 | F-10 / EP-03 | 3 | - |
| RF-27 | Liberação para pagamento, com vencimento calculado | F1 | RN-12, RN-13 | RNF-06 | POL 5.1; ata; ERP | US-27 | F-11 / EP-03 | 3 | DP-01, DP-12 |
| RF-28 | Tratamento de pagamento de contrato vencido | F1 | RN-20 | - | Ata; POL; ERP | US-28 | F-11 / EP-03 | 3 | DP-09 |
| RF-29 | Cálculo de atendimento de SLA por OS | F1 | RN-14 | RNF-04 | POL 5.3; R6; R11; ManutClin | US-29 | F-12 / EP-04 | 4 | DP-13 |
| RF-30 | Sugestão e decisão de glosa | F1 | RN-14 | RNF-09 | POL 5.3; R2; indicadores; M-02 | US-30 | F-12 / EP-04 | 4 | DP-13 |
| RF-31 | Visão consolidada por contrato, fornecedor, equipamento e unidade | F1 | RN-11 | RNF-09 | Escopo; R2 | US-31 | F-13 / EP-05 | 4 | DP-14 |
| RF-32 | Indicadores de acompanhamento do processo | F1 | - | - | Indicadores; POL | US-32 | F-13 / EP-05 | 4 | DP-03 |
| RF-33 | Criticidade oficial em quatro níveis por equipamento | F1 | RN-17 | - | POL 6.2; R13 | US-33 | F-14 / EP-05 | 3 | DP-15 |
| RF-34 | Painel de exceções: OS fechada sem teste ou liberação, calibração vencida em uso | F1 | RN-15, RN-16 | RNF-02 | Fluxo; POL 6.3; R14; ManutClin | US-34 | F-14 / EP-05 | 2 | DP-16, DP-17 |
| RF-35 | Custo por equipamento: contrato, chamados e peças | F2 | - | - | Ata; R2; R12; indicadores | US-35 | F-15 / EP-06 | 4 | DP-14 |
| RF-36 | Adequação de fluxo e planilha à Política durante a transição | F1 | RN-07, RN-09 | - | R4; R5; R6; fluxo; planilha | US-36 | F-04 / EP-01 | 1 | DP-07, DP-19 |
| RF-37 | Cadastro do Hospital Aurora Serra e carga de seus dois contratos | F1 | RN-08 | RNF-05, RNF-06 | M-01 item 1 | US-37 | F-04 / EP-01 | 1 | DP-02, DP-20 |

## 2. Regras de negócio e backlog

| Regra | Situação | Fonte | Histórias |
|---|---|---|---|
| RN-01 | Confirmada | POL 2 e 2.1; R3 | US-14, US-15 |
| RN-02 | Confirmada | POL 2.2; R3 | US-14, US-17 |
| RN-03 | Vigente | POL 2.3 | US-12, US-16 |
| RN-04 | Confirmada | POL 3; R3 | US-13, US-14 |
| RN-05 | Vigente | POL 3.1 | US-18 |
| RN-06 | Vigente | Portaria DG-017/2025 | US-14, US-19 |
| RN-07 | Confirmada | POL 4.5; R4 | US-07, US-08, US-14, US-17, US-36 |
| RN-08 | Vigente | POL 4.1; R8 | US-01, US-10, US-11, US-37 |
| RN-09 | Confirmada | POL 4.2; R5 | US-05, US-06, US-07, US-14, US-36 |
| RN-10 | Vigente | POL 4.3; R6 | US-09 |
| RN-11 | Vigente | POL 4.4; R12 | US-04, US-31 |
| RN-12 | Vigente | POL 5.1 | US-14, US-27 |
| RN-13 | Vigente | POL 5.2 | US-24, US-25, US-26, US-27 |
| RN-14 | Vigente | POL 5.3; M-02 | US-14, US-25, US-29, US-30 |
| RN-15 | Confirmada | Fluxo; R14 | US-34 |
| RN-16 | Vigente | POL 6.3 | US-34 |
| RN-17 | Confirmada | POL 6.2; R13 | US-33 |
| RN-18 | Confirmada | R13 | US-01 |
| RN-19 | Provisória | R6 (proposta minha) | US-08 |
| RN-20 | Provisória | Ata; proposta minha | US-28 |
| RN-21 | Provisória | Minimização; validar com DPO (DP-18) | US-21, US-22 |
| RN-22 | Confirmada | R2; R15 | US-15, US-17, US-20, US-26 |

## 3. Requisitos não funcionais e backlog

| RNF | Histórias | Observação |
|---|---|---|
| RNF-01 | US-20 |  |
| RNF-02 | US-20, US-22, US-34 |  |
| RNF-03 | US-21 |  |
| RNF-04 | US-22, US-25, US-29 |  |
| RNF-05 | US-22, US-37 |  |
| RNF-06 | US-10, US-22, US-27, US-37 |  |
| RNF-07 | - | Sem história: metas pendentes de DP-01 |
| RNF-08 | US-20 |  |
| RNF-09 | US-04, US-24, US-30, US-31 |  |
| RNF-10 | - | Critério transversal das histórias com tela |
| RNF-11 | - | Restrição de prazo, acompanhada no plano de entrega |

## 4. Achados do diagnóstico e backlog

| Achado | Histórias | Tratamento fora do backlog |
|---|---|---|
| DIV-01 | US-14, US-15 |  |
| DIV-02 | US-14, US-17 |  |
| DIV-03 | US-13, US-14 |  |
| DIV-04 | US-14, US-17, US-36 |  |
| DIV-05 | US-05, US-06, US-07, US-36 |  |
| DIV-06 | US-14, US-27 |  |
| DIV-07 | US-09, US-10 |  |
| DIV-08 | US-33 |  |
| DIV-09 | US-11 |  |
| DIV-10 | US-34 |  |
| DIV-11 | US-26 |  |
| DIV-12 | US-16, US-18 |  |
| DIV-13 | US-19 |  |
| DIV-14 | US-02, US-10 |  |
| DIV-15 | - | Ação 7 de `02-negocio.md`, seção 9; desfibriladores em DP-15 |
| DIV-16 | US-33 |  |
| DIV-17 | US-03 |  |
| DIV-18 | US-12, US-23 |  |
| DIV-19 | US-31, US-32, US-35 | Consolidação dos números de 2025, encaminhada pela ata |
| GAR-01 | US-07, US-17, US-32 | DP-06 |
| GAR-02 | US-23 |  |
| GAR-03 | US-25, US-32 |  |
| GAR-04 | US-27 |  |
| GAR-05 | US-01, US-08, US-20, US-36 |  |
| GAR-06 | US-01, US-22, US-31 |  |
| OPO-01 | US-23 |  |
| OPO-02 | US-25, US-29, US-30 |  |
| OPO-03 | US-14 |  |
| OPO-04 | US-06 |  |
| OPO-05 | US-35 |  |
| OPO-06 | - | Sem história: negociação comercial, fora do sistema |
| OPO-07 | US-11 | Parte comercial fora do sistema |
| OPO-08 | - | DP-06; sem história até haver resposta |
| OPO-09 | US-27 |  |
| RIS-01 | US-34 | Ações 1 e 2 |
| RIS-02 | US-21, US-22 | Ação 3; DP-18 |
| RIS-03 | US-21, US-22, US-29 | Ação 3 |
| RIS-04 | US-05, US-06, US-07, US-28 | Ação 4 |
| RIS-05 | US-13, US-15, US-16, US-17, US-18, US-20 |  |
| RIS-06 | US-11, US-24, US-26, US-27, US-28, US-30 |  |
| RIS-07 | US-01, US-08, US-10 |  |
| RIS-08 | US-36 | Ondas de entrega; ação 11 |
| RIS-09 | US-22 | DP-01 |
| RIS-10 | US-04, US-31 |  |
| RIS-11 | US-17 | DP-06 |
| RIS-12 | US-09 |  |
| RIS-13 | - | DP-04 |
| RIS-14 | US-11 |  |
| RIS-15 | US-37 | DP-02, DP-20; prazo a reavaliar |

## 5. Respostas e efeito

| Pergunta | Respondido | Sem resposta | Efeito |
|---|---|---|---|
| P1 | Nada | Tudo | DP-01; arquitetura em aberto |
| P2 | Prioridades; custo depois; portal fora | Quatro unidades, métrica, gases | Ordem do backlog; DP-02, DP-03, DP-04 |
| P3 | Limites da Política; ERP desatualizado | Exceção; contratos anteriores | RN-01, RN-02, RN-04; DP-05 |
| P4 | R$ 30 mil | Aditivo, renovação, causas, capacidade | RN-07; DP-06 |
| P5 | 120 dias; fluxo e planilha se adequam | Donos, transição, reajuste | RN-09, RF-36; DP-07 |
| P6 | CT-2024-0117, CT-2025-0064, CT-2023-0088 | Originais, dono, valor e parecer do aditivo | Carga (`03-tecnico.md`, seção 7); RN-19; DP-08 |
| P7 | Nada | Tudo | DP-09; RN-20 provisória |
| P8 | CT-2026-0021 assinado na unidade, pago por avulsas | Outros casos; AVULSA | RF-11; DP-10 |
| P9 | Nada | Tudo | DP-11 |
| P10 | Nada | Tudo | DP-12; RF-27 termina na liberação |
| P11 | Nada | Tudo | DP-13; glosa com regra provisória e decisão humana |
| P12 | Helvion em dólar, a R$ 5,40 | Rateio, equipe, histórico, valor consolidado | RN-11; DP-14 |
| P13 | Quatro níveis; mapeamento; ventilador semestral | Crítico, herança, tomógrafo, desfibriladores | RN-17, RN-18; DP-15 |
| P14 | Teste e assinatura obrigatórios | Impedir ou alertar; exceção; OS 88213; evento adverso | RN-15; DP-16, DP-17 |
| P15 | Portal fora; trilha nas aprovações | Dados de paciente, auditoria, retenção, uso do portal | RN-22; DP-18 |


## 6. Mudanças e efeito

| Mudança | Classificação | Efeito |
|---|---|---|
| M-01.1 Hospital Aurora Serra | novo | RF-37, US-37, DP-02, DP-20, RIS-15 |
| M-01.2 Alçada acima de R$ 250 mil | existente | RN-01, RN-02, sem alteração |
| M-01.3 Lotes de medicamentos | fora_escopo | Nenhum |
| M-02.1 Parecer acima de R$ 200 mil | conflitante | RN-07 mantida; DP-19 em US-07, US-08, US-14, US-17, US-36 |
| M-02.2 Teto de glosa de 10% | complementar | RN-14; US-14, US-30 |
