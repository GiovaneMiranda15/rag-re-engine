# Perguntas aos stakeholders

Respostas únicas, em ordem de prioridade por tema. Cada pergunta traz o que as fontes já dizem e a hipótese de trabalho usada se ela ficar sem resposta. Hipóteses não são decisões: elas serão marcadas como pendentes na Etapa 2.

1. **Para: Diretor Comercial — Alçada de desconto** (Q-001; achados: DIV-001, GAR-005, GAR-006)
   - **O que já se sabe:** O ERP recusa acima de 10% `[sql: SIS-01/schema.sql:fn_valida_desconto]`, a política permite 12% sem aprovação, até 20% com o gerente e acima disso com a diretoria `[doc: geral/politica-comercial.md#0]`, e a loja tem cupom de até 15% `[sql: SIS-03/schema.sql:cupons]`.
   - **Pergunta:** As faixas da política valem para todos os canais? O cupom de 15% (ex.: BLACK15) precisa de aprovação do gerente ou é pré-aprovado pela campanha? Quem aprova entre 12% e 20% nas férias do gerente (pendência do kickoff) e o que acontece se ninguém responder?
   - **Se ficar sem resposta:** Vale a política em todos os canais; cupom vigente é pré-aprovado; substituto a definir bloqueia a entrada em produção da regra.

2. **Para: Diretor Comercial — Preço** (Q-002; achados: DIV-011)
   - **O que já se sabe:** O escopo diz que cada canal tem preço próprio `[doc: escopo.md]`, mas a política define tabela única `[doc: geral/politica-comercial.md#0]` e a loja recebe o preço do ERP uma vez ao dia `[doc: SIS-03/integracao-erp.md#0]`.
   - **Pergunta:** Existe hoje algum preço realmente diferente por canal, cliente ou representante, ou a diferença é só o atraso do CSV? Na v1 há alguma exceção à tabela única?
   - **Se ficar sem resposta:** Tabela única, sem exceções; a diferença é só defasagem.

3. **Para: Diretor Comercial — Cadastro único e carteira** (Q-003; achados: DIV-003, DIV-010, RIS-010)
   - **O que já se sabe:** O ERP exige CNPJ e carteira opcional `[sql: SIS-01/schema.sql:cliente]`; a loja tem cadastro próprio, sem carteira `[sql: SIS-03/schema.sql:clientes]`. O Financeiro corrige vendedores trocados à mão `[doc: SIS-02/regras-comissao.md#0]`.
   - **Pergunta:** Quem será o dono do cadastro único e qual dado prevalece quando ERP e loja divergirem? Todo cliente precisa ter vendedor de carteira, inclusive pessoa física da loja, e quem define e troca essa carteira? O que causa os vendedores trocados?
   - **Se ficar sem resposta:** Comercial é dono; o ERP prevalece em PJ; cliente sem carteira é permitido e não gera comissão.

4. **Para: Coordenadora Financeira — Comissão: regra e base** (Q-004; achados: DIV-002, RIS-008)
   - **O que já se sabe:** O ERP grava 3% sobre o total `[sql: SIS-01/schema.sql:fn_calcula_comissao]`; a planilha paga sobre o líquido, com outros percentuais `[doc: SIS-02/regras-comissao.md#0]`. O pedido do ERP não tem imposto, frete nem data de faturamento `[sql: SIS-01/schema.sql:pedido]`.
   - **Pergunta:** A aba Leia-me de março/2026 é a regra completa a automatizar, e o valor do ERP pode ser ignorado? De onde vêm hoje impostos e frete, por pedido? Qual data define o mês de apuração e a meta (faturamento, pedido ou pagamento)? Como é o arredondamento?
   - **Se ficar sem resposta:** A aba Leia-me é a regra; data de faturamento define o mês; impostos e frete viriam do ERP, sujeito à Pergunta 10.

5. **Para: Coordenadora Financeira — Comissão: combinações e devolução** (Q-005; achados: DIV-002, DIV-009, DIV-010)
   - **O que já se sabe:** As regras da planilha não dizem como se combinam `[doc: SIS-02/regras-comissao.md#0]`, e o ERP lança devolução como pedido cancelado `[doc: geral/erd-vendamax.md#0]`.
   - **Pergunta:** Pedido da loja com cupom de 15% paga 1% ou 0,5%? Venda da loja conta para a meta? Se a carteira for de representante, vale 1% ou 4%? Metade da comissão vale também sobre os 5% acima da meta? Devolução parcial, no mesmo mês ou após mais de um mês: como fica o estorno? Pode mandar 2 ou 3 casos reais já calculados, sem nomes, para servirem de teste?
   - **Se ficar sem resposta:** Sem hipótese: estes casos serão marcados como pendentes, sem regra inventada.

