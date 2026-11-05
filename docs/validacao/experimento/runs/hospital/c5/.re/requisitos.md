# Requisitos

> Gerado por `recop.py render` a partir de `.re/modelo/requisitos.json`. Não edite à mão.

## Requisitos funcionais

### RF-001 — Cadastro único de contratos (v2)

- **Enunciado:** O sistema deve manter um cadastro único de contratos com aditivos, vigência, valor, SLA, índice e status calculado.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:regras_da_planilha.md#quem-mexe, entrevista:negocio Q-002
- **Perfis:** juridico-compliance
- **deriva de:** DIV-008, DIV-014, GAR-005, RIS-008, OPO-005
- **Critérios de aceite:**
  - Dado aditivo registrado, quando consultado o contrato, então todas as áreas veem a nova vigência e o histórico.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04  confirmado por Q-002 (prioridade 1)

### RF-002 — Migração e de-para de chaves (v1)

- **Enunciado:** O sistema deve fazer a carga inicial e o de-para de legado usando número do contrato, CNPJ, patrimônio e unidade.
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** sql:erp_suprimax_dump.sql:fornecedor, sql:manutclin_dump.sql:prestador
- **Perfis:** gestao-pmo
- **deriva de:** DIV-015, APO-001, APO-002
- **Critérios de aceite:**
  - Dado fornecedor com nomes diferentes e mesmo CNPJ, quando migrado, então resulta em um único cadastro.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas

### RF-003 — Fila de parecer (v2)

- **Enunciado:** O sistema deve registrar entrada, saída e responsável de cada parecer jurídico e mostrar a fila.
- **Prioridade:** Should
- **Status:** hipótese
- **Fontes:** doc:indicadores_manutencao_2025.md#tempos, entrevista:juridico-compliance Q-006
- **Perfis:** juridico-compliance
- **deriva de:** GAR-001, OPO-006
- **Critérios de aceite:**
  - Dado contrato em parecer, quando aberta a fila, então aparecem dias de espera e fim de vigência.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04  fora do mínimo de Q-002; relevante pelo limite de Q-006

### RF-004 — Requisição a partir de OS (v2)

- **Enunciado:** O sistema deve ligar OS, requisição e medição e criar requisição a partir de OS em AGUARDANDO_COMPRA, sem redigitação.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:ata_comite_contratos_2026-08-19.md#5, doc:fluxo_contratacao_manutencao.md#corretiva, entrevista:negocio Q-002
- **Perfis:** engenharia-clinica, suprimentos
- **deriva de:** GAR-002, OPO-001
- **Critérios de aceite:**
  - Dada OS em AGUARDANDO_COMPRA, quando importada, então a requisição recebe OS, patrimônio e unidade.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04  ligação confirmada por Q-002; meio pendente em Q-018

### RF-005 — Conferência assistida de medição (v2)

- **Enunciado:** O sistema deve cruzar medição com OS e SLA, apresentar divergências e registrar o ateste da Engenharia Clínica.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:ata_comite_contratos_2026-08-19.md#4, entrevista:negocio Q-002
- **Perfis:** engenharia-clinica
- **deriva de:** GAR-003, OPO-002, APO-006
- **Critérios de aceite:**
  - Dada medição mensal, quando aberta, então aparecem as OS do contrato e os eventos fora do SLA.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04  confirmado por Q-002

### RF-006 — Título com vencimento correto (v2)

- **Enunciado:** O sistema deve gerar o título com vencimento calculado pela regra vigente e registrar alterações com motivo.
- **Prioridade:** Should
- **Status:** hipótese
- **Fontes:** doc:ata_comite_contratos_2026-08-19.md#6, doc:politica_compras_POL-SUP-004_rev3.md#5.1
- **Perfis:** financeiro
- **deriva de:** GAR-004, OPO-004
- **Critérios de aceite:**
  - Dada nota de OC regular, quando gerado o título, então o vencimento é emissão + 45 dias.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04  Q-004 sem resposta; não integra o mínimo de Q-002

### RF-007 — Consulta de inventário e calibração (v1)

- **Enunciado:** O sistema deve receber do ManutClin patrimônio, unidade, status, criticidade e validade de calibração.
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** sql:manutclin_dump.sql:equipamento
- **Perfis:** engenharia-clinica
- **deriva de:** RIS-001
- **Critérios de aceite:**
  - Dada alteração de validade no ManutClin, quando sincronizada, então o novo valor aparece no equipamento.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas

### RF-008 — Alertas de renovação (v2)

- **Enunciado:** O sistema deve enviar alertas de renovação de contrato aos responsáveis.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:politica_compras_POL-SUP-004_rev3.md#4.2, entrevista:negocio Q-002
- **Perfis:** juridico-compliance, gestao-pmo
- **deriva de:** RIS-009, OPO-005
- **Critérios de aceite:**
  - Dado contrato que atinge a data de alerta, quando processada a rotina, então os responsáveis recebem o aviso.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04  alertas confirmados por Q-002; prazo em RN-006; importação separada em RF-014

