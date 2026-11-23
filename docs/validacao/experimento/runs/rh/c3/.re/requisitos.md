# Requisitos

> Gerado por `recop.py render` a partir de `.re/modelo/requisitos.json`. Não edite à mão.

## Requisitos funcionais

### RF-001 — Painel do gerente (v2)

- **Enunciado:** O sistema deve mostrar ao gerente, em um só lugar, a situação de cada etapa da admissão e se o colaborador pode começar.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:escopo.md, entrevista:negocio Q-002 (Helena Vasconcelos)
- **Perfis:** operacoes
- **deriva de:** GAR-008, OPO-005
- **Critérios de aceite:**
  - Dado um gerente de loja, quando consulta uma admissão, então vê oferta, documentos, exame, contrato, eSocial, acessos e treinamentos na mesma tela.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  respostas da Etapa 1

### RF-002 — Reaproveitamento de dados (v2)

- **Enunciado:** O sistema deve levar os dados da oferta aceita do Recruta+ à FolhaCerta, sem redigitação pelo DP.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:escopo.md, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0, entrevista:negocio Q-002 (Helena Vasconcelos)
- **Perfis:** departamento-pessoal
- **deriva de:** GAR-001, OPO-001
- **Critérios de aceite:**
  - Dado oferta aceita, quando os dados chegam à FolhaCerta, então o DP não digita novamente nenhum campo que já exista na oferta.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  necessidade confirmada; canal técnico desconhecido (Q-014)

### RF-003 — Coleta de documentos (v2)

- **Enunciado:** O sistema deve receber os documentos de admissão em formato digital e registrar entrega, conferência e pendência de cada um, com data.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:escopo.md, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0, entrevista:negocio Q-002 (Helena Vasconcelos)
- **Perfis:** departamento-pessoal
- **deriva de:** GAR-002, OPO-002
- **Critérios de aceite:**
  - Dado documento ilegível, quando o DP o devolve, então o motivo e a data ficam registrados.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  respostas da Etapa 1

### RF-004 — Acompanhamento do ASO (v2)

- **Enunciado:** O sistema deve registrar pedido, agendamento e emissão do exame admissional, sem expor dado clínico fora do SESMT.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:escopo.md, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1
- **Perfis:** sesmt
- **deriva de:** GAR-003, OPO-003
- **Critérios de aceite:**
  - Dado exame pedido, então a etapa mostra as datas de pedido, agendamento e emissão.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  respostas da Etapa 1

### RF-005 — Acompanhamento do eSocial (v1)

- **Enunciado:** O sistema deve exibir situação e prazo de S-2190 e S-2200 gerados na FolhaCerta.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:escopo.md, sql:SIS-01/folhacerta_dump.sql:fn_gera_esocial
- **Perfis:** departamento-pessoal
- **deriva de:** GAR-004
- **Critérios de aceite:**
  - Dado evento sem envio, então a admissão mostra o prazo e a situação pendente.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v1 2026-11-03  respostas da Etapa 1 (reforço de fonte ou status)

### RF-006 — Solicitação de acessos (v2)

- **Enunciado:** O sistema deve acompanhar a solicitação de acesso de cada novo colaborador.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:escopo.md, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1
- **Perfis:** operacoes, software-architect
- **deriva de:** GAR-005, RIS-003, OPO-006, DIV-015
- **Critérios de aceite:**
  - Dado colaborador com data de início, então a admissão mostra se o acesso foi solicitado e concluído.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  acompanhamento confirmado pelo escopo; solução para o login compartilhado segue em RNF-003

### RF-007 — Treinamentos obrigatórios (v1)

- **Enunciado:** O sistema deve acompanhar matrícula e conclusão de todos os cursos obrigatórios do cargo.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:escopo.md, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1, doc:SIS-04/lms-estrutura.md#0
- **Perfis:** operacoes
- **deriva de:** GAR-006, RIS-008, OPO-004
- **Critérios de aceite:**
  - Dado cargo com cursos obrigatórios no EducaFarma, então cada curso aparece com prazo e situação.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v1 2026-11-03  respostas da Etapa 1 (reforço de fonte ou status)

### RF-008 — Etapas da admissão (v2)

- **Enunciado:** O sistema deve registrar separadamente as etapas de oferta aceita, admissão efetivada e primeiro dia.
- **Prioridade:** Should
- **Status:** confirmado
- **Fontes:** doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0, entrevista:departamento-pessoal Q-003 (Rogério Tavares)
- **Perfis:** negocio
- **deriva de:** DIV-002, OPO-007
- **Critérios de aceite:**
  - Dada uma admissão, então as três datas são registradas e contadas de forma independente.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  respostas da Etapa 1

