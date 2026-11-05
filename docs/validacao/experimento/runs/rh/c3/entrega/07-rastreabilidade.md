# Rastreabilidade: requisitos, fontes e backlog

**Atualizada na Etapa 3.** **Baseline:** B-001, foto de trabalho, ainda não validada.

Gerado do modelo. Siglas: `doc:` trecho indexado, `sql:` objeto do dump, `entrevista:` resposta em `entrega/respostas.md`. As comunicações novas são `geral/M-01…` e `geral/M-02…`.

## 1. Requisito para fonte e backlog

| Requisito | Status | Versão | Prior. | Título | Fontes | Origem | Histórias | Features |
|---|---|---|---|---|---|---|---|---|
| RF-001 | confirmado | v2 | Must | Painel do gerente | doc:escopo.md<br>entrevista:negocio Q-002 (Helena Vasconcelos) | GAR-008, OPO-005 | US-001, US-002 | FT-001 |
| RF-002 | confirmado | v2 | Must | Reaproveitamento de dados | doc:escopo.md<br>doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0<br>entrevista:negocio Q-002 (Helena Vasconcelos) | GAR-001, OPO-001 | US-019, US-020, US-021 | FT-006 |
| RF-003 | confirmado | v2 | Must | Coleta de documentos | doc:escopo.md<br>doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0<br>entrevista:negocio Q-002 (Helena Vasconcelos) | GAR-002, OPO-002 | US-016, US-017, US-034 | FT-005 |
| RF-004 | confirmado | v2 | Must | Acompanhamento do ASO | doc:escopo.md<br>doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1 | GAR-003, OPO-003 | US-012 | FT-003 |
| RF-005 | confirmado | v1 | Must | Acompanhamento do eSocial | doc:escopo.md<br>sql:SIS-01/folhacerta_dump.sql:fn_gera_esocial | GAR-004 | US-005 | FT-001 |
| RF-006 | confirmado | v2 | Must | Solicitação de acessos | doc:escopo.md<br>doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1 | DIV-015, GAR-005, OPO-006, RIS-003 | US-006 | FT-001 |
| RF-007 | confirmado | v1 | Must | Treinamentos obrigatórios | doc:escopo.md<br>doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1<br>doc:SIS-04/lms-estrutura.md#0 | GAR-006, OPO-004, RIS-008 | US-013, US-014 | FT-004 |
| RF-008 | confirmado | v2 | Should | Etapas da admissão | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0<br>entrevista:departamento-pessoal Q-003 (Rogério Tavares) | DIV-002, OPO-007 | US-007 | FT-001 |
| RF-009 | confirmado | v2 | Should | Acompanhamento até o fim da experiência | doc:escopo.md<br>sql:SIS-01/folhacerta_dump.sql:contrato<br>entrevista:juridico-compliance Q-004 (Marina Quintela) | RIS-006 | US-015 | FT-004 |
| RF-010 | hipótese | v1 | Should | Parâmetros de regra | sql:SIS-01/folhacerta_dump.sql:cargo_piso | OPO-008 | — | — |
| RF-011 | confirmado | v1 | Must | Acompanhamento da oferta | doc:escopo.md | GAR-008 | US-003 | FT-001 |
| RF-012 | alterado | v2 | Must | Bloqueio de início | entrevista:negocio Q-002 (Helena Vasconcelos)<br>entrevista:juridico-compliance Q-005 (Fábio Arantes e Marina Quintela)<br>entrevista:juridico-compliance Q-006 (Beatriz Lobo)<br>doc:geral/M-02-email-juridico-2026-10-30.md#0 | DIV-014, RIS-001, RIS-002 | US-002, US-008, US-010, US-011, US-033 | FT-001, FT-002 |
| RF-013 | confirmado | v1 | Must | Acompanhamento do contrato | doc:escopo.md<br>sql:SIS-01/folhacerta_dump.sql:contrato.status | DIV-014 | US-004, US-011 | FT-001, FT-002 |
| RF-014 | confirmado | v1 | Must | Saída da planilha | entrevista:negocio Q-002 (Helena Vasconcelos) | OPO-009, RIS-004 | US-023, US-024 | FT-007 |
| RF-015 | confirmado | v1 | Should | Aprendiz com caminho próprio de registro | entrevista:departamento-pessoal Q-009 (Rogério Tavares)<br>sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato<br>sql:SIS-01/folhacerta_dump.sql:chk_tipo_contrato | DIV-009, RIS-007 | US-031, US-032 | FT-010 |
| RF-016 | hipótese | v1 | Could | Agendamento pela API da MedTrab | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1 | OPO-003 | — | — |
| RF-017 | hipótese | v1 | Should | Matrícula automática | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1<br>doc:SIS-04/lms-estrutura.md#0 | GAR-006, OPO-004 | — | — |
| RF-018 | hipótese | v1 | Should | Decisão de prorrogação | sql:SIS-01/folhacerta_dump.sql:contrato | RIS-006 | — | — |
| RF-019 | confirmado | v1 | Should | Aceitar CRNM como identificação | doc:geral/M-02-email-juridico-2026-10-30.md#0 | complementa RF-003 | US-034 | FT-005 |
| RF-020 | confirmado | v1 | Should | Controlar validade da CRNM | doc:geral/M-02-email-juridico-2026-10-30.md#0 | complementa RF-019 | US-035 | FT-005 |
| RN-001 | conflito | v2 | Must | Duração da experiência | doc:geral/politica-RH-012-admissao-integracao.md#0<br>doc:geral/manual-admissao-lojas-v3.2-2019.md#1<br>sql:SIS-01/folhacerta_dump.sql:contrato.dias_experiencia<br>entrevista:juridico-compliance Q-004 (Marina Quintela) | DIV-003, conflita com RN-017 | US-015, US-020 | FT-004, FT-006 |
| RN-002 | confirmado | v2 | Must | Validade do ASO | doc:geral/politica-RH-012-admissao-integracao.md#1<br>doc:SIS-03/LEIA-ME.md#0<br>sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato<br>entrevista:juridico-compliance Q-005 (Fábio Arantes e Marina Quintela)<br>entrevista:operacoes Q-015<br>doc:geral/M-02-email-juridico-2026-10-30.md#0 | DIV-004, RIS-001 | US-008, US-009, US-032, US-033 | FT-002, FT-010 |
| RN-003 | confirmado | v2 | Must | CRF para funções farmacêuticas | doc:geral/politica-RH-012-admissao-integracao.md#1<br>doc:SIS-03/LEIA-ME.md#0<br>sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato<br>entrevista:juridico-compliance Q-006 (Beatriz Lobo)<br>doc:geral/M-01-ata-comite-2026-10-28.md#0 | DIV-005, RIS-002 | US-010 | FT-002 |
| RN-004 | conflito | v2 | Must | Validação e alçada da oferta | doc:geral/politica-RH-012-admissao-integracao.md#0<br>sql:SIS-02/recrutamais_dump.sql:oferta.aprovador_perfil<br>sql:SIS-01/folhacerta_dump.sql:cargo_piso<br>entrevista:negocio Q-007 | DIV-006, DIV-007 | — | — |
| RN-005 | confirmado | v2 | Must | Prazo da integração | doc:geral/politica-RH-012-admissao-integracao.md#1<br>doc:geral/manual-admissao-lojas-v3.2-2019.md#1<br>doc:SIS-04/lms-estrutura.md#0<br>entrevista:negocio Q-008 (Beatriz Lobo) | DIV-008 | US-013 | FT-004 |
| RN-006 | confirmado | v2 | Should | Tratamento de aprendiz | doc:geral/politica-RH-012-admissao-integracao.md#0<br>doc:geral/fluxo-admissao-atual.md#0<br>sql:SIS-01/folhacerta_dump.sql:chk_tipo_contrato<br>entrevista:negocio Q-001 (Helena Vasconcelos)<br>entrevista:departamento-pessoal Q-009 (Rogério Tavares) | DIV-009, RIS-007 | US-032 | FT-010 |
| RN-007 | confirmado | v2 | Must | Retenção de candidatos | doc:geral/politica-RH-012-admissao-integracao.md#2<br>sql:SIS-02/recrutamais_dump.sql:sp_expurgo_candidatos<br>entrevista:encarregada-dados Q-012 (Paula Nogueira) | DIV-010 | US-029, US-030 | FT-009 |
| RN-008 | confirmado | v2 | Must | CID restrito ao SESMT | doc:geral/politica-RH-012-admissao-integracao.md#1<br>sql:SIS-01/folhacerta_dump.sql:GRANT rh_loja<br>entrevista:encarregada-dados Q-012 (Paula Nogueira)<br>entrevista:encarregada-dados Q-013 (Paula Nogueira) | DIV-011 | US-012, US-025, US-028 | FT-003, FT-008, FT-009 |
| RN-009 | hipótese | v2 | Must | Lista fechada de condições para início | doc:SIS-03/LEIA-ME.md#1<br>sql:SIS-01/folhacerta_dump.sql:contrato.status<br>doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0<br>doc:geral/politica-RH-012-admissao-integracao.md#1<br>entrevista:departamento-pessoal Q-010 (Rogério Tavares)<br>doc:geral/M-02-email-juridico-2026-10-30.md#0 | DIV-014, RIS-001 | — | — |
| RN-010 | confirmado | v1 | Must | Prazo de documentos | doc:geral/comunicado-dp-07-2024.md#0<br>doc:geral/politica-RH-012-admissao-integracao.md#0<br>doc:SIS-03/LEIA-ME.md#0<br>entrevista:departamento-pessoal Q-011 (Rogério Tavares) | DIV-012 | US-018 | FT-005 |
| RN-011 | confirmado | v1 | Must | Referência de piso | entrevista:negocio Q-007 (Rogério Tavares)<br>sql:SIS-01/folhacerta_dump.sql:cargo_piso | DIV-007 | US-022 | FT-006 |
| RN-012 | confirmado | v1 | Must | Gravidez e antecedentes fora da seleção | entrevista:encarregada-dados Q-012 (Paula Nogueira) | RIS-005 | US-027 | FT-009 |
| RN-013 | confirmado | v1 | Must | Dado de pessoa com deficiência | entrevista:encarregada-dados Q-012 (Paula Nogueira) | RIS-005 | US-028 | FT-009 |
| RN-014 | hipótese | v2 | Must | O que sai do SESMT | doc:geral/politica-RH-012-admissao-integracao.md#1<br>entrevista:departamento-pessoal Q-003 (Rogério Tavares)<br>doc:geral/M-02-email-juridico-2026-10-30.md#0 | DIV-011, DIV-017 | — | — |
| RN-015 | confirmado | v1 | Must | Definição de admissão | entrevista:departamento-pessoal Q-003 (Rogério Tavares)<br>sql:SIS-01/folhacerta_dump.sql:contrato.status | DIV-002 | US-007 | FT-001 |
| RN-016 | confirmado | v1 | Must | Vacinação de quem aplica injetáveis em SP | doc:geral/M-02-email-juridico-2026-10-30.md#0 | complementa RF-012, complementa RN-002 | US-002, US-033 | FT-001, FT-002 |
| RN-017 | conflito | v1 | Must | Experiência de 45+45 a partir de 01/12/2026 (pedido) | doc:geral/M-01-ata-comite-2026-10-28.md#0 | conflita com RN-001 | US-015, US-020 | FT-004, FT-006 |
| RNF-001 | hipótese | v1 | Must | Trilha de auditoria | doc:escopo.md | RIS-013 | — | — |
| RNF-002 | confirmado | v2 | Must | Proteção de dados pessoais | doc:geral/politica-RH-012-admissao-integracao.md#1<br>doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1<br>entrevista:negocio Q-002 (Helena Vasconcelos) | OPO-009, RIS-004, RIS-005 | US-001, US-016, US-024, US-026 | FT-001, FT-005, FT-007, FT-008 |
| RNF-003 | hipótese | v1 | Must | Responsabilização individual | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1 | RIS-003 | — | — |
| RNF-004 | hipótese | v1 | Should | Falha de integração | sem fonte (hipótese de análise) | RIS-014 | — | — |
| RNF-005 | hipótese | v1 | Should | Disponibilidade e desempenho | sem fonte (hipótese de análise) | RIS-014 | — | — |