### RF-009 — Visão consolidada (v2)

- **Enunciado:** O sistema deve apresentar painel consolidado por contrato, fornecedor, equipamento e unidade, em reais e na moeda original.
- **Prioridade:** Should
- **Status:** confirmado
- **Fontes:** doc:escopo.md#visao
- **Perfis:** negocio
- **deriva de:** RIS-010, OPO-007
- **Critérios de aceite:**
  - Dado filtro por unidade, quando aplicado, então os valores somam os contratos da unidade com moeda normalizada.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04  confirmado pelo escopo; fora do mínimo de Q-002

### RF-010 — Custo por equipamento (v2)

- **Enunciado:** O sistema deve calcular custo por equipamento somando contrato, chamados e peças.
- **Prioridade:** Could
- **Status:** confirmado
- **Fontes:** doc:ata_comite_contratos_2026-08-19.md#1, entrevista:negocio Q-002
- **Perfis:** negocio, financeiro
- **deriva de:** RIS-011, OPO-003
- **Critérios de aceite:**
  - Dado equipamento com contrato e peça comprada, quando consultado, então aparecem os três componentes.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04  segunda fase conforme Q-002; rateio pendente em RN-027

### RF-011 — Integração com sistemas mantidos (v1)

- **Enunciado:** O sistema deve integrar com os sistemas mantidos, com monitoramento, tratamento de falha e reprocessamento.
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** doc:escopo.md#relacao
- **Perfis:** gestao-pmo
- **deriva de:** RIS-012
- **Critérios de aceite:**
  - Dada falha de integração, quando detectada, então um alerta é gerado e o reprocessamento não duplica registros.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas

### RF-012 — Convivência e treinamento (v1)

- **Enunciado:** O sistema deve ter plano de transição com convivência, treinamento das áreas e desligamento da planilha.
- **Prioridade:** Should
- **Status:** hipótese
- **Fontes:** doc:escopo.md#prazo
- **Perfis:** gestao-pmo
- **deriva de:** RIS-009
- **Critérios de aceite:**
  - Dada a entrada em operação, quando a área inicia o uso, então os usuários foram treinados e a planilha fica somente leitura.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas

### RF-013 — Conciliação contrato x plano preventivo (v1)

- **Enunciado:** O sistema deve sinalizar diferença entre a periodicidade contratada e a do plano preventivo.
- **Prioridade:** Should
- **Status:** hipótese
- **Fontes:** sql:manutclin_dump.sql:plano_preventivo, doc:controle_contratos.csv#preventiva
- **Perfis:** engenharia-clinica
- **deriva de:** DIV-013, RIS-015
- **Critérios de aceite:**
  - Dado contrato semestral e plano de 365 dias, quando conciliados, então o sistema sinaliza a diferença.
- **Histórico:** v1 2026-11-04  criado (elicitação)

### RF-014 — Importação de renovações do legado (v1)

- **Enunciado:** O sistema deve permitir a importação das renovações feitas no legado durante a transição.
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** doc:politica_compras_POL-SUP-004_rev3.md#4.2, doc:escopo.md#prazo
- **Perfis:** juridico-compliance, gestao-pmo
- **deriva de:** RIS-009
- **Critérios de aceite:**
  - Dada renovação concluída no legado, quando importada, então o contrato mostra a vigência nova.
- **Histórico:** v1 2026-11-04  criado (elicitação)

### RF-015 — Fluxo de renovação (v1)

- **Enunciado:** O sistema deve conduzir a renovação de contrato até a assinatura, com status e responsável.
- **Prioridade:** Should
- **Status:** confirmado
- **Fontes:** doc:escopo.md#cobertura, doc:fluxo_contratacao_manutencao.md#contratacao
- **Perfis:** juridico-compliance
- **deriva de:** DIV-006, DIV-009
- **Critérios de aceite:**
  - Dada renovação aberta, quando a minuta é enviada, então o status indica a etapa e o responsável.
- **Histórico:** v1 2026-11-04  criado (elicitação)

### RF-016 — Fluxo de aprovação (v1)

- **Enunciado:** O sistema deve encaminhar OC e contrato ao aprovador da alçada e registrar a decisão.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** entrevista:negocio Q-002, doc:politica_compras_POL-SUP-004_rev3.md#2
- **Perfis:** financeiro, suprimentos
- **deriva de:** DIV-001, DIV-002
- **Critérios de aceite:**
  - Dada OC submetida, quando calculada a alçada, então a pendência aparece só para o aprovador correto.
- **Histórico:** v1 2026-11-04  criado (elicitação)

### RF-017 — Requisição e cotações (v1)

