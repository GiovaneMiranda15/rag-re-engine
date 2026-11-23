# Matriz de rastreabilidade

| Requisito | Status | Fontes | Sistemas | Achados | Histórias | Perfis | Depende de |
|---|---|---|---|---|---|---|---|
| RN-001 | conflito | doc:geral/politica-RH-012-admissao-integracao.md#0, doc:geral/manual-admissao-lojas-v3.2-2019.md#1, sql:SIS-01/folhacerta_dump.sql:contrato.dias_experiencia, entrevista:juridico-compliance Q-004 (Marina Quintela) | SIS-01 | DIV-003 | US-015, US-020 | juridico-compliance | — |
| RN-002 | confirmado | doc:geral/politica-RH-012-admissao-integracao.md#1, doc:SIS-03/LEIA-ME.md#0, sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato, entrevista:juridico-compliance Q-005 (Fábio Arantes e Marina Quintela), entrevista:operacoes Q-015, doc:geral/M-02-email-juridico-2026-10-30.md#0 | SIS-01 | DIV-004, RIS-001 | US-008, US-009, US-032, US-033 | juridico-compliance, sesmt | — |
| RN-003 | confirmado | doc:geral/politica-RH-012-admissao-integracao.md#1, doc:SIS-03/LEIA-ME.md#0, sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato, entrevista:juridico-compliance Q-006 (Beatriz Lobo), doc:geral/M-01-ata-comite-2026-10-28.md#0 | SIS-01 | DIV-005, RIS-002 | US-010 | juridico-compliance | — |
| RN-004 | conflito | doc:geral/politica-RH-012-admissao-integracao.md#0, sql:SIS-02/recrutamais_dump.sql:oferta.aprovador_perfil, sql:SIS-01/folhacerta_dump.sql:cargo_piso, entrevista:negocio Q-007 | SIS-02 | DIV-006, DIV-007 | — | negocio | — |
| RN-005 | confirmado | doc:geral/politica-RH-012-admissao-integracao.md#1, doc:geral/manual-admissao-lojas-v3.2-2019.md#1, doc:SIS-04/lms-estrutura.md#0, entrevista:negocio Q-008 (Beatriz Lobo) | SIS-04 | DIV-008 | US-013 | negocio, juridico-compliance | — |
| RN-006 | confirmado | doc:geral/politica-RH-012-admissao-integracao.md#0, doc:geral/fluxo-admissao-atual.md#0, sql:SIS-01/folhacerta_dump.sql:chk_tipo_contrato, entrevista:negocio Q-001 (Helena Vasconcelos), entrevista:departamento-pessoal Q-009 (Rogério Tavares) | SIS-01 | DIV-009, RIS-007 | US-032 | departamento-pessoal | — |
| RN-007 | confirmado | doc:geral/politica-RH-012-admissao-integracao.md#2, sql:SIS-02/recrutamais_dump.sql:sp_expurgo_candidatos, entrevista:encarregada-dados Q-012 (Paula Nogueira) | SIS-02 | DIV-010 | US-029, US-030 | encarregada-dados | — |
| RN-008 | confirmado | doc:geral/politica-RH-012-admissao-integracao.md#1, sql:SIS-01/folhacerta_dump.sql:GRANT rh_loja, entrevista:encarregada-dados Q-012 (Paula Nogueira), entrevista:encarregada-dados Q-013 (Paula Nogueira) | SIS-01 | DIV-011 | US-012, US-025, US-028 | encarregada-dados, sesmt | — |
| RN-009 | hipótese | doc:SIS-03/LEIA-ME.md#1, sql:SIS-01/folhacerta_dump.sql:contrato.status, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0, doc:geral/politica-RH-012-admissao-integracao.md#1, entrevista:departamento-pessoal Q-010 (Rogério Tavares), doc:geral/M-02-email-juridico-2026-10-30.md#0 | SIS-01 | DIV-014, RIS-001 | — | departamento-pessoal, juridico-compliance | — |
| RN-010 | confirmado | doc:geral/comunicado-dp-07-2024.md#0, doc:geral/politica-RH-012-admissao-integracao.md#0, doc:SIS-03/LEIA-ME.md#0, entrevista:departamento-pessoal Q-011 (Rogério Tavares) | SIS-03 | DIV-012 | US-018 | departamento-pessoal | — |
| RF-001 | confirmado | doc:escopo.md, entrevista:negocio Q-002 (Helena Vasconcelos) | — | GAR-008, OPO-005 | US-001, US-002 | operacoes | — |
| RF-002 | confirmado | doc:escopo.md, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0, entrevista:negocio Q-002 (Helena Vasconcelos) | SIS-01, SIS-02 | GAR-001, OPO-001 | US-019, US-020, US-021 | departamento-pessoal | — |
| RF-003 | confirmado | doc:escopo.md, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0, entrevista:negocio Q-002 (Helena Vasconcelos) | — | GAR-002, OPO-002 | US-016, US-017, US-034 | departamento-pessoal | — |
| RF-004 | confirmado | doc:escopo.md, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1 | — | GAR-003, OPO-003 | US-012 | sesmt | — |
| RF-005 | confirmado | doc:escopo.md, sql:SIS-01/folhacerta_dump.sql:fn_gera_esocial | SIS-01 | GAR-004 | US-005 | departamento-pessoal | — |
| RF-006 | confirmado | doc:escopo.md, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1 | — | DIV-015, GAR-005, OPO-006, RIS-003 | US-006 | operacoes, software-architect | — |
| RF-007 | confirmado | doc:escopo.md, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1, doc:SIS-04/lms-estrutura.md#0 | SIS-04 | GAR-006, OPO-004, RIS-008 | US-013, US-014 | operacoes | — |
| RF-008 | confirmado | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#0, entrevista:departamento-pessoal Q-003 (Rogério Tavares) | SIS-01, SIS-02, SIS-03 | DIV-002, OPO-007 | US-007 | negocio | — |
| RF-009 | confirmado | doc:escopo.md, sql:SIS-01/folhacerta_dump.sql:contrato, entrevista:juridico-compliance Q-004 (Marina Quintela) | SIS-01 | RIS-006 | US-015 | departamento-pessoal | — |
| RF-010 | hipótese | sql:SIS-01/folhacerta_dump.sql:cargo_piso | — | OPO-008 | — | juridico-compliance | — |
| RNF-001 | hipótese | doc:escopo.md | — | RIS-013 | — | juridico-compliance | — |
| RNF-002 | confirmado | doc:geral/politica-RH-012-admissao-integracao.md#1, doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1, entrevista:negocio Q-002 (Helena Vasconcelos) | — | OPO-009, RIS-004, RIS-005 | US-001, US-016, US-024, US-026 | encarregada-dados | — |
| RNF-003 | hipótese | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1 | — | RIS-003 | — | operacoes | — |
| RF-011 | confirmado | doc:escopo.md | SIS-02 | GAR-008 | US-003 | operacoes | — |
| RF-012 | alterado | entrevista:negocio Q-002 (Helena Vasconcelos), entrevista:juridico-compliance Q-005 (Fábio Arantes e Marina Quintela), entrevista:juridico-compliance Q-006 (Beatriz Lobo), doc:geral/M-02-email-juridico-2026-10-30.md#0 | SIS-01 | DIV-014, RIS-001, RIS-002 | US-002, US-008, US-010, US-011, US-033 | negocio, juridico-compliance | RN-016 |
| RF-013 | confirmado | doc:escopo.md, sql:SIS-01/folhacerta_dump.sql:contrato.status | SIS-01 | DIV-014 | US-004, US-011 | departamento-pessoal | — |
| RF-014 | confirmado | entrevista:negocio Q-002 (Helena Vasconcelos) | SIS-03 | OPO-009, RIS-004 | US-023, US-024 | negocio, operacoes | — |
| RF-015 | confirmado | entrevista:departamento-pessoal Q-009 (Rogério Tavares), sql:SIS-01/folhacerta_dump.sql:fn_valida_contrato, sql:SIS-01/folhacerta_dump.sql:chk_tipo_contrato | SIS-01 | DIV-009, RIS-007 | US-031, US-032 | departamento-pessoal | — |
| RF-016 | hipótese | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1 | — | OPO-003 | — | sesmt | — |
| RF-017 | hipótese | doc:geral/ata-2026-09-22-grupo-trabalho-admissao.md#1, doc:SIS-04/lms-estrutura.md#0 | SIS-04 | GAR-006, OPO-004 | — | operacoes | — |
| RF-018 | hipótese | sql:SIS-01/folhacerta_dump.sql:contrato | SIS-01 | RIS-006 | — | juridico-compliance, departamento-pessoal | — |
| RN-011 | confirmado | entrevista:negocio Q-007 (Rogério Tavares), sql:SIS-01/folhacerta_dump.sql:cargo_piso | SIS-01, SIS-02 | DIV-007 | US-022 | departamento-pessoal | — |
| RN-012 | confirmado | entrevista:encarregada-dados Q-012 (Paula Nogueira) | SIS-02, SIS-03 | RIS-005 | US-027 | encarregada-dados | — |
| RN-013 | confirmado | entrevista:encarregada-dados Q-012 (Paula Nogueira) | SIS-02 | RIS-005 | US-028 | encarregada-dados | — |
| RN-014 | hipótese | doc:geral/politica-RH-012-admissao-integracao.md#1, entrevista:departamento-pessoal Q-003 (Rogério Tavares), doc:geral/M-02-email-juridico-2026-10-30.md#0 | SIS-01 | DIV-011, DIV-017 | — | sesmt, encarregada-dados | — |
| RN-015 | confirmado | entrevista:departamento-pessoal Q-003 (Rogério Tavares), sql:SIS-01/folhacerta_dump.sql:contrato.status | SIS-01 | DIV-002 | US-007 | departamento-pessoal | — |
| RNF-004 | hipótese | — | — | RIS-014 | — | software-architect | — |
| RNF-005 | hipótese | — | — | RIS-014 | — | software-architect | — |
| RN-017 | conflito | doc:geral/M-01-ata-comite-2026-10-28.md#0 | SIS-01 | — | US-015, US-020 | operacoes, juridico-compliance | — |
| RN-016 | confirmado | doc:geral/M-02-email-juridico-2026-10-30.md#0 | SIS-01 | — | US-002, US-033 | juridico-compliance, sesmt | — |
| RF-019 | confirmado | doc:geral/M-02-email-juridico-2026-10-30.md#0 | SIS-01, SIS-02 | — | US-034 | juridico-compliance, departamento-pessoal | — |
| RF-020 | confirmado | doc:geral/M-02-email-juridico-2026-10-30.md#0 | SIS-01 | — | US-035 | juridico-compliance, departamento-pessoal | — |

**Sem fonte (órfãos):** RNF-004, RNF-005

**Confirmados/validados sem história direta:** nenhum
