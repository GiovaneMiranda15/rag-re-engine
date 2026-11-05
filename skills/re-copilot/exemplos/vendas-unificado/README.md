# Caso sintético — Vendas unificado (Distribuidora Aurora)

Empresa e dados **fictícios**, feitos para desenvolver e testar o re-copilot.

**Cenário:** a Distribuidora Aurora (atacado de material elétrico) vende por três canais
que não conversam entre si. A diretoria quer **um sistema de vendas único e integrado**.

| Sistema | Pasta | O que é |
|---|---|---|
| SIS-01 | `fontes/SIS-01-erp/` | ERP de vendas legado ("VendaMax"): pedidos, faturamento, comissão |
| SIS-02 | `fontes/SIS-02-comissoes/` | Planilha de comissões mantida pelo financeiro |
| SIS-03 | `fontes/SIS-03-loja-b2b/` | Loja B2B web, integrada ao ERP por arquivo CSV diário |
| — | `fontes/geral/` | Política comercial, ata de kickoff e ERD do ERP |

- `escopo.md`: o escopo que o usuário passaria para a skill.
- `mudancas/`: mudanças para testar o modo manutenção, a serem injetadas depois da baseline.
- `oraculo.md`: fatos do stakeholder simulado, usados na validação.
- `gabarito.md`: o que a skill **deveria** encontrar. Serve para avaliar a qualidade do
  diagnóstico e da classificação. **Não indexe este arquivo.**

## Uso rápido

```bash
cd /tmp && mkdir aurora && cp -r <skill>/exemplos/vendas-unificado/{escopo.md,fontes} aurora/
cd aurora   # abra o Claude Code aqui e digite: re-copilot
```
