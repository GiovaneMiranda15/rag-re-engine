# Rastreabilidade

**Projeto:** sistema único de compras e contratos de manutenção de equipamentos. **Data:** 04/11/2026. **Baseline:** sem baseline.

As matrizes são geradas de `.re/modelo/` por `recop.py render`. Citações `doc:` e `sql:` apontam para o arquivo em `fontes/` e o objeto ou seção; `entrevista:` aponta para a resposta em `respostas.md`.

## Análise

- **Requisitos:** 58, sendo 30 confirmados e 28 hipóteses. Hipótese não foi promovida por resposta "não sei".
- **Fontes sem requisito derivado:** `manual_processo_compras_v2_2019.md` só sustenta o achado RIS-013 e o fato EL-015, pois os capítulos 4 e 5 estão revogados; é o esperado. Todas as outras fontes têm requisitos.
- **Achados sem tratamento:** nenhum: os 28 achados abertos têm requisito ou pergunta. Seguem abertos: DIV-006, DIV-008, DIV-009, DIV-010, DIV-012, DIV-014, DIV-015, GAR-001, GAR-002, GAR-003, GAR-004, GAR-005, RIS-001, RIS-002, RIS-003, RIS-004, RIS-005, RIS-006, RIS-007, RIS-008, RIS-009, RIS-010, RIS-011, RIS-012, RIS-013, RIS-014, RIS-015, RIS-016.
- **Histórias bloqueadas:** 11 de 42: US-006, US-007, US-022, US-023, US-024, US-033, US-034, US-036, US-037, US-038, US-042.
- **Perguntas abertas:** Q-001, Q-002, Q-004, Q-005, Q-007, Q-008, Q-010, Q-013, Q-016, Q-017, Q-018. Q-014 e Q-015 foram encaminhadas e substituídas por Q-016, Q-017 e Q-018.


> Gerado por `recop.py render`. Não edite à mão.

## 1. Requisito → fontes → backlog