### RF-009 — Acompanhamento até o fim da experiência (v2)

- **Enunciado:** O sistema deve acompanhar cada admissão até o fim do período de experiência, sem tratar rescisão nem desligamento.
- **Prioridade:** Should
- **Status:** confirmado
- **Fontes:** doc:escopo.md, sql:SIS-01/folhacerta_dump.sql:contrato, entrevista:juridico-compliance Q-004 (Marina Quintela)
- **Perfis:** departamento-pessoal
- **deriva de:** RIS-006
- **Critérios de aceite:**
  - Dada a não continuidade, então o sistema não executa rescisão nem desligamento.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  respostas da Etapa 1

### RF-010 — Parâmetros de regra (v1)

- **Enunciado:** O sistema deve manter prazos e alçadas como parâmetros com vigência, origem e responsável.
- **Prioridade:** Should
- **Status:** hipótese
- **Fontes:** sql:SIS-01/folhacerta_dump.sql:cargo_piso
- **Perfis:** juridico-compliance
- **deriva de:** OPO-008
- **Histórico:** v1 2026-11-03  criado (diagnóstico)

### RF-011 — Acompanhamento da oferta (v1)

- **Enunciado:** O sistema deve exibir a situação da oferta do candidato aprovado.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:escopo.md
- **Perfis:** operacoes
- **deriva de:** GAR-008
- **Critérios de aceite:**
  - Dada oferta aceita no Recruta+, então a admissão aparece no fluxo com essa situação.
- **Histórico:** v1 2026-11-03  criado (respostas da Etapa 1)

### RF-012 — Bloqueio de início (v2)

- **Enunciado:** O sistema deve impedir a liberação de início sem ASO válido, em função farmacêutica sem CRF ativo e, quando aplicável, sem o comprovante de vacinação da RN-016.
- **Prioridade:** Must
- **Status:** alterado
- **Fontes:** entrevista:negocio Q-002 (Helena Vasconcelos), entrevista:juridico-compliance Q-005 (Fábio Arantes e Marina Quintela), entrevista:juridico-compliance Q-006 (Beatriz Lobo), doc:geral/M-02-email-juridico-2026-10-30.md#0
- **Perfis:** negocio, juridico-compliance
- **deriva de:** RIS-001, RIS-002, DIV-014
- **depende de:** RN-016
- **Critérios de aceite:**
  - Dado ASO inválido, quando alguém tenta liberar, então a liberação é recusada, sem opção de exceção.
- **Histórico:** v1 2026-11-03  criado (respostas da Etapa 1); v2 2026-11-04 CR-002 nova condição de início

### RF-013 — Acompanhamento do contrato (v1)

- **Enunciado:** O sistema deve exibir a situação do contrato na admissão.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:escopo.md, sql:SIS-01/folhacerta_dump.sql:contrato.status
- **Perfis:** departamento-pessoal
- **deriva de:** DIV-014
- **Critérios de aceite:**
  - Dado contrato PRE ou ATIVO na FolhaCerta, então a admissão mostra essa situação.
- **Histórico:** v1 2026-11-03  criado (respostas da Etapa 1)

### RF-014 — Saída da planilha (v1)

- **Enunciado:** O sistema deve substituir a planilha de controle nas admissões de CLT de loja.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** entrevista:negocio Q-002 (Helena Vasconcelos)
- **Perfis:** negocio, operacoes
- **deriva de:** RIS-004, OPO-009
- **Critérios de aceite:**
  - Dada admissão CLT de loja nova, então ela é controlada no sistema, sem linha na planilha.
- **Histórico:** v1 2026-11-03  criado (respostas da Etapa 1)

### RF-015 — Aprendiz com caminho próprio de registro (v1)

- **Enunciado:** O sistema deve conduzir aprendizes pelo fluxo único mesmo que a FolhaCerta não os aceite hoje.
- **Prioridade:** Should
- **Status:** confirmado
- **Fontes:** entrevista:departamento-pessoal Q-009 (Rogério Tavares), sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato, sql:SIS-01/folhacerta_dump.sql:chk_tipo_contrato
- **Perfis:** departamento-pessoal
- **deriva de:** DIV-009, RIS-007
- **Critérios de aceite:**
  - Dado aprendiz, então as condições de início são acompanhadas no fluxo único, qualquer que seja o caminho de registro.
