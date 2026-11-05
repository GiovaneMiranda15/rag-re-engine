# Rastreabilidade — Projeto Admissão Única

Liga requisitos, fontes e backlog. "Resposta N" é a resposta correspondente em `respostas.md`; D-xx, R-xx e Lxxx estão em `01-diagnostico.md`.

## 1. Requisitos → fontes → backlog

### Regras de negócio

| Requisito | Descrição | Fontes | Situação | Decisor | Histórias |
|---|---|---|---|---|---|
| RN-01 | Nas regras já definidas, vale a RH-012. | Resposta 1; RH-012 | Confirmado | Helena | US-001, US-002 |
| RN-02 | Documentos completos no DP até 5 dias úteis antes do início. Efeito do atraso em aberto. | RH-012 §2; Comunicado 07/2024; leia-me | Parcial (PD-14) | DP | US-023 |
| RN-03 | BP de RH valida toda oferta antes de apresentá-la ao candidato. Oferta acima do piso exige também o gerente regional. | RH-012 §3; resposta 9 | Confirmado | Jurídico | US-019, US-020 |
| RN-04 | O gerente de loja indica o candidato, mas não aprova sozinho. | Resposta 9 | Confirmado | Jurídico | US-018 |
| RN-05 | O piso é o da convenção coletiva vigente de cada UF, conforme o FolhaCerta. | Resposta 9; FolhaCerta `cargo_piso` | Confirmado | DP | US-020, US-021 |
| RN-06 | Ninguém começa sem ASO apto. Sem exceção, mesmo com a loja desfalcada; ninguém pode autorizar exceção. | RH-012 §6.1; respostas 5 e 8 | Confirmado | SESMT, Jurídico | US-003, US-010, US-028, US-036, US-064 |
| RN-07 | ASO emitido até 30 dias corridos antes do início. Se o início for adiado e passar disso, o ASO deixa de valer para aquele início. | RH-012 §6.2; resposta 5 | Confirmado | SESMT | US-010, US-028, US-039, US-064 |
| RN-08 | Farmacêutico, inclusive RT, precisa de certidão de regularidade com CRF ativo antes do início. Protocolo não vale. | RH-012 §7; respostas 7 e 8 | Confirmado (detalhes em PD-13) | Beatriz Lobo | US-009, US-029, US-036 |
| RN-09 | Experiência CLT de 30 dias, prorrogável por mais 60, total de 90. | RH-012 §4.1; resposta 4 | Confirmado (transição em PD-06; conflito em PD-25) | Jurídico | US-012, US-033, US-046 |
| RN-10 | Integração e Boas Práticas Farmacêuticas até o 5º dia corrido e antes de atender sozinho no balcão. | RH-012 §9; resposta 15 | Confirmado (comprovação em PD-21) | Beatriz Lobo | US-044, US-045 |
| RN-11 | S-2190 antes do início; S-2200 até o dia 15 do mês seguinte à admissão. | RH-012 §10; FolhaCerta; ata | Confirmado no prazo; bloqueio em PD-14 | DP | US-034, US-035 |
| RN-12 | Admissão oficial: contrato assinado, ASO apto validado e status ATIVO no FolhaCerta. | Resposta 3; comentário de `contrato.status` | Confirmado | DP | US-033 |
| RN-13 | Contratado (oferta aceita), admissão (ATIVO) e Iniciado (primeiro dia) são etapas diferentes e continuam úteis. | Resposta 3; ata; leia-me | Confirmado | DP | US-040, US-054 |
| RN-14 | Gravidez e antecedentes não devem ser perguntados nem guardados na seleção. | Resposta 11 | Confirmado | Encarregada | US-005, US-006, US-011, US-014, US-039 |
| RN-15 | CID só pode existir no ambiente do SESMT. Dados de saúde são acessados exclusivamente pelo SESMT. | RH-012 §11.2; respostas 6 e 11 | Confirmado (alcance em PD-09) | Encarregada | US-005, US-006, US-008, US-027, US-049, US-052, US-061, US-062, US-064 |
| RN-16 | Dado de pessoa com deficiência, só com finalidade clara de cota e acesso restrito. | Resposta 11 | Confirmado | Encarregada | US-006, US-052 |
| RN-17 | Candidatos não contratados: eliminação em até 6 meses, inclusive em cópias e backups. | RH-012 §11.3; resposta 11 | Confirmado | Encarregada | US-007, US-053 |
| RN-18 | Coletar só os dados necessários a cada etapa. | RH-012 §11.1 | Parcial (PD-17) | Encarregada | US-022, US-050 |
| RN-19 | Abrangência: 184 lojas próprias; CLT de loja primeiro; aprendiz depois (prioridade 5); CD e escritório fora da primeira fase; franqueadas fora. | Resposta 2; RH-012 §1 | Confirmado | Helena | US-014, US-058, US-059, US-060 |
| RN-20 | Identificadores: CPF só com dígitos para pessoa; código numérico do FolhaCerta para loja. | Resposta 13 | Confirmado | TI | US-014, US-015, US-031, US-043, US-065 |
| RN-21 | Folha continua no FolhaCerta; rescisão e desligamento ficam fora. | Escopo; ata; resposta 4 | Confirmado | Helena | US-031, US-032, US-047 |
| RN-22 | A partir de 01/02/2027, quem vai aplicar injetáveis em lojas de SP apresenta, junto com o ASO, comprovante de vacinação contra hepatite B e tétano antes do início das atividades. ASO e prazos atuais continuam valendo. | M-02 (Portaria CVS-SP 88/2026, conforme Marina; texto não conferido) | Parcial (PD-27) | Jurídico; execução SESMT | US-061, US-062, US-063, US-064 |
| RN-23 | A partir do 1º trimestre de 2027, nas admissões do programa Acolher, aceitar a CRNM como documento de identificação e controlar sua validade. | M-02 | Parcial (PD-28) | Jurídico; escopo com Helena | US-065, US-066, US-067 |