- **Enunciado:** O sistema deve registrar requisição, unidade, patrimônio quando houver e cotações.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:escopo.md#cobertura, sql:erp_suprimax_dump.sql:requisicao
- **Perfis:** suprimentos
- **deriva de:** DIV-003, RIS-011
- **Critérios de aceite:**
  - Dada requisição de peça, quando registrada, então guarda o patrimônio do equipamento.
- **Histórico:** v1 2026-11-04  criado (elicitação)

### RF-018 — Aditivos com histórico (v1)

- **Enunciado:** O sistema deve registrar cada aditivo com vigência e valor anteriores e novos e avisar o Jurídico.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:escopo.md#cobertura, doc:regras_da_planilha.md#status
- **Perfis:** juridico-compliance
- **deriva de:** DIV-008, DIV-014
- **Critérios de aceite:**
  - Dado aditivo salvo, quando concluído, então o Jurídico é avisado e o histórico mantém os valores anteriores.
- **Histórico:** v1 2026-11-04  criado (elicitação)

### RF-019 — Linha de base de indicadores (v1)

- **Enunciado:** O sistema deve apresentar os indicadores de ciclo de contratação, espera de compra, conferência, títulos alterados e glosas.
- **Prioridade:** Should
- **Status:** hipótese
- **Fontes:** doc:indicadores_manutencao_2025.md#tempos, doc:ata_comite_contratos_2026-08-19.md#4
- **Perfis:** negocio
- **deriva de:** RIS-016
- **Critérios de aceite:**
  - Dado mês encerrado, quando aberto o relatório, então mostra os indicadores com a linha de base de 2025.
- **Histórico:** v1 2026-11-04  criado (elicitação)

### RF-020 — Registro de compra emergencial (v1)

- **Enunciado:** O sistema deve registrar compra emergencial com proposta, aprovação posterior do Diretor Técnico e lista para o Comitê.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:portaria_DG-017-2025_compras_emergenciais.md#3, doc:portaria_DG-017-2025_compras_emergenciais.md#5
- **Perfis:** suprimentos
- **deriva de:** RIS-007, APO-003
- **Critérios de aceite:**
  - Dada emergencial emitida, quando decorrerem 72 horas sem aprovação, então Suprimentos e o Diretor Técnico são alertados.
- **Histórico:** v1 2026-11-04  criado (elicitação)

### RF-021 — Incorporação do Hospital Aurora Serra (v1)

- **Enunciado:** O sistema deve cadastrar o Hospital Aurora Serra como unidade e receber seus dois contratos de manutenção.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:M-01-email-suprimentos.md#1
- **Perfis:** suprimentos, juridico-compliance, gestao-pmo
- **deriva de:** RIS-017
- **Critérios de aceite:**
  - Dada a incorporação, quando cadastrada a unidade, então os dois contratos aparecem na visão consolidada da rede.
- **Histórico:** v1 2026-11-04 CR-001 criado a partir de M-01, item 1

## Requisitos não funcionais

### RNF-001 — Dados de paciente fora do sistema (v2)

- **Enunciado:** [hipótese] O sistema deve receber 0 campo identificador de paciente das OS (premissa; confirmar com o DPO).
- **Categoria:** segurança
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** sql:manutclin_dump.sql:paciente_nome
- **Perfis:** juridico-compliance, security
- **deriva de:** RIS-002
- **Critérios de aceite:**
  - Dada OS com nome de paciente, quando integrada, então o dado não é armazenado nem exibido.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04  encaminhada ao DPO (Q-016)

### RNF-002 — Trilha de auditoria (v2)

- **Enunciado:** O sistema deve gravar 1 registro de auditoria por aprovação, com usuário, data, valor anterior e valor novo.
- **Categoria:** segurança
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** sql:manutclin_dump.sql:prestador_portal, doc:regras_da_planilha.md#quem-mexe, entrevista:negocio Q-002
- **Perfis:** security, juridico-compliance
- **deriva de:** RIS-003, GAR-005
- **Critérios de aceite:**
  - Dada aprovação de OC, quando concluída, então a trilha mostra os quatro dados.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04  trilha de aprovações confirmada por Q-002; demais objetos separados em RNF-007

### RNF-003 — Atualização da integração (v2)

- **Enunciado:** [hipótese] O sistema deve refletir OS e inventário em até 24 horas (valor proposto; confirmar com TI e Engenharia Clínica).
- **Categoria:** desempenho
- **Prioridade:** Should
- **Status:** hipótese
- **Fontes:** doc:indicadores_manutencao_2025.md#tempos
- **Perfis:** gestao-pmo
- **deriva de:** GAR-002
- **Critérios de aceite:**
  - Dada OS alterada, quando decorrido o prazo definido, então o novo status aparece.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04  valor proposto

### RNF-004 — Permissões por papel (v1)