## 2. História para requisito

| História | Título | Situação | Feature | Épico | Prior. | Requisitos |
|---|---|---|---|---|---|---|
| US-001 | Ver a situação da admissão em um só lugar | proposto | FT-001 | EP-001 | Must | RF-001, RNF-002 |
| US-002 | Saber se o colaborador pode começar | revisar | FT-001 | EP-001 | Must | RF-001, RF-012, RN-016 |
| US-003 | Acompanhar a oferta | proposto | FT-001 | EP-001 | Must | RF-011 |
| US-004 | Acompanhar o contrato | proposto | FT-001 | EP-001 | Must | RF-013 |
| US-005 | Acompanhar S-2190 e S-2200 | proposto | FT-001 | EP-001 | Must | RF-005 |
| US-006 | Acompanhar a solicitação de acesso | proposto | FT-001 | EP-001 | Must | RF-006 |
| US-007 | Contar as etapas sem misturar conceitos | proposto | FT-001 | EP-001 | Should | RF-008, RN-015 |
| US-008 | Bloquear início sem ASO válido | proposto | FT-002 | EP-001 | Must | RF-012, RN-002 |
| US-009 | Revalidar o ASO quando o início é adiado | proposto | FT-002 | EP-001 | Must | RN-002 |
| US-010 | Bloquear farmacêutico sem CRF ativo | proposto | FT-002 | EP-001 | Must | RF-012, RN-003 |
| US-011 | Apontar contrato ativo sem condição atendida | proposto | FT-002 | EP-001 | Must | RF-012, RF-013 |
| US-012 | Registrar as etapas do exame | proposto | FT-003 | EP-001 | Must | RF-004, RN-008 |
| US-013 | Controlar a integração até o 5º dia | proposto | FT-004 | EP-001 | Must | RN-005, RF-007 |
| US-014 | Acompanhar os cursos obrigatórios do cargo | proposto | FT-004 | EP-001 | Must | RF-007 |
| US-015 | Acompanhar o fim da experiência | revisar | FT-004 | EP-001 | Should | RN-001, RF-009, RN-017 |
| US-016 | Entregar documentos em formato digital | proposto | FT-005 | EP-002 | Must | RF-003, RNF-002 |
| US-017 | Conferir e devolver com motivo | proposto | FT-005 | EP-002 | Must | RF-003 |
| US-018 | Sinalizar o prazo de 5 dias úteis | proposto | FT-005 | EP-002 | Must | RN-010 |
| US-019 | Verificar os canais da FolhaCerta e do Recruta+ | proposto | FT-006 | EP-002 | Must | RF-002 |
| US-020 | Levar os dados da oferta à FolhaCerta | revisar | FT-006 | EP-002 | Must | RF-002, RN-001, RN-017 |
| US-021 | Fazer a correspondência de loja, cargo e pessoa | revisar | FT-006 | EP-002 | Must | RF-002 |
| US-022 | Sinalizar oferta abaixo do piso | proposto | FT-006 | EP-002 | Must | RN-011 |
| US-023 | Controlar admissão nova fora da planilha | proposto | FT-007 | EP-003 | Must | RF-014 |
| US-024 | Migrar as admissões em andamento | proposto | FT-007 | EP-003 | Must | RF-014, RNF-002 |
| US-025 | Retirar CID do que está fora do SESMT | proposto | FT-008 | EP-003 | Must | RN-008 |
| US-026 | Aplicar a matriz de acesso | proposto | FT-008 | EP-003 | Must | RNF-002 |
| US-027 | Retirar gravidez e antecedentes da seleção | proposto | FT-009 | EP-003 | Must | RN-012 |
| US-028 | Restringir dado de pessoa com deficiência | proposto | FT-009 | EP-003 | Must | RN-013, RN-008 |
| US-029 | Eliminar candidatos não contratados em 6 meses | proposto | FT-009 | EP-003 | Must | RN-007 |
| US-030 | Eliminar dados em cópias e backups | proposto | FT-009 | EP-003 | Must | RN-007 |
| US-031 | Definir o caminho de registro do aprendiz | proposto | FT-010 | EP-004 | Should | RF-015 |
| US-032 | Conduzir o aprendiz pelo fluxo único | proposto | FT-010 | EP-004 | Should | RF-015, RN-006, RN-002 |
| US-033 | Exigir vacinação de quem aplica injetáveis em SP | proposto | FT-002 | EP-001 | Must | RN-016, RF-012, RN-002 |
| US-034 | Aceitar a CRNM como identificação | proposto | FT-005 | EP-002 | Should | RF-019, RF-003 |
| US-035 | Controlar a validade da CRNM | proposto | FT-005 | EP-002 | Should | RF-020 |

