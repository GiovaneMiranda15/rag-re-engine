# Achados do diagnóstico

## Divergências

| ID | Achado | Sistemas | Severidade | Fontes | Status | Gera |
|---|---|---|---|---|---|---|
| DIV-001 | Validade do ASO: 30, 60 ou 90 dias | geral, SIS-03, SIS-01 | critica | doc:geral/politica-RH-012-admissao-integracao.md#1, doc:SIS-03/LEIA-ME.md#0, sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato, doc:SIS-03/controle_admissoes_2026-estrutura.md#1 | tratado | RN-001, RF-015, RF-024, Q-004, Q-024, Q-025 |
| DIV-002 | Experiência: 30+60 ou 45+45 | geral, SIS-03, SIS-01 | alta | doc:geral/politica-RH-012-admissao-integracao.md#0, doc:geral/manual-admissao-lojas-v3.2-2019.md#1, doc:SIS-03/LEIA-ME.md#0, sql:SIS-01/folhacerta_dump.sql:contrato, sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato | tratado | RN-002, RF-024, Q-005, Q-027, Q-028 |
| DIV-003 | CRF: certidão, protocolo ou só número | geral, SIS-03, SIS-01 | critica | doc:geral/politica-RH-012-admissao-integracao.md#1, doc:SIS-03/LEIA-ME.md#0, doc:geral/manual-admissao-lojas-v3.2-2019.md#1, sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato, sql:SIS-01/folhacerta_dump.sql:contrato | tratado | RN-003, RF-016, RF-024, Q-006, Q-029, Q-030 |
| DIV-004 | Prazo da integração: 5, 15 ou 30 dias | geral, SIS-04 | alta | doc:geral/politica-RH-012-admissao-integracao.md#1, doc:geral/manual-admissao-lojas-v3.2-2019.md#1, doc:SIS-04/lms-estrutura.md#0 | tratado | RN-004, RF-022, RF-024, Q-015, Q-045 |
| DIV-005 | Aprovação da oferta sem o BP de RH | geral, SIS-02 | alta | doc:geral/politica-RH-012-admissao-integracao.md#0, doc:geral/manual-admissao-lojas-v3.2-2019.md#0, doc:geral/fluxo-admissao-atual.md#0, sql:SIS-02/recrutamais_dump.sql:oferta | tratado | RN-005, RF-012, Q-008, Q-034 |
| DIV-006 | Eliminação de candidatos: 6 ou 24 meses | geral, SIS-02 | critica | doc:geral/politica-RH-012-admissao-integracao.md#2, sql:SIS-02/recrutamais_dump.sql:sp_expurgo_candidatos, sql:SIS-02/recrutamais_dump.sql:candidato_bkp_2022 | tratado | RN-006, RF-017, RNF-010, Q-013, Q-043 |
| DIV-007 | Dados de saúde fora do SESMT | geral, SIS-01, SIS-03 | critica | doc:geral/politica-RH-012-admissao-integracao.md#1, sql:SIS-01/folhacerta_dump.sql:exame_admissional, sql:SIS-01/folhacerta_dump.sql:GRANT rh_loja, doc:SIS-03/controle_admissoes_2026-estrutura.md#1 | aberto | RN-007, RN-013, Q-012, Q-040 |
| DIV-008 | Aprendiz: política admite de 14 a 24 anos, FolhaCerta não | geral, SIS-01, SIS-03 | alta | doc:geral/politica-RH-012-admissao-integracao.md#0, sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato, sql:SIS-01/folhacerta_dump.sql:chk_tipo_contrato, doc:geral/fluxo-admissao-atual.md#0, doc:SIS-03/LEIA-ME.md#0 | aberto | RN-008, RF-021, Q-011, Q-038, Q-039 |
| DIV-009 | Três números para admissões do mesmo mês | SIS-01, SIS-02, SIS-03 | alta | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0, sql:SIS-02/recrutamais_dump.sql:trg_oferta_aceita, sql:SIS-01/folhacerta_dump.sql:contrato.status, doc:SIS-03/LEIA-ME.md#1 | tratado | RN-015, RF-010, Q-003, Q-022 |
| DIV-010 | Tabela salarial do Recruta+ defasada | SIS-01, SIS-02, SIS-03 | media | sql:SIS-02/recrutamais_dump.sql:tabela_salarial, sql:SIS-01/folhacerta_dump.sql:cargo_piso, doc:SIS-03/controle_admissoes_2026-estrutura.md#1 | tratado | RN-009, RF-013, RF-024, Q-008, Q-035 |
| DIV-011 | Prazo de documentos: 3 ou 5 dias úteis | geral, SIS-03 | baixa | doc:geral/manual-admissao-lojas-v3.2-2019.md#0, doc:geral/comunicado-dp-07-2024.md#0, doc:geral/politica-RH-012-admissao-integracao.md#0, doc:SIS-03/LEIA-ME.md#0 | tratado | RN-010 |
| DIV-012 | Sem chave comum e com identificadores diferentes | SIS-01, SIS-02, SIS-03, SIS-04 | alta | sql:SIS-01/folhacerta_dump.sql:colaborador, sql:SIS-02/recrutamais_dump.sql:candidato, doc:SIS-03/controle_admissoes_2026-estrutura.md#0, doc:SIS-04/lms-estrutura.md#0 | aberto | RF-002, RF-018, Q-014 |
| DIV-013 | Momento do chamado de acesso ao PDV | geral, SIS-03 | media | doc:geral/manual-admissao-lojas-v3.2-2019.md#1, doc:geral/fluxo-admissao-atual.md#0, doc:SIS-03/LEIA-ME.md#1 | aberto | RF-007, Q-014 |
| DIV-014 | Regra de não iniciar sem ASO e prática | geral, SIS-01, SIS-03 | critica | doc:geral/politica-RH-012-admissao-integracao.md#1, sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato, sql:SIS-01/folhacerta_dump.sql:evento_esocial, doc:SIS-03/controle_admissoes_2026-estrutura.md#1, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1 | aberto | RN-011, RNF-004, Q-007, Q-009 |
| DIV-015 | Critérios diferentes para poder começar | geral, SIS-03 | alta | doc:SIS-03/LEIA-ME.md#1, doc:geral/politica-RH-012-admissao-integracao.md#1, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0, doc:geral/manual-admissao-lojas-v3.2-2019.md#0 | aberto | RN-011, RN-018, RF-001, Q-007, Q-031 |
| DIV-016 | Abrangência: 212 ou 184 lojas | geral | media | doc:escopo.md, doc:geral/politica-RH-012-admissao-integracao.md#0, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0 | tratado | RN-016, Q-001, Q-016 |
| DIV-017 | Quem aprova mudança na RH-012 | geral | baixa | entrevista:gestao-pmo Q-002, entrevista:juridico-compliance Q-005, doc:geral/politica-RH-012-admissao-integracao.md#0 | aberto | Q-048 |
| DIV-018 | DP valida ASO, mas saúde é exclusiva do SESMT | geral, SIS-01 | alta | entrevista:departamento-pessoal Q-003, entrevista:juridico-compliance Q-012, doc:geral/politica-RH-012-admissao-integracao.md#1, sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato | aberto | RN-013, Q-040 |
| DIV-019 | Comunicado de 45+45 contra a RH-012 | geral, SIS-01 | alta | doc:geral/M-01-ata-comite-2026-10-28.md#0, doc:geral/politica-RH-012-admissao-integracao.md#0, entrevista:juridico-compliance Q-005 | aberto | RN-002, CR-001, Q-050 |