- **Histórico:** v1 2026-11-03  criado (respostas da Etapa 1)

### RF-016 — Agendamento pela API da MedTrab (v1)

- **Enunciado:** O sistema deve agendar exames pela API da MedTrab.
- **Prioridade:** Could
- **Status:** hipótese
- **Fontes:** doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1
- **Perfis:** sesmt
- **deriva de:** OPO-003
- **Histórico:** v1 2026-11-03  criado (respostas da Etapa 1)

### RF-017 — Matrícula automática (v1)

- **Enunciado:** O sistema deve matricular automaticamente no EducaFarma, por cargo, antes do início ou no início.
- **Prioridade:** Should
- **Status:** hipótese
- **Fontes:** doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1, doc:SIS-04/lms-estrutura.md#0
- **Perfis:** operacoes
- **deriva de:** OPO-004, GAR-006
- **Histórico:** v1 2026-11-03  criado (respostas da Etapa 1)

### RF-018 — Decisão de prorrogação (v1)

- **Enunciado:** O sistema deve avisar antes do fim do 1º período e registrar quem decidiu prorrogar ou efetivar.
- **Prioridade:** Should
- **Status:** hipótese
- **Fontes:** sql:SIS-01/folhacerta_dump.sql:contrato
- **Perfis:** juridico-compliance, departamento-pessoal
- **deriva de:** RIS-006
- **Histórico:** v1 2026-11-03  criado (respostas da Etapa 1)

### RF-019 — Aceitar CRNM como identificação (v1)

- **Enunciado:** O sistema deve aceitar a Carteira de Registro Nacional Migratório como documento de identificação nas admissões do programa Acolher, a partir do 1º trimestre de 2027.
- **Prioridade:** Should
- **Status:** confirmado
- **Fontes:** doc:geral/M-02-email-juridico-2026-10-30.md#0
- **Perfis:** juridico-compliance, departamento-pessoal
- **complementa:** RF-003
- **Critérios de aceite:**
  - Dada admissão do programa Acolher, quando o candidato apresenta a CRNM como identificação, então o documento é aceito.
- **Histórico:** v1 2026-11-04 CR-003 criado (Etapa 3)

### RF-020 — Controlar validade da CRNM (v1)

- **Enunciado:** O sistema deve registrar a validade da CRNM e sinalizar documento vencido.
- **Prioridade:** Should
- **Status:** confirmado
- **Fontes:** doc:geral/M-02-email-juridico-2026-10-30.md#0
- **Perfis:** juridico-compliance, departamento-pessoal
- **complementa:** RF-019
- **Critérios de aceite:**
  - Dada CRNM com validade vencida, quando a admissão é consultada, então o vencimento fica sinalizado ao DP.
- **Histórico:** v1 2026-11-04 CR-003 criado (Etapa 3)

## Requisitos não funcionais

### RNF-001 — Trilha de auditoria (v1)

- **Enunciado:** O sistema deve registrar autor, data e valor anterior de cada aprovação, liberação e exceção.
- **Categoria:** segurança
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** doc:escopo.md
- **Perfis:** juridico-compliance
- **deriva de:** RIS-013
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v1 2026-11-03  não coberto pelas respostas; segue hipótese (reforço de fonte ou status)

### RNF-002 — Proteção de dados pessoais (v2)

- **Enunciado:** O sistema deve restringir cada dado pessoal aos perfis que precisam dele em cada etapa.
- **Categoria:** segurança
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/politica-RH-012-admissao-integracao.md#1, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1, entrevista:negocio Q-002 (Helena Vasconcelos)
- **Perfis:** encarregada-dados
- **deriva de:** RIS-004, RIS-005, OPO-009
- **Critérios de aceite:**
  - Dado um perfil, quando acessa uma admissão, então vê apenas os dados previstos na matriz de acesso aprovada pela Encarregada.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  respostas da Etapa 1

### RNF-003 — Responsabilização individual (v1)

- **Enunciado:** O processo deve garantir credencial individual desde o primeiro dia de operação do PDV.
- **Categoria:** segurança
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1
- **Perfis:** operacoes
- **deriva de:** RIS-003
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v1 2026-11-03  Q-015 sem resposta; segue hipótese e risco crítico aberto (reforço de fonte ou status)

### RNF-004 — Falha de integração (v1)