- **Enunciado:** O sistema deve conceder acesso por papel e unidade, com 0 acesso externo a dados de pagamento.
- **Categoria:** segurança
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** doc:politica_compras_POL-SUP-004_rev3.md#2, sql:manutclin_dump.sql:prestador_portal
- **Perfis:** security
- **deriva de:** RIS-002, RIS-003
- **Critérios de aceite:**
  - Dado usuário de outra área, quando tenta aprovar sem papel, então é recusado.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas

### RNF-005 — Capacidade inicial (v2)

- **Enunciado:** O sistema deve suportar pelo menos 4.812 equipamentos, 640 OS por mês e 1.460 OCs por ano, mais os volumes do Hospital Aurora Serra (a definir), sem perda de registros.
- **Categoria:** desempenho
- **Prioridade:** Should
- **Status:** hipótese
- **Fontes:** doc:indicadores_manutencao_2025.md#inventario, doc:indicadores_manutencao_2025.md#tempos, doc:M-01-email-suprimentos.md#1
- **Perfis:** gestao-pmo
- **deriva de:** APO-004
- **Critérios de aceite:**
  - Dada carga com esses volumes, quando processada, então todos os registros são aceitos ou rejeitados com motivo.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04 CR-001 volume da nova unidade a definir (Q-020)

### RNF-006 — Parâmetros versionados (v1)

- **Enunciado:** O sistema deve manter 100% dos limites de alçada, cotação e prazo como parâmetros com vigência, sem exigir nova versão do software.
- **Categoria:** manutenibilidade
- **Prioridade:** Should
- **Status:** hipótese
- **Fontes:** doc:politica_compras_POL-SUP-004_rev3.md#1.3
- **Perfis:** financeiro, suprimentos
- **deriva de:** RIS-013, APO-007
- **Critérios de aceite:**
  - Dada nova revisão da política, quando cadastrada, então o novo limite vale a partir da data de vigência.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas

### RNF-007 — Auditoria de demais objetos (v1)

- **Enunciado:** [hipótese] O sistema deve registrar trilha em 100% das alterações de contrato, medição e título (valor proposto).
- **Categoria:** segurança
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** sql:manutclin_dump.sql:prestador_portal, doc:regras_da_planilha.md#quem-mexe
- **Perfis:** security
- **deriva de:** RIS-003, GAR-005
- **Critérios de aceite:**
  - Dada alteração de vencimento, quando concluída, então a trilha mostra usuário, data e valores.
- **Histórico:** v1 2026-11-04  criado (elicitação)

### RNF-008 — Disponibilidade (v1)

- **Enunciado:** [hipótese] O sistema deve ter disponibilidade mensal de 99,5% em horário comercial (valor proposto; confirmar com TI).
- **Categoria:** confiabilidade
- **Prioridade:** Should
- **Status:** hipótese
- **Fontes:** hipótese:ti
- **Perfis:** ti
- **deriva de:** RIS-016
- **Critérios de aceite:**
  - Dado um mês de operação, quando medida a disponibilidade, então é de pelo menos 99,5%.
- **Histórico:** v1 2026-11-04  criado (elicitação)

### RNF-009 — Tempo de resposta (v1)

- **Enunciado:** [hipótese] O sistema deve abrir consultas e painéis em até 3 s em 95% das requisições (valor proposto; confirmar com TI).
- **Categoria:** desempenho
- **Prioridade:** Should
- **Status:** hipótese
- **Fontes:** hipótese:ti
- **Perfis:** ti
- **deriva de:** OPO-007
- **Critérios de aceite:**
  - Dada a carga de RNF-005, quando medido, então o 95º percentil fica em até 3 s.
- **Histórico:** v1 2026-11-04  criado (elicitação)

### RNF-010 — Recuperação (v1)

- **Enunciado:** [hipótese] O sistema deve ter backup diário e restauração em até 8 horas (valor proposto; confirmar com TI).
- **Categoria:** confiabilidade
- **Prioridade:** Should
- **Status:** hipótese
- **Fontes:** hipótese:ti
- **Perfis:** ti
- **deriva de:** RIS-016
- **Critérios de aceite:**
  - Dado teste de restauração, quando executado, então conclui em até 8 horas.
- **Histórico:** v1 2026-11-04  criado (elicitação)

### RNF-011 — Monitoramento de integração (v1)

- **Enunciado:** [hipótese] O sistema deve alertar falha de integração em até 15 min (valor proposto; confirmar com TI).
- **Categoria:** confiabilidade
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** hipótese:ti
- **Perfis:** ti
- **deriva de:** GAR-002
- **Critérios de aceite:**
  - Dada falha na carga, quando detectada, então o alerta sai em até 15 min.
- **Histórico:** v1 2026-11-04  criado (elicitação)

## Regras de negócio

### RN-001 — Alçada de OC pela política (v2)

