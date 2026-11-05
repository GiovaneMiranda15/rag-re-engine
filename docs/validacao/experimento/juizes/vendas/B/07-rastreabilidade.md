# Rastreabilidade

- **Projeto:** Sistema de Vendas Unificado
- **Data:** 03/11/2026
- **Baseline:** sem baseline (documentos ainda não validados pelos stakeholders)
- **Revisão:** inclui CR-001 a CR-005 (ver `08-mudancas.md`)
- **Fontes:** `escopo.md`; `fontes/SIS-01-erp/` (manual-pedido.md, schema.sql); `fontes/SIS-02-comissoes/regras-comissao.md`; `fontes/SIS-03-loja-b2b/` (integracao-erp.md, schema.sql); `fontes/geral/` (ata-kickoff.md, erd-vendamax.md, politica-comercial.md); `entrega/respostas.md`; `mudancas/` (M-01, M-02)

Liga requisito, fonte, achado e backlog, a partir de `[método]modelo/` (`[método] check` sem erro). As mesmas ligações vão como `req-<ID>` nos CSVs.

## 1. Requisitos → fontes, achados e histórias

| Requisito | Status | Prioridade | Fontes | Achados | Histórias |
|---|---|---|---|---|---|
| RN-001 | confirmado | Must | doc:geral/politica-comercial.md#0, doc:geral/ata-kickoff.md#0, entrevista:comercial Q-001, doc:geral/M-01-ata-diretoria.md#0 | DIV-001, GAR-005 | US-010, US-011, US-012, US-014 |
| RN-002 | confirmado | Should | doc:SIS-02/regras-comissao.md#0, doc:geral/ata-kickoff.md#0, entrevista:financeiro Q-004, doc:geral/M-01-ata-diretoria.md#0 | DIV-002, DIV-009, DIV-010 | US-019 |
| RN-003 | confirmado | Must | doc:geral/politica-comercial.md#0, sql:SIS-03/schema.sql:clientes, doc:SIS-03/integracao-erp.md#0 | DIV-003, RIS-003 | US-001 |
| RN-004 | confirmado | Should | doc:geral/politica-comercial.md#0, doc:SIS-01/manual-pedido.md#0, entrevista:financeiro Q-008 | DIV-004, DIV-006, RIS-009 | US-025 |
| RN-005 | conflito | Should | doc:geral/ata-kickoff.md#0, entrevista:negocio Q-007 | DIV-005, OPO-005, RIS-009 | — |
| RN-006 | confirmado | Must | doc:SIS-01/manual-pedido.md#0, doc:SIS-03/integracao-erp.md#0, doc:escopo.md, entrevista:operacoes Q-012 | DIV-007 | US-015 |
| RN-007 | confirmado | Must | doc:geral/politica-comercial.md#0, entrevista:juridico-compliance Q-014 | DIV-008, OPO-009 | US-003, US-004 |
| RN-008 | confirmado | Must | doc:geral/politica-comercial.md#0, doc:escopo.md, entrevista:comercial Q-002 | DIV-011 | US-009 |
| RF-001 | confirmado | Must | doc:escopo.md, doc:SIS-03/integracao-erp.md#0, entrevista:gestao-pmo Q-011 | DIV-003, GAR-002, OPO-003 | US-001, US-002 |
| RF-002 | confirmado | Must | doc:escopo.md, doc:geral/ata-kickoff.md#0, entrevista:gestao-pmo Q-011 | GAR-004, OPO-006 | US-005, US-006, US-007 |
| RF-003 | confirmado | Must | doc:geral/politica-comercial.md#0, doc:geral/ata-kickoff.md#0, entrevista:comercial Q-001, entrevista:gestao-pmo Q-011, doc:geral/M-01-ata-diretoria.md#0 | DIV-001, GAR-006, OPO-001 | US-011, US-012 |
| RF-004 | confirmado | Should | doc:escopo.md, doc:geral/ata-kickoff.md#0, doc:geral/politica-comercial.md#0, doc:SIS-02/regras-comissao.md#0, entrevista:financeiro Q-004, entrevista:gestao-pmo Q-011, entrevista:negocio Q-013 | DIV-002, DIV-012, GAR-003, RIS-008, RIS-011, OPO-002 | US-019 |
| RF-005 | confirmado | Should | doc:SIS-01/manual-pedido.md#0, doc:geral/politica-comercial.md#0, entrevista:financeiro Q-008, entrevista:negocio Q-013 | DIV-004, GAR-001, OPO-005 | US-025 |
| RF-006 | confirmado | Must | doc:escopo.md, doc:SIS-03/integracao-erp.md#0, doc:SIS-01/manual-pedido.md#0, entrevista:gestao-pmo Q-011, entrevista:operacoes Q-012 | DIV-007, RIS-007, OPO-004 | US-016 |
| RF-007 | confirmado | Must | doc:geral/ata-kickoff.md#0, doc:escopo.md, entrevista:software-architect Q-010, entrevista:gestao-pmo Q-011, doc:geral/M-02-email-ti.md#0 | GAR-004, RIS-001, RIS-002, RIS-007, OPO-007 | US-017, US-018 |
| RF-008 | hipótese | Should | doc:escopo.md, sql:SIS-01/schema.sql:cliente, sql:SIS-03/schema.sql:clientes, entrevista:juridico-compliance Q-014 | RIS-010 | — |
| RF-009 | confirmado | Must | doc:geral/ata-kickoff.md#0, entrevista:gestao-pmo Q-011, doc:geral/M-01-ata-diretoria.md#0 | RIS-004, OPO-008 | US-031, US-032, US-033 |
| RNF-001 | hipótese | Must | doc:SIS-03/integracao-erp.md#0 | RIS-006, OPO-007 | — |
| RNF-002 | hipótese | Must | doc:geral/politica-comercial.md#0, doc:geral/ata-kickoff.md#0, doc:SIS-02/regras-comissao.md#0 | RIS-011 | — |
| RNF-003 | hipótese | Must | doc:geral/politica-comercial.md#0, entrevista:juridico-compliance Q-014 | DIV-008, RIS-012 | — |
| RNF-004 | hipótese | Must | doc:geral/ata-kickoff.md#0, entrevista:devops Q-015 | RIS-005 | — |
| RNF-005 | confirmado | Should | doc:geral/ata-kickoff.md#0, entrevista:negocio Q-013, doc:geral/M-02-email-ti.md#0 | OPO-006 | US-027 |
| RN-009 | confirmado | Must | entrevista:comercial Q-001, doc:geral/M-01-ata-diretoria.md#0 | DIV-001, GAR-005 | US-014 |
| RN-010 | confirmado | Should | entrevista:financeiro Q-008, doc:SIS-03/integracao-erp.md#0 | DIV-006 | US-026 |
| RN-011 | confirmado | Should | doc:SIS-02/regras-comissao.md#0, entrevista:financeiro Q-004 | DIV-002 | US-020 |
| RN-012 | confirmado | Should | doc:SIS-02/regras-comissao.md#0, entrevista:financeiro Q-004 | DIV-002, DIV-010 | US-021 |
| RN-013 | confirmado | Should | doc:SIS-02/regras-comissao.md#0, entrevista:financeiro Q-005 | DIV-009 | US-022 |
| RN-014 | confirmado | Should | doc:SIS-02/regras-comissao.md#0, entrevista:financeiro Q-004 | DIV-002 | US-023 |
| RF-010 | confirmado | Should | doc:geral/ata-kickoff.md#0, entrevista:financeiro Q-006, doc:geral/M-01-ata-diretoria.md#0 | DIV-012, RIS-011 | US-024 |
| RF-011 | confirmado | Must | entrevista:gestao-pmo Q-011, doc:geral/M-01-ata-diretoria.md#0 | OPO-008 | US-006 |
| RF-012 | confirmado | Should | doc:geral/ata-kickoff.md#0, entrevista:negocio Q-013 | OPO-006, DIV-014 | US-027 |
| RF-013 | confirmado | Must | entrevista:juridico-compliance Q-014 | DIV-008 | US-004 |
| RF-014 | confirmado | Must | entrevista:comercial Q-001, sql:SIS-03/schema.sql:cupons | DIV-001 | US-013 |
| RNF-006 | confirmado | Must | entrevista:devops Q-015, doc:geral/M-02-email-ti.md#0 | RIS-004 | US-008 |
| RN-015 | confirmado | Should | doc:geral/M-01-ata-diretoria.md#0 | DIV-016 | US-030 |
| RF-015 | confirmado | Must | doc:geral/M-02-email-ti.md#0 | RIS-015 | US-029 |
| RNF-007 | confirmado | Must | doc:geral/M-02-email-ti.md#0 | RIS-015 | US-028 |

