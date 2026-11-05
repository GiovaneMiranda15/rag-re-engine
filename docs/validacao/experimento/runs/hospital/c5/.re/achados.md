# Achados do diagnóstico

## Divergências

| ID | Achado | Sistemas | Severidade | Fontes | Status | Gera |
|---|---|---|---|---|---|---|
| DIV-001 | Alçada de OC: ERP 80 mil x política 50 mil | SIS-01, geral | alta | doc:politica_compras_POL-SUP-004_rev3.md#2, sql:erp_suprimax_dump.sql:fn_valida_alcada_oc, sql:erp_suprimax_dump.sql:OC-2026-00388 | tratado | Q-003, RN-001 |
| DIV-002 | Alçada de contrato: ERP usa valor mensal, política usa valor global | SIS-01, geral | alta | doc:politica_compras_POL-SUP-004_rev3.md#2.2, sql:erp_suprimax_dump.sql:fn_valida_alcada_contrato, sql:erp_suprimax_dump.sql:CT-2025-0064, sql:erp_suprimax_dump.sql:CT-2025-0102 | tratado | Q-003, RN-002 |
| DIV-003 | Cotações: ERP exige 3 a partir de 25 mil e só em REGULAR; política, 2 acima de 5 mil e 3 acima de 15 mil | SIS-01, geral | alta | doc:politica_compras_POL-SUP-004_rev3.md#3, sql:erp_suprimax_dump.sql:fn_valida_cotacoes, sql:erp_suprimax_dump.sql:OC-2026-00440 | tratado | Q-003, RN-003 |
| DIV-004 | Prazo de pagamento: ERP limita a 15-30 dias; política, padrão 45 e mínimo 30 | SIS-01, geral | alta | doc:politica_compras_POL-SUP-004_rev3.md#5.1, sql:erp_suprimax_dump.sql:chk_prazo_pagamento, sql:erp_suprimax_dump.sql:OC-2026-00440, doc:ata_comite_contratos_2026-08-19.md#6 | tratado | Q-003, Q-004, RN-004, GAR-004 |
| DIV-005 | Parecer jurídico: fluxo acima de 100 mil x política acima de 30 mil | geral | alta | doc:politica_compras_POL-SUP-004_rev3.md#4.5, doc:fluxo_contratacao_manutencao.md#contratacao, doc:controle_contratos.csv#CT-2026-0021 | tratado | Q-006, RN-005, GAR-001 |
| DIV-006 | Início da renovação: 120, 90 ou 60 dias, com responsáveis diferentes | SIS-03, geral | alta | doc:politica_compras_POL-SUP-004_rev3.md#4.2, doc:fluxo_contratacao_manutencao.md#contratacao, doc:regras_da_planilha.md#status | aberto | Q-008, RN-006 |
| DIV-007 | Índice de CT-2025-0064: IGP-M no ERP x IPCA na planilha | SIS-01, SIS-03, geral | alta | doc:politica_compras_POL-SUP-004_rev3.md#4.3, sql:erp_suprimax_dump.sql:indice_reajuste, sql:erp_suprimax_dump.sql:CT-2025-0064, doc:controle_contratos.csv#CT-2025-0064 | tratado | RN-007 |
| DIV-008 | CT-2023-0088: fim 31/12/2026 e ATIVO no ERP x fim 30/06/2026 e Vencido na planilha | SIS-01, SIS-03 | alta | sql:erp_suprimax_dump.sql:CT-2023-0088, doc:controle_contratos.csv#CT-2023-0088, doc:regras_da_planilha.md#status | aberto | Q-007, RF-001 |
| DIV-009 | CT-2022-0055: fim 31/08/2025, ATIVO no ERP e Em renovação na planilha | SIS-01, SIS-03, geral | critica | sql:erp_suprimax_dump.sql:CT-2022-0055, doc:controle_contratos.csv#CT-2022-0055, doc:ata_comite_contratos_2026-08-19.md#7 | aberto | Q-007, RN-008, RIS-004 |
| DIV-010 | CT-2026-0021 existe na planilha e no ManutClin, mas não no ERP | SIS-01, SIS-02, SIS-03, geral | alta | doc:politica_compras_POL-SUP-004_rev3.md#4.1, doc:controle_contratos.csv#CT-2026-0021, sql:manutclin_dump.sql:CT-2026-0021, sql:erp_suprimax_dump.sql:OC-2026-00409, sql:erp_suprimax_dump.sql:OC-2026-00431, sql:erp_suprimax_dump.sql:OC-2026-00452 | aberto | Q-007, RN-008 |
| DIV-011 | SLA de atendimento de CT-2024-0117: 4 h na planilha x 8 h no ManutClin | SIS-02, SIS-03 | alta | doc:controle_contratos.csv#CT-2024-0117, sql:manutclin_dump.sql:contrato_ref | tratado | Q-009, RN-009 |
| DIV-012 | Criticidade em três escalas sem equivalência | SIS-02, SIS-03, geral | alta | doc:politica_compras_POL-SUP-004_rev3.md#6.2, sql:manutclin_dump.sql:equipamento, doc:regras_da_planilha.md#colunas | aberto | Q-011, RN-010 |
| DIV-013 | Preventiva de ventiladores na Central: 365 dias no plano x Semestral no contrato | SIS-02, SIS-03 | alta | sql:manutclin_dump.sql:plano_preventivo, doc:controle_contratos.csv#CT-2023-0019 | tratado | Q-012, RN-011 |
| DIV-014 | Valor de CT-2024-0117: R$ 132.480,00 no ERP x R$ 126.000,00 na planilha (ano) | SIS-01, SIS-03 | media | sql:erp_suprimax_dump.sql:CT-2024-0117, doc:controle_contratos.csv#CT-2024-0117 | aberto | RF-001 |
| DIV-015 | Mesmo CNPJ com dois nomes: MTS (ERP) x BioVolt (ManutClin e planilha) | SIS-01, SIS-02, SIS-03 | baixa | sql:erp_suprimax_dump.sql:fornecedor, sql:manutclin_dump.sql:prestador, doc:controle_contratos.csv#CT-2023-0088 | aberto | RF-002 |
| DIV-016 | Regra de liberação do fluxo não é exigida pelo ManutClin | SIS-02, geral | critica | doc:fluxo_contratacao_manutencao.md#corretiva, sql:manutclin_dump.sql:trg_os_fecha, sql:manutclin_dump.sql:88213 | tratado | Q-013, RN-012 |
| DIV-017 | Política exige ateste para pagar; ERP permite pagar medição sem ateste | SIS-01, geral | alta | doc:politica_compras_POL-SUP-004_rev3.md#5.2, sql:erp_suprimax_dump.sql:fn_libera_medicao, sql:erp_suprimax_dump.sql:medicao | tratado | RN-013 |
| DIV-018 | Quem solicita não pode aprovar; ERP não impede | SIS-01, geral | media | doc:politica_compras_POL-SUP-004_rev3.md#2.3, sql:erp_suprimax_dump.sql:fn_valida_alcada_oc, sql:erp_suprimax_dump.sql:OC-2026-00420 | tratado | RN-014 |
| DIV-019 | Limite do parecer: R$ 30.000,00 na política e em Q-006 x R$ 200.000,00 no memorando | geral | alta | doc:politica_compras_POL-SUP-004_rev3.md#4.5, entrevista:juridico-compliance Q-006, doc:M-02-memorando-juridico-engclin.md#1 | aberto | Q-019, RN-005, RN-028 |