- **Enunciado:** O sistema deve exigir aprovador Gerente de Suprimentos até R$ 50.000,00, Diretor Financeiro de R$ 50.000,01 a R$ 250.000,00 e Diretora Geral acima de R$ 250.000,00.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:politica_compras_POL-SUP-004_rev3.md#2, entrevista:financeiro Q-003
- **Perfis:** financeiro
- **deriva de:** DIV-001
- **Critérios de aceite:**
  - Dada OC de R$ 50.000,00, quando o Gerente de Suprimentos aprova, então o sistema aceita.
  - Dada OC de R$ 50.000,01, quando o Gerente de Suprimentos tenta aprovar, então o sistema recusa e encaminha ao Diretor Financeiro.
  - Dada OC de R$ 250.000,01, quando o Diretor Financeiro tenta aprovar, então o sistema recusa e encaminha à Diretora Geral.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04  confirmado por Q-003

### RN-002 — Alçada de contrato pelo valor global (v2)

- **Enunciado:** O sistema deve definir a alçada de contrato assinado desde 01/01/2025 pelo valor global durante toda a vigência.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:politica_compras_POL-SUP-004_rev3.md#2.2, entrevista:financeiro Q-003, doc:M-01-email-suprimentos.md#2
- **Perfis:** financeiro, juridico-compliance
- **deriva de:** DIV-002
- **Critérios de aceite:**
  - Dado contrato de R$ 22.000,00/mês por 24 meses, quando enviado à aprovação, então a alçada usa R$ 528.000,00 e vai à Diretora Geral.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04  confirmado por Q-003, com recorte de data

### RN-003 — Cotações pela política (v2)

- **Enunciado:** O sistema deve exigir zero cotação até R$ 5.000,00, duas de R$ 5.000,01 a R$ 15.000,00 e três acima de R$ 15.000,00, salvo emergencial.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:politica_compras_POL-SUP-004_rev3.md#3, entrevista:financeiro Q-003
- **Perfis:** suprimentos
- **deriva de:** DIV-003
- **Critérios de aceite:**
  - Dada compra regular de R$ 19.800,00 com uma cotação, quando enviada à aprovação, então o sistema recusa.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04  confirmado por Q-003

### RN-004 — Prazo de pagamento (v2)

- **Enunciado:** O sistema deve usar prazo padrão de 45 dias da emissão da nota, com mínimo de 30 dias, salvo compra emergencial.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:politica_compras_POL-SUP-004_rev3.md#5.1, doc:portaria_DG-017-2025_compras_emergenciais.md#4, entrevista:financeiro Q-003
- **Perfis:** financeiro
- **deriva de:** DIV-004, OPO-004
- **Critérios de aceite:**
  - Dada OC regular com 28 dias, quando salva, então o sistema recusa.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04  confirmado por Q-003

### RN-005 — Parecer jurídico por valor (v3)

- **Enunciado:** O sistema deve exigir parecer jurídico antes da aprovação de contrato com valor global acima de R$ 30.000,00.
- **Prioridade:** Must
- **Status:** conflito
- **Fontes:** doc:politica_compras_POL-SUP-004_rev3.md#4.5, entrevista:juridico-compliance Q-006, doc:M-02-memorando-juridico-engclin.md#1
- **Perfis:** juridico-compliance
- **deriva de:** DIV-005
- **conflita com:** RN-028
- **Critérios de aceite:**
  - Dado contrato de R$ 58.800,00 sem parecer, quando enviado à aprovação, então o sistema recusa.
  - Dado contrato de exatamente R$ 30.000,00, quando enviado à aprovação, então o parecer não é exigido.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04  confirmado por Q-006; v3 2026-11-04 CR-002 marcado em conflito com o Memorando 2026/14; enunciado mantido

### RN-006 — Início da renovação (v2)

- **Enunciado:** O sistema deve abrir a renovação 120 dias antes do fim da vigência para a área gestora e o Jurídico.
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** doc:politica_compras_POL-SUP-004_rev3.md#4.2
- **Perfis:** juridico-compliance, suprimentos, engenharia-clinica
- **deriva de:** DIV-006
- **Critérios de aceite:**
  - Dado contrato com fim em 31/01/2027, quando chega 03/10/2026, então a renovação é aberta para os responsáveis.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04  Q-008 sem resposta; 120 dias segue como premissa pela política; fluxo de 90 dias não foi revogado por ninguém

### RN-007 — Índice de reajuste (v2)

- **Enunciado:** O sistema deve aplicar IPCA a contrato assinado desde 01/01/2024, manter o índice original nos anteriores até o fim da vigência e não aplicar índice a contrato em moeda estrangeira.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:politica_compras_POL-SUP-004_rev3.md#4.3, doc:politica_compras_POL-SUP-004_rev3.md#4.4, doc:controle_contratos.csv#CT-2025-0064, doc:regras_da_planilha.md#colunas
- **Perfis:** financeiro, juridico-compliance
- **deriva de:** DIV-007, RIS-014
- **Critérios de aceite:**
  - Dado contrato em BRL assinado em 2025, quando cadastrado com IGP-M, então o sistema recusa.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04  confirmado por evidência: política §4.3 e §4.4 e coluna indice da planilha (índice previsto em contrato)

