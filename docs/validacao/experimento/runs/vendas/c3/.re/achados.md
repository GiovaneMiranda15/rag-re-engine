# Achados do diagnóstico

## Divergências

| ID | Achado | Sistemas | Severidade | Fontes | Status | Gera |
|---|---|---|---|---|---|---|
| DIV-001 | Limite de desconto diverge entre ERP, política e loja | SIS-01, SIS-03, geral | alta | sql:SIS-01/schema.sql:fn_valida_desconto, doc:SIS-01/manual-pedido.md#0, doc:geral/politica-comercial.md#0, sql:SIS-03/schema.sql:cupons, doc:SIS-03/integracao-erp.md#0, doc:geral/ata-kickoff.md#0 | tratado | RN-001, RF-003, Q-001 |
| DIV-002 | Comissão do ERP diverge da comissão paga | SIS-01, SIS-02 | alta | sql:SIS-01/schema.sql:fn_calcula_comissao, doc:SIS-01/manual-pedido.md#0, doc:SIS-02/regras-comissao.md#0, doc:geral/ata-kickoff.md#0 | tratado | RN-002, RF-004, Q-004, Q-005 |
| DIV-003 | Pessoa física é aceita pela política e pela loja, mas não pelo ERP | SIS-01, SIS-03, geral | alta | doc:geral/politica-comercial.md#0, sql:SIS-01/schema.sql:cliente, sql:SIS-03/schema.sql:clientes, doc:SIS-03/integracao-erp.md#0 | aberto | RN-003, RF-001, Q-003, Q-009 |
| DIV-004 | Prazo de análise de crédito: 1 dia útil na política, 2 na prática | SIS-01, geral | media | doc:geral/politica-comercial.md#0, doc:SIS-01/manual-pedido.md#0 | tratado | RN-004, RF-005, Q-008 |
| DIV-005 | 'Bom pagador não trava' não existe na política nem nos dados | SIS-01, geral | alta | doc:geral/ata-kickoff.md#0, doc:geral/politica-comercial.md#0, sql:SIS-01/schema.sql:cliente | aberto | RN-005, Q-007 |
| DIV-006 | Crédito por forma de pagamento: documento e banco não fecham | SIS-01, SIS-03, geral | alta | doc:SIS-03/integracao-erp.md#0, sql:SIS-01/schema.sql:fn_checa_credito, sql:SIS-01/schema.sql:pedido, sql:SIS-03/schema.sql:pedidos_web, doc:geral/politica-comercial.md#0 | tratado | RN-004, Q-008 |
| DIV-007 | Estoque: baixa no faturamento no ERP, foto diária na loja | SIS-01, SIS-03 | alta | doc:SIS-01/manual-pedido.md#0, doc:SIS-03/integracao-erp.md#0, sql:SIS-03/schema.sql:produtos, doc:escopo.md | aberto | RN-006, RF-006, Q-012 |
| DIV-008 | Consentimento de marketing marcado por padrão | SIS-03, SIS-01, geral | alta | doc:geral/politica-comercial.md#0, sql:SIS-03/schema.sql:clientes, sql:SIS-01/schema.sql:cliente | tratado | RN-007, RNF-003, Q-014 |
| DIV-009 | Devolução estorna comissão, mas o ERP não tem devolução | SIS-01, SIS-02, geral | media | doc:SIS-02/regras-comissao.md#0, doc:geral/erd-vendamax.md#0, sql:SIS-01/schema.sql:fn_calcula_comissao | aberto | RN-002, Q-005 |
| DIV-010 | Carteira e vendedor do pedido: modelo, banco e prática diferem | SIS-01, SIS-02, SIS-03, geral | media | doc:geral/erd-vendamax.md#0, sql:SIS-01/schema.sql:cliente, sql:SIS-01/schema.sql:pedido, doc:SIS-01/manual-pedido.md#0, doc:SIS-02/regras-comissao.md#0 | aberto | RN-002, Q-003, Q-005 |
| DIV-011 | Escopo fala em preços próprios; fontes indicam tabela única com atraso | SIS-01, SIS-03, geral | media | doc:escopo.md, doc:geral/politica-comercial.md#0, doc:SIS-03/integracao-erp.md#0, sql:SIS-03/schema.sql:produtos, doc:SIS-01/manual-pedido.md#0 | tratado | RN-008, Q-002 |
| DIV-012 | Governança da regra de comissão | SIS-02, geral | media | doc:geral/politica-comercial.md#0, doc:geral/ata-kickoff.md#0, doc:SIS-02/regras-comissao.md#0 | aberto | RF-004, Q-006 |
| DIV-013 | Horizonte do ERP: 'este ano', 'por enquanto' e 6 meses | SIS-01, geral | media | doc:geral/ata-kickoff.md#0, doc:escopo.md | tratado | Q-010 |
| DIV-014 | Must da v1 não inclui o que as metas de 6 meses exigem | SIS-04, SIS-02 | critica | entrevista:gestao-pmo Q-011, entrevista:negocio Q-013, doc:escopo.md | aberto | RF-004, RF-005, RF-012, Q-025 |
| DIV-015 | App offline na v1 contraria o corte, o prazo e regras online | SIS-04 | critica | doc:geral/M-01-ata-diretoria.md#0, entrevista:gestao-pmo Q-011, doc:escopo.md | aberto | RF-009, Q-032 |
| DIV-016 | Bônus de meta do representante não tem valor definido | SIS-02, SIS-04 | alta | doc:geral/M-01-ata-diretoria.md#0, doc:SIS-02/regras-comissao.md#0 | aberto | RN-015, Q-030 |
| DIV-017 | Política e planilha ficaram desatualizadas em relação à ata | SIS-02, geral | media | doc:geral/M-01-ata-diretoria.md#0, doc:geral/politica-comercial.md#0, doc:SIS-02/regras-comissao.md#0 | aberto | Q-031 |

