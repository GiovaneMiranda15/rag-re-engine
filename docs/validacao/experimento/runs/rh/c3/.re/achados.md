# Achados do diagnóstico

## Divergências

| ID | Achado | Sistemas | Severidade | Fontes | Status | Gera |
|---|---|---|---|---|---|---|
| DIV-001 | Abrangência: 212 lojas no escopo, 184 próprias na Política e na ata | — | alta | doc:escopo.md, doc:geral/politica-RH-012-admissao-integracao.md#0, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0 | tratado | Q-001 |
| DIV-002 | Números de setembro: 214, 188 e 176 medem marcos diferentes | SIS-01, SIS-02, SIS-03 | alta | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0, sql:SIS-02/recrutamais_dump.sql:trg_oferta_aceita, sql:SIS-01/folhacerta_dump.sql:contrato.status, doc:SIS-03/LEIA-ME.md#1 | aberto | Q-003, RF-008, RN-015, Q-020 |
| DIV-003 | Experiência: 30+60 na Política, 45+45 na prática | SIS-01, SIS-03 | alta | doc:geral/politica-RH-012-admissao-integracao.md#0, doc:geral/manual-admissao-lojas-v3.2-2019.md#1, doc:SIS-03/LEIA-ME.md#0, sql:SIS-01/folhacerta_dump.sql:contrato.dias_experiencia, sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato | aberto | Q-004, RN-001, Q-021, Q-022, RN-017, Q-035 |
| DIV-004 | Validade do ASO: 30, 60 ou 90 dias | SIS-01, SIS-03 | alta | doc:geral/politica-RH-012-admissao-integracao.md#1, doc:SIS-03/LEIA-ME.md#0, sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato | tratado | Q-005, RN-002 |
| DIV-005 | CRF: certidão obrigatória na Política, protocolo aceito na planilha, RT sem validação na folha | SIS-01, SIS-03 | critica | doc:geral/politica-RH-012-admissao-integracao.md#1, doc:SIS-03/LEIA-ME.md#0, doc:geral/manual-admissao-lojas-v3.2-2019.md#1, sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato, sql:SIS-01/folhacerta_dump.sql:cargo.exige_crf | tratado | Q-006, RN-003 |
| DIV-006 | Aprovação da oferta: BP de RH não existe no fluxo nem no Recruta+ | SIS-02 | alta | doc:geral/politica-RH-012-admissao-integracao.md#0, doc:geral/manual-admissao-lojas-v3.2-2019.md#0, doc:geral/fluxo-admissao-atual.md#0, sql:SIS-02/recrutamais_dump.sql:oferta.aprovador_perfil | aberto | Q-007, RN-004, Q-025 |
| DIV-007 | Tabela salarial do Recruta+ desatualizada em SP | SIS-01, SIS-02 | alta | sql:SIS-02/recrutamais_dump.sql:tabela_salarial, sql:SIS-01/folhacerta_dump.sql:cargo_piso, sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato | tratado | Q-007, RN-004, RN-011 |
| DIV-008 | Prazo da integração: 5, 15 ou 30 dias | SIS-04 | alta | doc:geral/politica-RH-012-admissao-integracao.md#1, doc:geral/manual-admissao-lojas-v3.2-2019.md#1, doc:SIS-04/lms-estrutura.md#0 | tratado | Q-008, RN-005 |
| DIV-009 | Aprendiz previsto na Política, bloqueado na FolhaCerta | SIS-01, SIS-02, SIS-03 | alta | doc:geral/politica-RH-012-admissao-integracao.md#0, sql:SIS-01/folhacerta_dump.sql:chk_tipo_contrato, sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato, doc:geral/fluxo-admissao-atual.md#0, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1 | aberto | Q-009, RN-006, RF-015, Q-027 |
| DIV-010 | Retenção de candidatos: 6 meses na Política, 24 no expurgo, sem limite no backup | SIS-02 | critica | doc:geral/politica-RH-012-admissao-integracao.md#2, sql:SIS-02/recrutamais_dump.sql:sp_expurgo_candidatos, sql:SIS-02/recrutamais_dump.sql:candidato_bkp_2022 | tratado | Q-012, RN-007 |
| DIV-011 | Dado de saúde fora do SESMT | SIS-01, SIS-03 | critica | doc:geral/politica-RH-012-admissao-integracao.md#1, sql:SIS-01/folhacerta_dump.sql:GRANT rh_loja, sql:SIS-01/folhacerta_dump.sql:exame_admissional, doc:SIS-03/planilha-estrutura.md#0 | aberto | Q-012, Q-013, RN-008, RN-014, Q-031, Q-033 |
| DIV-012 | Prazo de documentos: Manual ainda publica 3 dias úteis | SIS-03 | baixa | doc:geral/manual-admissao-lojas-v3.2-2019.md#0, doc:geral/comunicado-dp-07-2024.md#0, doc:geral/politica-RH-012-admissao-integracao.md#0, doc:SIS-03/LEIA-ME.md#0 | tratado | RN-010 |
| DIV-013 | Identificadores diferentes entre os sistemas | SIS-01, SIS-02, SIS-03, SIS-04 | media | sql:SIS-01/folhacerta_dump.sql:filial, sql:SIS-02/recrutamais_dump.sql:unidade, doc:SIS-03/LEIA-ME.md#0, doc:SIS-04/lms-estrutura.md#0, doc:SIS-03/planilha-estrutura.md#0, sql:SIS-01/folhacerta_dump.sql:colaborador | aberto | Q-014 |
| DIV-014 | "Pode começar" não tem definição única | SIS-01, SIS-03 | alta | doc:SIS-03/LEIA-ME.md#1, sql:SIS-01/folhacerta_dump.sql:contrato.status, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0, doc:geral/politica-RH-012-admissao-integracao.md#0, doc:geral/politica-RH-012-admissao-integracao.md#1, doc:geral/fluxo-admissao-atual.md#0 | aberto | Q-010, RN-009, RF-012, Q-028 |
| DIV-015 | Momento do chamado de acesso ao PDV | SIS-03 | baixa | doc:geral/manual-admissao-lojas-v3.2-2019.md#1, doc:geral/fluxo-admissao-atual.md#0, doc:SIS-03/LEIA-ME.md#1 | aberto | Q-015, RF-006, Q-032 |
| DIV-016 | Lista de documentos só existe no Manual de 2019 | — | media | doc:geral/manual-admissao-lojas-v3.2-2019.md#0, doc:geral/politica-RH-012-admissao-integracao.md#1 | aberto | Q-011, Q-029, RF-019 |
| DIV-017 | Validação do ASO pelo DP e sigilo da saúde | SIS-01 | media | entrevista:departamento-pessoal Q-003 (Rogério Tavares), doc:geral/politica-RH-012-admissao-integracao.md#1 | aberto | RN-014, Q-031 |

