# LojaB2B — Integração com o VendaMax

Mantido por: TI (1 desenvolvedor terceirizado).

## Fluxo noturno (02:00)
1. A loja gera `pedidos_AAAAMMDD.csv` com os pedidos não exportados.
2. O VendaMax importa o CSV às 03:00. Clientes são casados pelo CNPJ **sem máscara**;
   se o cliente não existe no ERP, o pedido é rejeitado e vai para a pasta `erros/`.
3. O ERP gera `produtos.csv` (preço e estoque) às 04:00, que a loja importa às 05:00.

## Problemas conhecidos
- Clientes pessoa física (CPF) sempre caem em `erros/`, porque o ERP só aceita CNPJ. Uma
  pessoa do comercial recadastra no ERP toda manhã (cerca de 1h por dia).
- O estoque da loja fica desatualizado durante o dia: há vendas de itens sem estoque
  (média de 20 cancelamentos por mês).
- Pedidos com cupom de 15% (ex.: BLACK15) são rejeitados pelo ERP, que limita o desconto
  a 10%. O comercial reduz o desconto à mão e o cliente reclama.
- Pedido pago no cartão pela loja não passa pela análise de crédito do ERP; boleto passa.
- Se o servidor da loja cair às 02:00, o arquivo não é gerado e ninguém é avisado.