6. **Para: Coordenadora Financeira — Configuração da comissão** (Q-006; achados: DIV-012, RIS-011)
   - **O que já se sabe:** O kickoff pede regra configurável sem TI `[doc: geral/ata-kickoff.md#0]`; a política prevê aprovação anual da diretoria `[doc: geral/politica-comercial.md#0]`; a apuração vai à diretoria por e-mail `[doc: SIS-02/regras-comissao.md#0]`.
   - **Pergunta:** Quais itens o Financeiro precisa alterar sozinho (percentuais, faixas, meta, calendário)? Quem aprova uma regra nova, ela vale a partir de quando e pode ser retroativa? A aprovação mensal por e-mail continua, dentro do sistema?
   - **Se ficar sem resposta:** Parâmetros numéricos configuráveis, com vigência futura e aprovação registrada; sem retroatividade.

7. **Para: Diretor Comercial, com a Coordenadora Financeira — Bom pagador** (Q-007; achados: DIV-005, RIS-009)
   - **O que já se sabe:** O kickoff pede que o pedido não trave quando o cliente é bom pagador `[doc: geral/ata-kickoff.md#0]`; a política exige análise de todo pedido acima do limite `[doc: geral/politica-comercial.md#0]`. O dump do ERP não mostra histórico de pagamento `[sql: SIS-01/schema.sql:cliente]`.
   - **Pergunta:** Qual é o critério objetivo de bom pagador (tempo de relacionamento, atrasos, valor máximo acima do limite)? Onde está esse histórico? Quem assume o risco, e a política será revisada para permitir a exceção?
   - **Se ficar sem resposta:** Nenhuma liberação automática até o critério ser aprovado; só fila com prazo.

8. **Para: Coordenadora Financeira — Mecânica do crédito** (Q-008; achados: DIV-004, DIV-006, RIS-009, GAR-001)
   - **O que já se sabe:** O trigger compara só o valor de cada pedido com o limite e roda só em INSERT `[sql: SIS-01/schema.sql:fn_checa_credito]`. O documento da loja diz que cartão não passa pela análise `[doc: SIS-03/integracao-erp.md#0]`, e a prática leva 2 dias úteis contra 1 da política `[doc: SIS-01/manual-pedido.md#0]`.
   - **Pergunta:** O limite deve considerar o saldo em aberto ou só o pedido? Cartão e pix dispensam análise? O que fazer com cliente bloqueado e cliente novo (limite padrão 0)? O prazo de 1 dia útil continua e quem cobre o analista? Consulta ao Serasa integrada ao sistema faz parte da v1?
   - **Se ficar sem resposta:** Mantém a regra atual por pedido; cartão dispensa; pix e boleto passam pela análise; Serasa continua manual na v1.

9. **Para: Setor de Faturamento, com a Coordenadora Financeira — Pessoa física e NF-e** (Q-009; achados: DIV-003, RIS-003, GAR-002)
   - **O que já se sabe:** O ERP só aceita CNPJ, mas o comercial recadastra os pedidos de CPF toda manhã `[doc: SIS-03/integracao-erp.md#0]` `[sql: SIS-01/schema.sql:cliente]`, e a política vende a PF desde 2025 `[doc: geral/politica-comercial.md#0]`.
   - **Pergunta:** Como exatamente esses clientes são cadastrados no ERP hoje, e como sai a NF-e deles? Há impacto fiscal ou de contabilização que o novo fluxo deva corrigir?
   - **Se ficar sem resposta:** Sem hipótese: o fluxo de PF fica bloqueado até a resposta, por envolver risco fiscal.

10. **Para: Gerente de TI — VendaMax: API e regras internas** (Q-010; achados: RIS-001, RIS-002, DIV-013)
   - **O que já se sabe:** A integração deve ser por API `[doc: geral/ata-kickoff.md#0]`, mas as fontes só mostram arquivo `[doc: SIS-03/integracao-erp.md#0]`. Os triggers do ERP recusam desconto acima de 10%, reavaliam crédito e gravam comissão de 3% `[sql: SIS-01/schema.sql:fn_valida_desconto]`.
   - **Pergunta:** O VendaMax tem API para cliente, pedido, produto, estoque e retorno de faturamento? Se não, quem pode criá-la, com que custo e prazo? O fornecedor pode ajustar os três triggers e aceitar CPF? Até que data real o ERP continua, já que a ata cita só 'neste ano'?
   - **Se ficar sem resposta:** Sem API comprovada, a v1 precisa de plano alternativo; a arquitetura fica condicionada a esta resposta.