- **Enunciado:** O sistema deve tornar visível toda falha de integração, com reprocessamento controlado.
- **Categoria:** confiabilidade
- **Prioridade:** Should
- **Status:** hipótese
- **Perfis:** software-architect
- **deriva de:** RIS-014
- **Histórico:** v1 2026-11-03  criado (respostas da Etapa 1)

### RNF-005 — Disponibilidade e desempenho (v1)

- **Enunciado:** Os níveis de disponibilidade e desempenho devem ser definidos; não há número nas fontes.
- **Categoria:** desempenho
- **Prioridade:** Should
- **Status:** hipótese
- **Perfis:** software-architect
- **deriva de:** RIS-014
- **Histórico:** v1 2026-11-03  criado (respostas da Etapa 1)

## Regras de negócio

### RN-001 — Duração da experiência (v2)

- **Enunciado:** O sistema deve considerar, para CLT de loja, contrato de experiência de 30 dias, prorrogável por mais 60, totalizando 90 dias.
- **Prioridade:** Must
- **Status:** conflito
- **Fontes:** doc:geral/politica-RH-012-admissao-integracao.md#0, doc:geral/manual-admissao-lojas-v3.2-2019.md#1, sql:SIS-01/folhacerta_dump.sql:contrato.dias_experiencia, entrevista:juridico-compliance Q-004 (Marina Quintela)
- **Perfis:** juridico-compliance
- **deriva de:** DIV-003
- **conflita com:** RN-017
- **Critérios de aceite:**
  - Dado um contrato CLT de experiência com início em D, quando ele é acompanhado, então as datas exibidas são o fim do 1º período e o fim do período total, correspondentes a 30 e 90 dias.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  respostas da Etapa 1; v2 2026-11-04 CR-001 marcado em conflito com pedido do Comitê; valor de 30+60 mantido até decisão

### RN-002 — Validade do ASO (v2)

- **Enunciado:** O sistema deve considerar válido somente ASO apto emitido antes do início e no máximo 30 dias corridos antes dele, sem exceção.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/politica-RH-012-admissao-integracao.md#1, doc:SIS-03/LEIA-ME.md#0, sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato, entrevista:juridico-compliance Q-005 (Fábio Arantes e Marina Quintela), entrevista:operacoes Q-015, doc:geral/M-02-email-juridico-2026-10-30.md#0
- **Perfis:** juridico-compliance, sesmt
- **deriva de:** DIV-004, RIS-001
- **Critérios de aceite:**
  - Dado ASO apto emitido 30 dias corridos antes do início, então ele é válido.
  - Dado ASO apto emitido 31 dias corridos antes do início, então ele é inválido para aquele início.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  respostas da Etapa 1; v2 2026-11-04  reforço de fonte: e-mail do Jurídico mantém ASO e prazos; sem nova versão

### RN-003 — CRF para funções farmacêuticas (v2)

- **Enunciado:** O sistema deve exigir certidão de regularidade com CRF ativo antes do início para toda função farmacêutica, inclusive RT, sem aceitar protocolo.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/politica-RH-012-admissao-integracao.md#1, doc:SIS-03/LEIA-ME.md#0, sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato, entrevista:juridico-compliance Q-006 (Beatriz Lobo), doc:geral/M-01-ata-comite-2026-10-28.md#0
- **Perfis:** juridico-compliance
- **deriva de:** DIV-005, RIS-002
- **Critérios de aceite:**
  - Dado farmacêutico ou RT com apenas protocolo de inscrição, então a condição de CRF fica não atendida.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  respostas da Etapa 1; v2 2026-11-04  reforço de fonte (M-01, item 1); sem nova versão

### RN-004 — Validação e alçada da oferta (v2)

- **Enunciado:** O sistema deve exigir validação do BP de RH em toda oferta e do gerente regional nas acima do piso.
- **Prioridade:** Must
- **Status:** conflito
- **Fontes:** doc:geral/politica-RH-012-admissao-integracao.md#0, sql:SIS-02/recrutamais_dump.sql:oferta.aprovador_perfil, sql:SIS-01/folhacerta_dump.sql:cargo_piso, entrevista:negocio Q-007
- **Perfis:** negocio
- **deriva de:** DIV-006, DIV-007
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  pergunta sem resposta sobre a prática; piso separado em RN-011

### RN-005 — Prazo da integração (v2)