## 3. Achado para tratamento

| Achado | Título | Status | Sev. | Gera | Situação |
|---|---|---|---|---|---|
| DIV-001 | Abrangência: 212 lojas no escopo, 184 próprias na Política e na ata | tratado | alta | Q-001 | Franqueadas fora; CD e escritório fora na primeira fase (Q-001). |
| DIV-002 | Números de setembro: 214, 188 e 176 medem marcos diferentes | aberto | alta | Q-003, RF-008, RN-015, Q-020 | Etapas definidas por RN-015 e RF-008; números fechados e explicação seguem sem resposta. |
| DIV-003 | Experiência: 30+60 na Política, 45+45 na prática | aberto | alta | Q-004, RN-001, Q-021, Q-022, RN-017, Q-035 | Reaberto por CR-001: Marina Quintela confirmou 30+60; Sérgio Antunes comunicou 45+45 a partir de 01/12/2026. Sem decisão registrada. |
| DIV-004 | Validade do ASO: 30, 60 ou 90 dias | tratado | alta | Q-005, RN-002 | Vale 30 dias corridos (Q-005). Trigger da FolhaCerta ainda aceita 90. |
| DIV-005 | CRF: certidão obrigatória na Política, protocolo aceito na planilha, RT sem validação na folha | tratado | critica | Q-006, RN-003 | CRF ativo, sem protocolo, inclusive RT (Q-006). Trigger ainda não cobre FARM_RT. |
| DIV-006 | Aprovação da oferta: BP de RH não existe no fluxo nem no Recruta+ | aberto | alta | Q-007, RN-004, Q-025 | Sem resposta sobre a prática; RN-004 segue em conflito. |
| DIV-007 | Tabela salarial do Recruta+ desatualizada em SP | tratado | alta | Q-007, RN-004, RN-011 | Piso é o da CCT vigente conforme a FolhaCerta (Q-007). Dono da tabela do Recruta+ desconhecido. |
| DIV-008 | Prazo da integração: 5, 15 ou 30 dias | tratado | alta | Q-008, RN-005 | Vale o 5º dia corrido (Q-008). EducaFarma ainda mostra 30 dias. |
| DIV-009 | Aprendiz previsto na Política, bloqueado na FolhaCerta | aberto | alta | Q-009, RN-006, RF-015, Q-027 | Programa legítimo e dentro do novo processo, com prioridade 5; caminho técnico desconhecido. |
| DIV-010 | Retenção de candidatos: 6 meses na Política, 24 no expurgo, sem limite no backup | tratado | critica | Q-012, RN-007 | Vale 6 meses, inclusive cópias e backups (Q-012). Expurgo do Recruta+ ainda não reflete. |
| DIV-011 | Dado de saúde fora do SESMT | aberto | critica | Q-012, Q-013, RN-008, RN-014, Q-031, Q-033 | CID só no SESMT (Q-012). Observação clínica e o que sai do SESMT seguem abertos. |
| DIV-012 | Prazo de documentos: Manual ainda publica 3 dias úteis | tratado | baixa | RN-010 | Prazo vigente é 5 dias úteis (Q-011); só a seção 4 do Manual foi revogada (Q-004). |
| DIV-013 | Identificadores diferentes entre os sistemas | aberto | media | Q-014 | Sem resposta da TI (Q-014). |
| DIV-014 | "Pode começar" não tem definição única | aberto | alta | Q-010, RN-009, RF-012, Q-028 | Só ASO e CRF confirmados como condição; demais seguem abertos. |
| DIV-015 | Momento do chamado de acesso ao PDV | aberto | baixa | Q-015, RF-006, Q-032 | Sem resposta (Q-015). |
| DIV-016 | Lista de documentos só existe no Manual de 2019 | aberto | media | Q-011, Q-029, RF-019 | Sem resposta (Q-011). |
| GAR-001 | Redigitação na FolhaCerta | aberto | alta | Q-011, Q-014, RF-002 | — |
| GAR-002 | Devolução de pastas | aberto | alta | Q-011, RF-003 | — |
| GAR-003 | Agendamento de ASO por e-mail com uma analista | aberto | alta | Q-013, RF-004 | — |
| GAR-004 | Corrida do S-2190 na véspera | aberto | alta | Q-010, RF-005 | — |
| GAR-005 | Cerca de 3 dias sem login no PDV | aberto | alta | Q-014, Q-015, RF-006 | — |
| GAR-006 | Matrícula manual depois do início | aberto | media | Q-008, RF-007 | — |
| GAR-007 | Lote quinzenal de aprendizes | aberto | media | Q-009 | — |
| GAR-008 | Gerente acompanha por vários canais | aberto | alta | Q-015, RF-001 | — |
| RIS-001 | Início antes do ASO | aberto | critica | Q-005, Q-010, RN-002, RN-009, RF-012, Q-028 | Regra sem exceção confirmada; casos da amostra sem explicação. |
| RIS-002 | Farmacêutico RT em atividade sem CRF registrado | aberto | critica | Q-006, RN-003, RF-012, Q-024 | Regra confirmada; providência para o caso em aberto desconhecida. |
| RIS-003 | Login do gerente usado por colaborador novo, inclusive em venda com receita | aberto | critica | Q-015, RNF-003, RF-006, Q-032 | Sem resposta de Operações nem TI; segue crítico. |
| RIS-004 | Planilha com CPF e dados de saúde editável por qualquer pessoa com o link | aberto | critica | Q-012, RNF-002, RF-014, Q-030 | Saída da planilha confirmada como prioridade; contenção imediata sem responsável. |
| RIS-005 | Dados sensíveis e potencial discriminação na seleção | aberto | critica | Q-012, RNF-002, RN-012, RN-013, Q-030 | Regra de coleta confirmada; orientação do Jurídico sobre os casos sem resposta. |
| RIS-006 | Fim de experiência sem controle | aberto | alta | Q-004, RF-009, RF-018, Q-022 | Sem resposta sobre contratos vigentes e prorrogação. |
| RIS-007 | Aprendiz menor de idade fora dos controles | aberto | alta | Q-009 | — |
| RIS-008 | Treinamentos obrigatórios sem acompanhamento | aberto | alta | Q-008, RF-007 | — |
| RIS-009 | Dependência de pessoas | aberto | media | Q-013 | — |
| RIS-010 | Automatizar regra errada e dono indefinido do produto | aberto | alta | Q-002, Q-017, Q-018, Q-019 | Metas, orçamento e dono do produto sem resposta. |
| RIS-011 | Eventos eSocial ausentes na amostra | aberto | media | Q-010, Q-028 | Sem resposta. |
| RIS-012 | Caminhos de exceção não mapeados | aberto | media | Q-003, Q-015 | — |
| RIS-013 | Sem trilha de auditoria | aberto | alta | Q-012, RNF-001 | — |
| APO-001 | FolhaCerta valida piso por cargo, UF e vigência | aberto | media | reaproveitamento | — |
| APO-002 | FolhaCerta gera S-2190 e S-2200 com prazos coerentes | aberto | media | reaproveitamento | — |
| APO-003 | Regras já coerentes entre fontes | aberto | baixa | reaproveitamento | — |
| APO-004 | exige_crf já existe no cadastro de cargos | aberto | baixa | reaproveitamento | — |
| APO-005 | EducaFarma tem API REST e trilhas por cargo | aberto | media | reaproveitamento | — |
| APO-006 | MedTrab oferece portal com API de agendamento | aberto | media | reaproveitamento | — |
| APO-007 | CPF liga Recruta+, FolhaCerta e planilha | aberto | media | reaproveitamento | — |
| APO-008 | Dados coincidem apesar da redigitação | aberto | baixa | reaproveitamento | — |
| APO-009 | Base de processo e norma disponível | aberto | baixa | reaproveitamento | — |
| OPO-001 | Cadastro aproveitado da oferta à folha | aberto | alta | RF-002 | — |
| OPO-002 | Coleta e conferência prévia de documentos | aberto | alta | RF-003 | — |
| OPO-003 | Agendamento de ASO integrado com checagem de validade | aberto | alta | RF-004 | — |
| OPO-004 | Matrícula automática por cargo | aberto | alta | RF-007 | — |
| OPO-005 | Painel único de liberação para o gerente | aberto | alta | RF-001, RN-009 | — |
| OPO-006 | Acesso individual pronto para o primeiro dia | aberto | alta | RF-006, RNF-003 | — |
| OPO-007 | Funil único com marcos definidos | aberto | media | RF-008 | — |
| OPO-008 | Regras parametrizadas com vigência e origem | aberto | media | RF-010 | — |
| OPO-009 | Aposentar a planilha e atender ao inventário de dados | aberto | alta | RNF-002 | — |
| RIS-014 | Viabilidade técnica das prioridades desconhecida | aberto | critica | Q-014, RNF-004, RNF-005 | — |
| RIS-015 | Manual segue em uso com regras superadas | aberto | alta | Q-021 | Agravado pela comunicação de 45+45 à rede sem decisão do Jurídico. |
| RIS-016 | FolhaCerta pode contornar o bloqueio | aberto | alta | Q-014, RF-012 | — |
| RIS-017 | Processo residual fora da primeira fase | aberto | media | Q-016, RF-014 | — |
| DIV-017 | Validação do ASO pelo DP e sigilo da saúde | aberto | media | RN-014, Q-031 | — |
| RIS-018 | Datas externas sem cronograma do projeto | aberto | alta | Q-018, Q-033, Q-034 | — |
| RIS-019 | Dados de migrantes sem chave e sem campo nos sistemas | aberto | media | Q-034, RF-019 | — |