### Requisitos funcionais

| Requisito | Descrição | Fontes | Situação | Decisor | Histórias |
|---|---|---|---|---|---|
| RF-01 | Fluxo único por caso, do candidato aprovado ao fim da experiência, com situação de cada etapa. | Escopo; resposta 1 | Confirmado | Helena | US-014, US-016, US-058 |
| RF-02 | Validação da oferta: indicação do gerente, BP e regional quando acima do piso, com registro de responsável e data. | RH-012 §3; resposta 9; Recruta+ | Parcial (PD-15) | Jurídico, RH | US-018, US-019, US-020 |
| RF-03 | Verificar o piso vigente no momento da oferta, não só no FolhaCerta ao final. | Resposta 9; D-10; L433 | Derivado | DP | US-021 |
| RF-04 | Coleta e conferência de documentos por cargo, sem e-mail. | Escopo; ata; Manual §4 | Parcial (PD-18) | DP | US-022, US-066 |
| RF-05 | Acompanhar o prazo de documentos e registrar motivo de devolução. | RH-012 §2; ata | Derivado | DP | US-023, US-024 |
| RF-06 | Pedir e acompanhar o exame admissional. | Escopo; ata; fluxo | Parcial (PD-10) | SESMT | US-025, US-026 |
| RF-07 | Registrar a condição do ASO, sem dado clínico, e calcular a validade para a data de início. | RH-012 §6; respostas 5, 6 e 11 | Parcial (PD-09) | SESMT, Encarregada | US-027, US-028 |
| RF-08 | Conferir a certidão de CRF de farmacêutico e RT; protocolo não satisfaz. | RH-012 §7; resposta 7 | Parcial (PD-13) | Beatriz Lobo | US-029 |
| RF-09 | Integrar Recruta+ → FolhaCerta para o DP não redigitar. | Escopo; respostas 1 e 13; ata | Parcial (PD-19) | Helena, TI | US-014, US-015, US-030, US-031 |
| RF-10 | Acompanhar o contrato, sua assinatura e o tipo de experiência 30+60. | Escopo; respostas 3 e 4 | Parcial (PD-18) | DP | US-033 |
| RF-11 | Acompanhar S-2190 e S-2200, prazos e recibos. O FolhaCerta continua gerando os eventos. | Escopo; RH-012 §10; ata | Parcial (PD-19) | DP | US-034, US-035 |
| RF-12 | Mostrar ao gerente, em um só lugar, se e quando o colaborador pode começar. | Escopo; respostas 5, 7 e 8 | Parcial (PD-14) | A definir (PD-14) | US-036, US-037, US-038, US-039, US-040, US-064 |
| RF-13 | Solicitar e acompanhar acessos antes do início. | Escopo; ata; D-11 | Parcial (PD-20) | Operações, TI | US-013, US-041, US-042 |
| RF-14 | Matricular em treinamentos obrigatórios por cargo e acompanhar prazos, incluindo o 5º dia. | Escopo; RH-012 §9; resposta 15; ata | Parcial (PD-21) | Beatriz Lobo | US-043, US-044, US-045 |
| RF-15 | Acompanhar marcos da experiência e encaminhar a decisão de continuidade, sem tratar desligamento. | Escopo; respostas 4 e 15 | Parcial (PD-06, PD-07) | Jurídico, Helena | US-046, US-047, US-048 |
| RF-16 | Mostrar funil com as três etapas e indicadores por definição única. | Resposta 3; ata | Parcial (PD-05) | Helena | US-054, US-055 |
| RF-17 | Tirar a planilha de uso. | Resposta 1; leia-me | Confirmado | Helena | US-056, US-057 |
| RF-18 | Manter catálogo versionado de regras, com fonte, vigência e decisor; substituir o Manual. | Respostas 1 e 2; seção 3 do diagnóstico | Derivado | Helena, decisores | US-001, US-002, US-003, US-037, US-057 |
| RF-19 | Avisar responsáveis sobre tarefas e prazos no lugar do e-mail. | Escopo; fluxo | Derivado | Operações | US-017, US-067 |
| RF-20 | Incluir aprendizes no fluxo único, em etapa posterior. | Resposta 2; ata; D-07 | Parcial (PD-16) | Helena, DP | US-059, US-060 |
| RF-21 | Conter exposição de dados nos sistemas atuais, sem esperar o novo fluxo. | Resposta 11; R-03, R-04, R-06, R-07 | Parcial (PD-11) | Encarregada | US-004, US-005, US-006, US-007, US-008 |
| RF-22 | Tratar os casos já ocorridos fora da regra. | Respostas 4, 5, 7 e 11; seção 4 do diagnóstico | Parcial (PD-06, PD-08, PD-12, PD-13) | Jurídico, SESMT, Beatriz Lobo | US-009, US-010, US-011, US-012, US-013 |
| RF-23 | Identificar quem é abrangido pela portaria e controlar o comprovante de vacinação como condição de início, com o comprovante no ambiente do SESMT. | M-02; RN-15 | Parcial (PD-09, PD-27) | SESMT, Jurídico, Encarregada | US-062, US-063, US-064 |
| RF-24 | Aceitar a CRNM na coleta de documentos e acompanhar sua validade. | M-02 | Parcial (PD-19, PD-28) | DP, Jurídico | US-065, US-066, US-067 |

