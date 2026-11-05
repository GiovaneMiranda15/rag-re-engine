# ERD — VendaMax (transcrito do diagrama do fornecedor, 2022)

```mermaid
erDiagram
    VENDEDOR ||--o{ CLIENTE : "carteira"
    CLIENTE ||--o{ PEDIDO : faz
    VENDEDOR ||--o{ PEDIDO : "vende"
    PEDIDO ||--|{ PEDIDO_ITEM : contem
    PRODUTO ||--o{ PEDIDO_ITEM : "é vendido em"
    PEDIDO ||--o| COMISSAO : gera
```

Observações do diagrama: um cliente pertence a um único vendedor (carteira). Pedidos da
loja web não têm vendedor. Não há entidade de devolução: devoluções são lançadas como
pedido cancelado.
