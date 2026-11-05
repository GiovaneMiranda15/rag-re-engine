# Rastreabilidade

Projeto Admissão Única, Drogarias Caliandra S.A. Data: 04/11/2026. Baseline: sem baseline. Situação: não validado pelas áreas. Atualizado com `mudancas/` (ver `08-mudancas.md`).

Fontes: `escopo.md`; `fontes/geral/` (política RH-012 rev. 4, manual 3.2, comunicado DP 07/2024, fluxo atual, ata de 22/09/2026); SIS-01 FolhaCerta (dump); SIS-02 Recruta+ (dump); SIS-03 planilha e Leia-me; SIS-04 EducaFarma (exportações); `entrega/respostas.md`; `mudancas/` (ata de 28/10/2026 e e-mail de 30/10/2026).

Convenção: itens sem marca estão confirmados por resposta ou evidência; `[hipótese]` é proposta deste levantamento; `[conflito]` aguarda decisão. IDs seguem `.re/modelo/`.

## 1. Requisito, fonte e backlog

| Requisito | Status | Título | Fontes | Achados de origem | Histórias | Aberto em |
|---|---|---|---|---|---|---|
| RN-001 | confirmado | Validade do ASO | doc:geral/politica-RH-012-admissao-integracao.md#1; entrevista:sesmt Q-004; entrevista:operacoes Q-007; doc:geral/M-02-email-juridico-2026-10-30.md#0 | DIV-001 | US-004, US-005, US-020, US-021 | — |
| RN-002 | conflito | Duração da experiência | doc:geral/politica-RH-012-admissao-integracao.md#0; entrevista:juridico-compliance Q-005; doc:geral/M-01-ata-comite-2026-10-28.md#0 | DIV-002 | US-004, US-005, US-036 | Q-050 |
| RN-003 | confirmado | CRF de função farmacêutica | doc:geral/politica-RH-012-admissao-integracao.md#1; entrevista:regulatorio Q-006; entrevista:operacoes Q-007; doc:geral/M-01-ata-comite-2026-10-28.md#0 | DIV-003, RIS-005 | US-004, US-005, US-031 | Q-029 |
| RN-004 | confirmado | Prazo da integração | doc:geral/politica-RH-012-admissao-integracao.md#1; entrevista:regulatorio Q-015 | DIV-004 | US-004, US-008, US-033, US-034 | — |
| RN-005 | confirmado | Alçada da oferta | doc:geral/politica-RH-012-admissao-integracao.md#0; entrevista:juridico-compliance Q-008; entrevista:departamento-pessoal Q-008 | DIV-005 | US-013, US-014 | — |
| RN-006 | confirmado | Eliminação de dados de candidatos | doc:geral/politica-RH-012-admissao-integracao.md#2; entrevista:juridico-compliance Q-013 | DIV-006 | US-003, US-043 | Q-049 |
| RN-007 | confirmado | CID e dados de saúde | doc:geral/politica-RH-012-admissao-integracao.md#1; entrevista:juridico-compliance Q-012; entrevista:juridico-compliance Q-013 | DIV-007 | US-002, US-006, US-022, US-041 | — |
| RN-008 | confirmado | Aprendiz no fluxo único | doc:geral/politica-RH-012-admissao-integracao.md#0; entrevista:negocio Q-001; entrevista:departamento-pessoal Q-011 | DIV-008, RIS-009 | US-037 | Q-021 |
| RN-009 | confirmado | Piso conforme a FolhaCerta | sql:SIS-01/folhacerta_dump.sql:cargo_piso; entrevista:departamento-pessoal Q-008 | DIV-010 | US-007, US-014, US-015 | — |
| RN-010 | confirmado | Prazo de documentos | doc:geral/politica-RH-012-admissao-integracao.md#0; doc:geral/comunicado-dp-07-2024.md#0; doc:SIS-03/LEIA-ME.md#0 | DIV-011 | US-018 | — |
| RN-011 | confirmado | Critérios bloqueantes confirmados | doc:geral/politica-RH-012-admissao-integracao.md#1; entrevista:operacoes Q-007; entrevista:sesmt Q-004; entrevista:regulatorio Q-006; doc:geral/M-02-email-juridico-2026-10-30.md#0 | DIV-014, DIV-015, RIS-006 | US-020, US-028, US-029 | — |
| RN-012 | confirmado | Gravidez e antecedentes | sql:SIS-02/recrutamais_dump.sql:candidato; entrevista:juridico-compliance Q-013 | RIS-003 | US-007, US-041 | Q-042 |
| RN-013 | conflito | Visibilidade do resultado do ASO | doc:geral/politica-RH-012-admissao-integracao.md#1; entrevista:departamento-pessoal Q-003; entrevista:juridico-compliance Q-012; doc:geral/fluxo-admissao-atual.md#0 | DIV-018 | US-022 | Q-040 |
| RN-014 | confirmado | Dado de pessoa com deficiência | sql:SIS-02/recrutamais_dump.sql:candidato; entrevista:juridico-compliance Q-013 | RIS-002 | US-002, US-039 | — |
| RN-015 | confirmado | Admissão concluída | sql:SIS-01/folhacerta_dump.sql:contrato.status; entrevista:departamento-pessoal Q-003 | DIV-009 | US-045 | — |
| RN-016 | confirmado | Abrangência da primeira fase | doc:geral/politica-RH-012-admissao-integracao.md#0; entrevista:negocio Q-001 | DIV-016 | US-012 | — |
| RN-017 | confirmado | Prazos dos eventos de admissão | doc:geral/politica-RH-012-admissao-integracao.md#1; sql:SIS-01/folhacerta_dump.sql:esocial_prazo; sql:SIS-01/folhacerta_dump.sql:fn_gera_esocial | GAR-006 | US-027 | — |
| RN-018 | hipótese | Demais critérios de início | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0; doc:geral/politica-RH-012-admissao-integracao.md#1; entrevista:operacoes Q-007 | DIV-015 | US-030 | Q-031 |
| RF-001 | confirmado | Painel de prontidão para início | doc:escopo.md; doc:SIS-03/LEIA-ME.md#1; entrevista:operacoes Q-007 | DIV-015, GAR-007, OPO-002 | US-028 | — |
| RF-002 | confirmado | Dados sem redigitação até a folha | doc:escopo.md; doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0 | GAR-001, DIV-012, RIS-012, OPO-001 | US-024, US-025 | — |
| RF-003 | confirmado | Documentos da admissão | doc:escopo.md; doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0; doc:geral/politica-RH-012-admissao-integracao.md#0; doc:geral/M-02-email-juridico-2026-10-30.md#0 | GAR-002, OPO-003 | US-016, US-017 | Q-036 |
| RF-004 | confirmado | Situação do contrato | doc:escopo.md; sql:SIS-01/folhacerta_dump.sql:contrato.status | DIV-015 | US-026 | — |
| RF-005 | confirmado | Acompanhamento do exame | doc:escopo.md; doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1; entrevista:juridico-compliance Q-012 | GAR-003, RIS-008 | US-019 | Q-025 |
| RF-006 | confirmado | Acompanhamento de eSocial | doc:escopo.md; sql:SIS-01/folhacerta_dump.sql:evento_esocial; doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1 | GAR-006, RIS-011 | US-027 | — |
| RF-007 | hipótese | Acesso individual ao PDV | doc:escopo.md; doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1; doc:geral/manual-admissao-lojas-v3.2-2019.md#1; doc:geral/fluxo-admissao-atual.md#0 | GAR-004, DIV-013, RIS-004, OPO-006 | US-032 | — |
| RF-008 | confirmado | Acompanhamento de treinamentos | doc:escopo.md; doc:SIS-04/lms-estrutura.md#0; entrevista:regulatorio Q-015 | GAR-005, DIV-004 | US-033 | Q-046 |
| RF-009 | hipótese | Controle do fim da experiência | doc:escopo.md; doc:geral/fluxo-admissao-atual.md#0; doc:geral/manual-admissao-lojas-v3.2-2019.md#1; entrevista:juridico-compliance Q-005 | RIS-007 | US-036 | Q-028, Q-047 |
| RF-010 | confirmado | Funil de admissão | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0; entrevista:departamento-pessoal Q-003 | DIV-009, OPO-007 | US-045 | — |
| RF-011 | confirmado | Abertura da admissão a partir da oferta | doc:escopo.md; doc:geral/fluxo-admissao-atual.md#0 | GAR-007 | US-012 | — |
| RF-012 | confirmado | Registro de aprovação da oferta | doc:geral/politica-RH-012-admissao-integracao.md#0; entrevista:juridico-compliance Q-008 | DIV-005 | US-013, US-014 | — |
| RF-013 | confirmado | Conferência do piso antes da oferta | sql:SIS-01/folhacerta_dump.sql:cargo_piso; sql:SIS-02/recrutamais_dump.sql:tabela_salarial; entrevista:departamento-pessoal Q-008 | DIV-010 | US-015 | — |
| RF-014 | hipótese | Matrícula automática | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1; doc:SIS-04/lms-estrutura.md#0 | GAR-005, OPO-005 | US-035 | — |
| RF-015 | confirmado | Reavaliação ao mudar o início | entrevista:sesmt Q-004; doc:SIS-03/controle_admissoes_2026-estrutura.md#1 | DIV-001, RIS-006 | US-021 | Q-024 |
| RF-016 | confirmado | Registro da certidão de CRF | doc:geral/politica-RH-012-admissao-integracao.md#1; entrevista:regulatorio Q-006; sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato | DIV-003, RIS-005 | US-031 | Q-029 |
| RF-017 | confirmado | Eliminação automática | doc:geral/politica-RH-012-admissao-integracao.md#2; entrevista:juridico-compliance Q-013; sql:SIS-02/recrutamais_dump.sql:sp_expurgo_candidatos | DIV-006, OPO-008 | US-043 | — |
| RF-018 | hipótese | Migração e convivência com o legado | doc:SIS-03/controle_admissoes_2026-estrutura.md#0; entrevista:negocio Q-001; entrevista:juridico-compliance Q-013 | DIV-012, RIS-017 | US-009, US-010 | — |
| RF-019 | hipótese | Agendamento com a clínica | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1; entrevista:sesmt Q-004 | GAR-003, RIS-008, OPO-004 | US-023 | Q-026 |
| RF-020 | hipótese | Fila de falhas de integração | entrevista:software-architect Q-014 | RIS-016 | US-044 | — |
| RF-021 | confirmado | Fluxo de aprendiz | entrevista:negocio Q-001; entrevista:departamento-pessoal Q-011; sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato; doc:geral/fluxo-admissao-atual.md#0 | DIV-008, GAR-008, RIS-009 | US-037, US-038 | Q-032, Q-038 |
| RF-022 | confirmado | Restrição de atendimento sozinho | doc:geral/politica-RH-012-admissao-integracao.md#1; entrevista:regulatorio Q-015 | DIV-004 | US-034 | Q-045 |
| RF-023 | hipótese | Treinamento e transição de usuários | entrevista:negocio Q-001; doc:geral/manual-admissao-lojas-v3.2-2019.md#0 | RIS-017 | US-011 | — |
| RF-024 | hipótese | Alinhamento das regras nos legados | doc:geral/manual-admissao-lojas-v3.2-2019.md#1; doc:SIS-03/LEIA-ME.md#0; sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato; sql:SIS-02/recrutamais_dump.sql:tabela_salarial; doc:SIS-04/lms-estrutura.md#0; entrevista:software-architect Q-014 | DIV-001, DIV-002, DIV-003, DIV-004, DIV-006, DIV-010 | US-004, US-005, US-006, US-007, US-008 | — |
| RF-025 | hipótese | Medição do processo | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0; entrevista:departamento-pessoal Q-003; entrevista:departamento-pessoal Q-010 | GAR-001, GAR-002, GAR-009 | US-017, US-046 | Q-023 |
| RNF-001 | hipótese | Dados fora de canais abertos | doc:SIS-03/LEIA-ME.md#0; doc:geral/fluxo-admissao-atual.md#0; entrevista:juridico-compliance Q-012; entrevista:juridico-compliance Q-013 | RIS-001, RIS-013, OPO-008 | US-001, US-016, US-039 | Q-041, Q-049 |
| RNF-002 | confirmado | Permissões por papel | doc:geral/politica-RH-012-admissao-integracao.md#1; sql:SIS-02/recrutamais_dump.sql:GRANT gerente_loja; sql:SIS-01/folhacerta_dump.sql:GRANT rh_loja; entrevista:juridico-compliance Q-012; entrevista:juridico-compliance Q-013 | RIS-002, OPO-008 | US-002, US-039 | — |
| RNF-003 | hipótese | Autoria individual no PDV | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1; entrevista:software-architect Q-014 | RIS-004 | US-032 | — |
| RNF-004 | hipótese | Trilha de auditoria | doc:escopo.md; doc:SIS-03/LEIA-ME.md#0 | RIS-001, DIV-014 | US-029, US-042 | — |
| RNF-005 | confirmado | Capacidade no pico | entrevista:departamento-pessoal Q-010 | GAR-009 | US-047 | — |
| RNF-006 | hipótese | Disponibilidade | entrevista:software-architect Q-014 | RIS-016 | US-048 | — |
| RNF-007 | hipótese | Monitoramento de integrações | entrevista:software-architect Q-014 | RIS-016 | US-044 | — |
| RNF-008 | hipótese | Uso pelo gerente | doc:escopo.md | OPO-002 | US-028 | — |
| RNF-009 | hipótese | Regras parametrizadas com vigência | entrevista:juridico-compliance Q-005; doc:geral/politica-RH-012-admissao-integracao.md#0 | DIV-002 | US-049 | — |
| RNF-010 | confirmado | Comprovação de retenção | entrevista:juridico-compliance Q-013; doc:geral/politica-RH-012-admissao-integracao.md#2 | DIV-006 | US-043 | — |
| RNF-011 | hipótese | Proteção de dados pessoais em transporte e repouso | doc:geral/politica-RH-012-admissao-integracao.md#1 | RIS-013 | US-040 | — |
| RN-019 | confirmado | Vacinação para aplicar injetáveis em SP | doc:geral/M-02-email-juridico-2026-10-30.md#0 | RIS-020 | US-029, US-050, US-052, US-053 | Q-052 |
| RN-020 | hipótese | Sigilo do comprovante de vacinação | doc:geral/politica-RH-012-admissao-integracao.md#1; doc:geral/M-02-email-juridico-2026-10-30.md#0 | RIS-020 | US-052 | Q-051 |
| RN-021 | confirmado | Admissões do programa Acolher | doc:geral/M-02-email-juridico-2026-10-30.md#0 | RIS-019 | US-054 | Q-055 |
| RN-022 | hipótese | Sigilo da condição de refugiado ou migrante | doc:geral/M-02-email-juridico-2026-10-30.md#0; doc:geral/politica-RH-012-admissao-integracao.md#1 | RIS-019 | US-057 | Q-054 |
| RF-026 | confirmado | Comprovante de vacinação como critério | doc:geral/M-02-email-juridico-2026-10-30.md#0 | RIS-020 | US-028, US-051, US-053 | Q-052 |
| RF-027 | confirmado | Aceite da CRNM | doc:geral/M-02-email-juridico-2026-10-30.md#0 | RIS-019 | US-016, US-054 | — |
| RF-028 | confirmado | Controle da validade da CRNM | doc:geral/M-02-email-juridico-2026-10-30.md#0 | RIS-019 | US-055 | Q-053 |
| RF-029 | hipótese | Admissão sem CPF confirmado nos legados | doc:geral/M-02-email-juridico-2026-10-30.md#0; sql:SIS-01/folhacerta_dump.sql:colaborador; sql:SIS-02/recrutamais_dump.sql:candidato | RIS-019 | US-024, US-025, US-056 | Q-053 |

