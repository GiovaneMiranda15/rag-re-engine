# Requisitos

> Gerado por `recop.py render` a partir de `.re/modelo/requisitos.json`. Não edite à mão.

## Requisitos funcionais

### RF-001 — Painel de prontidão para início (v3)

- **Enunciado:** O sistema deve mostrar ao gerente de loja, em um só lugar, se o novo colaborador pode começar e quais critérios estão pendentes.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:escopo.md, doc:SIS-03/LEIA-ME.md#1, entrevista:operacoes Q-007
- **Perfis:** operacoes, negocio
- **deriva de:** DIV-015, GAR-007, OPO-002
- **Critérios de aceite:**
  - Dada uma admissão com ASO válido e demais bloqueantes atendidos, quando o gerente abre o painel, então vê Pode começar e a data.
  - Dado ASO vencido, quando o gerente abre o painel, então vê Não pode começar, com a pendência e sem dado clínico.
  - Dado critério condicional aplicável, como comprovante de vacinação ou CRNM, quando o gerente abre o painel, então vê só a situação do critério, sem dado de saúde.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); v2 2026-11-04  atualizado com as respostas (Etapa 2); v3 2026-11-04 CR-002 Critério de aceite acrescentado; enunciado mantido.

### RF-002 — Dados sem redigitação até a folha (v2)

- **Enunciado:** O sistema deve levar à FolhaCerta os dados já coletados sem nova digitação, usando CPF normalizado de 11 dígitos como chave.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:escopo.md, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0
- **Perfis:** departamento-pessoal, software-architect
- **deriva de:** GAR-001, DIV-012, RIS-012, OPO-001
- **Critérios de aceite:**
  - Dado candidato com oferta aceita, quando o DP envia o cadastro, então nenhum campo já coletado é digitado de novo.
  - Dado CPF com dígito verificador inválido ou diferente entre fontes, quando há envio, então ele é retido para correção.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); v2 2026-11-04  atualizado com as respostas (Etapa 2)

### RF-003 — Documentos da admissão (v3)

- **Enunciado:** O sistema deve registrar os documentos exigidos por modalidade, cargo e situação específica, sinalizar faltantes e registrar a conferência ou devolução pelo DP.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:escopo.md, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0, doc:geral/politica-RH-012-admissao-integracao.md#0, doc:geral/M-02-email-juridico-2026-10-30.md#0
- **Perfis:** departamento-pessoal
- **deriva de:** GAR-002, OPO-003
- **Critérios de aceite:**
  - Dado checklist com um item faltante, quando a loja envia a pasta, então o sistema aponta o item antes da conferência.
  - Dado documento ilegível, quando o DP devolve, então o motivo é registrado e a devolução entra no indicador.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); v2 2026-11-04  atualizado com as respostas (Etapa 2); v3 2026-11-04 CR-003 Situação específica acrescentada: CRNM.

### RF-004 — Situação do contrato (v2)

- **Enunciado:** O sistema deve mostrar a situação de geração e assinatura do contrato de cada admissão.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:escopo.md, sql:SIS-01/folhacerta_dump.sql:contrato.status
- **Perfis:** departamento-pessoal
- **deriva de:** DIV-015
- **Critérios de aceite:**
  - Dado contrato assinado, quando o DP registra ou o sistema recebe a informação, então a situação muda com data e responsável.
  - Dado contrato não assinado, quando o funil é calculado, então a admissão não conta como concluída.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); v2 2026-11-04  atualizado com as respostas (Etapa 2)

### RF-005 — Acompanhamento do exame (v2)

- **Enunciado:** O sistema deve acompanhar pedido, agendamento e situação do exame admissional, sem expor dado clínico fora do SESMT.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:escopo.md, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1, entrevista:juridico-compliance Q-012
- **Perfis:** sesmt
- **deriva de:** GAR-003, RIS-008
- **Critérios de aceite:**
  - Dado pedido de exame, quando o SESMT agenda, então gerente e DP veem data e situação.
  - Dado exame com restrição, quando o gerente consulta, então não vê CID nem observação clínica.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); v2 2026-11-04  atualizado com as respostas (Etapa 2)

### RF-006 — Acompanhamento de eSocial (v2)

- **Enunciado:** O sistema deve mostrar situação, prazo e recibo dos eventos de admissão gerados pela FolhaCerta.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:escopo.md, sql:SIS-01/folhacerta_dump.sql:evento_esocial, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1
- **Perfis:** departamento-pessoal
- **deriva de:** GAR-006, RIS-011
- **Critérios de aceite:**
  - Dado S-2190 com recibo, quando o painel é consultado, então aparece enviado, com a data.
  - Dado S-2190 sem envio na véspera do início, quando chega a data limite, então o DP recebe alerta.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); v2 2026-11-04  atualizado com as respostas (Etapa 2)

### RF-007 — Acesso individual ao PDV (v2)

- **Enunciado:** O sistema deve acompanhar o pedido de acesso individual ao PDV a partir da liberação, com meta de estar ativo no primeiro dia.
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** doc:escopo.md, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1, doc:geral/manual-admissao-lojas-v3.2-2019.md#1, doc:geral/fluxo-admissao-atual.md#0
- **Perfis:** software-architect, operacoes
- **deriva de:** GAR-004, DIV-013, RIS-004, OPO-006
- **Critérios de aceite:**
  - Dado início marcado, quando a admissão é liberada, então o pedido de acesso é aberto e acompanhado no painel.
  - Dado acesso não ativo na véspera, quando o gerente consulta, então vê alerta e o responsável pelo chamado.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); v2 2026-11-04  atualizado com as respostas (Etapa 2)

### RF-008 — Acompanhamento de treinamentos (v2)

- **Enunciado:** O sistema deve mostrar por colaborador os treinamentos obrigatórios do cargo, com prazo e situação.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:escopo.md, doc:SIS-04/lms-estrutura.md#0, entrevista:regulatorio Q-015
- **Perfis:** operacoes, regulatorio
- **deriva de:** GAR-005, DIV-004
- **Critérios de aceite:**
  - Dado balconista iniciado, quando o gerente consulta, então vê integração com prazo do 5º dia e os demais cursos da trilha.
  - Dado curso vencido, quando o painel é atualizado, então o caso fica destacado como vencido.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); v2 2026-11-04  atualizado com as respostas (Etapa 2)

