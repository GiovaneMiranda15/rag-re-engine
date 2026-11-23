# Matriz de rastreabilidade

| Requisito | Status | Fontes | Sistemas | Achados | Histórias | Perfis | Depende de |
|---|---|---|---|---|---|---|---|
| RN-001 | confirmado | doc:geral/politica-comercial.md#0, doc:geral/ata-kickoff.md#0, entrevista:comercial Q-001, doc:geral/M-01-ata-diretoria.md#0 | SIS-04, SIS-01, SIS-03 | DIV-001, GAR-005 | US-010, US-011, US-012, US-014 | comercial | — |
| RN-002 | confirmado | doc:SIS-02/regras-comissao.md#0, doc:geral/ata-kickoff.md#0, entrevista:financeiro Q-004, doc:geral/M-01-ata-diretoria.md#0 | SIS-04, SIS-02 | DIV-002, DIV-009, DIV-010 | US-019 | financeiro | — |
| RN-003 | confirmado | doc:geral/politica-comercial.md#0, sql:SIS-03/schema.sql:clientes, doc:SIS-03/integracao-erp.md#0 | SIS-04, SIS-01, SIS-03 | DIV-003, RIS-003 | US-001 | comercial, financeiro | — |
| RN-004 | confirmado | doc:geral/politica-comercial.md#0, doc:SIS-01/manual-pedido.md#0, entrevista:financeiro Q-008 | SIS-04 | DIV-004, DIV-006, RIS-009 | US-025 | financeiro | — |
| RN-005 | conflito | doc:geral/ata-kickoff.md#0, entrevista:negocio Q-007 | SIS-04 | DIV-005, OPO-005, RIS-009 | — | negocio, financeiro | — |
| RN-006 | confirmado | doc:SIS-01/manual-pedido.md#0, doc:SIS-03/integracao-erp.md#0, doc:escopo.md, entrevista:operacoes Q-012 | SIS-04, SIS-01 | DIV-007 | US-015 | operacoes | — |
| RN-007 | confirmado | doc:geral/politica-comercial.md#0, entrevista:juridico-compliance Q-014 | SIS-04 | DIV-008, OPO-009 | US-003, US-004 | juridico-compliance | — |
| RN-008 | confirmado | doc:geral/politica-comercial.md#0, doc:escopo.md, entrevista:comercial Q-002 | SIS-04 | DIV-011 | US-009 | comercial | — |
| RF-001 | confirmado | doc:escopo.md, doc:SIS-03/integracao-erp.md#0, entrevista:gestao-pmo Q-011 | SIS-04 | DIV-003, GAR-002, OPO-003 | US-001, US-002 | comercial | — |
| RF-002 | confirmado | doc:escopo.md, doc:geral/ata-kickoff.md#0, entrevista:gestao-pmo Q-011 | SIS-04 | GAR-004, OPO-006 | US-005, US-006, US-007 | comercial | — |
| RF-003 | confirmado | doc:geral/politica-comercial.md#0, doc:geral/ata-kickoff.md#0, entrevista:comercial Q-001, entrevista:gestao-pmo Q-011, doc:geral/M-01-ata-diretoria.md#0 | SIS-04 | DIV-001, GAR-006, OPO-001 | US-011, US-012 | comercial | — |
| RF-004 | confirmado | doc:escopo.md, doc:geral/ata-kickoff.md#0, doc:geral/politica-comercial.md#0, doc:SIS-02/regras-comissao.md#0, entrevista:financeiro Q-004, entrevista:gestao-pmo Q-011, entrevista:negocio Q-013 | SIS-04 | DIV-002, DIV-012, GAR-003, OPO-002, RIS-008, RIS-011 | US-019 | financeiro | — |
| RF-005 | confirmado | doc:SIS-01/manual-pedido.md#0, doc:geral/politica-comercial.md#0, entrevista:financeiro Q-008, entrevista:negocio Q-013 | SIS-04 | DIV-004, GAR-001, OPO-005 | US-025 | financeiro | — |
| RF-006 | confirmado | doc:escopo.md, doc:SIS-03/integracao-erp.md#0, doc:SIS-01/manual-pedido.md#0, entrevista:gestao-pmo Q-011, entrevista:operacoes Q-012 | SIS-04, SIS-01 | DIV-007, OPO-004, RIS-007 | US-016 | operacoes | — |
| RF-007 | confirmado | doc:geral/ata-kickoff.md#0, doc:escopo.md, entrevista:software-architect Q-010, entrevista:gestao-pmo Q-011, doc:geral/M-02-email-ti.md#0 | SIS-04, SIS-01 | GAR-004, OPO-007, RIS-001, RIS-002, RIS-007 | US-017, US-018 | software-architect, backend-engineer | — |
| RF-008 | hipótese | doc:escopo.md, sql:SIS-01/schema.sql:cliente, sql:SIS-03/schema.sql:clientes, entrevista:juridico-compliance Q-014 | SIS-04, SIS-01, SIS-03 | RIS-010 | — | dba | — |
| RF-009 | confirmado | doc:geral/ata-kickoff.md#0, entrevista:gestao-pmo Q-011, doc:geral/M-01-ata-diretoria.md#0 | SIS-04 | OPO-008, RIS-004 | US-031, US-032, US-033 | comercial, gestao-pmo | — |
| RNF-001 | hipótese | doc:SIS-03/integracao-erp.md#0 | SIS-04 | OPO-007, RIS-006 | — | devops | — |
| RNF-002 | hipótese | doc:geral/politica-comercial.md#0, doc:geral/ata-kickoff.md#0, doc:SIS-02/regras-comissao.md#0 | SIS-04 | RIS-011 | — | security, financeiro | — |
| RNF-003 | hipótese | doc:geral/politica-comercial.md#0, entrevista:juridico-compliance Q-014 | SIS-04 | DIV-008, RIS-012 | — | juridico-compliance, security | — |
| RNF-004 | hipótese | doc:geral/ata-kickoff.md#0, entrevista:devops Q-015 | SIS-04 | RIS-005 | — | devops | — |
| RNF-005 | confirmado | doc:geral/ata-kickoff.md#0, entrevista:negocio Q-013, doc:geral/M-02-email-ti.md#0 | SIS-04 | OPO-006 | US-027 | negocio | — |
| RN-009 | confirmado | entrevista:comercial Q-001, doc:geral/M-01-ata-diretoria.md#0 | SIS-04 | DIV-001, GAR-005 | US-014 | comercial | — |
| RN-010 | confirmado | entrevista:financeiro Q-008, doc:SIS-03/integracao-erp.md#0 | SIS-04 | DIV-006 | US-026 | financeiro | — |
| RN-011 | confirmado | doc:SIS-02/regras-comissao.md#0, entrevista:financeiro Q-004 | SIS-04 | DIV-002 | US-020 | financeiro | — |
| RN-012 | confirmado | doc:SIS-02/regras-comissao.md#0, entrevista:financeiro Q-004 | SIS-04 | DIV-002, DIV-010 | US-021 | financeiro | — |
| RN-013 | confirmado | doc:SIS-02/regras-comissao.md#0, entrevista:financeiro Q-005 | SIS-04 | DIV-009 | US-022 | financeiro | — |
| RN-014 | confirmado | doc:SIS-02/regras-comissao.md#0, entrevista:financeiro Q-004 | SIS-04 | DIV-002 | US-023 | financeiro | — |
| RF-010 | confirmado | doc:geral/ata-kickoff.md#0, entrevista:financeiro Q-006, doc:geral/M-01-ata-diretoria.md#0 | SIS-04 | DIV-012, RIS-011 | US-024 | financeiro | — |
| RF-011 | confirmado | entrevista:gestao-pmo Q-011, doc:geral/M-01-ata-diretoria.md#0 | SIS-04 | OPO-008 | US-006 | comercial | — |
| RF-012 | confirmado | doc:geral/ata-kickoff.md#0, entrevista:negocio Q-013 | SIS-04 | DIV-014, OPO-006 | US-027 | negocio | — |
| RF-013 | confirmado | entrevista:juridico-compliance Q-014 | SIS-04, SIS-03 | DIV-008 | US-004 | juridico-compliance | — |
| RF-014 | confirmado | entrevista:comercial Q-001, sql:SIS-03/schema.sql:cupons | SIS-04 | DIV-001 | US-013 | comercial | — |
| RNF-006 | confirmado | entrevista:devops Q-015, doc:geral/M-02-email-ti.md#0 | SIS-04 | RIS-004 | US-008 | devops | — |
| RN-015 | confirmado | doc:geral/M-01-ata-diretoria.md#0 | SIS-04, SIS-02 | DIV-016 | US-030 | financeiro, comercial | — |
| RF-015 | confirmado | doc:geral/M-02-email-ti.md#0 | SIS-04, SIS-01 | RIS-015 | US-029 | backend-engineer | — |
| RNF-007 | confirmado | doc:geral/M-02-email-ti.md#0 | SIS-04, SIS-01 | RIS-015 | US-028 | software-architect, devops | — |

**Sem fonte (órfãos):** nenhum

**Confirmados/validados sem história direta:** nenhum