## 2. Histórias → requisitos

| História | Título | Requisitos | Feature |
|---|---|---|---|
| US-001 | Cadastrar cliente por CPF ou CNPJ | RN-003, RF-001 | FT-001 |
| US-002 | Usar o mesmo cadastro em todos os canais | RF-001 | FT-001 |
| US-003 | Dar consentimento explícito | RN-007 | FT-002 |
| US-004 | Reconfirmar consentimento da base da loja | RF-013, RN-007 | FT-002 |
| US-005 | Registrar pedido como vendedor interno | RF-002 | FT-003 |
| US-006 | Registrar pedido na web responsiva | RF-011, RF-002 | FT-003 |
| US-007 | Receber pedido da loja sem lote noturno | RF-002 | FT-003 |
| US-008 | Suportar o pico de pedidos | RNF-006 | FT-003 |
| US-009 | Aplicar tabela única de preço | RN-008 | FT-004 |
| US-010 | Aplicar faixas de desconto | RN-001 | FT-005 |
| US-011 | Aprovar ou recusar desconto | RF-003, RN-001 | FT-005 |
| US-012 | Aprovar desconto acima de 20% | RF-003, RN-001 | FT-005 |
| US-013 | Criar cupom com validade | RF-014 | FT-006 |
| US-014 | Autorizar cupom acima de 15% | RN-009, RN-001 | FT-006 |
| US-015 | Reservar item na confirmação | RN-006 | FT-007 |
| US-016 | Consultar o mesmo saldo em todos os canais | RF-006 | FT-007 |
| US-017 | Comprovar a API e os triggers do VendaMax | RF-007 | FT-008 |
| US-018 | Enviar pedido aprovado para faturamento | RF-007 | FT-008 |
| US-028 | Enfileirar envios no limite da API | RNF-007 | FT-008 |
| US-029 | Consultar periodicamente o faturamento | RF-015 | FT-008 |
| US-019 | Calcular comissão por tipo de vendedor | RF-004, RN-002 | FT-009 |
| US-030 | Aplicar bônus de meta ao representante | RN-015 | FT-009 |
| US-020 | Aplicar redutor acima de 8% | RN-011 | FT-009 |
| US-021 | Pagar 1% em pedido da loja | RN-012 | FT-009 |
| US-022 | Estornar comissão por devolução | RN-013 | FT-009 |
| US-023 | Fechar comissão no calendário | RN-014 | FT-009 |
| US-024 | Alterar regra de comissão sem TI | RF-010 | FT-010 |
| US-025 | Trabalhar a fila com prazo | RF-005, RN-004 | FT-011 |
| US-026 | Dispensar análise em cartão e pix | RN-010 | FT-011 |
| US-027 | Ver vendas de todos os canais | RF-012, RNF-005 | FT-012 |
| US-031 | Definir as regras do pedido offline | RF-009 | FT-013 |
| US-032 | Registrar pedido sem internet | RF-009 | FT-013 |
| US-033 | Sincronizar pedido ao reconectar | RF-009 | FT-013 |