## Gargalos

| ID | Achado | Sistemas | Severidade | Fontes | Status | Gera |
|---|---|---|---|---|---|---|
| GAR-001 | Fila manual de crédito | SIS-01 | alta | doc:SIS-01/manual-pedido.md#0, sql:SIS-01/schema.sql:cliente | aberto | RF-005 |
| GAR-002 | Recadastro diário de pessoa física | SIS-03, SIS-01 | media | doc:SIS-03/integracao-erp.md#0 | aberto | RF-001 |
| GAR-003 | Apuração manual de comissão | SIS-01, SIS-02 | alta | doc:SIS-02/regras-comissao.md#0 | aberto | RF-004 |
| GAR-004 | Pedido da loja chega ao ERP só no dia seguinte | SIS-03, SIS-01 | alta | doc:SIS-03/integracao-erp.md#0 | aberto | RF-007, RF-002 |
| GAR-005 | Ajuste manual de pedidos com cupom | SIS-03, SIS-01 | media | doc:SIS-03/integracao-erp.md#0 | aberto | RN-001 |
| GAR-006 | Aprovação de desconto fora do sistema | SIS-01, geral | media | doc:geral/politica-comercial.md#0, sql:SIS-01/schema.sql:pedido, doc:geral/ata-kickoff.md#0 | aberto | RF-003, Q-001 |

## Riscos

| ID | Achado | Sistemas | Severidade | Fontes | Status | Gera |
|---|---|---|---|---|---|---|
| RIS-001 | Regras do ERP podem anular a nova política quando ele continuar faturando | SIS-01, SIS-04 | critica | sql:SIS-01/schema.sql:fn_valida_desconto, sql:SIS-01/schema.sql:fn_checa_credito, sql:SIS-01/schema.sql:fn_calcula_comissao, doc:escopo.md, doc:geral/ata-kickoff.md#0 | aberto | RF-007, Q-023 |
| RIS-002 | API do VendaMax não comprovada | SIS-01, SIS-04 | alta | doc:geral/ata-kickoff.md#0, doc:SIS-03/integracao-erp.md#0, doc:geral/erd-vendamax.md#0 | aberto | RF-007, Q-023 |
| RIS-003 | NF-e de pessoa física com ERP só CNPJ | SIS-01, SIS-03 | alta | doc:SIS-03/integracao-erp.md#0, sql:SIS-01/schema.sql:cliente, doc:geral/politica-comercial.md#0, doc:escopo.md | aberto | RN-003, Q-009 |
| RIS-004 | Escopo maior que prazo e equipe | SIS-04 | critica | doc:escopo.md, doc:geral/ata-kickoff.md#0 | aberto | RF-009, Q-011 |
| RIS-005 | Servidor da loja antigo, sem backup testado, e dependência de um terceirizado | SIS-03 | alta | doc:geral/ata-kickoff.md#0, doc:SIS-03/integracao-erp.md#0 | aberto | RNF-004, Q-015 |
| RIS-006 | Falha silenciosa da integração | SIS-03, SIS-01 | alta | doc:SIS-03/integracao-erp.md#0 | aberto | RNF-001 |
| RIS-007 | Duas fontes da verdade na convivência | SIS-01, SIS-04 | alta | doc:escopo.md, doc:SIS-01/manual-pedido.md#0, doc:geral/ata-kickoff.md#0 | aberto | RF-006, RF-007, Q-011, Q-012 |
| RIS-008 | Comissão automática sem os dados necessários | SIS-01, SIS-02, SIS-04 | alta | doc:SIS-02/regras-comissao.md#0, sql:SIS-01/schema.sql:pedido, doc:geral/erd-vendamax.md#0 | aberto | RF-004, Q-004 |
| RIS-009 | Controle de crédito com brechas | SIS-01 | media | sql:SIS-01/schema.sql:fn_checa_credito, sql:SIS-01/schema.sql:cliente | aberto | RN-004, RN-005, Q-008 |
| RIS-010 | Qualidade dos dados na unificação | SIS-01, SIS-03 | alta | sql:SIS-03/schema.sql:clientes, sql:SIS-01/schema.sql:cliente, doc:SIS-03/integracao-erp.md#0 | aberto | RF-008, Q-003 |
| RIS-011 | Regra configurável sem controle | SIS-02, SIS-04 | media | doc:geral/ata-kickoff.md#0, doc:geral/politica-comercial.md#0 | aberto | RF-004, RNF-002, Q-006 |
| RIS-012 | Dados pessoais em arquivos e dumps | SIS-01, SIS-03 | media | doc:SIS-03/integracao-erp.md#0, doc:SIS-01/schema.sql#0, doc:geral/politica-comercial.md#0 | aberto | RNF-003, Q-014 |
| RIS-013 | Contrato de representante pode restringir comissão | SIS-02 | media | doc:SIS-02/regras-comissao.md#0 | aberto | Q-014 |
| RIS-014 | Donos das regras ausentes da rodada de respostas | SIS-04 | alta | entrevista:operacoes Q-012, entrevista:juridico-compliance Q-014, entrevista:financeiro Q-009 | aberto | Q-026, Q-028 |
| RIS-015 | Consulta periódica com limite de 60/min pode não atender 5 minutos | SIS-04, SIS-01 | alta | doc:geral/M-02-email-ti.md#0, entrevista:negocio Q-013, entrevista:devops Q-015 | aberto | RF-015, RNF-007, Q-027, Q-033 |
| RIS-016 | API confirmada cobre só dois fluxos | SIS-04, SIS-01 | alta | doc:geral/M-02-email-ti.md#0, doc:geral/ata-kickoff.md#0, doc:SIS-03/integracao-erp.md#0 | aberto | RF-007, Q-033 |