## Gargalos

| ID | Achado | Sistemas | Severidade | Fontes | Status | Gera |
|---|---|---|---|---|---|---|
| GAR-001 | Redigitação na FolhaCerta | SIS-01, SIS-03 | alta | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0 | aberto | RF-002, RF-025, Q-037 |
| GAR-002 | Devolução de pastas | geral | alta | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0, doc:geral/fluxo-admissao-atual.md#0 | aberto | RF-003, RF-025, Q-010, Q-037 |
| GAR-003 | Agendamento de exame por e-mail | geral, SIS-03 | alta | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1, doc:SIS-03/controle_admissoes_2026-estrutura.md#1 | aberto | RF-005 |
| GAR-004 | Espera pelo login do PDV | geral | alta | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1 | aberto | RF-007 |
| GAR-005 | Matrícula manual no LMS | SIS-04 | media | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1, doc:SIS-04/lms-estrutura.md#0 | aberto | RF-008 |
| GAR-006 | Corrida do S-2190 na véspera | SIS-01 | alta | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0, sql:SIS-01/folhacerta_dump.sql:fn_gera_esocial, sql:SIS-01/folhacerta_dump.sql:contrato.status | aberto | RF-006, RN-017, Q-009 |
| GAR-007 | Planilha paralela como painel | SIS-03 | media | doc:SIS-03/LEIA-ME.md#0 | aberto | RF-001 |
| GAR-008 | Lote quinzenal do aprendiz | geral, SIS-03 | media | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1, doc:SIS-03/LEIA-ME.md#0 | aberto | RF-021, Q-011, Q-038 |
| GAR-009 | Pico de novembro e dezembro | SIS-01 | alta | entrevista:departamento-pessoal Q-010, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0 | aberto | RNF-005, RF-025 |