## 4. Mudança para itens afetados

| CR | Título | Classe | Status | Origem | Afetados |
|---|---|---|---|---|---|
| CR-001 | Experiência de 45+45 a partir de 01/12/2026 | conflitante | proposta | doc:geral/M-01-ata-comite-2026-10-28.md#0 | RN-001, RN-017, DIV-003, RF-009, RF-002, US-015, US-020 |
| CR-002 | Comprovante de vacinação para quem aplica injetáveis em SP | novo | aplicada | doc:geral/M-02-email-juridico-2026-10-30.md#0 | RN-016, RF-012, RN-014, RN-009, US-002, US-033 |
| CR-003 | CRNM no programa Acolher | novo | aplicada | doc:geral/M-02-email-juridico-2026-10-30.md#0 | RF-019, RF-020, RF-003, DIV-016, US-021, US-034, US-035 |

## 5. Análise de cobertura

- Requisitos confirmados: 28; alterados depois da baseline: 1; em conflito: 3; hipóteses: 10; validados pelas áreas: 0.
- Confirmados ou alterados sem história: nenhum.
- Histórias sem requisito: nenhuma.
- Histórias ligadas a requisito em conflito, todas em `revisar`: US-015 (RN-001), US-015 (RN-017), US-020 (RN-001), US-020 (RN-017).
- Requisitos sem fonte, todos hipóteses de análise: RNF-004, RNF-005.
- Achados abertos sem requisito, só com pergunta: DIV-013, GAR-007, RIS-007, RIS-009, RIS-010, RIS-011, RIS-012, RIS-015, RIS-018.
- Ter requisito não significa ter solução: RIS-003 depende de RNF-003, que é hipótese; RIS-001 e RIS-002 têm regra, mas a causa e os casos seguem em aberto.