| Requisito | Status | Fontes | Sistemas | Achados | Histórias | Perfis | Depende de |
|---|---|---|---|---|---|---|---|
| RN-001 | confirmado | doc:politica_compras_POL-SUP-004_rev3.md#2, entrevista:financeiro Q-003 | SIS-01 | APO-005, DIV-001 | US-014 | financeiro | — |
| RN-002 | confirmado | doc:politica_compras_POL-SUP-004_rev3.md#2.2, entrevista:financeiro Q-003 | SIS-01 | DIV-002 | US-015 | financeiro, juridico-compliance | — |
| RN-003 | confirmado | doc:politica_compras_POL-SUP-004_rev3.md#3, entrevista:financeiro Q-003 | SIS-01 | DIV-003 | US-013 | suprimentos | — |
| RN-004 | confirmado | doc:politica_compras_POL-SUP-004_rev3.md#5.1, doc:portaria_DG-017-2025_compras_emergenciais.md#4, entrevista:financeiro Q-003 | SIS-01 | DIV-004, OPO-004 | US-034 | financeiro | — |
| RN-005 | confirmado | doc:politica_compras_POL-SUP-004_rev3.md#4.5, entrevista:juridico-compliance Q-006 | SIS-01 | DIV-005 | US-011 | juridico-compliance | — |
| RN-006 | hipótese | doc:politica_compras_POL-SUP-004_rev3.md#4.2 | SIS-03 | DIV-006 | US-007 | juridico-compliance, suprimentos, engenharia-clinica | — |
| RN-007 | confirmado | doc:politica_compras_POL-SUP-004_rev3.md#4.3, doc:politica_compras_POL-SUP-004_rev3.md#4.4, doc:controle_contratos.csv#CT-2025-0064, doc:regras_da_planilha.md#colunas | SIS-01 | DIV-007, RIS-014 | US-003 | financeiro, juridico-compliance | — |
| RN-008 | hipótese | doc:politica_compras_POL-SUP-004_rev3.md#4.1, doc:ata_comite_contratos_2026-08-19.md#7 | SIS-01 | DIV-009, DIV-010, RIS-004 | US-006 | juridico-compliance, financeiro | — |
| RN-009 | confirmado | doc:regras_da_planilha.md#colunas, sql:manutclin_dump.sql:contrato_ref, entrevista:juridico-compliance Q-009, entrevista:negocio Q-002 | SIS-02, SIS-03 | DIV-011 | US-002, US-031 | juridico-compliance, engenharia-clinica | — |
| RN-010 | confirmado | doc:politica_compras_POL-SUP-004_rev3.md#6.2, entrevista:engenharia-clinica Q-011 | SIS-02, SIS-03 | DIV-012 | US-029 | engenharia-clinica | — |
| RN-011 | confirmado | sql:manutclin_dump.sql:plano_preventivo, doc:controle_contratos.csv#preventiva, entrevista:engenharia-clinica Q-012 | SIS-02 | DIV-013, RIS-015 | US-002 | engenharia-clinica | — |
| RN-012 | confirmado | doc:fluxo_contratacao_manutencao.md#corretiva, entrevista:engenharia-clinica Q-013 | SIS-02 | DIV-016 | US-027 | engenharia-clinica | — |
| RN-013 | confirmado | doc:politica_compras_POL-SUP-004_rev3.md#5.2, entrevista:negocio Q-002 | SIS-01 | DIV-017 | US-026 | engenharia-clinica, financeiro | — |
| RN-014 | confirmado | doc:politica_compras_POL-SUP-004_rev3.md#2.3 | SIS-01 | DIV-018 | US-016 | suprimentos | — |
| RN-015 | hipótese | doc:politica_compras_POL-SUP-004_rev3.md#6.3 | SIS-02 | RIS-001 | US-028 | engenharia-clinica | — |
| RN-016 | confirmado | doc:politica_compras_POL-SUP-004_rev3.md#3.1, entrevista:negocio Q-002 | SIS-01 | RIS-005, RIS-007 | US-017 | suprimentos, financeiro | — |
| RN-017 | confirmado | doc:politica_compras_POL-SUP-004_rev3.md#5.3, entrevista:negocio Q-002 | SIS-01, SIS-02 | OPO-002, RIS-006 | US-032 | financeiro, engenharia-clinica | — |
| RN-018 | confirmado | doc:portaria_DG-017-2025_compras_emergenciais.md#2, doc:portaria_DG-017-2025_compras_emergenciais.md#3, doc:portaria_DG-017-2025_compras_emergenciais.md#5 | SIS-01 | APO-003, RIS-007 | US-021 | suprimentos | — |
| RN-019 | confirmado | doc:politica_compras_POL-SUP-004_rev3.md#4.4, doc:regras_da_planilha.md#colunas | SIS-01, SIS-03 | RIS-010 | US-003 | financeiro | — |
| RF-001 | confirmado | doc:regras_da_planilha.md#quem-mexe, entrevista:negocio Q-002 | SIS-01, SIS-03 | DIV-008, DIV-014, GAR-005, OPO-005, RIS-008 | US-002, US-004 | juridico-compliance | — |
| RF-002 | hipótese | sql:erp_suprimax_dump.sql:fornecedor, sql:manutclin_dump.sql:prestador | SIS-01, SIS-02, SIS-03 | APO-001, APO-002, DIV-015 | US-040 | gestao-pmo | — |
| RF-003 | hipótese | doc:indicadores_manutencao_2025.md#tempos, entrevista:juridico-compliance Q-006 | SIS-01 | GAR-001, OPO-006 | US-012 | juridico-compliance | — |
| RF-004 | confirmado | doc:ata_comite_contratos_2026-08-19.md#5, doc:fluxo_contratacao_manutencao.md#corretiva, entrevista:negocio Q-002 | SIS-01, SIS-02 | GAR-002, OPO-001 | US-024 | engenharia-clinica, suprimentos | — |
| RF-005 | confirmado | doc:ata_comite_contratos_2026-08-19.md#4, entrevista:negocio Q-002 | SIS-01, SIS-02 | APO-006, GAR-003, OPO-002 | US-025, US-026 | engenharia-clinica | — |
| RF-006 | hipótese | doc:ata_comite_contratos_2026-08-19.md#6, doc:politica_compras_POL-SUP-004_rev3.md#5.1 | SIS-01 | GAR-004, OPO-004 | US-034 | financeiro | — |
| RF-007 | hipótese | sql:manutclin_dump.sql:equipamento | SIS-02 | RIS-001 | US-023 | engenharia-clinica | — |
| RF-008 | confirmado | doc:politica_compras_POL-SUP-004_rev3.md#4.2, entrevista:negocio Q-002 | SIS-01, SIS-03 | OPO-005, RIS-009 | US-007 | juridico-compliance, gestao-pmo | — |
| RF-009 | confirmado | doc:escopo.md#visao | SIS-01, SIS-02, SIS-03 | OPO-007, RIS-010 | US-035 | negocio | — |
| RF-010 | confirmado | doc:ata_comite_contratos_2026-08-19.md#1, entrevista:negocio Q-002 | SIS-01, SIS-02 | OPO-003, RIS-011 | US-037 | negocio, financeiro | — |
| RF-011 | hipótese | doc:escopo.md#relacao | SIS-01, SIS-02 | RIS-012 | US-022 | gestao-pmo | — |
| RF-012 | hipótese | doc:escopo.md#prazo | SIS-03 | RIS-009 | US-041 | gestao-pmo | — |
| RNF-001 | hipótese | sql:manutclin_dump.sql:paciente_nome | SIS-02 | RIS-002 | US-038 | juridico-compliance, security | — |
| RNF-002 | confirmado | sql:manutclin_dump.sql:prestador_portal, doc:regras_da_planilha.md#quem-mexe, entrevista:negocio Q-002 | SIS-01, SIS-02, SIS-03 | GAR-005, RIS-003 | US-019 | security, juridico-compliance | — |
| RNF-003 | hipótese | doc:indicadores_manutencao_2025.md#tempos | SIS-02 | GAR-002 | US-022 | gestao-pmo | — |
| RNF-004 | hipótese | doc:politica_compras_POL-SUP-004_rev3.md#2, sql:manutclin_dump.sql:prestador_portal | SIS-01, SIS-02 | RIS-002, RIS-003 | US-001 | security | — |
| RNF-005 | hipótese | doc:indicadores_manutencao_2025.md#inventario, doc:indicadores_manutencao_2025.md#tempos | SIS-01, SIS-02 | APO-004 | US-042 | gestao-pmo | — |
| RNF-006 | hipótese | doc:politica_compras_POL-SUP-004_rev3.md#1.3 | SIS-01 | APO-007, RIS-013 | US-020 | financeiro, suprimentos | — |
| RN-020 | hipótese | doc:politica_compras_POL-SUP-004_rev3.md#2.2, doc:politica_compras_POL-SUP-004_rev3.md#4.4 | SIS-01 | DIV-002 | US-015 | financeiro | — |
| RN-021 | confirmado | doc:politica_compras_POL-SUP-004_rev3.md#4.1 | SIS-01 | DIV-010 | US-005 | juridico-compliance, financeiro | — |
| RN-022 | hipótese | doc:regras_da_planilha.md#colunas, doc:politica_compras_POL-SUP-004_rev3.md#6.2 | SIS-03 | DIV-012 | US-029 | engenharia-clinica | — |
| RN-023 | confirmado | entrevista:engenharia-clinica Q-011, doc:politica_compras_POL-SUP-004_rev3.md#6.2 | SIS-02 | DIV-012 | US-029 | engenharia-clinica | — |
| RN-024 | hipótese | entrevista:engenharia-clinica Q-013 | SIS-02 | DIV-016, RIS-001 | — | engenharia-clinica | — |
| RN-025 | hipótese | doc:politica_compras_POL-SUP-004_rev3.md#3.1, sql:erp_suprimax_dump.sql:OC-2026-00452 | SIS-01 | DIV-010, RIS-005 | US-018 | suprimentos | — |
| RN-026 | hipótese | doc:politica_compras_POL-SUP-004_rev3.md#5.3, sql:manutclin_dump.sql:88190 | SIS-01, SIS-02 | RIS-006 | US-033 | engenharia-clinica, financeiro | — |
| RN-027 | hipótese | doc:ata_comite_contratos_2026-08-19.md#1 | SIS-01 | RIS-011 | US-037 | financeiro | — |
| RF-013 | hipótese | sql:manutclin_dump.sql:plano_preventivo, doc:controle_contratos.csv#preventiva | SIS-02 | DIV-013, RIS-015 | US-030 | engenharia-clinica | — |
| RF-014 | hipótese | doc:politica_compras_POL-SUP-004_rev3.md#4.2, doc:escopo.md#prazo | SIS-01, SIS-03 | RIS-009 | US-010 | juridico-compliance, gestao-pmo | — |
| RF-015 | confirmado | doc:escopo.md#cobertura, doc:fluxo_contratacao_manutencao.md#contratacao | SIS-03 | DIV-006, DIV-009 | US-008 | juridico-compliance | — |
| RF-016 | confirmado | entrevista:negocio Q-002, doc:politica_compras_POL-SUP-004_rev3.md#2 | SIS-01 | DIV-001, DIV-002 | US-014, US-015 | financeiro, suprimentos | — |
| RF-017 | confirmado | doc:escopo.md#cobertura, sql:erp_suprimax_dump.sql:requisicao | SIS-01 | DIV-003, RIS-011 | US-013 | suprimentos | — |
| RF-018 | confirmado | doc:escopo.md#cobertura, doc:regras_da_planilha.md#status | SIS-01, SIS-03 | DIV-008, DIV-014 | US-009 | juridico-compliance | — |
| RF-019 | hipótese | doc:indicadores_manutencao_2025.md#tempos, doc:ata_comite_contratos_2026-08-19.md#4 | SIS-01, SIS-02 | RIS-016 | US-036 | negocio | — |
| RF-020 | confirmado | doc:portaria_DG-017-2025_compras_emergenciais.md#3, doc:portaria_DG-017-2025_compras_emergenciais.md#5 | SIS-01 | APO-003, RIS-007 | US-021 | suprimentos | — |
| RNF-007 | hipótese | sql:manutclin_dump.sql:prestador_portal, doc:regras_da_planilha.md#quem-mexe | SIS-01, SIS-02, SIS-03 | GAR-005, RIS-003 | US-039 | security | — |
| RNF-008 | hipótese | hipótese:ti | — | RIS-016 | US-042 | ti | — |
| RNF-009 | hipótese | hipótese:ti | — | OPO-007 | US-042 | ti | — |
| RNF-010 | hipótese | hipótese:ti | — | RIS-016 | US-042 | ti | — |
| RNF-011 | hipótese | hipótese:ti | SIS-01, SIS-02 | GAR-002 | US-022 | ti | — |