11. **Para: PO — Fronteiras e corte da v1** (Q-011; achados: RIS-004, RIS-007, OPO-008)
   - **O que já se sabe:** O escopo quer sistema único em 6 meses com 4 devs e 1 PO `[doc: escopo.md]`; o kickoff acrescenta app offline a avaliar `[doc: geral/ata-kickoff.md#0]`.
   - **Pergunta:** Na v1, vendedores deixam de digitar no VendaMax? A LojaB2B é substituída ou só reconectada? A planilha deixa de ser usada ou roda em paralelo, e por quantos ciclos? O app offline entra? Se só couberem 3 entregas, quais são? Os 6 meses são data fixa, a contar de quando, e há QA, UX e DevOps além da equipe citada?
   - **Se ficar sem resposta:** Pedido passa ao sistema novo; loja mantém a vitrine e troca a integração; app offline fica fora da v1; comissão roda em paralelo por 2 fechamentos.

12. **Para: Responsável por Operações/Estoque — Reserva de estoque** (Q-012; achados: DIV-007, RIS-007)
   - **O que já se sabe:** O ERP baixa estoque no faturamento `[doc: SIS-01/manual-pedido.md#0]`, e a loja recebe saldo uma vez ao dia, com cerca de 20 cancelamentos/mês `[doc: SIS-03/integracao-erp.md#0]`.
   - **Pergunta:** Em que momento o item deve ficar reservado (digitação, aprovação de crédito ou pagamento) e por quanto tempo? Pedido em análise de crédito segura estoque? Há mais de um depósito? Venda sem saldo é bloqueada ou pode ficar pendente? Quem cuida do estorno ao cliente quando pedido pago é cancelado?
   - **Se ficar sem resposta:** Reserva na criação do pedido, liberada no cancelamento; um único saldo; venda sem saldo bloqueada.

13. **Para: Diretor Comercial — Sucesso e 'tempo real'** (Q-013; achados: OPO-006)
   - **O que já se sabe:** O kickoff pede ver vendas de todos os canais em tempo real `[doc: geral/ata-kickoff.md#0]`, sem meta numérica nas fontes.
   - **Pergunta:** Quais números mostram que a v1 deu certo em 3 meses, e qual a meta de cada um (ex.: reclamações de comissão, cancelamentos, tempo de crédito)? Para o painel, quais indicadores, com que atraso máximo aceitável, e 'venda' é pedido criado ou faturado?
   - **Se ficar sem resposta:** Metas a validar sobre os números atuais (15 reclamações, 20 cancelamentos, 2 dias úteis); painel de pedidos criados com até 5 minutos de atraso.

14. **Para: Jurídico / Encarregado de dados (LGPD) — LGPD e contratos de representantes** (Q-014; achados: DIV-008, RIS-012, RIS-013)
   - **O que já se sabe:** O consentimento nasce marcado na loja `[sql: SIS-03/schema.sql:clientes]`, contra a exigência de consentimento explícito `[doc: geral/politica-comercial.md#0]`. Não há contrato de representante nas fontes, e a planilha estorna comissão e lança na folha `[doc: SIS-02/regras-comissao.md#0]`.
   - **Pergunta:** Os consentimentos atuais valem na migração ou precisam ser recoletados? Quais prazos de retenção e quais direitos do titular o sistema deve atender, inclusive arquivos CSV e erros/? Os contratos de representantes definem base, prazo ou estorno de comissão diferentes da planilha?
   - **Se ficar sem resposta:** Consentimento antigo não migra como válido; prazos de retenção ficam pendentes; contratos não restringem a regra, sujeito a validação.

15. **Para: Gerente de TI — Volumes e operação** (Q-015; achados: RIS-005, RIS-006)
   - **O que já se sabe:** As fontes não trazem volumes de pedidos nem metas de disponibilidade, e o servidor da loja é antigo, sem backup testado `[doc: geral/ata-kickoff.md#0]`.
   - **Pergunta:** Quantos pedidos por mês e no pico, por canal, quantos clientes e usuários? Qual horário de operação, tempo máximo fora do ar e perda de dados aceitável? Há stack ou hospedagem obrigatória? Quem responde pela loja e pelo backup até a virada?
   - **Se ficar sem resposta:** Sem hipótese numérica: requisitos de desempenho e disponibilidade ficam pendentes.