## Gargalos

| ID | Achado | Sistemas | Severidade | Fontes | Status | Gera |
|---|---|---|---|---|---|---|
| GAR-001 | Contratação leva 38 dias, 23 aguardando o Jurídico | geral | alta | doc:indicadores_manutencao_2025.md#tempos, doc:politica_compras_POL-SUP-004_rev3.md#4.5 | aberto | Q-006, RF-003, OPO-006 |
| GAR-002 | OS redigitada como requisição; 21 dias em AGUARDANDO_COMPRA | SIS-01, SIS-02, geral | alta | doc:indicadores_manutencao_2025.md#tempos, doc:ata_comite_contratos_2026-08-19.md#5, doc:fluxo_contratacao_manutencao.md#corretiva, sql:erp_suprimax_dump.sql:origem_os, sql:manutclin_dump.sql:requisicao_erp, sql:manutclin_dump.sql:88190 | aberto | Q-018, RF-004, OPO-001 |
| GAR-003 | Conferência de medição: duas analistas, cerca de 6 dias úteis por mês | SIS-01, SIS-02, geral | alta | doc:ata_comite_contratos_2026-08-19.md#4, doc:indicadores_manutencao_2025.md#tempos | aberto | Q-010, RF-005, OPO-002 |
| GAR-004 | Cerca de 140 títulos por mês têm vencimento alterado à mão | SIS-01, geral | alta | doc:ata_comite_contratos_2026-08-19.md#6, doc:indicadores_manutencao_2025.md#tempos | aberto | Q-004, RF-006, OPO-004 |
| GAR-005 | Planilha centralizada em uma pessoa, com pedidos por e-mail e cópia em PDF | SIS-03 | alta | doc:regras_da_planilha.md#quem-mexe | aberto | RF-001, RIS-008 |