### RF-009 — Controle do fim da experiência (v2)

- **Enunciado:** O sistema deve registrar os marcos de 30 e 90 dias e a decisão de prorrogar ou encerrar, com alerta prévio ao gerente e ao DP.
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** doc:escopo.md, doc:geral/fluxo-admissao-atual.md#0, doc:geral/manual-admissao-lojas-v3.2-2019.md#1, entrevista:juridico-compliance Q-005
- **Perfis:** departamento-pessoal, operacoes
- **deriva de:** RIS-007
- **Critérios de aceite:**
  - Dado colaborador no 20º dia de experiência, com antecedência de 10 dias [hipótese], quando o alerta roda, então gerente e DP são avisados.
  - Dado marco de 30 dias sem decisão registrada, quando chega a data, então o caso fica vencido para o responsável.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); v2 2026-11-04  atualizado com as respostas (Etapa 2)

### RF-010 — Funil de admissão (v2)

- **Enunciado:** O sistema deve apresentar por período aceites, admissões concluídas e inícios, com admissão concluída como número oficial.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0, entrevista:departamento-pessoal Q-003
- **Perfis:** negocio, departamento-pessoal
- **deriva de:** DIV-009, OPO-007
- **Critérios de aceite:**
  - Dado um mês fechado, quando o funil é gerado, então as três etapas aparecem separadas, com destaque para admissões concluídas.
  - Dado aprendiz fora da primeira fase, quando o funil é gerado, então o recorte aparece indicado.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); v2 2026-11-04  atualizado com as respostas (Etapa 2)

### RF-011 — Abertura da admissão a partir da oferta (v1)

- **Enunciado:** O sistema deve abrir um processo de admissão para cada oferta de candidato aprovado e acompanhá-lo até o fim da experiência.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:escopo.md, doc:geral/fluxo-admissao-atual.md#0
- **Perfis:** negocio, operacoes
- **deriva de:** GAR-007
- **Critérios de aceite:**
  - Dado candidato aprovado, quando a oferta é criada, então nasce um único processo vinculado ao CPF.
  - Dada segunda oferta para o mesmo candidato e vaga, quando a anterior foi cancelada, então o histórico é mantido sem duplicar o processo.
- **Histórico:** v1 2026-11-04  criado (Etapa 2)

### RF-012 — Registro de aprovação da oferta (v1)

- **Enunciado:** O sistema deve registrar autor, papel, data e valor de cada aprovação de oferta conforme RN-005.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/politica-RH-012-admissao-integracao.md#0, entrevista:juridico-compliance Q-008
- **Perfis:** juridico-compliance, negocio
- **deriva de:** DIV-005
- **Critérios de aceite:**
  - Dada aprovação pelo BP de RH, quando registrada, então autor, data e valor ficam na trilha.
  - Dado gerente de loja, quando tenta aprovar, então o sistema só permite indicar o candidato.
- **Histórico:** v1 2026-11-04  criado (Etapa 2)

### RF-013 — Conferência do piso antes da oferta (v1)

- **Enunciado:** O sistema deve conferir o valor da oferta contra o piso vigente da FolhaCerta antes de ela ser apresentada ao candidato.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** sql:SIS-01/folhacerta_dump.sql:cargo_piso, sql:SIS-02/recrutamais_dump.sql:tabela_salarial, entrevista:departamento-pessoal Q-008
- **Perfis:** departamento-pessoal
- **deriva de:** DIV-010
- **Critérios de aceite:**
  - Dado piso atualizado na FolhaCerta, quando a oferta é registrada, então o enquadramento usa esse valor.
  - Dado piso indisponível para cargo e UF, quando a oferta é registrada, então fica retida para o BP de RH.
- **Histórico:** v1 2026-11-04  criado (Etapa 2)

### RF-014 — Matrícula automática (v1)

- **Enunciado:** O sistema deve matricular o colaborador nas trilhas obrigatórias do cargo pela API do EducaFarma, até o dia do início.
- **Prioridade:** Should
- **Status:** hipótese
- **Fontes:** doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1, doc:SIS-04/lms-estrutura.md#0
- **Perfis:** operacoes, software-architect
- **deriva de:** GAR-005, OPO-005
- **Critérios de aceite:**
  - Dado início confirmado de balconista, quando a admissão é liberada, então as três trilhas ficam matriculadas até a data de início.
  - Dada falha da API, quando as tentativas se esgotam, então há alerta e opção de matrícula manual.
- **Histórico:** v1 2026-11-04  criado (Etapa 2)

### RF-015 — Reavaliação ao mudar o início (v1)

- **Enunciado:** O sistema deve reavaliar os critérios sempre que a data de início mudar e bloquear o início se o ASO deixar de estar válido.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** entrevista:sesmt Q-004, doc:SIS-03/controle_admissoes_2026-estrutura.md#1
- **Perfis:** sesmt, operacoes
- **deriva de:** DIV-001, RIS-006
- **Critérios de aceite:**
  - Dado ASO emitido em 18/02/2027 e início adiado de 20/03 para 21/03/2027, quando a data muda, então o critério fica vencido.
  - Dado adiamento com ASO ainda válido, quando a data muda, então o critério segue atendido e os prazos são recalculados.
- **Histórico:** v1 2026-11-04  criado (Etapa 2)

### RF-016 — Registro da certidão de CRF (v1)

- **Enunciado:** O sistema deve registrar certidão, número e conferência do CRF para toda função farmacêutica, inclusive RT.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/politica-RH-012-admissao-integracao.md#1, entrevista:regulatorio Q-006, sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato
- **Perfis:** regulatorio, departamento-pessoal
- **deriva de:** DIV-003, RIS-005
- **Critérios de aceite:**
  - Dado cargo FARM_RT, quando a certidão é conferida, então o critério CRF fica atendido.
  - Dado cargo FARM_RT sem número de CRF, quando o DP tenta enviar à folha, então o envio é bloqueado.
- **Histórico:** v1 2026-11-04  criado (Etapa 2)

### RF-017 — Eliminação automática (v1)