## 2. História → requisito → pendência

| História | Título | Requisitos | Pai | Bloqueada por | Status |
|---|---|---|---|---|---|
| US-001 | Controlar acesso por papel e unidade | RNF-004 | FT-014 | — | proposto |
| US-002 | Cadastrar contrato com vigência, valor e SLA | RF-001, RN-009, RN-011 | FT-001 | — | proposto |
| US-003 | Validar índice e moeda do contrato | RN-007, RN-019 | FT-001 | — | proposto |
| US-004 | Calcular status da vigência | RF-001 | FT-001 | — | proposto |
| US-005 | Impedir pagamento de contrato não registrado | RN-021 | FT-001 | — | proposto |
| US-006 | Bloquear medição de contrato vencido, com exceção | RN-008 | FT-001 | Q-007 | proposto |
| US-007 | Receber alerta de renovação | RF-008, RN-006 | FT-002 | Q-008 | proposto |
| US-008 | Acompanhar a renovação | RF-015 | FT-002 | — | proposto |
| US-009 | Registrar aditivo com histórico | RF-018 | FT-002 | — | proposto |
| US-010 | Importar renovações do legado | RF-014 | FT-002 | — | proposto |
| US-011 | Exigir parecer acima de R$ 30.000,00 | RN-005 | FT-003 | — | proposto |
| US-012 | Ver fila de pareceres | RF-003 | FT-003 | — | proposto |
| US-013 | Registrar requisição com cotações | RF-017, RN-003 | FT-004 | — | proposto |
| US-014 | Aprovar OC pela alçada | RF-016, RN-001 | FT-005 | — | proposto |
| US-015 | Aprovar contrato pelo valor global | RF-016, RN-002, RN-020 | FT-005 | — | proposto |
| US-016 | Impedir autoaprovação | RN-014 | FT-005 | — | proposto |
| US-017 | Somar ordens da mesma requisição | RN-016 | FT-005 | — | proposto |
| US-018 | Alertar compras recorrentes sem contrato | RN-025 | FT-005 | — | proposto |
| US-019 | Registrar trilha das aprovações | RNF-002 | FT-005 | — | proposto |
| US-020 | Manter limites como parâmetros com vigência | RNF-006 | FT-005 | — | proposto |
| US-021 | Registrar compra emergencial | RF-020, RN-018 | FT-006 | — | proposto |
| US-022 | Conectar aos sistemas mantidos com monitoramento | RF-011, RNF-003, RNF-011 | FT-015 | Q-001, Q-018 | proposto |
| US-023 | Receber inventário e calibração | RF-007 | FT-007 | Q-018 | proposto |
| US-024 | Criar requisição a partir da OS | RF-004 | FT-007 | Q-018 | proposto |
| US-025 | Conferir medição contra OS | RF-005 | FT-008 | — | proposto |
| US-026 | Atestar medição no sistema | RF-005, RN-013 | FT-008 | — | proposto |
| US-027 | Listar OS corretivas sem teste ou liberação | RN-012 | FT-009 | — | proposto |
| US-028 | Alertar calibração vencida | RN-015 | FT-009 | — | proposto |
| US-029 | Classificar equipamentos em quatro níveis | RN-010, RN-023, RN-022 | FT-009 | — | proposto |
| US-030 | Conciliar preventiva do contrato e do plano | RF-013 | FT-009 | — | proposto |
| US-031 | Apurar tempos de SLA por OS | RN-009 | FT-010 | — | proposto |
| US-032 | Calcular glosa por evento | RN-017 | FT-010 | — | proposto |
| US-033 | Aceitar ou justificar glosa no ateste e pausar relógio | RN-026 | FT-010 | Q-010 | proposto |
| US-034 | Gerar título com vencimento correto | RF-006, RN-004 | FT-011 | Q-004 | proposto |
| US-035 | Ver visão consolidada da rede | RF-009 | FT-012 | — | proposto |
| US-036 | Acompanhar indicadores do processo | RF-019 | FT-012 | Q-002 | proposto |
| US-037 | Consultar custo por equipamento | RF-010, RN-027 | FT-013 | Q-005 | proposto |
| US-038 | Excluir dados de paciente da integração | RNF-001 | FT-014 | Q-016, Q-017 | proposto |
| US-039 | Registrar trilha de contrato, medição e título | RNF-007 | FT-014 | — | proposto |
| US-040 | Sanear e migrar contratos | RF-002 | FT-016 | — | proposto |
| US-041 | Conduzir convivência e treinamento | RF-012 | FT-016 | — | proposto |
| US-042 | Garantir capacidade, disponibilidade e recuperação | RNF-005, RNF-008, RNF-009, RNF-010 | FT-017 | Q-018 | proposto |