## Riscos

| ID | Achado | Sistemas | Severidade | Fontes | Status | Gera |
|---|---|---|---|---|---|---|
| RIS-001 | Equipamento em uso com calibração vencida, sem bloqueio | SIS-02, geral | critica | doc:politica_compras_POL-SUP-004_rev3.md#6.3, sql:manutclin_dump.sql:PAT-004512, sql:manutclin_dump.sql:PAT-016002, sql:manutclin_dump.sql:88213 | aberto | Q-013, RN-015, RF-007 |
| RIS-002 | Dados de paciente em OS, com leitura pelo portal de prestadores | SIS-02 | critica | sql:manutclin_dump.sql:paciente_nome, sql:manutclin_dump.sql:paciente_prontuario, sql:manutclin_dump.sql:prestador_portal | aberto | Q-016, Q-017, RNF-001 |
| RIS-003 | Prestador pode editar a hora de atendimento que mede seu próprio SLA | SIS-02 | alta | sql:manutclin_dump.sql:prestador_portal | aberto | Q-010, RNF-002 |
| RIS-004 | Serviço e pagamento com contrato vencido | SIS-01, geral | critica | sql:erp_suprimax_dump.sql:CT-2022-0055, sql:erp_suprimax_dump.sql:fn_libera_medicao, sql:erp_suprimax_dump.sql:OC-2026-00440, doc:ata_comite_contratos_2026-08-19.md#7 | aberto | Q-007, RN-008 |
| RIS-005 | Indício de fracionamento em OCs | SIS-01, geral | alta | doc:politica_compras_POL-SUP-004_rev3.md#3.1, sql:erp_suprimax_dump.sql:OC-2026-00301, sql:erp_suprimax_dump.sql:OC-2026-00302, sql:erp_suprimax_dump.sql:OC-2026-00303 | aberto | Q-003, RN-016 |
| RIS-006 | Glosa prevista e não aplicada | SIS-01, SIS-02, geral | alta | doc:politica_compras_POL-SUP-004_rev3.md#5.3, doc:indicadores_manutencao_2025.md#gasto, sql:manutclin_dump.sql:88170, sql:erp_suprimax_dump.sql:medicao | aberto | Q-010, RN-017 |
| RIS-007 | Controles do ERP podem ser contornados | SIS-01, geral | alta | sql:erp_suprimax_dump.sql:fn_valida_alcada_oc, sql:erp_suprimax_dump.sql:fn_valida_cotacoes, sql:erp_suprimax_dump.sql:trg_oc_alcada, doc:portaria_DG-017-2025_compras_emergenciais.md#2, doc:portaria_DG-017-2025_compras_emergenciais.md#3 | aberto | RN-018, RN-016 |
| RIS-008 | Dependência de uma única pessoa para a planilha | SIS-03 | alta | doc:regras_da_planilha.md#quem-mexe, doc:ata_comite_contratos_2026-08-19.md#encaminhamentos | aberto | RF-001 |
| RIS-009 | Seis contratos acabam antes da entrada em operação | SIS-01, SIS-03, geral | alta | sql:erp_suprimax_dump.sql:contrato, doc:controle_contratos.csv#fim, doc:politica_compras_POL-SUP-004_rev3.md#4.2, doc:escopo.md#prazo | aberto | Q-002, Q-008, RF-008 |
| RIS-010 | Soma de contratos pode misturar reais e dólares | SIS-01, SIS-03, geral | media | sql:erp_suprimax_dump.sql:CT-2025-0031, doc:controle_contratos.csv#CT-2025-0031, doc:politica_compras_POL-SUP-004_rev3.md#4.4, doc:regras_da_planilha.md#colunas | aberto | RN-019, RF-009 |
| RIS-011 | Custo por equipamento não pode ser calculado hoje | SIS-01, SIS-02, geral | alta | doc:ata_comite_contratos_2026-08-19.md#1, doc:indicadores_manutencao_2025.md#gasto, doc:indicadores_manutencao_2025.md#inventario, sql:erp_suprimax_dump.sql:ordem_compra | aberto | Q-005, RF-010, OPO-003 |
| RIS-012 | Conclusões limitadas pelas fontes disponíveis | SIS-01, SIS-02, geral | media | sql:erp_suprimax_dump.sql:Recorte, sql:manutclin_dump.sql:Recorte | aberto | Q-001, Q-004, Q-018 |
| RIS-013 | Manual de 2019 parcialmente sem revogação | geral, SIS-01 | baixa | doc:politica_compras_POL-SUP-004_rev3.md#1.3, doc:manual_processo_compras_v2_2019.md#2, doc:manual_processo_compras_v2_2019.md#5, sql:erp_suprimax_dump.sql:OC-2026-00440 | aberto | RNF-006 |
| RIS-014 | Reajuste pode estar atrasado ou sem controle | SIS-01 | media | sql:erp_suprimax_dump.sql:dt_ultimo_reajuste, sql:erp_suprimax_dump.sql:contrato | aberto | RN-007 |
| RIS-015 | Lacunas possíveis no plano preventivo | SIS-02 | media | sql:manutclin_dump.sql:plano_preventivo, doc:indicadores_manutencao_2025.md#inventario | aberto | Q-012, RN-011 |
| RIS-016 | Decisões estruturais sem dono | geral | alta | entrevista:negocio Q-001, entrevista:financeiro Q-004, entrevista:gestao-pmo Q-015 | aberto | Q-001, Q-002, Q-004, Q-007, Q-018, RF-019, RNF-008, RNF-010 |
| RIS-017 | Nova unidade sem dados, com prazo mantido | geral | media | doc:M-01-email-suprimentos.md#1, doc:politica_compras_POL-SUP-004_rev3.md#1.1, doc:escopo.md#prazo | aberto | Q-020, Q-021, RF-021 |

