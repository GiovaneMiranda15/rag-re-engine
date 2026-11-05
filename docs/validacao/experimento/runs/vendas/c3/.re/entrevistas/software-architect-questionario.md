# Questionário delegado — software-architect

Gerado em 2026-11-03. Respostas voltam por `entrega/respostas.md` e passam pelo classificador.

**Q-010 (Gerente de TI — VendaMax: API e regras internas)** O VendaMax tem API para cliente, pedido, produto, estoque e retorno de faturamento? Se não, quem pode criá-la, com que custo e prazo? O fornecedor pode ajustar os três triggers e aceitar CPF? Até que data real o ERP continua, já que a ata cita só 'neste ano'?

Contexto: A integração deve ser por API `[doc: geral/ata-kickoff.md#0]`, mas as fontes só mostram arquivo `[doc: SIS-03/integracao-erp.md#0]`. Os triggers do ERP recusam desconto acima de 10%, reavaliam crédito e gravam comissão de 3% `[sql: SIS-01/schema.sql:fn_valida_desconto]`.