## 2. Fonte e requisitos

| Fonte | Requisitos |
|---|---|
| Política RH-012 | RN-001, RN-002, RN-003, RN-004, RN-005, RN-006, RN-007, RN-008, RN-010, RN-011, RN-013, RN-016, RN-017, RN-018, RF-003, RF-012, RF-016, RF-017, RF-022, RNF-002, RNF-009, RNF-010, RNF-011, RN-020, RN-022 |
| Manual 3.2 | RF-007, RF-009, RF-023, RF-024 |
| Comunicado DP 07/2024 | RN-010 |
| Fluxo atual | RN-013, RF-007, RF-009, RF-011, RF-021, RNF-001 |
| Ata 22/09/2026 | RN-018, RF-002, RF-003, RF-005, RF-006, RF-007, RF-010, RF-014, RF-019, RF-025, RNF-003 |
| Leia-me da planilha | RN-010, RF-001, RF-024, RNF-001, RNF-004 |
| Estrutura da planilha | RF-015, RF-018 |
| EducaFarma | RF-008, RF-014, RF-024 |
| FolhaCerta | RN-009, RN-015, RN-017, RF-004, RF-006, RF-013, RF-016, RF-021, RF-024, RNF-002, RF-029 |
| Recruta+ | RN-012, RN-014, RF-013, RF-017, RF-024, RNF-002, RF-029 |
| Escopo | RF-001, RF-002, RF-003, RF-004, RF-005, RF-006, RF-007, RF-008, RF-009, RF-011, RNF-004, RNF-008 |
| Respostas | RN-001, RN-002, RN-003, RN-004, RN-005, RN-006, RN-007, RN-008, RN-009, RN-011, RN-012, RN-013, RN-014, RN-015, RN-016, RN-018, RF-001, RF-005, RF-008, RF-009, RF-010, RF-012, RF-013, RF-015, RF-016, RF-017, RF-018, RF-019, RF-020, RF-021, RF-022, RF-023, RF-024, RF-025, RNF-001, RNF-002, RNF-003, RNF-005, RNF-006, RNF-007, RNF-009, RNF-010 |
| M-01 Ata 28/10/2026 | RN-002, RN-003 |
| M-02 E-mail 30/10/2026 | RN-001, RN-011, RF-003, RN-019, RN-020, RN-021, RN-022, RF-026, RF-027, RF-028, RF-029 |

