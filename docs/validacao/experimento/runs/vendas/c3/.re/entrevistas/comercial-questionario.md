# Questionário delegado — comercial

Gerado em 2026-11-03. Respostas voltam por `entrega/respostas.md` e passam pelo classificador.

**Q-001 (Diretor Comercial — Alçada de desconto)** As faixas da política valem para todos os canais? O cupom de 15% (ex.: BLACK15) precisa de aprovação do gerente ou é pré-aprovado pela campanha? Quem aprova entre 12% e 20% nas férias do gerente (pendência do kickoff) e o que acontece se ninguém responder?

Contexto: O ERP recusa acima de 10% `[sql: SIS-01/schema.sql:fn_valida_desconto]`, a política permite 12% sem aprovação, até 20% com o gerente e acima disso com a diretoria `[doc: geral/politica-comercial.md#0]`, e a loja tem cupom de até 15% `[sql: SIS-03/schema.sql:cupons]`.

**Q-002 (Diretor Comercial — Preço)** Existe hoje algum preço realmente diferente por canal, cliente ou representante, ou a diferença é só o atraso do CSV? Na v1 há alguma exceção à tabela única?

Contexto: O escopo diz que cada canal tem preço próprio `[doc: escopo.md]`, mas a política define tabela única `[doc: geral/politica-comercial.md#0]` e a loja recebe o preço do ERP uma vez ao dia `[doc: SIS-03/integracao-erp.md#0]`.

**Q-003 (Diretor Comercial — Cadastro único e carteira)** Quem será o dono do cadastro único e qual dado prevalece quando ERP e loja divergirem? Todo cliente precisa ter vendedor de carteira, inclusive pessoa física da loja, e quem define e troca essa carteira? O que causa os vendedores trocados?

Contexto: O ERP exige CNPJ e carteira opcional `[sql: SIS-01/schema.sql:cliente]`; a loja tem cadastro próprio, sem carteira `[sql: SIS-03/schema.sql:clientes]`. O Financeiro corrige vendedores trocados à mão `[doc: SIS-02/regras-comissao.md#0]`.