## 3. Fonte → requisitos

| Fonte | Requisitos |
|---|---|
| ata_comite_contratos_2026-08-19.md | RF-004, RF-005, RF-006, RF-010, RF-019, RN-008, RN-027 |
| controle_contratos.csv | RF-013, RN-007, RN-011 |
| erp_suprimax_dump.sql | RF-002, RF-017, RN-025 |
| escopo.md | RF-009, RF-011, RF-012, RF-014, RF-015, RF-017, RF-018 |
| fluxo_contratacao_manutencao.md | RF-004, RF-015, RN-012 |
| indicadores_manutencao_2025.md | RF-003, RF-019, RNF-003, RNF-005 |
| manutclin_dump.sql | RF-002, RF-007, RF-013, RN-009, RN-011, RN-026, RNF-001, RNF-002, RNF-004, RNF-007 |
| politica_compras_POL-SUP-004_rev3.md | RF-006, RF-008, RF-014, RF-016, RN-001, RN-002, RN-003, RN-004, RN-005, RN-006, RN-007, RN-008, RN-010, RN-013, RN-014, RN-015, RN-016, RN-017, RN-019, RN-020, RN-021, RN-022, RN-023, RN-025, RN-026, RNF-004, RNF-006 |
| portaria_DG-017-2025_compras_emergenciais.md | RF-020, RN-004, RN-018 |
| regras_da_planilha.md | RF-001, RF-018, RN-007, RN-009, RN-019, RN-022, RNF-002, RNF-007 |