## Riscos

| ID | Achado | Sistemas | Severidade | Fontes | Status | Gera |
|---|---|---|---|---|---|---|
| RIS-001 | Planilha aberta com dados pessoais | SIS-03 | critica | doc:SIS-03/LEIA-ME.md#0, doc:SIS-03/controle_admissoes_2026-estrutura.md#0 | aberto | RNF-001, Q-013, Q-044 |
| RIS-002 | Dados sensíveis de candidatos acessíveis a gerentes | SIS-02 | critica | sql:SIS-02/recrutamais_dump.sql:candidato, sql:SIS-02/recrutamais_dump.sql:candidato_bkp_2022, sql:SIS-02/recrutamais_dump.sql:GRANT gerente_loja | aberto | RNF-002, RN-012, RN-014, Q-013, Q-044 |
| RIS-003 | Risco de discriminação na admissão | SIS-02, SIS-03 | critica | sql:SIS-02/recrutamais_dump.sql:candidato, doc:SIS-03/controle_admissoes_2026-estrutura.md#1 | aberto | RN-012, Q-013, Q-042 |
| RIS-004 | Login do gerente usado por colaborador novo | geral | critica | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1 | aberto | RF-007, RNF-003, Q-014 |
| RIS-005 | Farmacêutico em atividade sem certidão | SIS-01, SIS-03 | critica | doc:SIS-03/LEIA-ME.md#0, sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato, doc:SIS-03/controle_admissoes_2026-estrutura.md#1 | aberto | RN-003, RF-016, Q-006, Q-030 |
| RIS-006 | Início sem ASO válido sob pressão da loja | geral, SIS-03 | critica | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1, doc:SIS-03/controle_admissoes_2026-estrutura.md#1 | aberto | RN-011, RF-015, Q-007, Q-033 |
| RIS-007 | Fim da experiência sem controle | SIS-01, SIS-03 | alta | sql:SIS-01/folhacerta_dump.sql:contrato, doc:SIS-03/LEIA-ME.md#1, doc:geral/fluxo-admissao-atual.md#0 | aberto | RF-009, Q-005, Q-028 |
| RIS-008 | Dependência de pessoa no SESMT | geral | alta | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1 | aberto | RF-005 |
| RIS-009 | Aprendiz fora dos controles | geral, SIS-03, SIS-04 | alta | doc:geral/fluxo-admissao-atual.md#0, doc:SIS-03/LEIA-ME.md#0, doc:SIS-04/lms-estrutura.md#0, doc:geral/politica-RH-012-admissao-integracao.md#1 | aberto | RN-008, RF-021, Q-011, Q-038, Q-039 |
| RIS-010 | Adiamento pode não recalcular eventos | SIS-01 | media | sql:SIS-01/folhacerta_dump.sql:trg_gera_esocial | aberto | Q-009 |
| RIS-011 | Cobertura de eventos eSocial a verificar | SIS-01 | media | sql:SIS-01/folhacerta_dump.sql:evento_esocial, sql:SIS-01/folhacerta_dump.sql:esocial_prazo | aberto | Q-009 |
| RIS-012 | CPF redigitado errado na folha | SIS-01 | alta | sql:SIS-01/folhacerta_dump.sql:colaborador, sql:SIS-02/recrutamais_dump.sql:candidato, doc:SIS-03/controle_admissoes_2026-estrutura.md#1 | aberto | RF-002 |
| RIS-013 | Documentos pessoais circulando por e-mail | geral | alta | doc:geral/fluxo-admissao-atual.md#0 | aberto | RNF-001, Q-012 |
| RIS-014 | Lacunas de fonte para o projeto | geral | alta | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0 | aberto | Q-002, Q-014, Q-017, Q-018, Q-019, Q-020 |
| RIS-015 | Casos em curso fora da regra confirmada | SIS-01, SIS-03 | alta | entrevista:juridico-compliance Q-005, entrevista:regulatorio Q-006, sql:SIS-01/folhacerta_dump.sql:contrato | aberto | Q-027, Q-030 |
| RIS-016 | Perguntas 9 e 14 sem resposta | SIS-01, SIS-02, SIS-04, SIS-07 | critica | entrevista:departamento-pessoal Q-009, entrevista:software-architect Q-014 | aberto | RF-020, RNF-006, RNF-007, Q-009, Q-014 |
| RIS-017 | Convivência prolongada de processos | SIS-03 | media | entrevista:negocio Q-001 | aberto | RF-018, RF-023, Q-016 |
| RIS-018 | Lojas adotarem 45+45 antes de uma decisão | SIS-01, SIS-03 | alta | doc:geral/M-01-ata-comite-2026-10-28.md#0, entrevista:departamento-pessoal Q-010 | aberto | CR-001, Q-050 |
| RIS-019 | CRNM sem lugar nos cadastros atuais | SIS-01, SIS-02 | alta | doc:geral/M-02-email-juridico-2026-10-30.md#0, sql:SIS-01/folhacerta_dump.sql:colaborador, sql:SIS-02/recrutamais_dump.sql:candidato | aberto | RF-027, RF-028, RF-029, RN-021, RN-022, Q-053, Q-054, Q-055 |
| RIS-020 | Datas externas antes de o sistema existir | geral | alta | doc:geral/M-02-email-juridico-2026-10-30.md#0 | aberto | RN-019, RF-026, RN-020, Q-017, Q-051, Q-052 |