## Gargalos

| ID | Achado | Sistemas | Severidade | Fontes | Status | Gera |
|---|---|---|---|---|---|---|
| GAR-001 | Redigitação na FolhaCerta | SIS-01, SIS-03 | alta | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0 | aberto | Q-011, Q-014, RF-002 |
| GAR-002 | Devolução de pastas | SIS-03 | alta | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0, doc:geral/fluxo-admissao-atual.md#0, doc:SIS-03/planilha-estrutura.md#0 | aberto | Q-011, RF-003 |
| GAR-003 | Agendamento de ASO por e-mail com uma analista | — | alta | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1, doc:geral/fluxo-admissao-atual.md#0 | aberto | Q-013, RF-004 |
| GAR-004 | Corrida do S-2190 na véspera | SIS-01 | alta | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0, sql:SIS-01/folhacerta_dump.sql:fn_gera_esocial | aberto | Q-010, RF-005 |
| GAR-005 | Cerca de 3 dias sem login no PDV | — | alta | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1, doc:geral/manual-admissao-lojas-v3.2-2019.md#1 | aberto | Q-014, Q-015, RF-006 |
| GAR-006 | Matrícula manual depois do início | SIS-04 | media | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1, doc:geral/fluxo-admissao-atual.md#0 | aberto | Q-008, RF-007 |
| GAR-007 | Lote quinzenal de aprendizes | — | media | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0, doc:SIS-03/LEIA-ME.md#0 | aberto | Q-009 |
| GAR-008 | Gerente acompanha por vários canais | SIS-02, SIS-03, SIS-04 | alta | doc:escopo.md, doc:geral/fluxo-admissao-atual.md#0 | aberto | Q-015, RF-001 |

## Riscos