**Fontes sem nenhum requisito:** fontes/geral/manual_processo_compras_v2_2019.md

## 4. Divergência → tratamento

| Divergência | Título | Sistemas | Status | Tratamento |
|---|---|---|---|---|
| DIV-001 | Alçada de OC: ERP 80 mil x política 50 mil | SIS-01, geral | tratado | Q-003, RF-016, RN-001, geral |
| DIV-002 | Alçada de contrato: ERP usa valor mensal, política usa valor global | SIS-01, geral | tratado | Q-003, RF-016, RN-002, RN-020, geral |
| DIV-003 | Cotações: ERP exige 3 a partir de 25 mil e só em REGULAR; política, 2 acima de 5 mil e 3 acima de 15 mil | SIS-01, geral | tratado | Q-003, RF-017, RN-003, geral |
| DIV-004 | Prazo de pagamento: ERP limita a 15-30 dias; política, padrão 45 e mínimo 30 | SIS-01, geral | tratado | GAR-004, Q-003, Q-004, RN-004, geral |
| DIV-005 | Parecer jurídico: fluxo acima de 100 mil x política acima de 30 mil | geral | tratado | GAR-001, Q-006, RN-005, geral |
| DIV-006 | Início da renovação: 120, 90 ou 60 dias, com responsáveis diferentes | SIS-03, geral | aberto | Q-008, RF-015, RN-006, geral |
| DIV-007 | Índice de CT-2025-0064: IGP-M no ERP x IPCA na planilha | SIS-01, SIS-03, geral | tratado | RN-007, geral |
| DIV-008 | CT-2023-0088: fim 31/12/2026 e ATIVO no ERP x fim 30/06/2026 e Vencido na planilha | SIS-01, SIS-03 | aberto | Q-007, RF-001, RF-018 |
| DIV-009 | CT-2022-0055: fim 31/08/2025, ATIVO no ERP e Em renovação na planilha | SIS-01, SIS-03, geral | aberto | Q-007, RF-015, RIS-004, RN-008, geral |
| DIV-010 | CT-2026-0021 existe na planilha e no ManutClin, mas não no ERP | SIS-01, SIS-02, SIS-03, geral | aberto | Q-007, RN-008, RN-021, RN-025, geral |
| DIV-011 | SLA de atendimento de CT-2024-0117: 4 h na planilha x 8 h no ManutClin | SIS-02, SIS-03 | tratado | Q-009, RN-009 |
| DIV-012 | Criticidade em três escalas sem equivalência | SIS-02, SIS-03, geral | aberto | Q-011, RN-010, RN-022, RN-023, geral |
| DIV-013 | Preventiva de ventiladores na Central: 365 dias no plano x Semestral no contrato | SIS-02, SIS-03 | tratado | Q-012, RF-013, RN-011 |
| DIV-014 | Valor de CT-2024-0117: R$ 132.480,00 no ERP x R$ 126.000,00 na planilha (ano) | SIS-01, SIS-03 | aberto | RF-001, RF-018 |
| DIV-015 | Mesmo CNPJ com dois nomes: MTS (ERP) x BioVolt (ManutClin e planilha) | SIS-01, SIS-02, SIS-03 | aberto | RF-002 |
| DIV-016 | Regra de liberação do fluxo não é exigida pelo ManutClin | SIS-02, geral | tratado | Q-013, RN-012, RN-024, geral |
| DIV-017 | Política exige ateste para pagar; ERP permite pagar medição sem ateste | SIS-01, geral | tratado | RN-013, geral |
| DIV-018 | Quem solicita não pode aprovar; ERP não impede | SIS-01, geral | tratado | RN-014, geral |