### RN-008 — Pagamento depende de contrato vigente e registrado (v2)

- **Enunciado:** O sistema deve bloquear a liberação de medição de contrato com vigência encerrada, salvo exceção aprovada com justificativa.
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** doc:politica_compras_POL-SUP-004_rev3.md#4.1, doc:ata_comite_contratos_2026-08-19.md#7
- **Perfis:** juridico-compliance, financeiro
- **deriva de:** DIV-009, DIV-010, RIS-004
- **Critérios de aceite:**
  - Dada medição de contrato com fim anterior à competência, quando liberada sem exceção, então o sistema recusa.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04  Q-007 sem resposta; bloqueio segue como premissa; parte de registro separada em RN-021

### RN-009 — Fonte única do SLA (v2)

- **Enunciado:** O sistema deve guardar SLA de atendimento e de solução em um único cadastro por contrato, com o valor do contrato assinado; em CT-2024-0117, o atendimento é de 4 horas.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:regras_da_planilha.md#colunas, sql:manutclin_dump.sql:contrato_ref, entrevista:juridico-compliance Q-009, entrevista:negocio Q-002
- **Perfis:** juridico-compliance, engenharia-clinica
- **deriva de:** DIV-011
- **Critérios de aceite:**
  - Dado CT-2024-0117 migrado, quando consultado, então o SLA de atendimento é 4 horas, não 8.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04  confirmado por Q-009 e Q-002; CT-2024-0117 = 4 horas

### RN-010 — Criticidade única (v2)

- **Enunciado:** O sistema deve classificar cada equipamento nos quatro níveis da política: 1 Suporte à vida, 2 Alto, 3 Médio, 4 Baixo.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:politica_compras_POL-SUP-004_rev3.md#6.2, entrevista:engenharia-clinica Q-011
- **Perfis:** engenharia-clinica
- **deriva de:** DIV-012
- **Critérios de aceite:**
  - Dado equipamento sem classificação, quando incluído em contrato, então o sistema exige o nível.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04  níveis confirmados por política e Q-011; derivação do contrato separada em RN-022

### RN-011 — Preventiva de ventiladores da Central (v2)

- **Enunciado:** O sistema deve registrar preventiva semestral para os ventiladores de CT-2023-0019, conforme o contrato assinado.
- **Prioridade:** Should
- **Status:** confirmado
- **Fontes:** sql:manutclin_dump.sql:plano_preventivo, doc:controle_contratos.csv#preventiva, entrevista:engenharia-clinica Q-012
- **Perfis:** engenharia-clinica
- **deriva de:** DIV-013, RIS-015
- **Critérios de aceite:**
  - Dado CT-2023-0019 migrado, quando consultada a preventiva, então consta Semestral.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04  confirmado por Q-012; conciliação separada em RF-013

### RN-012 — Retorno ao uso depende de teste e liberação (v2)

- **Enunciado:** O sistema deve identificar como irregular toda OS corretiva fechada sem teste aprovado e liberação assinada.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:fluxo_contratacao_manutencao.md#corretiva, entrevista:engenharia-clinica Q-013
- **Perfis:** engenharia-clinica
- **deriva de:** DIV-016
- **Critérios de aceite:**
  - Dada OS corretiva fechada sem liberação, quando recebida, então entra na lista de irregularidades da Engenharia Clínica.
  - Dada OS corretiva com teste aprovado e liberação, quando recebida, então não entra na lista.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04  regra confirmada por Q-013; alerta x bloqueio separado em RN-024

### RN-013 — Pagamento depende de ateste (v2)

- **Enunciado:** O sistema deve bloquear o pagamento de medição sem ateste da Engenharia Clínica.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:politica_compras_POL-SUP-004_rev3.md#5.2, entrevista:negocio Q-002
- **Perfis:** engenharia-clinica, financeiro
- **deriva de:** DIV-017
- **Critérios de aceite:**
  - Dada medição sem ateste, quando enviada a pagamento, então o sistema recusa.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04  confirmado por política §5.2 e Q-002

### RN-014 — Segregação de funções (v2)

- **Enunciado:** O sistema deve impedir que o solicitante aprove a própria compra.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:politica_compras_POL-SUP-004_rev3.md#2.3
- **Perfis:** suprimentos
- **deriva de:** DIV-018
- **Critérios de aceite:**
  - Dada OC solicitada pelo usuário X, quando X tenta aprovar, então o sistema recusa.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04  confirmado por evidência: política §2.3

### RN-015 — Calibração vencida (v2)

