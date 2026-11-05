# Escopo reformulado: Sistema de Vendas Unificado

> Base: `escopo.md` e `fontes/geral/ata-kickoff.md`. Não houve confirmação humana (modo Delegado). As ambiguidades estão em `entrega/perguntas.md`.

## Objetivo
Criar um sistema de vendas único, com um cadastro de clientes, uma política de preço e desconto, pedidos de todos os canais no mesmo lugar, comissão calculada automaticamente e estoque atualizado para todos. [doc: escopo.md]

## Problema
Venda por três caminhos (VendaMax, LojaB2B e planilha de comissão), com regras e cadastros separados e integração noturna por CSV. [doc: escopo.md] [doc: SIS-03/integracao-erp.md#0]

## Atores
Vendedor interno, representante, cliente da loja (PJ e PF profissional), analista de crédito, setor de faturamento, Financeiro, gerente comercial, diretoria, comercial (recadastro), TI, PO. [doc: SIS-01/manual-pedido.md#0] [doc: geral/politica-comercial.md#0] [doc: SIS-02/regras-comissao.md#0]

## Áreas envolvidas
Comercial, Financeiro, Faturamento, Operações/Estoque, TI, Jurídico/LGPD.

## Dentro do escopo
- Cadastro único de clientes; política única de preço e desconto; pedidos multicanal. [doc: escopo.md]
- Comissão automática e estoque compartilhado. [doc: escopo.md]
- Integração com o VendaMax por API. [doc: geral/ata-kickoff.md#0]

## Fora do escopo
- Faturamento e NF-e, que continuam no ERP "por enquanto". [doc: escopo.md]

## Alterado pela ata de 20/01/2027
- App offline para representantes entra na primeira versão. Antes estava fora. [doc: geral/M-01-ata-diretoria.md#0]

## A decidir (Q-024, Q-025, Q-032)
- Comissão automática, fila de crédito e painel como Must (DIV-014).
- Substituição ou manutenção da vitrine da LojaB2B; fim da digitação no VendaMax; fim da planilha.

## Premissas (hipóteses)
- O VendaMax emite NF-e em 2027, com data final desconhecida. [entrevista:software-architect Q-010]
- A política comercial de 2025 e as regras de comissão de março/2026 são as regras de negócio vigentes (a confirmar em Q-001 e Q-004).

## Restrições
- Primeira versão desejada em 6 meses; equipe de 4 devs e 1 PO. [doc: escopo.md]
- VendaMax não pode ser desligado neste ano por causa da NF-e. [doc: geral/ata-kickoff.md#0]
- Consentimento explícito para marketing (LGPD). [doc: geral/politica-comercial.md#0]

## Glossário

| Termo | Definição | Fonte |
|---|---|---|
| VendaMax | ERP de pedido, crédito, faturamento e NF-e | SIS-01/manual-pedido.md#0 |
| LojaB2B | Loja web de autoatendimento | SIS-03/integracao-erp.md#0 |
| Carteira | Vínculo do cliente com um único vendedor | geral/erd-vendamax.md#0 |
| Alçada | Faixa de desconto e quem a aprova | geral/politica-comercial.md#0 |
| Base líquida | Total do pedido menos impostos e frete | SIS-02/regras-comissao.md#0 |
| PF profissional | Pessoa física profissional, como eletricista autônomo, que compra pela loja | geral/politica-comercial.md#0 |
| Bom pagador | Cliente sem atraso nos últimos 12 meses; regra em conflito com a política (RN-005) | entrevista:negocio Q-007 |
| Confirmação do pedido | Momento da reserva; definição pendente (Q-026) | entrevista:operacoes Q-012 |