| ID | Achado | Sistemas | Severidade | Fontes | Status | Gera |
|---|---|---|---|---|---|---|
| RIS-001 | Início antes do ASO | SIS-01, SIS-03 | critica | doc:geral/politica-RH-012-admissao-integracao.md#1, sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato, sql:SIS-01/folhacerta_dump.sql:fn_gera_esocial, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1, doc:SIS-03/planilha-estrutura.md#0 | aberto | Q-005, Q-010, RN-002, RN-009, RF-012, Q-028 |
| RIS-002 | Farmacêutico RT em atividade sem CRF registrado | SIS-01, SIS-03 | critica | doc:geral/politica-RH-012-admissao-integracao.md#1, sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato, doc:SIS-03/LEIA-ME.md#0 | aberto | Q-006, RN-003, RF-012, Q-024 |
| RIS-003 | Login do gerente usado por colaborador novo, inclusive em venda com receita | — | critica | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1 | aberto | Q-015, RNF-003, RF-006, Q-032 |
| RIS-004 | Planilha com CPF e dados de saúde editável por qualquer pessoa com o link | SIS-03 | critica | doc:SIS-03/LEIA-ME.md#0, doc:SIS-03/planilha-estrutura.md#0 | aberto | Q-012, RNF-002, RF-014, Q-030 |
| RIS-005 | Dados sensíveis e potencial discriminação na seleção | SIS-02, SIS-03 | critica | sql:SIS-02/recrutamais_dump.sql:candidato, sql:SIS-02/recrutamais_dump.sql:GRANT gerente_loja, sql:SIS-02/recrutamais_dump.sql:candidato_bkp_2022, doc:SIS-03/planilha-estrutura.md#0 | aberto | Q-012, RNF-002, RN-012, RN-013, Q-030 |
| RIS-006 | Fim de experiência sem controle | SIS-01 | alta | sql:SIS-01/folhacerta_dump.sql:contrato | aberto | Q-004, RF-009, RF-018, Q-022 |
| RIS-007 | Aprendiz menor de idade fora dos controles | SIS-01, SIS-04 | alta | doc:geral/fluxo-admissao-atual.md#0, sql:SIS-01/folhacerta_dump.sql:chk_tipo_contrato, doc:SIS-04/lms-estrutura.md#0, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0 | aberto | Q-009 |
| RIS-008 | Treinamentos obrigatórios sem acompanhamento | SIS-04 | alta | doc:SIS-04/lms-estrutura.md#0 | aberto | Q-008, RF-007 |
| RIS-009 | Dependência de pessoas | SIS-03 | media | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1, doc:SIS-03/LEIA-ME.md#0 | aberto | Q-013 |
| RIS-010 | Automatizar regra errada e dono indefinido do produto | — | alta | doc:escopo.md | aberto | Q-002, Q-017, Q-018, Q-019 |
| RIS-011 | Eventos eSocial ausentes na amostra | SIS-01 | media | sql:SIS-01/folhacerta_dump.sql:fn_gera_esocial, sql:SIS-01/folhacerta_dump.sql:evento_esocial | aberto | Q-010, Q-028 |
| RIS-012 | Caminhos de exceção não mapeados | SIS-02 | media | doc:geral/fluxo-admissao-atual.md#0, sql:SIS-02/recrutamais_dump.sql:candidato.status, sql:SIS-02/recrutamais_dump.sql:vaga | aberto | Q-003, Q-015 |
| RIS-013 | Sem trilha de auditoria | SIS-01, SIS-02, SIS-03 | alta | sql:SIS-02/recrutamais_dump.sql:GRANT gerente_loja, doc:SIS-03/LEIA-ME.md#0 | aberto | Q-012, RNF-001 |
| RIS-014 | Viabilidade técnica das prioridades desconhecida | SIS-01, SIS-02 | critica | entrevista:negocio Q-002 (Helena Vasconcelos), entrevista:software-architect Q-014 | aberto | Q-014, RNF-004, RNF-005 |
| RIS-015 | Manual segue em uso com regras superadas | SIS-03 | alta | entrevista:juridico-compliance Q-004 (Rogério Tavares), doc:geral/manual-admissao-lojas-v3.2-2019.md#1, doc:geral/comunicado-dp-07-2024.md#0 | aberto | Q-021 |
| RIS-016 | FolhaCerta pode contornar o bloqueio | SIS-01 | alta | sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato, entrevista:software-architect Q-014 | aberto | Q-014, RF-012 |
| RIS-017 | Processo residual fora da primeira fase | SIS-03 | media | entrevista:negocio Q-001 (Helena Vasconcelos), doc:geral/politica-RH-012-admissao-integracao.md#0 | aberto | Q-016, RF-014 |
| RIS-018 | Datas externas sem cronograma do projeto | — | alta | doc:geral/M-02-email-juridico-2026-10-30.md#0, entrevista:negocio Q-002 | aberto | Q-018, Q-033, Q-034 |
| RIS-019 | Dados de migrantes sem chave e sem campo nos sistemas | SIS-01, SIS-02 | media | doc:geral/M-02-email-juridico-2026-10-30.md#0, sql:SIS-01/folhacerta_dump.sql:colaborador, sql:SIS-02/recrutamais_dump.sql:candidato | aberto | Q-034, RF-019 |