### Requisitos não funcionais

| Requisito | Descrição | Fontes | Situação | Decisor | Histórias |
|---|---|---|---|---|---|
| RNF-01 | Acesso por papel e loja ou regional. | RH-012 §11; resposta 11; dumps | Confirmado no princípio | Encarregada | US-004, US-008, US-027, US-036, US-049, US-066 |
| RNF-02 | Trilha de auditoria. | Escopo (segurança do Jurídico); R-04 | Derivado | Jurídico | US-038, US-042, US-051 |
| RNF-03 | Retenção e eliminação comprovada. | RH-012 §11.3; resposta 11 | Parcial (PD-17) | Encarregada | US-007, US-053 |
| RNF-04 | Coleta mínima, sem campos proibidos e sem texto livre não controlado. | RH-012 §11.1; resposta 11; leia-me | Parcial (PD-17) | Encarregada | US-016, US-017, US-022, US-048, US-050, US-056 |
| RNF-05 | Integrações resilientes e conciliação. | Respostas 1 e 13 | Derivado | TI | US-030, US-031, US-032 |
| RNF-06 | Volume e calendário: 190 admissões por mês, 184 lojas, MG e SP. | Ata; RH-012 §1 | Derivado | TI | US-023, US-031, US-058 |
| RNF-07 | Sustentação compatível com TI em papel de apoio. | Escopo; resposta 13 | Derivado | TI, Helena | US-030 |