- **Enunciado:** O sistema deve alertar a Engenharia Clínica sobre equipamento em uso com calibração vencida.
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** doc:politica_compras_POL-SUP-004_rev3.md#6.3
- **Perfis:** engenharia-clinica
- **deriva de:** RIS-001
- **Critérios de aceite:**
  - Dado equipamento EM_USO com validade passada, quando processada a carga, então um alerta é gerado.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04  Q-013 sem decisão sobre bloqueio; alerta comum às duas opções, mantido como premissa

### RN-016 — Detecção de fracionamento (v2)

- **Enunciado:** O sistema deve somar as ordens da mesma requisição para definir alçada e cotações.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:politica_compras_POL-SUP-004_rev3.md#3.1, entrevista:negocio Q-002
- **Perfis:** suprimentos, financeiro
- **deriva de:** RIS-005, RIS-007
- **Critérios de aceite:**
  - Dadas três OCs da mesma requisição somando R$ 149.300,00, quando aprovadas, então a alçada usa o total.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04  vedação confirmada por política §3.1 e Q-002; recorrência separada em RN-025

### RN-017 — Glosa por descumprimento de SLA (v3)

- **Enunciado:** O sistema deve calcular glosa de 2% do valor mensal por evento de descumprimento de SLA, com soma limitada a 10% do valor mensal do contrato em cada competência.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:politica_compras_POL-SUP-004_rev3.md#5.3, entrevista:negocio Q-002, doc:M-02-memorando-juridico-engclin.md#2
- **Perfis:** financeiro, engenharia-clinica
- **deriva de:** RIS-006, OPO-002
- **Critérios de aceite:**
  - Dado evento acima do SLA em contrato de R$ 11.040,00/mês, quando aberta a medição, então a proposta é de R$ 220,80.
  - Dados 5 eventos em contrato de R$ 11.040,00/mês, quando calculada a competência, então a glosa é R$ 1.104,00.
  - Dados 6 eventos no mesmo contrato e competência, quando calculada, então a glosa continua R$ 1.104,00.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04  cálculo confirmado por política §5.3 e Q-002; relógio e aceite separados em RN-026; v3 2026-11-04 CR-003 limite por competência acrescentado (Memorando 2026/14)

### RN-018 — Compra emergencial (v2)

- **Enunciado:** O sistema deve limitar a compra emergencial a R$ 100.000,00 por ocorrência, com aprovação do Diretor Técnico em até 72 horas e comunicação ao Comitê.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:portaria_DG-017-2025_compras_emergenciais.md#2, doc:portaria_DG-017-2025_compras_emergenciais.md#3, doc:portaria_DG-017-2025_compras_emergenciais.md#5
- **Perfis:** suprimentos
- **deriva de:** RIS-007, APO-003
- **Critérios de aceite:**
  - Dada emergencial de R$ 120.000,00, quando registrada, então o sistema recusa como emergencial.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04  confirmado por evidência: Portaria DG-017/2025

### RN-019 — Moeda estrangeira (v2)

- **Enunciado:** O sistema deve guardar contrato na moeda original e o câmbio de referência definido pelo Financeiro para consolidação.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:politica_compras_POL-SUP-004_rev3.md#4.4, doc:regras_da_planilha.md#colunas
- **Perfis:** financeiro
- **deriva de:** RIS-010
- **Critérios de aceite:**
  - Dado contrato em USD, quando consolidado, então usa o câmbio de referência e exibe a moeda original.
- **Histórico:** v1 2026-11-04  criado (diagnóstico); aguarda resposta das perguntas; v2 2026-11-04  confirmado por evidência: política §4.4 e regras da planilha

### RN-020 — Valor global com aditivo e moeda (v1)

- **Enunciado:** O sistema deve somar aditivos ao valor global e converter moeda estrangeira pelo câmbio de referência ao definir alçada e parecer.
- **Prioridade:** Should
- **Status:** hipótese
- **Fontes:** doc:politica_compras_POL-SUP-004_rev3.md#2.2, doc:politica_compras_POL-SUP-004_rev3.md#4.4
- **Perfis:** financeiro
- **deriva de:** DIV-002
- **Critérios de aceite:**
  - Dado contrato de 9.800 USD/mês por 36 meses com câmbio 5,40, quando enviado à aprovação, então a base é R$ 1.905.120,00.
- **Histórico:** v1 2026-11-04  criado (elicitação)

### RN-021 — Registro antes do primeiro pagamento (v1)

- **Enunciado:** O sistema deve impedir o primeiro pagamento de contrato não registrado.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:politica_compras_POL-SUP-004_rev3.md#4.1
- **Perfis:** juridico-compliance, financeiro
- **deriva de:** DIV-010
- **Critérios de aceite:**
  - Dada medição sem contrato registrado, quando enviada a pagamento, então o sistema recusa.
- **Histórico:** v1 2026-11-04  criado (elicitação)

### RN-022 — Criticidade do contrato (v1)