## Pontos de apoio

| ID | Achado | Sistemas | Severidade | Fontes | Status | Gera |
|---|---|---|---|---|---|---|
| APO-001 | Política comercial aprovada e objetiva | geral | media | doc:geral/politica-comercial.md#0 | aberto | — |
| APO-002 | Regras de comissão documentadas | SIS-02 | media | doc:SIS-02/regras-comissao.md#0 | aberto | — |
| APO-003 | NF-e já emitida pelo VendaMax | SIS-01 | media | doc:SIS-01/manual-pedido.md#0, doc:geral/ata-kickoff.md#0, doc:escopo.md | aberto | — |
| APO-004 | SKU como identificador comum | SIS-01, SIS-03 | media | sql:SIS-01/schema.sql:produto, sql:SIS-03/schema.sql:produtos | aberto | — |
| APO-005 | Loja já modela o que falta no ERP | SIS-03 | baixa | sql:SIS-03/schema.sql:clientes, sql:SIS-03/schema.sql:cupons, sql:SIS-03/schema.sql:pedidos_web | aberto | — |
| APO-006 | ERP já modela vendedor, carteira, meta e estados do pedido | SIS-01 | baixa | sql:SIS-01/schema.sql:vendedor, sql:SIS-01/schema.sql:cliente, sql:SIS-01/schema.sql:pedido | aberto | — |

## Oportunidades

| ID | Achado | Sistemas | Severidade | Fontes | Status | Gera |
|---|---|---|---|---|---|---|
| OPO-001 | Motor único de desconto e alçada | SIS-04 | alta | doc:geral/politica-comercial.md#0, doc:geral/ata-kickoff.md#0, doc:SIS-03/integracao-erp.md#0 | aberto | RF-003 |
| OPO-002 | Comissão automática e rastreável | SIS-04 | alta | doc:SIS-02/regras-comissao.md#0, doc:geral/ata-kickoff.md#0 | aberto | RF-004 |
| OPO-003 | Cadastro único com PF | SIS-04 | alta | doc:SIS-03/integracao-erp.md#0, doc:geral/politica-comercial.md#0, doc:escopo.md | aberto | RF-001 |
| OPO-004 | Reserva de estoque compartilhada | SIS-04 | alta | doc:SIS-03/integracao-erp.md#0, doc:SIS-01/manual-pedido.md#0, doc:escopo.md | aberto | RF-006 |
| OPO-005 | Crédito com fila, prazo e critério | SIS-04 | alta | doc:SIS-01/manual-pedido.md#0, doc:geral/politica-comercial.md#0, doc:geral/ata-kickoff.md#0 | aberto | RF-005, RN-005 |
| OPO-006 | Visão consolidada de vendas | SIS-04 | media | doc:geral/ata-kickoff.md#0, doc:escopo.md | aberto | RF-002, RNF-005 |
| OPO-007 | Integração monitorada | SIS-04, SIS-01 | alta | doc:geral/ata-kickoff.md#0, doc:SIS-03/integracao-erp.md#0 | aberto | RF-007, RNF-001 |
| OPO-008 | Canal móvel do representante | SIS-04 | baixa | doc:geral/ata-kickoff.md#0 | aberto | RF-009 |
| OPO-009 | Consentimento auditável | SIS-04 | media | doc:geral/politica-comercial.md#0, sql:SIS-03/schema.sql:clientes | aberto | RN-007 |