## 2. Achados do diagnóstico → requisitos

| Achado | Requisitos | Situação |
|---|---|---|
| D-01 Validade do ASO | RN-07, RF-07 | Decidido: 30 dias |
| D-02 ASO antes do início | RN-06, RF-07, RF-22 | Decidido; casos em PD-08 |
| D-03 Experiência | RN-09, RF-15, RF-22 | Decidido: 30+60; transição em PD-06 |
| D-04 CRF | RN-08, RF-08, RF-22 | Decidido; complementos em PD-13 |
| D-05 Aprovação da oferta | RN-03, RN-04, RF-02 | Decidido; operação em PD-15 |
| D-06 Integração | RN-10, RF-14 | Decidido: 5º dia; comprovação em PD-21 |
| D-07 Aprendiz | RF-20, RN-19 | Depois (prioridade 5); PD-16 |
| D-08 Retenção | RN-17, RF-21, RNF-03 | Decidido: 6 meses |
| D-09 Dado de saúde | RN-15, RF-07, RF-21, RNF-01 | Decidido para CID; alcance em PD-09 |
| D-10 Tabela salarial | RN-05, RF-03 | Referência decidida; dono em PD-15 |
| D-11 Chamado de acesso | RF-13 | Aberto: PD-20 |
| D-12 Prazo de documentos | RN-02, RF-05 | Regra clara; efeito em PD-14 |
| Números de setembro (3.3) | RN-12, RN-13, RF-16 | Conceito decidido; números em PD-05 |
| Abrangência (3.4) | RN-19 | Decidida, exceto estágio (PD-22) |
| Dados mestres (3.5) | RN-20, RF-09 | Identificadores decididos; lacunas no doc. técnico |
| G-01 Digitação | RF-09 | Depende de PD-19 |
| G-02 Devolução | RF-04, RF-05 | Depende de PD-18 |
| G-03 Exame | RF-06 | Depende de PD-10 |
| G-04 Acesso ao PDV | RF-13 | Depende de PD-20 |
| G-05 Corrida pelo S-2190 | RF-11, RF-05 | Depende de PD-14 |
| G-06 Lote de aprendiz | RF-20 | Depende de PD-16 |
| G-07 Matrícula tardia | RF-14 | Depende de PD-19, PD-21 |
| G-08 Conciliação manual | RF-01, RNF-05 | Depende de PD-19 |
| R-01 | RN-06, RF-07, RF-12 | Regra decidida |
| R-02 | RN-08, RF-08, RF-22 | Regra decidida |
| R-03 | RN-14, RF-21, RF-22 | Regra decidida; caso em PD-12 |
| R-04 | RF-21, RF-17, RNF-01 | Autorização em PD-11 |
| R-05 | RF-13, RF-22 | Aberto: PD-20 |
| R-06 | RN-15, RF-21, RNF-01 | Regra decidida; execução em PD-11, PD-19 |
| R-07 | RN-17, RF-21, RNF-03 | Regra decidida |
| R-08 | RN-09, RF-15, RF-22 | Regra decidida; transição em PD-06 |
| R-09 | RN-03, RN-05, RF-02, RF-03 | Regra decidida |
| R-10 | RF-20 | Depois; PD-16 |
| R-11 | RN-10, RF-14 | Comprovação em PD-21 |
| R-12 | RF-18 | Aviso provisório a decidir |
| R-13 | RF-18 | Regras principais decididas |
| R-14 | RF-18 | Árbitro em aberto: PD-01 |
| R-15 | RF-16 | Metas em PD-05 |
| R-16 | RF-09, RNF-05 | Aberto: PD-19 |
| R-17 | RF-18 | Aviso provisório a decidir (US-002) |
| R-18 | RN-12, RF-10, RF-12 | Compensação no fluxo; correção em PD-19 |
| R-19 | RF-21 | Aberto: PD-11 |
| R-20 | RN-09 | Aberto: PD-25 |
| R-21 | RF-23, RF-24 | Controle provisório: US-062, US-065 |
| R-22 | RN-15, RF-23 | Aberto: PD-27 |
| R-23 | RF-24, RN-20 | Aberto: PD-19, PD-28 |

