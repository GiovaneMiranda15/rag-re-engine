# Entrevista — financeiro
## Rodada 1 — 2026-11-03 (modo Delegado)

**Q-004** A aba Leia-me de março/2026 é a regra completa a automatizar, e o valor do ERP pode ser ignorado? De onde vêm hoje impostos e frete, por pedido? Qual data define o mês de apuração e a meta (faturamento, pedido ou pagamento)? Como é o arredondamento?
**R:** Parcial. Vale a regra da planilha do financeiro; o cálculo do ERP será abandonado. Completude da aba Leia-me, origem de impostos e frete, data de apuração e arredondamento: não sabe.
→ classe: conflitante · itens: RN-002, RF-004, DIV-002

**Q-005** Pedido da loja com cupom de 15% paga 1% ou 0,5%? Venda da loja conta para a meta? Se a carteira for de representante, vale 1% ou 4%? Metade da comissão vale também sobre os 5% acima da meta? Devolução parcial, no mesmo mês ou após mais de um mês: como fica o estorno? Pode mandar 2 ou 3 casos reais já calculados, sem nomes, para servirem de teste?
**R:** Parcial. Estorno em devolução mantém a regra da planilha. Demais combinações, devolução parcial ou por período e casos reais: não sabe.
→ classe: existente · itens: RN-013

**Q-006** Quais itens o Financeiro precisa alterar sozinho (percentuais, faixas, meta, calendário)? Quem aprova uma regra nova, ela vale a partir de quando e pode ser retroativa? A aprovação mensal por e-mail continua, dentro do sistema?
**R:** Parcial. Quer alterar as regras de comissão sem depender de TI. Itens, aprovador, vigência, retroatividade e aprovação mensal: não sabe.
→ classe: existente · itens: RF-010, DIV-012

**Q-008** O limite deve considerar o saldo em aberto ou só o pedido? Cartão e pix dispensam análise? O que fazer com cliente bloqueado e cliente novo (limite padrão 0)? O prazo de 1 dia útil continua e quem cobre o analista? Consulta ao Serasa integrada ao sistema faz parte da v1?
**R:** Parcial. Cartão e pix dispensam análise; a meta de 1 dia útil continua. Saldo ou pedido, bloqueado, cliente novo, cobertura do analista e Serasa: não sabe.
→ classe: complementar · itens: RN-004, RN-010, DIV-004, DIV-006

**Q-009** Como exatamente esses clientes são cadastrados no ERP hoje, e como sai a NF-e deles? Há impacto fiscal ou de contabilização que o novo fluxo deva corrigir?
**R:** Não sabe (respondido pelo Financeiro, na ausência do Faturamento).
→ classe: sem informação · itens: nenhum; pergunta segue aberta