## 3. Achado e tratamento

| Achado | Título | Status | Gera |
|---|---|---|---|
| DIV-001 | Validade do ASO: 30, 60 ou 90 dias | tratado | RN-001, RF-015, RF-024, Q-004, Q-024, Q-025 |
| DIV-002 | Experiência: 30+60 ou 45+45 | tratado | RN-002, RF-024, Q-005, Q-027, Q-028 |
| DIV-003 | CRF: certidão, protocolo ou só número | tratado | RN-003, RF-016, RF-024, Q-006, Q-029, Q-030 |
| DIV-004 | Prazo da integração: 5, 15 ou 30 dias | tratado | RN-004, RF-022, RF-024, Q-015, Q-045 |
| DIV-005 | Aprovação da oferta sem o BP de RH | tratado | RN-005, RF-012, Q-008, Q-034 |
| DIV-006 | Eliminação de candidatos: 6 ou 24 meses | tratado | RN-006, RF-017, RNF-010, Q-013, Q-043 |
| DIV-007 | Dados de saúde fora do SESMT | aberto | RN-007, RN-013, Q-012, Q-040 |
| DIV-008 | Aprendiz: política admite de 14 a 24 anos, FolhaCerta não | aberto | RN-008, RF-021, Q-011, Q-038, Q-039 |
| DIV-009 | Três números para admissões do mesmo mês | tratado | RN-015, RF-010, Q-003, Q-022 |
| DIV-010 | Tabela salarial do Recruta+ defasada | tratado | RN-009, RF-013, RF-024, Q-008, Q-035 |
| DIV-011 | Prazo de documentos: 3 ou 5 dias úteis | tratado | RN-010 |
| DIV-012 | Sem chave comum e com identificadores diferentes | aberto | RF-002, RF-018, Q-014 |
| DIV-013 | Momento do chamado de acesso ao PDV | aberto | RF-007, Q-014 |
| DIV-014 | Regra de não iniciar sem ASO e prática | aberto | RN-011, RNF-004, Q-007, Q-009 |
| DIV-015 | Critérios diferentes para poder começar | aberto | RN-011, RN-018, RF-001, Q-007, Q-031 |
| DIV-016 | Abrangência: 212 ou 184 lojas | tratado | RN-016, Q-001, Q-016 |
| GAR-001 | Redigitação na FolhaCerta | aberto | RF-002, RF-025, Q-037 |
| GAR-002 | Devolução de pastas | aberto | RF-003, RF-025, Q-010, Q-037 |
| GAR-003 | Agendamento de exame por e-mail | aberto | RF-005 |
| GAR-004 | Espera pelo login do PDV | aberto | RF-007 |
| GAR-005 | Matrícula manual no LMS | aberto | RF-008 |
| GAR-006 | Corrida do S-2190 na véspera | aberto | RF-006, RN-017, Q-009 |
| GAR-007 | Planilha paralela como painel | aberto | RF-001 |
| GAR-008 | Lote quinzenal do aprendiz | aberto | RF-021, Q-011, Q-038 |
| RIS-001 | Planilha aberta com dados pessoais | aberto | RNF-001, Q-013, Q-044 |
| RIS-002 | Dados sensíveis de candidatos acessíveis a gerentes | aberto | RNF-002, RN-012, RN-014, Q-013, Q-044 |
| RIS-003 | Risco de discriminação na admissão | aberto | RN-012, Q-013, Q-042 |
| RIS-004 | Login do gerente usado por colaborador novo | aberto | RF-007, RNF-003, Q-014 |
| RIS-005 | Farmacêutico em atividade sem certidão | aberto | RN-003, RF-016, Q-006, Q-030 |
| RIS-006 | Início sem ASO válido sob pressão da loja | aberto | RN-011, RF-015, Q-007, Q-033 |
| RIS-007 | Fim da experiência sem controle | aberto | RF-009, Q-005, Q-028 |
| RIS-008 | Dependência de pessoa no SESMT | aberto | RF-005 |
| RIS-009 | Aprendiz fora dos controles | aberto | RN-008, RF-021, Q-011, Q-038, Q-039 |
| RIS-010 | Adiamento pode não recalcular eventos | aberto | Q-009 |
| RIS-011 | Cobertura de eventos eSocial a verificar | aberto | Q-009 |
| RIS-012 | CPF redigitado errado na folha | aberto | RF-002 |
| RIS-013 | Documentos pessoais circulando por e-mail | aberto | RNF-001, Q-012 |
| RIS-014 | Lacunas de fonte para o projeto | aberto | Q-002, Q-014, Q-017, Q-018, Q-019, Q-020 |
| APO-001 | FolhaCerta como sistema estável da folha | aberto | preservar/reaproveitar |
| APO-002 | S-2200 coerente | aberto | preservar/reaproveitar |
| APO-003 | Carência do plano coerente | aberto | preservar/reaproveitar |
| APO-004 | EducaFarma com API e trilhas por cargo | aberto | preservar/reaproveitar |
| APO-005 | Datas coerentes entre sistemas | aberto | preservar/reaproveitar |
| APO-006 | Checklist de primeiro dia e fluxo mapeado | aberto | preservar/reaproveitar |
| APO-007 | Política RH-012 como referência | aberto | preservar/reaproveitar |
| APO-008 | Oferta aceita e piso por vigência | aberto | preservar/reaproveitar |
| OPO-001 | Cadastro único do aceite à folha | aberto | RF-002 |
| OPO-002 | Painel Pode começar para o gerente | aberto | RF-001 |
| OPO-003 | Coleta e pré-conferência de documentos | aberto | RF-003 |
| OPO-004 | Agendamento pela API da MedTrab | aberto | RF-005 |
| OPO-005 | Matrícula automática pela API do EducaFarma | aberto | RF-008 |
| OPO-006 | Acesso pronto no primeiro dia | aberto | RF-007 |
| OPO-007 | Funil único de admissão | aberto | RF-010 |
| OPO-008 | Saneamento LGPD com o inventário | aberto | RNF-001, RNF-002 |
| DIV-017 | Quem aprova mudança na RH-012 | aberto | Q-048 |
| DIV-018 | DP valida ASO, mas saúde é exclusiva do SESMT | aberto | RN-013, Q-040 |
| GAR-009 | Pico de novembro e dezembro | aberto | RNF-005, RF-025 |
| RIS-015 | Casos em curso fora da regra confirmada | aberto | Q-027, Q-030 |
| RIS-016 | Perguntas 9 e 14 sem resposta | aberto | RF-020, RNF-006, RNF-007, Q-009, Q-014 |
| RIS-017 | Convivência prolongada de processos | aberto | RF-018, RF-023, Q-016 |
| DIV-019 | Comunicado de 45+45 contra a RH-012 | aberto | RN-002, CR-001, Q-050 |
| RIS-018 | Lojas adotarem 45+45 antes de uma decisão | aberto | CR-001, Q-050 |
| RIS-019 | CRNM sem lugar nos cadastros atuais | aberto | RF-027, RF-028, RF-029, RN-021, RN-022, Q-053, Q-054, Q-055 |
| RIS-020 | Datas externas antes de o sistema existir | aberto | RN-019, RF-026, RN-020, Q-017, Q-051, Q-052 |

