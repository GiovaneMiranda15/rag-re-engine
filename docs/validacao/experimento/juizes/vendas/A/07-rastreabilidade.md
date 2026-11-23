# Rastreabilidade — requisitos, fontes e backlog

"Resp." aponta para `respostas.md`, e M-01 e M-02 para `mudancas/`. Diagnóstico aponta para `01-diagnostico.md`. RF, RN e PA estão em `02-negocio.md`, RNF em `03-tecnico.md`, e histórias em `04-backlog.md`. As histórias listadas abaixo foram extraídas do próprio backlog.

## 1. Requisitos funcionais

| Requisito | Descrição | Fontes | Resp. | Diagnóstico | Histórias |
|---|---|---|---|---|---|
| RF-01 | Cadastro único PJ e PF | escopo; schemas ERP e loja; política 2 | — | D-14, D-15, D-16 | US-009, US-012 |
| RF-02 | Vários usuários por cliente | schema loja | — | D-15 | US-010 |
| RF-03 | Carteira com histórico | ERD; schema ERP; planilha | — | D-09, D-27 | US-011 |
| RF-04 | Consentimento e reconfirmação | política 6; schema loja | 14 | D-17 | US-015, US-016, US-050 |
| RF-05 | Migrar e unificar clientes | escopo; schemas | 9, 15 | D-15, D-16 | US-013, US-014 |
| RF-06 | Tabela de preços única | escopo; política 4 | 9 | D-18, D-38 | US-007, US-020 |
| RF-07 | Pedidos multicanal | escopo; manual 5 | 10 | D-34 | US-017, US-018, US-019, US-022 |
| RF-08 | Web responsiva | ata de kickoff | 10, 12 | D-33 | US-018 |
| RF-09 | Ciclo de vida e consulta | schema ERP; schema loja | 10 | D-35 | US-004, US-021, US-022 |
| RF-10 | Faixas de desconto | política 1; schema ERP; integração; M-01 item 3 | 2 | D-01, D-03 | US-002, US-025 |
| RF-11 | Aprovação, substituto e trilha | política 1; ata de kickoff | 2 | D-02, D-05 | US-026, US-027 |
| RF-12 | Cupons na política | schema loja; integração; M-01 item 3 | 2, 3 | D-03 | US-028, US-029, US-030 |
| RF-13 | Reservar e liberar estoque | manual 3; escopo | 10, 11 | D-19, D-20 | US-032, US-033 |
| RF-14 | Disponibilidade comum | escopo; integração; M-02 | 11 | D-20, D-40 | US-031 |
| RF-15 | Conciliar reserva e baixa | manual 3; M-02 | 9 | D-19, D-39 | US-034 |
| RF-16 | Pedido e faturamento por API | ata de kickoff; escopo; M-02 | 7, 9, 10 | D-29, D-30, D-31, D-41 | US-001, US-002, US-003, US-004, US-029 |
| RF-17 | Sincronizar cliente e preço | ata de kickoff; integração | 7, 9 | D-14, D-29, D-40 | US-001, US-006, US-007, US-012 |
| RF-18 | Monitorar e reprocessar | integração; M-02 | 10 | R-04, R-16 | US-005 |
| RF-19 | Análise manual com SLA | política 3; manual 2 | 13 | D-06, D-11, D-13 | US-002, US-023 |
| RF-20 | Dispensa em cartão e Pix | integração; schema ERP | 13 | D-12 | US-002, US-024 |
| RF-21 | Aprovação automática de bom pagador | ata de kickoff | 1, 10 | D-07, D-08, D-36 | US-035, US-036 |
| RF-22 | Regras de comissão configuráveis | ata de kickoff; política 5 | 6 | D-28 | US-038 |
| RF-23 | Cálculo automático | escopo; planilha; schema ERP; M-01 itens 1 e 2 | 4, 10 | D-21, D-23, D-25, D-26, D-42 | US-037, US-039 |
| RF-24 | Estorno por devolução | planilha; ERD | 5 | D-24 | US-040 |
| RF-25 | Fechamento, comparação e extrato | planilha; ata de kickoff | 4, 6 | D-21, D-22 | US-041, US-042, US-043 |
| RF-26 | Painel em até 5 minutos | ata de kickoff; M-02 | 10, 11 | D-31, D-41 | US-044, US-045 |
| RF-27 | Encerrar CSV | ata de kickoff; escopo; integração | 7 | D-29 | US-008, US-019, US-051 |
| RF-28 | Continuidade da planilha | planilha; M-01 itens 1 e 2 | 4, 10 | D-37 | US-003, US-043, US-048 |
| RF-29 | Proteção e implantação | ata de kickoff; integração | 10, 15 | R-03, R-04, R-05, R-12 | US-017, US-030, US-046, US-047, US-051, US-052, US-055 |
| RF-30 | Catálogo e pré-pedido offline | ata de kickoff; M-01 item 4 | 12 (superada) | D-33, R-17 | US-054, US-055, US-056, US-057 |
| RF-31 | Sincronização e divergências | M-01 item 4 | 12 (em aberto) | D-33, R-18 | US-054, US-058, US-059 |
| RF-32 | Dados no dispositivo | M-01 item 4; política 6 | 14 | R-08 | US-060 |