## 3. Backlog → requisitos

| Épico | Feature | História | Prioridade | Requisitos | Pendências |
|---|---|---|---|---|---|
| E-01 | F-01 | US-001 Definir arbitragem e fechar decisões | 1 | RF-18, RN-01 | PD-01, PD-03, PD-23 |
| E-01 | F-01 | US-002 Publicar catálogo vigente de regras | 1 | RF-18, RN-01 | PD-23 |
| E-01 | F-02 | US-003 Parametrizar regras com vigência | 2 | RF-18, RN-06 | — |
| E-02 | F-03 | US-004 Fechar o link aberto da planilha | 1 | RF-21, RNF-01 | PD-11 |
| E-02 | F-03 | US-005 Retirar dados sensíveis da planilha | 1 | RF-21, RN-14, RN-15 | PD-11, PD-12 |
| E-02 | F-03 | US-006 Parar a coleta de gestação e antecedentes no Recruta+ | 1 | RF-21, RN-14, RN-15, RN-16 | PD-11, PD-19 |
| E-02 | F-03 | US-007 Aplicar retenção de 6 meses no Recruta+ | 1 | RF-21, RN-17, RNF-03 | PD-11, PD-19 |
| E-02 | F-03 | US-008 Retirar CID e observação clínica do FolhaCerta | 1 | RF-21, RN-15, RNF-01 | PD-09, PD-11, PD-19 |
| E-02 | F-04 | US-009 Regularizar farmacêuticos sem CRF ativo | 1 | RF-22, RN-08 | PD-13 |
| E-02 | F-04 | US-010 Analisar casos de ASO fora da regra | 1 | RF-22, RN-06, RN-07 | PD-08, PD-18 |
| E-02 | F-04 | US-011 Analisar o registro de reavaliação após menção a gravidez | 1 | RF-22, RN-14 | PD-12 |
| E-02 | F-04 | US-012 Definir transição dos contratos de experiência | 1 | RF-22, RN-09 | PD-06, PD-25 |
| E-02 | F-04 | US-013 Eliminar o uso de login do gerente no PDV | 1 | RF-22, RF-13 | PD-20 |
| E-03 | F-05 | US-014 Abrir caso a partir do candidato aprovado | 2 | RF-01, RF-09, RN-19, RN-20, RN-14 | PD-02, PD-19 |
| E-03 | F-05 | US-015 Criar tabelas de equivalência | 2 | RN-20, RF-09 | PD-15, PD-19 |
| E-03 | F-05 | US-016 Ver a situação do caso por etapa | 2 | RF-01, RNF-04 | — |
| E-03 | F-05 | US-017 Receber avisos de tarefas e prazos | 3 | RF-19, RNF-04 | — |
| E-03 | F-06 | US-018 Indicar candidato e propor oferta | 2 | RF-02, RN-04 | PD-15, PD-19 |
| E-03 | F-06 | US-019 Validar oferta pelo BP de RH | 2 | RF-02, RN-03 | PD-15 |
| E-03 | F-06 | US-020 Exigir regional acima do piso | 2 | RF-02, RN-03, RN-05 | PD-15 |
| E-03 | F-06 | US-021 Barrar oferta abaixo do piso na origem | 2 | RF-03, RN-05 | PD-15, PD-19 |
| E-04 | F-07 | US-022 Coletar documentos por cargo | 2 | RF-04, RN-18, RNF-04 | PD-17, PD-18 |
| E-04 | F-07 | US-023 Acompanhar o prazo de 5 dias úteis | 2 | RF-05, RN-02, RNF-06 | PD-14, PD-18 |
| E-04 | F-07 | US-024 Devolver documento com motivo | 3 | RF-05 | PD-18 |
| E-05 | F-08 | US-025 Pedir e acompanhar o exame | 2 | RF-06 | PD-10 |
| E-05 | F-08 | US-026 Avaliar o uso do portal da MedTrab | 3 | RF-06 | PD-10, PD-19 |
| E-05 | F-08 | US-027 Registrar a condição do ASO sem dado clínico | 1 | RF-07, RN-15, RNF-01 | PD-09 |
| E-05 | F-08 | US-028 Calcular a validade do ASO | 1 | RF-07, RN-06, RN-07 | — |
| E-05 | F-09 | US-029 Conferir a certidão de CRF | 1 | RF-08, RN-08 | PD-13 |
| E-06 | F-10 | US-030 Avaliar as integrações | 1 | RF-09, RNF-05, RNF-07 | PD-02, PD-19 |
| E-06 | F-10 | US-031 Levar os dados ao FolhaCerta sem redigitar | 2 | RF-09, RN-20, RN-21, RNF-05, RNF-06 | PD-18, PD-19 |
| E-06 | F-10 | US-032 Conciliar os sistemas | 3 | RNF-05, RN-21 | PD-19 |
| E-06 | F-11 | US-033 Acompanhar contrato e assinatura | 2 | RF-10, RN-12, RN-09 | PD-18, PD-19 |
| E-06 | F-11 | US-034 Acompanhar o S-2190 | 1 | RF-11, RN-11 | PD-14, PD-18, PD-19 |
| E-06 | F-11 | US-035 Acompanhar o S-2200 | 2 | RF-11, RN-11 | PD-18, PD-19 |
| E-07 | F-12 | US-036 Ver em um só lugar quem pode começar | 1 | RF-12, RN-06, RN-08, RNF-01 | PD-14 |
| E-07 | F-12 | US-037 Definir e configurar as condições de início | 1 | RF-12, RF-18 | PD-14 |
| E-07 | F-12 | US-038 Registrar a liberação final | 1 | RF-12, RNF-02 | PD-14 |
| E-07 | F-12 | US-039 Reavaliar ao mudar a data de início | 2 | RF-12, RN-07, RN-14 | — |
| E-07 | F-12 | US-040 Marcar o início | 2 | RF-12, RN-13 | PD-14 |
| E-08 | F-13 | US-041 Solicitar acessos antes do início | 2 | RF-13 | PD-20 |
| E-08 | F-13 | US-042 Acompanhar a situação do acesso | 3 | RF-13, RNF-02 | PD-19, PD-20 |
| E-09 | F-14 | US-043 Matricular nas trilhas obrigatórias por cargo | 2 | RF-14, RN-20 | PD-19, PD-21 |
| E-09 | F-14 | US-044 Acompanhar o prazo de integração | 2 | RF-14, RN-10 | PD-19, PD-21 |
| E-09 | F-14 | US-045 Controlar atendimento sozinho no balcão | 2 | RF-14, RN-10 | PD-21 |
| E-10 | F-15 | US-046 Calcular marcos de experiência | 2 | RF-15, RN-09 | PD-06, PD-25 |
| E-10 | F-15 | US-047 Encaminhar a decisão de continuidade | 2 | RF-15, RN-21 | PD-06, PD-07, PD-19 |
| E-10 | F-15 | US-048 Registrar conversas de 30 e 60 dias | 4 | RF-15, RNF-04 | PD-21 |
| E-11 | F-16 | US-049 Aplicar perfis por papel e loja | 1 | RNF-01, RN-15 | PD-09, PD-17 |
| E-11 | F-16 | US-050 Completar o inventário de dados por etapa | 1 | RN-18, RNF-04 | PD-17 |
| E-11 | F-16 | US-051 Registrar trilha de auditoria | 1 | RNF-02 | — |
| E-11 | F-16 | US-052 Restringir dado de deficiência à finalidade de cota | 2 | RN-16, RN-15 | PD-17 |
| E-11 | F-16 | US-053 Aplicar retenção no fluxo único | 2 | RNF-03, RN-17 | PD-17 |
| E-12 | F-17 | US-054 Mostrar funil de três etapas | 3 | RF-16, RN-13 | PD-05 |
| E-12 | F-17 | US-055 Medir linha de base e definir metas | 2 | RF-16 | PD-05 |
| E-12 | F-18 | US-056 Desativar a planilha | 3 | RF-17, RNF-04 | PD-11, PD-17 |
| E-12 | F-18 | US-057 Publicar o novo Manual | 3 | RF-18, RF-17 | — |
| E-12 | F-18 | US-058 Executar piloto com lojas de MG e SP | 3 | RF-01, RN-19, RNF-06 | PD-03, PD-05 |
| E-13 | F-19 | US-059 Levantar o processo de aprendizes | 5 | RF-20, RN-19 | PD-16, PD-17 |
| E-13 | F-19 | US-060 Incluir aprendizes no fluxo único | 5 | RF-20, RN-19 | PD-16 |
| E-05 | F-20 | US-061 Confirmar o alcance da Portaria CVS-SP 88/2026 | 1 | RN-22, RN-15 | PD-27 |
| E-05 | F-20 | US-062 Aplicar controle provisório a partir de 01/02/2027 | 1 | RF-23, RN-22, RN-15 | PD-27 |
| E-05 | F-20 | US-063 Indicar no caso quem vai aplicar injetáveis | 2 | RF-23, RN-22 | PD-27 |
| E-05 | F-20 | US-064 Exigir comprovante de vacinação para iniciar | 2 | RF-23, RF-12, RN-22, RN-06, RN-07, RN-15 | PD-09, PD-27 |
| E-04 | F-21 | US-065 Definir as regras do programa Acolher | 1 | RN-23, RF-24, RN-20 | PD-28 |
| E-04 | F-21 | US-066 Aceitar a CRNM como documento de identificação | 2 | RF-24, RF-04, RN-23, RNF-01 | PD-19, PD-28 |
| E-04 | F-21 | US-067 Controlar a validade da CRNM | 2 | RF-24, RF-19, RN-23 | PD-28 |