## 5. Risco → requisitos → histórias

| Risco | Título | Severidade | Requisitos | Histórias |
|---|---|---|---|---|
| RIS-001 | Equipamento em uso com calibração vencida, sem bloqueio | critica | RF-007, RN-015, RN-024 | US-023, US-028 |
| RIS-002 | Dados de paciente em OS, com leitura pelo portal de prestadores | critica | RNF-001, RNF-004 | US-001, US-038 |
| RIS-003 | Prestador pode editar a hora de atendimento que mede seu próprio SLA | alta | RNF-002, RNF-004, RNF-007 | US-001, US-019, US-039 |
| RIS-004 | Serviço e pagamento com contrato vencido | critica | RN-008 | US-006 |
| RIS-005 | Indício de fracionamento em OCs | alta | RN-016, RN-025 | US-017, US-018 |
| RIS-006 | Glosa prevista e não aplicada | alta | RN-017, RN-026 | US-032, US-033 |
| RIS-007 | Controles do ERP podem ser contornados | alta | RF-020, RN-016, RN-018 | US-017, US-021 |
| RIS-008 | Dependência de uma única pessoa para a planilha | alta | RF-001 | US-002, US-004 |
| RIS-009 | Seis contratos acabam antes da entrada em operação | alta | RF-008, RF-012, RF-014 | US-007, US-010, US-041 |
| RIS-010 | Soma de contratos pode misturar reais e dólares | media | RF-009, RN-019 | US-003, US-035 |
| RIS-011 | Custo por equipamento não pode ser calculado hoje | alta | RF-010, RF-017, RN-027 | US-013, US-037 |
| RIS-012 | Conclusões limitadas pelas fontes disponíveis | media | RF-011 | US-022 |
| RIS-013 | Manual de 2019 parcialmente sem revogação | baixa | RNF-006 | US-020 |
| RIS-014 | Reajuste pode estar atrasado ou sem controle | media | RN-007 | US-003 |
| RIS-015 | Lacunas possíveis no plano preventivo | media | RF-013, RN-011 | US-002, US-030 |
| RIS-016 | Decisões estruturais sem dono | alta | RF-019, RNF-008, RNF-010 | US-036, US-042 |