## 2. Regras de negócio

| Regra | Descrição | Fontes | Resp. | Histórias |
|---|---|---|---|---|
| RN-01 | Faixas de 15% e 20% | política 1; M-01 item 3 | 2 | US-025, US-026 |
| RN-02 | Política para todos, inclusive cupom | política 1; integração | 2, 3 | US-025, US-029 |
| RN-03 | Cupom acima do limite autorizado | schema loja; M-01 item 3 | 3 | US-028 |
| RN-04 | Tabela única no novo sistema | política 4 | 9 | US-020 |
| RN-05 | Análise em 1 dia útil | política 3 | — | US-023 |
| RN-06 | Bom pagador e 120% | ata de kickoff | 1 | US-035, US-036 |
| RN-07 | Cartão e Pix dispensam análise | integração | 13 | US-024 |
| RN-08 | Regras de comissão da planilha e da ata | planilha; M-01 itens 1 e 2 | 4 | US-037, US-039, US-048 |
| RN-09 | Estorno por devolução | planilha | 5 | US-037, US-040 |
| RN-10 | Reserva na confirmação | escopo | 11 | US-032, US-057, US-058 |
| RN-11 | Baixa no faturamento | manual 3 | 9 | US-034 |
| RN-12 | NF-e no VendaMax | escopo; ata de kickoff | 9 | US-003, US-004 (por RF-16) |
| RN-13 | Consentimento explícito | política 6 | 14 | US-015, US-016 |
| RN-14 | Regras sem TI, política de aprovação | ata de kickoff; política 5 | 6 | US-038 |
| RN-15 | Fechamento dia 5, pagamento dia 10 | planilha | — | US-041 |
| RN-16 | PJ e PF profissional | política 2 | — | US-009, US-012 |

## 3. Requisitos não funcionais

| Requisito | Descrição | Origem (Resp. ou mudança) | Histórias |
|---|---|---|---|
| RNF-01 | Painel até 5 minutos | 11 | US-044, US-045 |
| RNF-02 | Capacidade | 15 | US-014, US-020, US-031, US-053 |
| RNF-03 | Integração por API | 7; M-02 | US-001, US-003, US-008 |
| RNF-04 | Auditoria | derivado | US-011, US-021, US-023, US-026, US-027, US-028, US-036, US-038 |
| RNF-05 | LGPD | 14 | US-015, US-016, US-022, US-042, US-050, US-060 |
| RNF-06 | Disponibilidade e recuperação | 15 | US-047, US-049 |
| RNF-07 | Observabilidade | derivado | US-005, US-045, US-046, US-049 |
| RNF-08 | Web responsiva | 12 | US-018 |
| RNF-09 | Consistência de estoque | 11 (derivado) | US-032, US-053 |
| RNF-10 | Idempotência | derivado | US-003, US-005, US-006, US-058 |
| RNF-11 | Atraso de estoque | 11 (pendente) | US-031 |
| RNF-12 | Limite de 60 requisições por minuto | M-02 | US-003, US-004, US-005, US-007, US-031, US-053 |
| RNF-13 | Dados no dispositivo | M-01 item 4 (derivado) | US-056, US-060 |
| RNF-14 | Detecção de faturamento por consulta | M-02 | US-004, US-034 |

## 4. Pendências que bloqueiam ou condicionam histórias

| Pendência | Histórias |
|---|---|
| PA-01 | US-001, US-004, US-006, US-007, US-031, US-034 |
| PA-02 | US-002, US-012 |
| PA-03 | US-012 |
| PA-04 | US-027 |
| PA-05 | US-025, US-026 |
| PA-06 | US-028, US-029, US-030 |
| PA-07 | US-035, US-036 |
| PA-08 | US-023, US-024 |
| PA-09 | US-011, US-037 |
| PA-10 | US-037, US-040 |
| PA-11 | US-038, US-041, US-043 |
| PA-12 | US-006, US-014, US-020, US-031 |
| PA-13 | US-021, US-031, US-032, US-033 |
| PA-14 | US-044 |
| PA-15 | US-008, US-017, US-051 |
| PA-16 | US-015, US-016, US-037, US-050, US-060 |
| PA-17 | US-049 |
| PA-19 | US-054, US-057, US-059 |
| PA-20 | US-037, US-039, US-048 |
| PA-21 | US-025, US-028 |
| PA-22 | US-055 |