- **Enunciado:** O sistema deve executar a eliminação dos dados de não contratados no prazo de RN-006 e guardar comprovação sem dados pessoais.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/politica-RH-012-admissao-integracao.md#2, entrevista:juridico-compliance Q-013, sql:SIS-02/recrutamais_dump.sql:sp_expurgo_candidatos
- **Perfis:** juridico-compliance
- **deriva de:** DIV-006, OPO-008
- **Critérios de aceite:**
  - Dado candidato não contratado no 6º mês, quando a rotina diária roda, então os dados são eliminados e a contagem registrada.
  - Dada falha na eliminação, quando a rotina termina, então a Encarregada recebe alerta.
- **Histórico:** v1 2026-11-04  criado (Etapa 2)

### RF-018 — Migração e convivência com o legado (v1)

- **Enunciado:** O sistema deve carregar as admissões em andamento e conviver com planilha, Recruta+, FolhaCerta e EducaFarma durante a transição, sem migrar dados vedados.
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** doc:SIS-03/controle_admissoes_2026-estrutura.md#0, entrevista:negocio Q-001, entrevista:juridico-compliance Q-013
- **Perfis:** departamento-pessoal, software-architect, gestao-pmo
- **deriva de:** DIV-012, RIS-017
- **Critérios de aceite:**
  - Dada admissão em andamento na planilha, quando a carga inicial roda, então ela aparece sem a coluna de observações e sem CPF inválido.
  - Dado campo de gravidez, antecedentes ou CID na origem, quando a carga roda, então o campo não é levado.
- **Histórico:** v1 2026-11-04  criado (Etapa 2)

### RF-019 — Agendamento com a clínica (v1)

- **Enunciado:** O sistema deve agendar o exame pela API da MedTrab, sujeito à verificação do contrato e da API.
- **Prioridade:** Should
- **Status:** hipótese
- **Fontes:** doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1, entrevista:sesmt Q-004
- **Perfis:** sesmt, software-architect
- **deriva de:** GAR-003, RIS-008, OPO-004
- **Critérios de aceite:**
  - Dado pedido de exame, quando há vaga na agenda, então o agendamento retorna data e local.
  - Dada falha da API, quando a tentativa se esgota, então o pedido vai para a fila manual do SESMT.
- **Histórico:** v1 2026-11-04  criado (Etapa 2)

### RF-020 — Fila de falhas de integração (v1)

- **Enunciado:** O sistema deve manter fila de falha e reprocessamento por integração, sem perda de mensagem.
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** entrevista:software-architect Q-014
- **Perfis:** software-architect
- **deriva de:** RIS-016
- **Critérios de aceite:**
  - Dada indisponibilidade da FolhaCerta, quando há envio, então a mensagem fica na fila e é reprocessada.
  - Dada falha definitiva, quando as tentativas se esgotam, então o responsável vê erro e o caso aparece no painel.
- **Histórico:** v1 2026-11-04  criado (Etapa 2)

### RF-021 — Fluxo de aprendiz (v1)

- **Enunciado:** O sistema deve acompanhar aprendiz no fluxo único, com critérios próprios de modalidade, sem a regra de 18 anos da FolhaCerta.
- **Prioridade:** Should
- **Status:** confirmado
- **Fontes:** entrevista:negocio Q-001, entrevista:departamento-pessoal Q-011, sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato, doc:geral/fluxo-admissao-atual.md#0
- **Perfis:** departamento-pessoal, juridico-compliance
- **deriva de:** DIV-008, GAR-008, RIS-009
- **Critérios de aceite:**
  - Dado aprendiz de 16 anos, quando a admissão avança, então as etapas ficam visíveis no mesmo painel.
  - Dado destino do cadastro ainda indefinido, quando o sistema chega nesse passo, então a etapa fica como pendente de decisão de Q-038.
- **Histórico:** v1 2026-11-04  criado (Etapa 2)

### RF-022 — Restrição de atendimento sozinho (v1)

- **Enunciado:** O sistema deve indicar ao gerente que o colaborador não pode atender sozinho no balcão até concluir a integração.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/politica-RH-012-admissao-integracao.md#1, entrevista:regulatorio Q-015
- **Perfis:** regulatorio, operacoes
- **deriva de:** DIV-004
- **Critérios de aceite:**
  - Dada integração não concluída, quando o gerente consulta o colaborador, então vê a restrição.
  - Dada integração concluída, quando o painel é atualizado, então a restrição é retirada com a data.
- **Histórico:** v1 2026-11-04  criado (Etapa 2)

### RF-023 — Treinamento e transição de usuários (v1)

- **Enunciado:** O projeto deve capacitar gerentes das 184 lojas, DP, SESMT e BPs antes da ativação de cada onda.
- **Prioridade:** Should
- **Status:** hipótese
- **Fontes:** entrevista:negocio Q-001, doc:geral/manual-admissao-lojas-v3.2-2019.md#0
- **Perfis:** gestao-pmo, operacoes
- **deriva de:** RIS-017
- **Critérios de aceite:**
  - Dada uma onda planejada, quando entra em operação, então os usuários previstos concluíram a capacitação.
  - Dado gerente sem capacitação, quando a loja entra na onda, então a pendência aparece ao coordenador.
- **Histórico:** v1 2026-11-04  criado (Etapa 2)

### RF-024 — Alinhamento das regras nos legados (v1)

- **Enunciado:** O projeto deve alinhar à RH-012 o manual, a planilha, a FolhaCerta, o Recruta+ e o EducaFarma, ou desativar a regra divergente.
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** doc:geral/manual-admissao-lojas-v3.2-2019.md#1, doc:SIS-03/LEIA-ME.md#0, sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato, sql:SIS-02/recrutamais_dump.sql:tabela_salarial, doc:SIS-04/lms-estrutura.md#0, entrevista:software-architect Q-014
- **Perfis:** software-architect, departamento-pessoal, operacoes
- **deriva de:** DIV-001, DIV-002, DIV-003, DIV-004, DIV-006, DIV-010
- **Critérios de aceite:**
  - Dada a janela de ASO de 90 dias na FolhaCerta, quando o ajuste é feito, então a regra efetiva é de 30 dias.
  - Dado ajuste inviável num legado, quando a viabilidade for avaliada, então o controle fica no novo sistema e a exceção é registrada.