## Pontos de apoio

| ID | Achado | Sistemas | Severidade | Fontes | Status | Gera |
|---|---|---|---|---|---|---|
| APO-001 | Etiqueta patrimonial como chave de equipamento | SIS-01, SIS-02, geral | alta | doc:indicadores_manutencao_2025.md#inventario, sql:erp_suprimax_dump.sql:contrato_item, sql:manutclin_dump.sql:equipamento | aberto | RF-002 |
| APO-002 | Número do contrato e CNPJ como chaves entre sistemas | SIS-01, SIS-02, SIS-03 | alta | sql:erp_suprimax_dump.sql:contrato, sql:manutclin_dump.sql:contrato_ref, doc:controle_contratos.csv#numero_contrato | aberto | RF-002 |
| APO-003 | Fluxo emergencial funcionou no caso observado | SIS-01, geral | media | doc:portaria_DG-017-2025_compras_emergenciais.md#2, doc:portaria_DG-017-2025_compras_emergenciais.md#3, doc:portaria_DG-017-2025_compras_emergenciais.md#4, doc:portaria_DG-017-2025_compras_emergenciais.md#5, sql:erp_suprimax_dump.sql:OC-2026-00412, doc:ata_comite_contratos_2026-08-19.md#2 | aberto | RN-018 |
| APO-004 | Indicadores se reconciliam com as bases | SIS-03, geral | media | doc:indicadores_manutencao_2025.md#gasto, doc:indicadores_manutencao_2025.md#inventario, doc:controle_contratos.csv#valor_anual_brl, doc:ata_comite_contratos_2026-08-19.md#1 | aberto | Q-005 |
| APO-005 | Mecânica de controles do ERP é reaproveitável | SIS-01 | media | sql:erp_suprimax_dump.sql:fn_valida_alcada_oc, sql:erp_suprimax_dump.sql:fn_libera_medicao, sql:erp_suprimax_dump.sql:glosa, sql:erp_suprimax_dump.sql:nivel_alcada | aberto | RN-001 |
| APO-006 | ManutClin guarda o necessário para apurar SLA e liberação | SIS-02 | media | sql:manutclin_dump.sql:ordem_servico, sql:manutclin_dump.sql:contrato_ref, sql:manutclin_dump.sql:trg_os_abre | aberto | RF-005 |
| APO-007 | Política versionada e Comitê de Contratos ativo | geral | media | doc:politica_compras_POL-SUP-004_rev3.md#1.3, doc:ata_comite_contratos_2026-08-19.md#assuntos | aberto | RNF-006 |