## 4. Pendências → histórias

| Pendência | Histórias afetadas |
|---|---|
| PD-01 Quem arbitra discordância entre áreas | US-001 |
| PD-02 Recruta+ e EducaFarma serão substituídos? | US-014, US-030 |
| PD-03 Data-limite e orçamento | US-001, US-058 |
| PD-04 Encerrada: a ata de 28/10 registra só informes | — |
| PD-05 Números fechados, decomposição das diferenças, metas | US-054, US-055, US-058 |
| PD-06 Contratos em curso de 45+45; como a prorrogação é registrada; C9140 e C9177; contagem dos dias | US-012, US-046, US-047 |
| PD-07 Ponto exato em que o projeto termina; antecedência do aviso ao DP | US-047 |
| PD-08 Tratamento de L438, L415 e L426 | US-010 |
| PD-09 O que chega a DP e gerente sobre o ASO; onde fica o ambiente do SESMT; origem de CID no FolhaCerta; inapto e restrição | US-008, US-027, US-049, US-064 |
| PD-10 Cobertura e contrato da MedTrab; substituta da analista do SESMT | US-025, US-026 |
| PD-11 Quem autoriza as contenções imediatas, e quando | US-004, US-005, US-006, US-007, US-008, US-056 |
| PD-12 Registro de "reavaliar início" de candidata após menção a gravidez | US-005, US-011 |
| PD-13 Quantos farmacêuticos estão em protocolo; origem da regra da planilha; o que conferir além do número; vaga de RT aberta | US-009, US-029 |
| PD-14 Quais condições bloqueiam; por modalidade; quem dá a liberação final | US-023, US-034, US-036, US-037, US-038, US-040 |
| PD-15 BP hoje valida fora do Recruta+? Quem são os BPs, prazo; dono da tabela salarial e da lista de regionais | US-015, US-018, US-019, US-020, US-021 |
| PD-16 Aprendiz: toda a pergunta 10 sem resposta (motivo da Contábil Alfa, eSocial, folha, regras de menores) | US-059, US-060 |
| PD-17 Dados por etapa, finalidade, base legal; retenção de contratados; contratos de operador | US-022, US-049, US-050, US-052, US-053, US-056, US-059 |
| PD-18 Toda a pergunta 12 sem resposta: lista de documentos, causas de devolução, assinatura do contrato, anomalia de C9240, eventos ausentes, calendário | US-010, US-022, US-023, US-024, US-031, US-033, US-034, US-035 |
| PD-19 APIs e integrações; criação sem digitação; recibo; correções no FolhaCerta; permissões de produção; sustentação | US-006, US-007, US-008, US-014, US-015, US-018, US-021, US-026, US-030, US-031, US-032, US-033, US-034, US-035, US-042, US-043, US-044, US-047, US-066 |
| PD-20 Toda a pergunta 14 sem resposta: acessos por cargo, causa dos 3 dias, substituto do login do gerente | US-013, US-041, US-042 |
| PD-21 Viabilidade do 5º dia; comprovação e responsável; atribuição de trilhas; trilhas de RT; conversas de 30 e 60 dias | US-043, US-044, US-045, US-048 |
| PD-22 Estágio; papel do gerente em CD e escritório | Sem história específica |
| PD-23 Ordem completa de autoridade, com Comunicado e planilha | US-001, US-002 |
| PD-24 Vigência do Acordo Coletivo de 2024 (carência) | Sem história específica |
| PD-25 Conflito 30+60 x 45+45 (M-01) | US-012, US-046 |
| PD-26 Resposta ao pedido de rescisão e homologação | Sem história: fora do escopo |
| PD-27 Alcance da Portaria CVS-SP 88/2026 | US-061, US-062, US-063, US-064 |
| PD-28 Regras do programa Acolher | US-065, US-066, US-067 |

## 5. Comunicações → requisitos

Avaliação completa em `08-mudancas.md`.

| Afirmação | Classificação | Requisitos | Histórias | Aplicada? |
|---|---|---|---|---|
| M-01.1 CRF | existente | RN-08 | US-009, US-029 | Sem mudança de regra |
| M-01.2 Experiência 45+45 | conflitante | RN-09, RF-15, RF-22 | US-012, US-046 | Não; PD-25 |
| M-01.3 Rescisão e homologação | fora_escopo | RN-21 | — | Não; PD-26 |
| M-02.1 Vacinação para injetáveis em SP | novo | RN-22, RF-23 | US-061 a US-064 | Sim, parcial |
| M-02.2 ASO e prazos continuam | existente | RN-06, RN-07 | US-028, US-064 | Sem mudança de regra |
| M-02.3 Adesão ao programa Acolher | novo | RN-23 | US-065 | Sim, parcial |
| M-02.4 Aceitar CRNM e controlar validade | complementar | RN-23, RF-24, RF-04 | US-066, US-067 | Sim, parcial |