## Pontos de apoio

| ID | Achado | Sistemas | Severidade | Fontes | Status | Gera |
|---|---|---|---|---|---|---|
| APO-001 | FolhaCerta valida piso por cargo, UF e vigência | SIS-01 | media | sql:SIS-01/folhacerta_dump.sql:cargo_piso, sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1 | aberto | — |
| APO-002 | FolhaCerta gera S-2190 e S-2200 com prazos coerentes | SIS-01 | media | sql:SIS-01/folhacerta_dump.sql:fn_gera_esocial, doc:geral/politica-RH-012-admissao-integracao.md#1 | aberto | — |
| APO-003 | Regras já coerentes entre fontes | SIS-01, SIS-03 | baixa | doc:geral/politica-RH-012-admissao-integracao.md#0, doc:geral/politica-RH-012-admissao-integracao.md#1, sql:SIS-01/folhacerta_dump.sql:beneficio_regra, sql:SIS-01/folhacerta_dump.sql:cargo, doc:SIS-03/LEIA-ME.md#0 | aberto | — |
| APO-004 | exige_crf já existe no cadastro de cargos | SIS-01 | baixa | sql:SIS-01/folhacerta_dump.sql:cargo.exige_crf | aberto | — |
| APO-005 | EducaFarma tem API REST e trilhas por cargo | SIS-04 | media | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1, doc:SIS-04/lms-estrutura.md#0 | aberto | — |
| APO-006 | MedTrab oferece portal com API de agendamento | — | media | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1 | aberto | — |
| APO-007 | CPF liga Recruta+, FolhaCerta e planilha | SIS-01, SIS-02, SIS-03 | media | sql:SIS-01/folhacerta_dump.sql:colaborador, sql:SIS-02/recrutamais_dump.sql:candidato, doc:SIS-03/planilha-estrutura.md#0 | aberto | — |
| APO-008 | Dados coincidem apesar da redigitação | SIS-01, SIS-02, SIS-03 | baixa | sql:SIS-01/folhacerta_dump.sql:contrato, sql:SIS-02/recrutamais_dump.sql:oferta, doc:SIS-03/planilha-estrutura.md#0 | aberto | — |
| APO-009 | Base de processo e norma disponível | SIS-03 | baixa | doc:geral/fluxo-admissao-atual.md#0, doc:geral/politica-RH-012-admissao-integracao.md#0, doc:SIS-03/LEIA-ME.md#1 | aberto | — |

## Oportunidades

| ID | Achado | Sistemas | Severidade | Fontes | Status | Gera |
|---|---|---|---|---|---|---|
| OPO-001 | Cadastro aproveitado da oferta à folha | SIS-01, SIS-02 | alta | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1 | aberto | RF-002 |
| OPO-002 | Coleta e conferência prévia de documentos | — | alta | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0 | aberto | RF-003 |
| OPO-003 | Agendamento de ASO integrado com checagem de validade | — | alta | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1 | aberto | RF-004 |
| OPO-004 | Matrícula automática por cargo | SIS-04 | alta | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1 | aberto | RF-007 |
| OPO-005 | Painel único de liberação para o gerente | — | alta | doc:escopo.md | aberto | RF-001, RN-009 |
| OPO-006 | Acesso individual pronto para o primeiro dia | — | alta | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1 | aberto | RF-006, RNF-003 |
| OPO-007 | Funil único com marcos definidos | SIS-01, SIS-02, SIS-03 | media | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0 | aberto | RF-008 |
| OPO-008 | Regras parametrizadas com vigência e origem | — | media | sql:SIS-01/folhacerta_dump.sql:cargo_piso | aberto | RF-010 |
| OPO-009 | Aposentar a planilha e atender ao inventário de dados | SIS-03 | alta | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1, doc:SIS-03/LEIA-ME.md#0 | aberto | RNF-002 |