- **Enunciado:** O sistema deve derivar a criticidade do contrato do maior nível dos equipamentos cobertos.
- **Prioridade:** Could
- **Status:** hipótese
- **Fontes:** doc:regras_da_planilha.md#colunas, doc:politica_compras_POL-SUP-004_rev3.md#6.2
- **Perfis:** engenharia-clinica
- **deriva de:** DIV-012
- **Critérios de aceite:**
  - Dado contrato com itens de nível 1 e 3, quando consultado, então a criticidade é nível 1.
- **Histórico:** v1 2026-11-04  criado (elicitação)

### RN-023 — Conversão de A, B, C (v1)

- **Enunciado:** O sistema deve converter A para nível 1 e C para nível 4 e deixar B pendente de escolha entre níveis 2 e 3 pela Engenharia Clínica.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** entrevista:engenharia-clinica Q-011, doc:politica_compras_POL-SUP-004_rev3.md#6.2
- **Perfis:** engenharia-clinica
- **deriva de:** DIV-012
- **Critérios de aceite:**
  - Dado equipamento B na carga, quando importado, então fica com classificação pendente entre 2 e 3.
  - Dado equipamento A, quando importado, então recebe nível 1.
- **Histórico:** v1 2026-11-04  criado (elicitação)

### RN-024 — Bloqueio operacional (v1)

- **Enunciado:** O ManutClin deve bloquear o retorno ao uso sem liberação e o uso com calibração vencida.
- **Prioridade:** Should
- **Status:** hipótese
- **Fontes:** entrevista:engenharia-clinica Q-013
- **Perfis:** engenharia-clinica
- **deriva de:** DIV-016, RIS-001
- **Critérios de aceite:**
  - Dada OS sem liberação, quando há tentativa de fechar, então o ManutClin recusa.
- **Histórico:** v1 2026-11-04  criado (elicitação)

### RN-025 — Alerta de recorrência (v1)

- **Enunciado:** O sistema deve alertar sobre OCs recorrentes do mesmo fornecedor e unidade sem contrato vinculado.
- **Prioridade:** Should
- **Status:** hipótese
- **Fontes:** doc:politica_compras_POL-SUP-004_rev3.md#3.1, sql:erp_suprimax_dump.sql:OC-2026-00452
- **Perfis:** suprimentos
- **deriva de:** RIS-005, DIV-010
- **Critérios de aceite:**
  - Dadas três OCs mensais de R$ 4.900,00 ao mesmo fornecedor sem contrato, quando emitida a terceira, então Suprimentos recebe alerta.
- **Histórico:** v1 2026-11-04  criado (elicitação)

### RN-026 — Relógio do SLA e aceite da glosa (v1)

- **Enunciado:** O sistema deve pausar o relógio em espera de item não coberto e submeter a glosa proposta ao aceite no ateste.
- **Prioridade:** Should
- **Status:** hipótese
- **Fontes:** doc:politica_compras_POL-SUP-004_rev3.md#5.3, sql:manutclin_dump.sql:88190
- **Perfis:** engenharia-clinica, financeiro
- **deriva de:** RIS-006
- **Critérios de aceite:**
  - Dada OS em AGUARDANDO_COMPRA, quando apurado o SLA de solução, então o período é excluído.
  - Dada glosa proposta, quando recusada, então exige justificativa.
- **Histórico:** v1 2026-11-04  criado (elicitação)

### RN-027 — Rateio do contrato (v1)

- **Enunciado:** O sistema deve ratear o valor do contrato igualmente entre os equipamentos cobertos, com critério configurável.
- **Prioridade:** Could
- **Status:** hipótese
- **Fontes:** doc:ata_comite_contratos_2026-08-19.md#1
- **Perfis:** financeiro
- **deriva de:** RIS-011
- **Critérios de aceite:**
  - Dado contrato de R$ 1.000,00 com 2 equipamentos, quando calculado, então cada um recebe R$ 500,00.
- **Histórico:** v1 2026-11-04  criado (elicitação)

### RN-028 — Parecer jurídico acima de R$ 200 mil (memorando) (v1)

- **Enunciado:** O sistema deve exigir parecer jurídico apenas para contrato com valor global acima de R$ 200.000,00.
- **Prioridade:** Must
- **Status:** conflito
- **Fontes:** doc:M-02-memorando-juridico-engclin.md#1
- **Perfis:** juridico-compliance, negocio
- **conflita com:** RN-005
- **deriva de:** DIV-019
- **Critérios de aceite:**
  - Dado contrato de R$ 163.200,00 sem parecer, quando enviado à aprovação, então o sistema aceita.
  - Dado contrato de R$ 200.000,01 sem parecer, quando enviado à aprovação, então o sistema recusa.
- **Histórico:** v1 2026-11-04 CR-002 criado em conflito; não vigente no modelo até a decisão de Q-019
