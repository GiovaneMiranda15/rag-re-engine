# Questionário delegado — financeiro

Gerado em 2026-11-03. Respostas voltam por `entrega/respostas.md` e passam pelo classificador.

**Q-004 (Coordenadora Financeira — Comissão: regra e base)** A aba Leia-me de março/2026 é a regra completa a automatizar, e o valor do ERP pode ser ignorado? De onde vêm hoje impostos e frete, por pedido? Qual data define o mês de apuração e a meta (faturamento, pedido ou pagamento)? Como é o arredondamento?

Contexto: O ERP grava 3% sobre o total `[sql: SIS-01/schema.sql:fn_calcula_comissao]`; a planilha paga sobre o líquido, com outros percentuais `[doc: SIS-02/regras-comissao.md#0]`. O pedido do ERP não tem imposto, frete nem data de faturamento `[sql: SIS-01/schema.sql:pedido]`.

**Q-005 (Coordenadora Financeira — Comissão: combinações e devolução)** Pedido da loja com cupom de 15% paga 1% ou 0,5%? Venda da loja conta para a meta? Se a carteira for de representante, vale 1% ou 4%? Metade da comissão vale também sobre os 5% acima da meta? Devolução parcial, no mesmo mês ou após mais de um mês: como fica o estorno? Pode mandar 2 ou 3 casos reais já calculados, sem nomes, para servirem de teste?

Contexto: As regras da planilha não dizem como se combinam `[doc: SIS-02/regras-comissao.md#0]`, e o ERP lança devolução como pedido cancelado `[doc: geral/erd-vendamax.md#0]`.

**Q-006 (Coordenadora Financeira — Configuração da comissão)** Quais itens o Financeiro precisa alterar sozinho (percentuais, faixas, meta, calendário)? Quem aprova uma regra nova, ela vale a partir de quando e pode ser retroativa? A aprovação mensal por e-mail continua, dentro do sistema?

Contexto: O kickoff pede regra configurável sem TI `[doc: geral/ata-kickoff.md#0]`; a política prevê aprovação anual da diretoria `[doc: geral/politica-comercial.md#0]`; a apuração vai à diretoria por e-mail `[doc: SIS-02/regras-comissao.md#0]`.

**Q-008 (Coordenadora Financeira — Mecânica do crédito)** O limite deve considerar o saldo em aberto ou só o pedido? Cartão e pix dispensam análise? O que fazer com cliente bloqueado e cliente novo (limite padrão 0)? O prazo de 1 dia útil continua e quem cobre o analista? Consulta ao Serasa integrada ao sistema faz parte da v1?

Contexto: O trigger compara só o valor de cada pedido com o limite e roda só em INSERT `[sql: SIS-01/schema.sql:fn_checa_credito]`. O documento da loja diz que cartão não passa pela análise `[doc: SIS-03/integracao-erp.md#0]`, e a prática leva 2 dias úteis contra 1 da política `[doc: SIS-01/manual-pedido.md#0]`.

**Q-009 (Setor de Faturamento, com a Coordenadora Financeira — Pessoa física e NF-e)** Como exatamente esses clientes são cadastrados no ERP hoje, e como sai a NF-e deles? Há impacto fiscal ou de contabilização que o novo fluxo deva corrigir?

Contexto: O ERP só aceita CNPJ, mas o comercial recadastra os pedidos de CPF toda manhã `[doc: SIS-03/integracao-erp.md#0]` `[sql: SIS-01/schema.sql:cliente]`, e a política vende a PF desde 2025 `[doc: geral/politica-comercial.md#0]`.