- **Histórico:** v1 2026-11-04  criado (Etapa 2)

### RF-025 — Medição do processo (v1)

- **Enunciado:** O sistema deve medir redigitação, devoluções e motivo, oferta até início e acesso no primeiro dia, para definir a linha de base e as metas.
- **Prioridade:** Should
- **Status:** hipótese
- **Fontes:** doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0, entrevista:departamento-pessoal Q-003, entrevista:departamento-pessoal Q-010
- **Perfis:** negocio, departamento-pessoal
- **deriva de:** GAR-001, GAR-002, GAR-009
- **Critérios de aceite:**
  - Dado um mês de operação, quando o relatório é gerado, então mostra os quatro indicadores por regional.
  - Dada a ausência de meta aprovada, quando o relatório é gerado, então mostra só a medida, sem semáforo.
- **Histórico:** v1 2026-11-04  criado (Etapa 2)

### RF-026 — Comprovante de vacinação como critério (v1)

- **Enunciado:** O sistema deve identificar na vaga quem vai aplicar injetáveis e, conforme UF e vigência, incluir o comprovante de vacinação entre os critérios de início.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/M-02-email-juridico-2026-10-30.md#0
- **Perfis:** sesmt, regulatorio, operacoes
- **deriva de:** RIS-020
- **complementa:** RF-001
- **Critérios de aceite:**
  - Dada vaga marcada para aplicar injetáveis em SP, quando o processo é aberto, então o critério aparece.
  - Dada vaga sem essa marca, quando o processo é aberto, então o critério não aparece.
- **Histórico:** v1 2026-11-04 CR-002 criado (Etapa 3)

### RF-027 — Aceite da CRNM (v1)

- **Enunciado:** O sistema deve aceitar a CRNM como documento de identificação no checklist e registrar número e validade.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/M-02-email-juridico-2026-10-30.md#0
- **Perfis:** departamento-pessoal, juridico-compliance
- **deriva de:** RIS-019
- **complementa:** RF-003
- **Critérios de aceite:**
  - Dada admissão do programa Acolher, quando o checklist é gerado, então a CRNM aparece como documento de identificação.
  - Dada CRNM sem data de validade, quando o DP tenta concluir a conferência, então o sistema exige a data.
- **Histórico:** v1 2026-11-04 CR-003 criado (Etapa 3)

### RF-028 — Controle da validade da CRNM (v1)

- **Enunciado:** O sistema deve controlar a validade da CRNM e alertar DP e gerente antes do vencimento, com regra de bloqueio e antecedência definidas em Q-053.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/M-02-email-juridico-2026-10-30.md#0
- **Perfis:** departamento-pessoal, juridico-compliance
- **deriva de:** RIS-019
- **Critérios de aceite:**
  - Dada CRNM vigente, quando o painel é consultado, então mostra a data de validade e a situação em dia.
  - Dada CRNM vencida antes do início, quando o painel é consultado, então aparece como pendência; bloquear ou alertar depende de Q-053.
- **Histórico:** v1 2026-11-04 CR-003 criado (Etapa 3)

### RF-029 — Admissão sem CPF confirmado nos legados (v1)

- **Enunciado:** O sistema deve tratar a identificação da pessoa com CRNM e o envio à FolhaCerta e ao Recruta+, cujos cadastros exigem CPF e não têm campo de CRNM, conforme a decisão de Q-053.
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** doc:geral/M-02-email-juridico-2026-10-30.md#0, sql:SIS-01/folhacerta_dump.sql:colaborador, sql:SIS-02/recrutamais_dump.sql:candidato
- **Perfis:** departamento-pessoal, software-architect
- **deriva de:** RIS-019
- **complementa:** RF-002
- **Critérios de aceite:**
  - Dada pessoa com CRNM e CPF, quando enviada à folha, então o CPF permanece como chave e a CRNM fica no novo sistema.
  - Dada pessoa com CRNM sem CPF, quando se tenta enviar à folha, então o caso fica retido para o DP.
- **Histórico:** v1 2026-11-04 CR-003 criado (Etapa 3)

## Requisitos não funcionais

### RNF-001 — Dados fora de canais abertos (v2)

- **Enunciado:** O sistema deve manter 100% dos dados e documentos de admissão em ambiente autenticado, sem link aberto nem anexo de e-mail.
- **Categoria:** segurança
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** doc:SIS-03/LEIA-ME.md#0, doc:geral/fluxo-admissao-atual.md#0, entrevista:juridico-compliance Q-012, entrevista:juridico-compliance Q-013
- **Perfis:** juridico-compliance, security
- **deriva de:** RIS-001, RIS-013, OPO-008
- **Critérios de aceite:**
  - Dado acesso sem login, quando se tenta abrir um documento, então é negado.
  - Dada a ativação da onda, quando verificada, então 0 documentos da onda circulam por e-mail.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); v2 2026-11-04  atualizado com as respostas (Etapa 2)

### RNF-002 — Permissões por papel (v2)

- **Enunciado:** O sistema deve aplicar permissões de acesso por papel, unidade e categoria de dado, com 0 acesso de gerente a dado sensível.
- **Categoria:** segurança
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/politica-RH-012-admissao-integracao.md#1, sql:SIS-02/recrutamais_dump.sql:GRANT gerente_loja, sql:SIS-01/folhacerta_dump.sql:GRANT rh_loja, entrevista:juridico-compliance Q-012, entrevista:juridico-compliance Q-013
- **Perfis:** juridico-compliance, security
- **deriva de:** RIS-002, OPO-008
- **Critérios de aceite:**
  - Dado gerente de uma loja, quando busca admissão de outra loja, então é negado.
  - Dado usuário fora do SESMT, quando tenta acessar CID, então é negado e registrado.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); v2 2026-11-04  atualizado com as respostas (Etapa 2)

### RNF-003 — Autoria individual no PDV (v1)