## 6. Pergunta → resposta → itens

| Pergunta | Texto | Responsável | Status | Resposta | Itens |
|---|---|---|---|---|---|
| Q-001 | Qual é o destino de cada sistema na fase 1: o ERP e o ManutClin são substituídos ou integrados? | negocio | aberta | Diretora Geral: não sei. | RF-011, RIS-012, RIS-016, US-022 |
| Q-002 | Se nem tudo couber até 30/06/2027, que indicador define o sucesso da fase 1 e quais etapas formam o mínimo para mudá-lo? | negocio | aberta | Diretora Geral: mínimo em ordem: 1) cadastro único de contratos com vigência, valor, SLA e alertas de renovação; 2) aprovações conforme a Política, com trilha de auditoria; 3) ligação entre OS, requisição e medição, com ateste no sistema; 4) cálculo de glosa por SLA; 5) custo por equipamento: desejável, pode ficar para a segunda fase. Número e meta de sucesso: não sei. | RF-008, RIS-009, RIS-016, US-036 |
| Q-003 | A POL-SUP-004 rev. 3 vale integralmente no novo sistema, inclusive onde o ERP difere? | financeiro | respondida | Diretor Financeiro e Gerente de Suprimentos: vale a Política nos pontos citados: alçada de OC R$ 50 mil e R$ 250 mil; alçada de contrato pelo valor global da vigência em qualquer contrato assinado desde 01/01/2025; três cotações acima de R$ 15 mil e duas de R$ 5 mil a R$ 15 mil; prazo padrão de 45 dias, mínimo de 30, salvo emergencial. A configuração do ERP é antiga e ninguém a revisou após a rev. 3. Outra exceção aprovada: não sei. | DIV-001, DIV-002, DIV-003, DIV-004, RIS-005, RN-001, RN-002, RN-003, RN-004, RN-016 |
| Q-004 | O pagamento termina no novo sistema ou segue para outro sistema financeiro, e por que os títulos são alterados? | financeiro | aberta | Diretor Financeiro: não sei. | DIV-004, GAR-004, RF-006, RIS-012, RIS-016, US-034 |
| Q-005 | Qual regra calcula o custo por equipamento, em especial o rateio do contrato? | financeiro | aberta | Diretor Financeiro: não sei. | APO-004, OPO-003, RF-010, RIS-011, US-037 |
| Q-006 | Parecer jurídico: vale acima de R$ 30.000,00 ou de R$ 100.000,00? | juridico-compliance | respondida | Jurídico: vale a Política: acima de R$ 30 mil de valor global. | DIV-005, GAR-001, RN-005 |
| Q-007 | O sistema deve bloquear pagamento de contrato vencido ou não registrado, e quem autoriza exceção? | juridico-compliance | aberta | Jurídico e Diretor Financeiro: não sei. | DIV-008, DIV-009, DIV-010, RIS-004, RIS-016, RN-008, US-006 |
| Q-008 | Quem inicia a renovação e com quantos dias de antecedência? | suprimentos | aberta | Gerente de Suprimentos: não sei. | DIV-006, RIS-009, RN-006, US-007 |
| Q-009 | Qual SLA de atendimento consta em CT-2024-0117: 4 ou 8 horas? | juridico-compliance | respondida | Jurídico: 4 horas, como no contrato assinado. | DIV-011, RN-009 |
| Q-010 | Como apurar SLA e aplicar glosa? | engenharia-clinica | aberta | Gerente de Engenharia Clínica: não sei. | GAR-003, RIS-003, RIS-006, RN-017, US-033 |
| Q-011 | Qual é a escala oficial de criticidade e a equivalência com A, B, C e Crítico? | engenharia-clinica | respondida | Gerente de Engenharia Clínica: enquanto o sistema novo não chega, usamos no ManutClin: A para nível 1, B para níveis 2 e 3, C para nível 4. | DIV-012, RN-010 |
| Q-012 | Qual é a periodicidade correta da preventiva de ventiladores da Central: 365 ou cerca de 180 dias? | engenharia-clinica | respondida | Gerente de Engenharia Clínica: semestral, como no contrato assinado. | DIV-013, RIS-015, RN-011 |
| Q-013 | O novo sistema deve alertar ou bloquear em caso de calibração vencida ou falta de liberação? | engenharia-clinica | aberta | Gerente de Engenharia Clínica e Diretor Técnico: na liberação após reparo vale o fluxo: teste e assinatura são obrigatórios. Se o tratamento deve ser só alerta e relatório ou também bloqueio operacional no ManutClin: não sei. | DIV-016, RIS-001, RN-012, RN-015 |
| Q-014 | Dados de paciente e evento adverso devem ficar fora do novo sistema? | juridico-compliance | cancelada | Jurídico e Diretor Técnico: identificação de paciente nas OS: não sei, encaminhar ao encarregado de dados (DPO). Evento adverso e notificação: não sei, encaminhar à Gerência de Qualidade e Segurança do Paciente. | RIS-002, RNF-001 |
| Q-015 | Quais meios de integração e migração existem para ERP e ManutClin, e quem os mantém? | gestao-pmo | cancelada | Área de TI: não sei, encaminhar ao coordenador de TI. | GAR-002, RF-004, RF-011, RF-012, RIS-012, RNF-003 |
| Q-016 | O novo sistema deve excluir totalmente a identificação de paciente das OS, inclusive na migração? (encaminhada pelo Jurídico) | dpo | aberta | — | RIS-002, RNF-001, US-038 |
| Q-017 | O novo sistema deve receber das OS só o indicador de evento adverso, mantendo tratamento e notificação fora do projeto? (encaminhada pelo Jurídico e pelo Diretor Técnico) | qualidade-seguranca-paciente | aberta | — | RIS-001, RIS-002, RN-024, US-038 |
| Q-018 | Quais meios podem ser usados para ler e gravar no ERP e no ManutClin (API, tabela intermediária, arquivo) e quem responde por eles? (encaminhada pela área de TI) | ti | aberta | — | GAR-002, RF-004, RF-011, RIS-012, RIS-016, RNF-003, US-022, US-023, US-024, US-042 |