## 3. Achados → tratamento

| Achado | Status | Gera |
|---|---|---|
| DIV-001 | tratado | RN-001, RF-003, Q-001 |
| DIV-002 | tratado | RN-002, RF-004, Q-004, Q-005 |
| DIV-003 | aberto | RN-003, RF-001, Q-003, Q-009 |
| DIV-004 | tratado | RN-004, RF-005, Q-008 |
| DIV-005 | aberto | RN-005, Q-007 |
| DIV-006 | tratado | RN-004, Q-008 |
| DIV-007 | aberto | RN-006, RF-006, Q-012 |
| DIV-008 | tratado | RN-007, RNF-003, Q-014 |
| DIV-009 | aberto | RN-002, Q-005 |
| DIV-010 | aberto | RN-002, Q-003, Q-005 |
| DIV-011 | tratado | RN-008, Q-002 |
| DIV-012 | aberto | RF-004, Q-006 |
| DIV-013 | tratado | Q-010 |
| GAR-001 | aberto | RF-005 |
| GAR-002 | aberto | RF-001 |
| GAR-003 | aberto | RF-004 |
| GAR-004 | aberto | RF-007, RF-002 |
| GAR-005 | aberto | RN-001 |
| GAR-006 | aberto | RF-003, Q-001 |
| RIS-001 | aberto | RF-007, Q-023 |
| RIS-002 | aberto | RF-007, Q-023 |
| RIS-003 | aberto | RN-003, Q-009 |
| RIS-004 | aberto | RF-009, Q-011 |
| RIS-005 | aberto | RNF-004, Q-015 |
| RIS-006 | aberto | RNF-001 |
| RIS-007 | aberto | RF-006, RF-007, Q-011, Q-012 |
| RIS-008 | aberto | RF-004, Q-004 |
| RIS-009 | aberto | RN-004, RN-005, Q-008 |
| RIS-010 | aberto | RF-008, Q-003 |
| RIS-011 | aberto | RF-004, RNF-002, Q-006 |
| RIS-012 | aberto | RNF-003, Q-014 |
| RIS-013 | aberto | Q-014 |
| APO-001 | aberto | ponto de apoio, sem item gerado |
| APO-002 | aberto | ponto de apoio, sem item gerado |
| APO-003 | aberto | ponto de apoio, sem item gerado |
| APO-004 | aberto | ponto de apoio, sem item gerado |
| APO-005 | aberto | ponto de apoio, sem item gerado |
| APO-006 | aberto | ponto de apoio, sem item gerado |
| OPO-001 | aberto | RF-003 |
| OPO-002 | aberto | RF-004 |
| OPO-003 | aberto | RF-001 |
| OPO-004 | aberto | RF-006 |
| OPO-005 | aberto | RF-005, RN-005 |
| OPO-006 | aberto | RF-002, RNF-005 |
| OPO-007 | aberto | RF-007, RNF-001 |
| OPO-008 | aberto | RF-009 |
| OPO-009 | aberto | RN-007 |
| DIV-014 | aberto | RF-004, RF-005, RF-012, Q-025 |
| RIS-014 | aberto | Q-026, Q-028 |
| DIV-015 | aberto | RF-009, Q-032 |
| DIV-016 | aberto | RN-015, Q-030 |
| DIV-017 | aberto | Q-031 |
| RIS-015 | aberto | RF-015, RNF-007, Q-027, Q-033 |
| RIS-016 | aberto | RF-007, Q-033 |

## 4. Análise

- **Requisitos sem fonte:** nenhum.
- **Histórias sem requisito:** 0.
- **Requisitos confirmados sem história:** nenhum.
- **Requisitos sem história por estarem pendentes:** RN-005, RF-008, RNF-001, RNF-002, RNF-003, RNF-004.
- **Achados `tratado`:** DIV-001, DIV-002, DIV-004, DIV-006, DIV-008, DIV-011, DIV-013. A regra foi decidida, e o que restou está ligado a outra pergunta ou risco.
- **Riscos sem requisito, só com pergunta:** RIS-013, RIS-014.
- **Mudanças:** CR-001, CR-002, CR-003, CR-004, CR-005; histórico por requisito em `[método]requisitos.md`.
- **Fontes de menor autoridade:** RN-006 e RF-006 (parte de reserva), RN-007 e RF-013 vieram do PO, no lugar dos donos (RIS-014).