- **Enunciado:** O processo deve garantir que 0 colaborador novo opere o PDV com credencial de outra pessoa.
- **Categoria:** segurança
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1, entrevista:software-architect Q-014
- **Perfis:** security, operacoes
- **deriva de:** RIS-004
- **Critérios de aceite:**
  - Dado colaborador iniciado sem login, quando está nesse estado, então o gerente é alertado e o caso aparece no indicador.
  - Dado acesso ativo, quando verificado, então a credencial é individual.
- **Histórico:** v1 2026-11-04  criado (diagnóstico)

### RNF-004 — Trilha de auditoria (v1)

- **Enunciado:** O sistema deve registrar em trilha de auditoria 100% das aprovações, validações, mudanças de data e acessos a dado sensível, com autor, data, antes e depois.
- **Categoria:** segurança
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** doc:escopo.md, doc:SIS-03/LEIA-ME.md#0
- **Perfis:** juridico-compliance, security
- **deriva de:** RIS-001, DIV-014
- **Critérios de aceite:**
  - Dada mudança na data de início, quando salva, então a trilha guarda autor, data e valores.
  - Dado usuário comum, quando tenta alterar a trilha, então é negado.
- **Histórico:** v1 2026-11-04  criado (Etapa 2)

### RNF-005 — Capacidade no pico (v1)

- **Enunciado:** O sistema deve operar com 320 admissões por mês em novembro e dezembro e responder ao painel em até 3 s no percentil 95 [hipótese de tempo].
- **Categoria:** desempenho
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** entrevista:departamento-pessoal Q-010
- **Perfis:** departamento-pessoal, software-architect
- **deriva de:** GAR-009
- **Critérios de aceite:**
  - Dada carga equivalente a 320 admissões por mês, quando o teste roda, então o painel fica em até 3 s no p95.
  - Dado o pico simulado, quando o teste termina, então não há perda de registro.
- **Histórico:** v1 2026-11-04  criado (Etapa 2)

### RNF-006 — Disponibilidade (v1)

- **Enunciado:** O sistema deve ter disponibilidade de 99,5% ao mês [hipótese].
- **Categoria:** confiabilidade
- **Prioridade:** Should
- **Status:** hipótese
- **Fontes:** entrevista:software-architect Q-014
- **Perfis:** software-architect
- **deriva de:** RIS-016
- **Critérios de aceite:**
  - Dado um mês de operação, quando medido, então a disponibilidade é de pelo menos 99,5%.
  - Dada queda do sistema, quando ocorre, então há alerta em até 5 min [hipótese].
- **Histórico:** v1 2026-11-04  criado (Etapa 2)

### RNF-007 — Monitoramento de integrações (v1)

- **Enunciado:** O sistema deve alertar o responsável em até 15 min [hipótese] após falha de integração e reprocessar com 0 perda.
- **Categoria:** confiabilidade
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** entrevista:software-architect Q-014
- **Perfis:** software-architect, devops
- **deriva de:** RIS-016
- **Critérios de aceite:**
  - Dada falha de integração, quando ocorre, então o alerta sai em até 15 min.
  - Dada integração restabelecida, quando a fila é processada, então 100% das mensagens são entregues.
- **Histórico:** v1 2026-11-04  criado (Etapa 2)

### RNF-008 — Uso pelo gerente (v1)

- **Enunciado:** O gerente deve identificar em no máximo 1 tela e 30 s [hipótese] se o colaborador pode começar.
- **Categoria:** usabilidade
- **Prioridade:** Should
- **Status:** hipótese
- **Fontes:** doc:escopo.md
- **Perfis:** ux-designer, operacoes
- **deriva de:** OPO-002
- **Critérios de aceite:**
  - Dado gerente em teste, quando procura a situação, então encontra em até 30 s.
  - Dado critério pendente, quando exibido, então o motivo aparece em linguagem de negócio.
- **Histórico:** v1 2026-11-04  criado (Etapa 2)

### RNF-009 — Regras parametrizadas com vigência (v1)

- **Enunciado:** O sistema deve permitir alterar prazos e regras por parâmetro com vigência, em até 1 dia útil [hipótese], sem nova versão de software.
- **Categoria:** manutenibilidade
- **Prioridade:** Should
- **Status:** hipótese
- **Fontes:** entrevista:juridico-compliance Q-005, doc:geral/politica-RH-012-admissao-integracao.md#0
- **Perfis:** software-architect, juridico-compliance
- **deriva de:** DIV-002
- **Critérios de aceite:**
  - Dada revisão da RH-012 aprovada, quando o parâmetro é alterado, então vale a partir da vigência.
  - Dada admissão anterior à vigência, quando é consultada, então mantém a regra da data aplicável.
- **Histórico:** v1 2026-11-04  criado (Etapa 2)

### RNF-010 — Comprovação de retenção (v1)

- **Enunciado:** O sistema deve verificar diariamente a retenção de dados de candidatos e reportar 100% das pendências, incluindo cópias e backups.
- **Categoria:** segurança
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** entrevista:juridico-compliance Q-013, doc:geral/politica-RH-012-admissao-integracao.md#2
- **Perfis:** juridico-compliance
- **deriva de:** DIV-006
- **Critérios de aceite:**
  - Dado candidato vencido, quando a verificação roda, então é apontado no mesmo dia.
  - Dado backup com dados vencidos, quando a verificação roda, então a pendência é registrada.
- **Histórico:** v1 2026-11-04  criado (Etapa 2)

### RNF-011 — Proteção de dados pessoais em transporte e repouso (v1)

- **Enunciado:** O sistema deve criptografar 100% dos dados pessoais em trânsito (TLS 1.2 ou superior) e em repouso [hipótese].
- **Categoria:** segurança
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** doc:geral/politica-RH-012-admissao-integracao.md#1
- **Perfis:** security
- **deriva de:** RIS-013
- **Critérios de aceite:**
  - Dada conexão sem TLS, quando tentada, então é recusada.
  - Dado documento armazenado, quando inspecionado, então está criptografado.
- **Histórico:** v1 2026-11-04  criado (Etapa 2)

## Regras de negócio

### RN-001 — Validade do ASO (v2)