## Pontos de apoio

| ID | Achado | Sistemas | Severidade | Fontes | Status | Gera |
|---|---|---|---|---|---|---|
| APO-001 | FolhaCerta como sistema estável da folha | SIS-01 | media | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1, doc:escopo.md | aberto | — |
| APO-002 | S-2200 coerente | SIS-01, geral | baixa | sql:SIS-01/folhacerta_dump.sql:fn_gera_esocial, doc:geral/politica-RH-012-admissao-integracao.md#1 | aberto | — |
| APO-003 | Carência do plano coerente | geral, SIS-01, SIS-03 | baixa | doc:geral/politica-RH-012-admissao-integracao.md#1, doc:SIS-03/LEIA-ME.md#0, sql:SIS-01/folhacerta_dump.sql:beneficio_regra | aberto | — |
| APO-004 | EducaFarma com API e trilhas por cargo | SIS-04 | media | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1, doc:SIS-04/lms-estrutura.md#0 | aberto | — |
| APO-005 | Datas coerentes entre sistemas | SIS-01, SIS-02, SIS-03 | baixa | doc:SIS-03/controle_admissoes_2026-estrutura.md#1, sql:SIS-01/folhacerta_dump.sql:contrato, sql:SIS-02/recrutamais_dump.sql:oferta | aberto | — |
| APO-006 | Checklist de primeiro dia e fluxo mapeado | SIS-03, geral | baixa | doc:SIS-03/LEIA-ME.md#1, doc:geral/fluxo-admissao-atual.md#0 | aberto | — |
| APO-007 | Política RH-012 como referência | geral | media | doc:geral/politica-RH-012-admissao-integracao.md#0 | aberto | — |
| APO-008 | Oferta aceita e piso por vigência | SIS-01, SIS-02 | baixa | sql:SIS-02/recrutamais_dump.sql:trg_oferta_aceita, sql:SIS-01/folhacerta_dump.sql:cargo_piso | aberto | — |

## Oportunidades

| ID | Achado | Sistemas | Severidade | Fontes | Status | Gera |
|---|---|---|---|---|---|---|
| OPO-001 | Cadastro único do aceite à folha | SIS-01, SIS-02 | alta | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0 | aberto | RF-002 |
| OPO-002 | Painel Pode começar para o gerente | SIS-03 | alta | doc:escopo.md, doc:SIS-03/LEIA-ME.md#0 | aberto | RF-001 |
| OPO-003 | Coleta e pré-conferência de documentos | geral | alta | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0 | aberto | RF-003 |
| OPO-004 | Agendamento pela API da MedTrab | geral | media | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1 | aberto | RF-005 |
| OPO-005 | Matrícula automática pela API do EducaFarma | SIS-04 | media | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1 | aberto | RF-008 |
| OPO-006 | Acesso pronto no primeiro dia | geral | alta | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1, doc:geral/fluxo-admissao-atual.md#0 | aberto | RF-007 |
| OPO-007 | Funil único de admissão | SIS-01, SIS-02, SIS-03 | media | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0 | aberto | RF-010 |
| OPO-008 | Saneamento LGPD com o inventário | SIS-01, SIS-02, SIS-03 | alta | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1, doc:geral/politica-RH-012-admissao-integracao.md#2 | aberto | RNF-001, RNF-002 |