## 7. Pendência → histórias bloqueadas

| Pergunta | Texto | Responsável | Histórias |
|---|---|---|---|
| Q-001 | Qual é o destino de cada sistema na fase 1: o ERP e o ManutClin são substituídos ou integrados? | negocio | US-022 |
| Q-002 | Se nem tudo couber até 30/06/2027, que indicador define o sucesso da fase 1 e quais etapas formam o mínimo para mudá-lo? | negocio | US-036 |
| Q-004 | O pagamento termina no novo sistema ou segue para outro sistema financeiro, e por que os títulos são alterados? | financeiro | US-034 |
| Q-005 | Qual regra calcula o custo por equipamento, em especial o rateio do contrato? | financeiro | US-037 |
| Q-007 | O sistema deve bloquear pagamento de contrato vencido ou não registrado, e quem autoriza exceção? | juridico-compliance | US-006 |
| Q-008 | Quem inicia a renovação e com quantos dias de antecedência? | suprimentos | US-007 |
| Q-010 | Como apurar SLA e aplicar glosa? | engenharia-clinica | US-033 |
| Q-013 | O novo sistema deve alertar ou bloquear em caso de calibração vencida ou falta de liberação? | engenharia-clinica | — |
| Q-016 | O novo sistema deve excluir totalmente a identificação de paciente das OS, inclusive na migração? (encaminhada pelo Jurídico) | dpo | US-038 |
| Q-017 | O novo sistema deve receber das OS só o indicador de evento adverso, mantendo tratamento e notificação fora do projeto? (encaminhada pelo Jurídico e pelo Diretor Técnico) | qualidade-seguranca-paciente | US-038 |
| Q-018 | Quais meios podem ser usados para ler e gravar no ERP e no ManutClin (API, tabela intermediária, arquivo) e quem responde por eles? (encaminhada pela área de TI) | ti | US-022, US-023, US-024, US-042 |

## 8. Mudança → impacto

| CR | Título | Classe | Status | Itens afetados |
|---|---|---|---|---|

**Sem fonte (órfãos):** nenhum

**Confirmados/validados sem história direta:** nenhum