- **Enunciado:** O sistema deve aceitar só ASO com resultado apto emitido no máximo 30 dias corridos antes do início e antes da data de início, sem exceção.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/politica-RH-012-admissao-integracao.md#1, entrevista:sesmt Q-004, entrevista:operacoes Q-007, doc:geral/M-02-email-juridico-2026-10-30.md#0
- **Perfis:** sesmt, juridico-compliance
- **deriva de:** DIV-001
- **Critérios de aceite:**
  - Dado início em 20/03/2027, quando o ASO apto foi emitido em 18/02/2027, então o critério fica atendido.
  - Dado início em 20/03/2027, quando o ASO apto foi emitido em 17/02/2027, então o critério fica vencido e o início fica bloqueado.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); v2 2026-11-04  atualizado com as respostas (Etapa 2)

### RN-002 — Duração da experiência (v3)

- **Enunciado:** O sistema deve aplicar à experiência CLT 30 dias, prorrogáveis por mais 60, totalizando 90 dias.
- **Prioridade:** Must
- **Status:** conflito
- **Fontes:** doc:geral/politica-RH-012-admissao-integracao.md#0, entrevista:juridico-compliance Q-005, doc:geral/M-01-ata-comite-2026-10-28.md#0
- **Perfis:** juridico-compliance, departamento-pessoal
- **deriva de:** DIV-002
- **conflita com:** CR-001
- **Critérios de aceite:**
  - Dada uma nova admissão CLT, quando a experiência é registrada, então os marcos são de 30 e de 90 dias.
  - Dado o valor 45+45, quando alguém tenta registrá-lo em nova admissão, então o sistema recusa e informa a regra RH-012.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); v2 2026-11-04  atualizado com as respostas (Etapa 2); v3 2026-11-04 CR-001 Sérgio comunicou 45+45 a partir de 01/12/2026 (M-01). Enunciado mantido; RH-012 segue vigente até decisão.

### RN-003 — CRF de função farmacêutica (v2)

- **Enunciado:** O sistema deve exigir CRF ativo comprovado por certidão de regularidade antes do início de toda função farmacêutica, inclusive RT, sem aceitar protocolo.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/politica-RH-012-admissao-integracao.md#1, entrevista:regulatorio Q-006, entrevista:operacoes Q-007, doc:geral/M-01-ata-comite-2026-10-28.md#0
- **Perfis:** regulatorio, juridico-compliance
- **deriva de:** DIV-003, RIS-005
- **Critérios de aceite:**
  - Dado um RT com certidão de CRF ativo conferida, quando o painel é consultado, então o critério CRF fica atendido.
  - Dado um farmacêutico só com protocolo de inscrição, quando se tenta confirmar o início, então o sistema bloqueia.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); v2 2026-11-04  atualizado com as respostas (Etapa 2)

### RN-004 — Prazo da integração (v2)

- **Enunciado:** O sistema deve exigir a conclusão de Integração e Boas Práticas Farmacêuticas até o 5º dia corrido após o início e antes de o colaborador atender sozinho no balcão.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/politica-RH-012-admissao-integracao.md#1, entrevista:regulatorio Q-015
- **Perfis:** regulatorio, operacoes
- **deriva de:** DIV-004
- **Critérios de aceite:**
  - Dado início em 15/03/2027, quando a integração é concluída em 20/03/2027, então o prazo é cumprido.
  - Dado início em 15/03/2027, quando em 21/03/2027 não há conclusão, então o caso aparece como vencido para gerente e responsável.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); v2 2026-11-04  atualizado com as respostas (Etapa 2)

### RN-005 — Alçada da oferta (v2)

- **Enunciado:** O sistema deve exigir aprovação do BP de RH em toda oferta e também do gerente regional quando o valor estiver acima do piso, sem permitir aprovação só pelo gerente de loja.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/politica-RH-012-admissao-integracao.md#0, entrevista:juridico-compliance Q-008, entrevista:departamento-pessoal Q-008
- **Perfis:** juridico-compliance, departamento-pessoal
- **deriva de:** DIV-005
- **Critérios de aceite:**
  - Dada oferta no piso, quando o BP de RH aprova, então a oferta pode ser apresentada.
  - Dada oferta acima do piso aprovada só pelo BP de RH, quando se tenta apresentá-la, então o sistema exige o gerente regional.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); v2 2026-11-04  atualizado com as respostas (Etapa 2)

### RN-006 — Eliminação de dados de candidatos (v2)

- **Enunciado:** O sistema deve eliminar dados de candidatos não contratados, incluindo cópias e backups, em até 6 meses após o encerramento do processo seletivo.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/politica-RH-012-admissao-integracao.md#2, entrevista:juridico-compliance Q-013
- **Perfis:** juridico-compliance
- **deriva de:** DIV-006
- **Critérios de aceite:**
  - Dado encerramento em 10/01/2027, quando chega 10/07/2027, então os dados do não contratado estão eliminados.
  - Dada uma cópia em backup após o prazo, quando a verificação periódica roda, então a pendência é apontada à Encarregada de Dados.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); v2 2026-11-04  atualizado com as respostas (Etapa 2)

### RN-007 — CID e dados de saúde (v2)

- **Enunciado:** O sistema deve manter CID só no ambiente do SESMT e restringir dados de saúde ao SESMT, nos termos da RH-012, sem armazenar CID em outro sistema.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/politica-RH-012-admissao-integracao.md#1, entrevista:juridico-compliance Q-012, entrevista:juridico-compliance Q-013
- **Perfis:** juridico-compliance, sesmt
- **deriva de:** DIV-007
- **Critérios de aceite:**
  - Dado um analista do DP ou gerente, quando consulta uma admissão, então nenhum CID é exibido.
  - Dada a carga de dados legados, quando houver campo de CID, então ele não é levado para fora do ambiente do SESMT.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); v2 2026-11-04  atualizado com as respostas (Etapa 2)

### RN-008 — Aprendiz no fluxo único (v2)