- **Enunciado:** O sistema deve controlar a conclusão do treinamento de Integração e Boas Práticas Farmacêuticas até o 5º dia corrido após o início e antes de o colaborador atender sozinho no balcão.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/politica-RH-012-admissao-integracao.md#1, doc:geral/manual-admissao-lojas-v3.2-2019.md#1, doc:SIS-04/lms-estrutura.md#0, entrevista:negocio Q-008 (Beatriz Lobo)
- **Perfis:** negocio, juridico-compliance
- **deriva de:** DIV-008
- **Critérios de aceite:**
  - Dado início em D e integração não concluída ao fim de D+5, então a pendência fica sinalizada como vencida.
  - Dado integração não concluída, então o colaborador consta como não apto a atender sozinho no balcão.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  respostas da Etapa 1

### RN-006 — Tratamento de aprendiz (v2)

- **Enunciado:** O sistema deve incluir no fluxo único a admissão de jovem aprendiz de 14 a 24 anos, depois de CLT de loja.
- **Prioridade:** Should
- **Status:** confirmado
- **Fontes:** doc:geral/politica-RH-012-admissao-integracao.md#0, doc:geral/fluxo-admissao-atual.md#0, sql:SIS-01/folhacerta_dump.sql:chk_tipo_contrato, entrevista:negocio Q-001 (Helena Vasconcelos), entrevista:departamento-pessoal Q-009 (Rogério Tavares)
- **Perfis:** departamento-pessoal
- **deriva de:** DIV-009, RIS-007
- **Critérios de aceite:**
  - Dado candidato a aprendiz de 16 anos, então o sistema aceita a admissão no fluxo, sem aplicar a idade mínima de 18 anos.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  respostas da Etapa 1

### RN-007 — Retenção de candidatos (v2)

- **Enunciado:** O sistema deve eliminar dados de candidatos não contratados em até 6 meses após o encerramento do processo seletivo, inclusive em cópias e backups.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/politica-RH-012-admissao-integracao.md#2, sql:SIS-02/recrutamais_dump.sql:sp_expurgo_candidatos, entrevista:encarregada-dados Q-012 (Paula Nogueira)
- **Perfis:** encarregada-dados
- **deriva de:** DIV-010
- **Critérios de aceite:**
  - Dado candidato não contratado com processo encerrado há mais de 6 meses, então não restam dados dele na base, nas cópias e nos backups sob controle da empresa.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  respostas da Etapa 1

### RN-008 — CID restrito ao SESMT (v2)

- **Enunciado:** O sistema deve manter CID somente no ambiente do SESMT.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/politica-RH-012-admissao-integracao.md#1, sql:SIS-01/folhacerta_dump.sql:GRANT rh_loja, entrevista:encarregada-dados Q-012 (Paula Nogueira), entrevista:encarregada-dados Q-013 (Paula Nogueira)
- **Perfis:** encarregada-dados, sesmt
- **deriva de:** DIV-011
- **Critérios de aceite:**
  - Dado qualquer perfil fora do SESMT, então nenhum CID fica visível ou armazenado no seu ambiente.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  respostas da Etapa 1

### RN-009 — Lista fechada de condições para início (v2)

- **Enunciado:** O sistema deve aplicar a lista fechada de condições de início, na ordem e com o responsável que forem definidos.
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** doc:SIS-03/LEIA-ME.md#1, sql:SIS-01/folhacerta_dump.sql:contrato.status, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0, doc:geral/politica-RH-012-admissao-integracao.md#1, entrevista:departamento-pessoal Q-010 (Rogério Tavares), doc:geral/M-02-email-juridico-2026-10-30.md#0
- **Perfis:** departamento-pessoal, juridico-compliance
- **deriva de:** DIV-014, RIS-001
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  só ASO e CRF foram confirmados como condição; lista, ordem e liberador seguem abertos; v2 2026-11-04 CR-002 nova condição conhecida para a lista; lista fechada segue aberta

### RN-010 — Prazo de documentos (v1)

- **Enunciado:** O sistema deve sinalizar documentação incompleta a menos de 5 dias úteis do início.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/comunicado-dp-07-2024.md#0, doc:geral/politica-RH-012-admissao-integracao.md#0, doc:SIS-03/LEIA-ME.md#0, entrevista:departamento-pessoal Q-011 (Rogério Tavares)
- **Perfis:** departamento-pessoal
- **deriva de:** DIV-012
- **Critérios de aceite:**
  - Dado início em D e pasta incompleta no 5º dia útil antes de D, então a pendência fica sinalizada ao gerente e ao DP.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v1 2026-11-03  respostas da Etapa 1 (reforço de fonte ou status)

### RN-011 — Referência de piso (v1)