## 4. Pergunta original e resultado

| Pergunta | Status | Resposta resumida |
|---|---|---|
| Q-001 | respondida | 184 próprias dentro; CD e escritório fora na primeira fase; 28 franqueadas fora. CLT de loja é a primeira prioridade; aprendizes como prioridade 5. Estágio: não sabe. |
| Q-002 | respondida | Helena decide escopo, prioridades e texto final da RH-012. Data, teto (indica Vera Castro, CFO), critérios, aprovador de requisitos e comitê: não sabe. |
| Q-003 | respondida | Rogério: admissão concluída é contrato assinado, ASO apto validado e ATIVO; 188 na projeção de setembro. Parcelas e metas: não sabe. |
| Q-004 | respondida | 30 dias corridos; sem outra janela; ASO válido antes do início, sem exceção. Procedimento, inapto/restrição e API: não sabe. |
| Q-005 | respondida | 30+60; mudança exige revisão aprovada por Helena e Marina. Contratos em curso e decisão de prorrogação: não sabe. |
| Q-006 | respondida | Beatriz Lobo: CRF ativo antes do início, inclusive RT; protocolo não vale; nenhuma exceção a informar. Conferência, validade e casos atuais: não sabe. |
| Q-007 | respondida | Bloqueiam: ASO válido e CRF ativo. Sem exceção para ASO. Demais critérios, aprendiz e alternativa: não sabe. |
| Q-008 | respondida | BP de RH sempre; regional acima do piso da CCT vigente da UF; gerente indica; piso conforme FolhaCerta. Canal atual e dono do Recruta+: não sabe. |
| Q-009 | aberta | Não sei. |
| Q-010 | respondida | Pico de cerca de 320 admissões por mês em novembro e dezembro. Lista, causas e campos: não sabe. |
| Q-011 | respondida | Aprendiz de 14 a 24 anos entra no novo processo. Motivo da Contábil Alfa, eSocial, destino do fluxo e menores: não sabe. |
| Q-012 | respondida | CID só no ambiente do SESMT; FolhaCerta não deve manter CID. Visão de DP e gerente, restrição, observação clínica e eliminação: não sabe. |
| Q-013 | respondida | Gravidez e antecedentes não devem ser perguntados nem guardados na seleção; CID no SESMT; dado PCD só para cota; 6 meses inclusive cópias e backups. Tabela específica, oferta recusada, base legal e contenção: não sabe. |
| Q-014 | aberta | Não sei. |
| Q-015 | respondida | Beatriz Lobo: 5º dia corrido, antes de atender sozinho. Quem atesta, trilhas e acompanhamento: não sabe. |

## 5. Pedidos de mudança

| CR | Título | Classe | Status | Itens afetados |
|---|---|---|---|---|
| CR-001 | Experiência 45+45 a partir de 01/12/2026 | conflitante | proposta | RN-002, DIV-002, DIV-019, RF-009, RF-024, US-004, US-005, US-036 |
| CR-002 | Vacinação para aplicar injetáveis em SP | complementar | aplicada | RN-011, RN-019, RN-020, RF-001, RF-026, US-028, US-029 |
| CR-003 | Programa Acolher e CRNM | novo | aplicada | RF-002, RF-003, RF-027, RF-028, RF-029, RN-021, RN-022, US-016, US-017, US-024, US-025 |

## 6. Análise

- Requisitos sem fonte: nenhum.
- Requisitos sem história: nenhum.
- Histórias sem requisito: nenhuma; achados abertos sem tratamento: nenhum (conferido por `recop.py lint`).
- Total: 62 requisitos, sendo 39 confirmados, 21 hipóteses e 2 em conflito. Nenhum foi validado em revisão formal.
- `recop.py lint` aponta Q-036 e Q-051 a Q-055 como abertas e ligadas a mudança aplicada: é esperado, pois elas definem detalhes de CR-002 e CR-003.