**Pendências sem história associada:** PA-18. Não bloqueiam diretamente uma história do backlog da v1, mas continuam com responsável em `02-negocio.md`.

## 5. Destino dos achados do diagnóstico

| Achado | Tratamento |
|---|---|
| D-01 | RF-10, US-002, US-025 |
| D-02 | RF-11, US-026 |
| D-03 | RF-12, US-028 a US-030. PA-06 em aberto |
| D-04 | RN-08. Corte de 8% em PA-09 |
| D-05 | US-026, US-027. PA-04 e PA-05 em aberto |
| D-06 | RF-19, US-023 |
| D-07 | C-03, RN-06, US-036 |
| D-08 | PA-07, US-035 |
| D-09 | RF-03, US-011 |
| D-11 | PR-04, PR-05, R-15, PA-08 |
| D-12 | RN-07, US-001, US-024 |
| D-13 | PR-10, US-036 |
| D-14 | RF-01, US-012. PA-03 em aberto |
| D-15 | RF-01, RF-02, US-013 |
| D-16 | US-006, US-013 |
| D-17 | RF-04, US-015, US-016 |
| D-18 | RN-04, US-020. Exceções em PA-12 |
| D-19 | RF-13, RF-15, US-032, US-034 |
| D-20 | RF-14, US-031 |
| D-21 | RN-08, US-039, US-043 |
| D-22 | Planilha prevalece (Resp. 4). Sem história |
| D-23 | PA-10, US-037 |
| D-24 | PA-10, US-021, US-040 |
| D-25 | US-039, ADR-04 |
| D-26 | PA-09, US-037 |
| D-27 | US-011, PA-10 |
| D-28 | C-05, US-038 |
| D-29 | C-07, US-001 |
| D-30 | PA-02, US-002 |
| D-31 | RNF-01, RNF-14, US-004, US-044. Atraso de estoque em PA-13 |
| D-32 | RN-12, PA-18 |
| D-33 | E10, RF-30 a RF-32, PA-19, PA-22 |
| D-34 | PA-15, US-017, US-051 |
| D-35 | US-021, US-024 |
| D-36 | C-01, E6 |
| D-37 | C-02, US-048 |
| D-38 | C-04, US-007 |
| D-39 | C-08, US-034 |
| D-40 | RNF-12, US-001, US-031 |
| D-41 | RNF-14, C-12, US-004, US-044 |
| D-42 | PA-20, PA-21 |
| R-01 | US-001, US-002 |
| R-02 | PA-15, PA-22, US-055 |
| R-03 | US-047 |
| R-04 | US-046 |
| R-05 | US-017, PA-15 |
| R-06 | US-037, US-043 |
| R-07 | US-036 |
| R-08 | US-015, US-016, US-050, US-060 |
| R-09 | PA-16, PA-20, US-037 |
| R-10 | US-013, US-014 |
| R-11 | PA-12 |
| R-12 | US-052 |
| R-13 | PA-06, US-030 |
| R-14 | US-001 |
| R-15 | PR-04, PA-08 |
| R-16 | US-003 a US-005, US-053 |
| R-17 | PA-22, US-055 |
| R-18 | US-057, US-059 |

## 6. Comunicações novas

| Afirmação | Classificação | Requisitos afetados | Histórias |
|---|---|---|---|
| M-01.1 Interno a 6% acima da meta | conflitante | RN-08, RF-23, RF-28 | US-037, US-039, US-043, US-048 |
| M-01.2 Bônus de meta para representantes | conflitante | RN-08, RF-23, RF-28 | US-037, US-039, US-043, US-048 |
| M-01.3 Desconto sem aprovação a 15% | conflitante | RN-01, RN-03, RF-10, RF-12 | US-025, US-028, US-030 |
| M-01.4 App offline na v1 | conflitante | RF-30, RF-31, RF-32, RNF-13 | US-018, US-032, US-052, US-054 a US-060 |
| M-02.1 API REST existe | complementar | RNF-03 | US-001 |
| M-02.2 API cria pedido | complementar | RF-16 | US-001, US-003 |
| M-02.3 API consulta faturamento | complementar | RF-16, RF-15 | US-004, US-034 |
| M-02.4 Limite de 60 por minuto | novo | RNF-12 | US-001, US-003, US-004, US-005, US-007, US-031, US-053 |
| M-02.5 Sem webhook | novo | RNF-14, RNF-01 | US-004, US-034, US-044 |
| M-02.6 Consulta periódica | complementar | RF-15, RF-16, RNF-14 | US-004, US-034 |

## 7. Cobertura

- Backlog: 10 épicos, 27 features e 60 histórias (49 Must e 11 Should).
- Requisitos funcionais sem história: 0.
- Regras sem citação direta em história: RN-12. Ela é atendida pelas histórias indicadas na seção 2.
- Requisitos não funcionais sem história: nenhum.