- **Enunciado:** O sistema deve tratar no fluxo único a admissão de aprendiz de 14 a 24 anos, com jornada de 30 horas semanais, com prioridade posterior à CLT de loja.
- **Prioridade:** Should
- **Status:** confirmado
- **Fontes:** doc:geral/politica-RH-012-admissao-integracao.md#0, entrevista:negocio Q-001, entrevista:departamento-pessoal Q-011
- **Perfis:** negocio, departamento-pessoal, juridico-compliance
- **deriva de:** DIV-008, RIS-009
- **Critérios de aceite:**
  - Dado candidato de 16 anos em vaga de aprendiz, quando a admissão é aberta, então não há recusa por idade.
  - Dado candidato com 25 anos em vaga de aprendiz, quando a admissão é aberta, então o sistema aponta fora da faixa.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); v2 2026-11-04  atualizado com as respostas (Etapa 2)

### RN-009 — Piso conforme a FolhaCerta (v2)

- **Enunciado:** O sistema deve usar como referência o piso da convenção coletiva vigente de cada UF, conforme a FolhaCerta, para enquadrar toda oferta.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** sql:SIS-01/folhacerta_dump.sql:cargo_piso, entrevista:departamento-pessoal Q-008
- **Perfis:** departamento-pessoal
- **deriva de:** DIV-010
- **Critérios de aceite:**
  - Dado balconista em SP com piso de R$ 1.820,00, quando a oferta é de R$ 1.820,00, então basta o BP de RH; com R$ 1.820,01, também o gerente regional.
  - Dado balconista em SP, quando a oferta é de R$ 1.750,00, então o sistema recusa por estar abaixo do piso.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); v2 2026-11-04  atualizado com as respostas (Etapa 2)

### RN-010 — Prazo de documentos (v2)

- **Enunciado:** O sistema deve exigir documentos completos no DP até 5 dias úteis antes do início e sinalizar o descumprimento.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/politica-RH-012-admissao-integracao.md#0, doc:geral/comunicado-dp-07-2024.md#0, doc:SIS-03/LEIA-ME.md#0
- **Perfis:** departamento-pessoal
- **deriva de:** DIV-011
- **Critérios de aceite:**
  - Dado início em 15/03/2027, sem feriado no período, quando os documentos ficam completos em 08/03/2027, então o prazo é cumprido.
  - Dado o mesmo início, quando os documentos ficam completos em 09/03/2027, então o sistema sinaliza atraso.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); v2 2026-11-04  atualizado com as respostas (Etapa 2)

### RN-011 — Critérios bloqueantes confirmados (v3)

- **Enunciado:** O sistema deve bloquear a confirmação de início sem ASO válido; em função farmacêutica, sem CRF ativo; e, nos casos de RN-019, sem comprovante de vacinação, sem exceção para ASO mesmo com loja desfalcada.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/politica-RH-012-admissao-integracao.md#1, entrevista:operacoes Q-007, entrevista:sesmt Q-004, entrevista:regulatorio Q-006, doc:geral/M-02-email-juridico-2026-10-30.md#0
- **Perfis:** operacoes, juridico-compliance
- **deriva de:** DIV-014, DIV-015, RIS-006
- **Critérios de aceite:**
  - Dado ASO vencido e loja desfalcada, quando o gerente tenta confirmar o início, então o sistema bloqueia e não oferece exceção.
  - Dado balconista com ASO válido, quando o gerente consulta, então CRF não aparece como critério.
  - Dado quem vai aplicar injetáveis em loja de SP, com início em 01/02/2027 e ASO válido, quando falta o comprovante de vacinação, então o início fica bloqueado.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); v2 2026-11-04  atualizado com as respostas (Etapa 2); v3 2026-11-04 CR-002 Critério condicional acrescentado.

### RN-012 — Gravidez e antecedentes (v2)

- **Enunciado:** O sistema não deve perguntar nem guardar gravidez e antecedentes na seleção.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** sql:SIS-02/recrutamais_dump.sql:candidato, entrevista:juridico-compliance Q-013
- **Perfis:** juridico-compliance
- **deriva de:** RIS-003
- **Critérios de aceite:**
  - Dados os formulários e cargas do sistema, quando revisados, então não há campo de gravidez nem de antecedentes.
  - Dado um registro de origem com esses campos, quando importado, então os campos são descartados.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); v2 2026-11-04  atualizado com as respostas (Etapa 2)

### RN-013 — Visibilidade do resultado do ASO (v1)

- **Enunciado:** O sistema deve mostrar a DP e gerente a informação sobre o ASO que a Encarregada de Dados definir; está em aberto, porque a RH-012 restringe dados de saúde ao SESMT e o conceito de admissão exige ASO apto validado pelo DP.
- **Prioridade:** Must
- **Status:** conflito
- **Fontes:** doc:geral/politica-RH-012-admissao-integracao.md#1, entrevista:departamento-pessoal Q-003, entrevista:juridico-compliance Q-012, doc:geral/fluxo-admissao-atual.md#0
- **Perfis:** juridico-compliance, sesmt, departamento-pessoal
- **deriva de:** DIV-018
- **conflita com:** RN-007
- **Critérios de aceite:**
  - Dada a decisão de Q-040, quando DP e gerente consultam, então veem só os atributos definidos.
  - Sem decisão de Q-040, quando o sistema entra em operação, então este requisito impede a homologação do módulo de ASO.
- **Histórico:** v1 2026-11-04  criado (Etapa 2)

### RN-014 — Dado de pessoa com deficiência (v1)

- **Enunciado:** O sistema deve tratar dado de pessoa com deficiência só com finalidade clara de cota e acesso restrito, sem CID fora do SESMT.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** sql:SIS-02/recrutamais_dump.sql:candidato, entrevista:juridico-compliance Q-013
- **Perfis:** juridico-compliance
- **deriva de:** RIS-002
- **Critérios de aceite:**
  - Dado um candidato PCD, quando o gerente de loja consulta, então não vê esse dado.
  - Dado usuário sem papel autorizado, quando tenta acessar o dado de cota, então o acesso é negado e registrado.
- **Histórico:** v1 2026-11-04  criado (Etapa 2)

### RN-015 — Admissão concluída (v1)

- **Enunciado:** O sistema deve considerar concluída a admissão com contrato assinado, ASO apto validado e status ATIVO na FolhaCerta, mantendo oferta aceita e primeiro dia como etapas distintas.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** sql:SIS-01/folhacerta_dump.sql:contrato.status, entrevista:departamento-pessoal Q-003
- **Perfis:** departamento-pessoal, negocio
- **deriva de:** DIV-009
- **Critérios de aceite:**
  - Dado contrato ATIVO, assinado e com ASO apto validado, quando o funil é calculado, então conta como admissão concluída.
  - Dada oferta aceita sem contrato ATIVO, quando o funil é calculado, então conta só na etapa de aceite.