## Oportunidades

| ID | Achado | Sistemas | Severidade | Fontes | Status | Gera |
|---|---|---|---|---|---|---|
| OPO-001 | Gerar a requisição a partir da OS | SIS-01, SIS-02 | alta | doc:indicadores_manutencao_2025.md#tempos, doc:ata_comite_contratos_2026-08-19.md#5 | aberto | RF-004 |
| OPO-002 | Conferência assistida de medição e proposta de glosa | SIS-01, SIS-02 | alta | doc:ata_comite_contratos_2026-08-19.md#4, doc:politica_compras_POL-SUP-004_rev3.md#5.3 | aberto | RF-005, RN-017 |
| OPO-003 | Custo total por equipamento para decidir manter ou substituir | SIS-01, SIS-02 | alta | doc:ata_comite_contratos_2026-08-19.md#1 | aberto | RF-010 |
| OPO-004 | Título que nasce com o vencimento certo | SIS-01 | media | doc:ata_comite_contratos_2026-08-19.md#6, doc:politica_compras_POL-SUP-004_rev3.md#5.1 | aberto | RF-006, RN-004 |
| OPO-005 | Cadastro único de contratos com alertas e histórico | SIS-01, SIS-03 | alta | doc:regras_da_planilha.md#quem-mexe, doc:politica_compras_POL-SUP-004_rev3.md#4.2 | aberto | RF-001, RF-008 |
| OPO-006 | Fila de parecer com visibilidade e prioridade | geral | media | doc:indicadores_manutencao_2025.md#tempos | aberto | RF-003 |
| OPO-007 | Visão consolidada por contrato, fornecedor, equipamento e unidade | SIS-01, SIS-02, SIS-03 | alta | doc:escopo.md#visao, sql:erp_suprimax_dump.sql:contrato, sql:manutclin_dump.sql:equipamento | aberto | RF-009 |