- **Enunciado:** O sistema deve usar como piso o valor da convenção coletiva vigente de cada UF, conforme a FolhaCerta.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** entrevista:negocio Q-007 (Rogério Tavares), sql:SIS-01/folhacerta_dump.sql:cargo_piso
- **Perfis:** departamento-pessoal
- **deriva de:** DIV-007
- **Critérios de aceite:**
  - Dada oferta de balconista em SP abaixo do piso vigente na FolhaCerta, então ela é sinalizada antes de chegar ao candidato.
- **Histórico:** v1 2026-11-03  criado (respostas da Etapa 1)

### RN-012 — Gravidez e antecedentes fora da seleção (v1)

- **Enunciado:** O processo de seleção não deve perguntar nem guardar gravidez e antecedentes.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** entrevista:encarregada-dados Q-012 (Paula Nogueira)
- **Perfis:** encarregada-dados
- **deriva de:** RIS-005
- **Critérios de aceite:**
  - Dado qualquer formulário ou campo de seleção, então não há campo de gravidez nem de antecedentes.
- **Histórico:** v1 2026-11-03  criado (respostas da Etapa 1)

### RN-013 — Dado de pessoa com deficiência (v1)

- **Enunciado:** O sistema deve tratar dado de pessoa com deficiência somente para a finalidade de cota e com acesso restrito.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** entrevista:encarregada-dados Q-012 (Paula Nogueira)
- **Perfis:** encarregada-dados
- **deriva de:** RIS-005
- **Critérios de aceite:**
  - Dado gerente de loja sem autorização, então o dado de pessoa com deficiência não fica visível.
- **Histórico:** v1 2026-11-03  criado (respostas da Etapa 1)

### RN-014 — O que sai do SESMT (v2)

- **Enunciado:** O sistema deve expor fora do SESMT somente aptidão e datas do ASO e a situação do comprovante de vacinação; observação clínica e conteúdo do comprovante ficam restritos ao SESMT.
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** doc:geral/politica-RH-012-admissao-integracao.md#1, entrevista:departamento-pessoal Q-003 (Rogério Tavares), doc:geral/M-02-email-juridico-2026-10-30.md#0
- **Perfis:** sesmt, encarregada-dados
- **deriva de:** DIV-011, DIV-017
- **Histórico:** v1 2026-11-03  criado (respostas da Etapa 1); v2 2026-11-04 CR-002 hipótese estendida ao comprovante, por ser dado de saúde (POL §11.2)

### RN-015 — Definição de admissão (v1)

- **Enunciado:** O sistema deve considerar admissão efetivada apenas com contrato assinado, ASO apto validado e status ATIVO na FolhaCerta.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** entrevista:departamento-pessoal Q-003 (Rogério Tavares), sql:SIS-01/folhacerta_dump.sql:contrato.status
- **Perfis:** departamento-pessoal
- **deriva de:** DIV-002
- **Critérios de aceite:**
  - Dada oferta aceita sem contrato ATIVO, então ela conta como oferta aceita, não como admissão.
- **Histórico:** v1 2026-11-03  criado (respostas da Etapa 1)

### RN-017 — Experiência de 45+45 a partir de 01/12/2026 (pedido) (v1)

- **Enunciado:** O sistema deve considerar contrato de experiência padrão de 45 dias, prorrogável por mais 45, a partir de 01/12/2026.
- **Prioridade:** Must
- **Status:** conflito
- **Fontes:** doc:geral/M-01-ata-comite-2026-10-28.md#0
- **Perfis:** operacoes, juridico-compliance
- **conflita com:** RN-001
- **Histórico:** v1 2026-11-04 CR-001 criado (Etapa 3)

### RN-016 — Vacinação de quem aplica injetáveis em SP (v1)

- **Enunciado:** O sistema deve exigir, a partir de 01/02/2027, comprovante de vacinação contra hepatite B e tétano, junto com o ASO e antes do início, de quem vai aplicar injetáveis em loja de São Paulo.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/M-02-email-juridico-2026-10-30.md#0
- **Perfis:** juridico-compliance, sesmt
- **complementa:** RN-002, RF-012
- **Critérios de aceite:**
  - Dado admitido que vai aplicar injetáveis em loja de SP, com início em 01/02/2027, sem o comprovante, então a liberação é recusada.
  - Dado o mesmo caso com início em 31/01/2027, então a condição não se aplica.
  - Dado admitido em loja de MG, ou em SP sem aplicar injetáveis, então a condição não se aplica.
- **Histórico:** v1 2026-11-04 CR-002 criado (Etapa 3)