- **Histórico:** v1 2026-11-04  criado (Etapa 2)

### RN-016 — Abrangência da primeira fase (v1)

- **Enunciado:** O sistema deve abranger na primeira fase as 184 lojas próprias, com CLT de balconista, caixa e farmacêutico, excluindo escritório central, centro de distribuição e as 28 franqueadas.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/politica-RH-012-admissao-integracao.md#0, entrevista:negocio Q-001
- **Perfis:** negocio
- **deriva de:** DIV-016
- **Critérios de aceite:**
  - Dada loja própria e cargo de caixa, quando se abre a admissão, então é aceita.
  - Dada loja franqueada, quando se tenta abrir a admissão, então é recusada.
- **Histórico:** v1 2026-11-04  criado (Etapa 2)

### RN-017 — Prazos dos eventos de admissão (v1)

- **Enunciado:** O sistema deve acompanhar S-2190 até a véspera do início e S-2200 até o dia 15 do mês seguinte ao da admissão.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/politica-RH-012-admissao-integracao.md#1, sql:SIS-01/folhacerta_dump.sql:esocial_prazo, sql:SIS-01/folhacerta_dump.sql:fn_gera_esocial
- **Perfis:** departamento-pessoal
- **deriva de:** GAR-006
- **Critérios de aceite:**
  - Dado início em 15/03/2027, quando os prazos são calculados, então S-2190 vence em 14/03/2027 e S-2200 em 15/04/2027.
  - Dado S-2200 sem recibo após o prazo, quando o painel é consultado, então o caso aparece como vencido.
- **Histórico:** v1 2026-11-04  criado (Etapa 2)

### RN-018 — Demais critérios de início (v1)

- **Enunciado:** O sistema deve tratar documentos, contrato assinado, S-2190, acesso e kit como critérios configuráveis, bloqueantes ou de alerta, conforme decisão ainda não tomada.
- **Prioridade:** Should
- **Status:** hipótese
- **Fontes:** doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0, doc:geral/politica-RH-012-admissao-integracao.md#1, entrevista:operacoes Q-007
- **Perfis:** operacoes, juridico-compliance, departamento-pessoal
- **deriva de:** DIV-015
- **Critérios de aceite:**
  - Dado um critério definido como alerta, quando está pendente, então o início não é bloqueado e o alerta aparece.
  - Dado um critério definido como bloqueante, quando está pendente, então o início é bloqueado.
- **Histórico:** v1 2026-11-04  criado (Etapa 2)

### RN-019 — Vacinação para aplicar injetáveis em SP (v1)

- **Enunciado:** O sistema deve exigir, a partir de 01/02/2027, junto com o ASO e antes do início das atividades, comprovante de vacinação contra hepatite B e tétano de quem vai aplicar injetáveis em lojas de São Paulo.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/M-02-email-juridico-2026-10-30.md#0
- **Perfis:** juridico-compliance, sesmt, regulatorio
- **deriva de:** RIS-020
- **complementa:** RN-011
- **Critérios de aceite:**
  - Dado aplicador de injetáveis em loja de SP, com início em 01/02/2027, quando há ASO válido e comprovantes de hepatite B e tétano, então o critério fica atendido.
  - Dado o mesmo caso sem o comprovante de tétano, quando se tenta confirmar o início, então o sistema bloqueia.
  - Dado aplicador em loja de MG, ou início em 31/01/2027, quando o painel é consultado, então o critério não se aplica.
- **Histórico:** v1 2026-11-04 CR-002 criado (Etapa 3)

### RN-020 — Sigilo do comprovante de vacinação (v1)

- **Enunciado:** O sistema deve tratar o comprovante de vacinação como dado de saúde, com acesso só do SESMT, mostrando aos demais só a situação do critério.
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** doc:geral/politica-RH-012-admissao-integracao.md#1, doc:geral/M-02-email-juridico-2026-10-30.md#0
- **Perfis:** juridico-compliance, sesmt
- **deriva de:** RIS-020
- **complementa:** RN-007
- **Critérios de aceite:**
  - Dado comprovante enviado, quando o gerente consulta, então vê só atendido ou pendente.
  - Dado usuário fora do SESMT, quando tenta abrir o comprovante, então é negado e registrado.
- **Histórico:** v1 2026-11-04 CR-002 criado (Etapa 3)

### RN-021 — Admissões do programa Acolher (v1)

- **Enunciado:** O sistema deve aceitar, a partir do 1º trimestre de 2027, admissões de pessoas refugiadas e migrantes do programa Acolher, com a CRNM como documento de identificação.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/M-02-email-juridico-2026-10-30.md#0
- **Perfis:** juridico-compliance, negocio, departamento-pessoal
- **deriva de:** RIS-019
- **complementa:** RF-003
- **Critérios de aceite:**
  - Dada admissão do programa Acolher com CRNM, quando aberta, então segue o fluxo sem exigir outro documento de identificação.
  - Dada admissão fora do programa, quando aberta, então a CRNM não é exigida.
- **Histórico:** v1 2026-11-04 CR-003 criado (Etapa 3)

### RN-022 — Sigilo da condição de refugiado ou migrante (v1)

- **Enunciado:** O sistema deve limitar a visibilidade da condição de pessoa refugiada ou migrante aos papéis definidos pela Encarregada de Dados.
- **Prioridade:** Should
- **Status:** hipótese
- **Fontes:** doc:geral/M-02-email-juridico-2026-10-30.md#0, doc:geral/politica-RH-012-admissao-integracao.md#1
- **Perfis:** juridico-compliance
- **deriva de:** RIS-019
- **complementa:** RNF-002
- **Critérios de aceite:**
  - Dada a matriz definida em Q-054, quando um papel consulta a admissão, então vê só o permitido.
  - Dado acesso negado, quando ocorre, então fica registrado na trilha.
- **Histórico:** v1 2026-11-04 CR-003 criado (Etapa 3)
