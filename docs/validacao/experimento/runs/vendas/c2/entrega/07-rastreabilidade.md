# Rastreabilidade — Vendas Unificado

Versão 2, inclui `mudancas/`.

Liga requisitos, fontes e backlog. Gerada a partir da mesma base do backlog; verificação automática: 53 de 53 requisitos têm história, e todas as 56 histórias têm requisito.

Legenda: ESC escopo; ATA ata; POL-n Política; MAN-n manual; PLA planilha; INT integração da loja; SQL-ERP e SQL-LOJA schemas; ERD diagrama; Rn resposta n; MUD-nn.n afirmação de `mudancas/` (ver `08-mudancas.md`).

## 1. Requisito > fonte > backlog

| Requisito | Descrição | Prioridade | Situação | Fontes | Histórias |
|---|---|---|---|---|---|
| RN-01 | Cliente é identificado por CPF ou CNPJ sem máscara; o documento é a chave única do Cliente. | Must | confirmado | R12; INT; SQL-ERP; SQL-LOJA | US-011, US-015 |
| RN-02 | PJ e PF profissional são Clientes válidos em todos os fluxos, inclusive no Faturamento. | Must | confirmado; solução no ERP pendente | POL-2; INT | US-002, US-011, US-013 |
| RN-03 | A Tabela de preços é única para todos os Canais. | Must | confirmado | POL-4; ESC | US-020 |
| RN-04 | Alçadas de Desconto: até 15% (inclusive) o Vendedor; acima de 15% até 20% (inclusive) o gerente comercial; acima de 20% a diretoria. | Must | alterado por MUD-01.3; Política a revisar (CON-10); representante é premissa (PRE-05) | POL-1; ATA; MUD-01.3 | US-021, US-022, US-049, US-057 |
| RN-05 | Aprovador de Desconto acima de 15% até 20% na ausência do gerente comercial. | Must | pendente (PEND-01) | ATA; R7; MUD-01.3 | US-023 |
| RN-06 | Cupom segue a política de Desconto; Cupom acima da alçada do Vendedor (agora 15%) precisa de autorização do gerente comercial ao criar a campanha. | Must | R7 citava 12%; novo limiar é premissa (PRE-15); limite de 15% pendente | R7; INT; SQL-LOJA; MUD-01.3 | US-024, US-025 |
| RN-07 | Pedido acima do Limite de crédito exige Análise de crédito do financeiro em até 1 dia útil. | Must | confirmado (Must derivado) | POL-3; R1; MAN-2 | US-036, US-037 |
| RN-08 | Pedido em cartão ou pix dispensa Análise de crédito; boleto precisa. | Must | confirmado; exceção não consta da Política | R6; INT | US-036 |
| RN-09 | Bom pagador é o Cliente sem atraso nos últimos 12 meses; o Pedido dele é aprovado automaticamente se estiver dentro de 120% do Limite de crédito. | Should | confirmado; depende de alteração da Política e de dados de títulos (PEND-05) | R5; ATA; POL-3 | US-038, US-039 |
| RN-10 | O estoque é reservado na confirmação do Pedido, em qualquer Canal. | Must | confirmado; Pedido offline reserva só ao sincronizar (PRE-14) | R11; R1; MUD-01.4 | US-031, US-032, US-055, US-058 |
| RN-11 | Comissão segue a planilha: base líquida; interno 3% até a meta e, sobre o excedente, 5% até fevereiro e 6% a partir de março; representante 4% e bônus de meta igual ao do interno (forma pendente); Desconto acima de 8% paga metade; Pedido da loja paga 1% ao Vendedor da Carteira. | Should | alterado por MUD-01.1 e MUD-01.2; PEND-06 e PEND-11 abertas | PLA; R8; MUD-01.1; MUD-01.2 | US-040, US-041, US-043 |
| RN-12 | Devolução no mês seguinte estorna a Comissão. | Should | confirmado; parcial e mesmo mês pendentes | PLA; R9 | US-044 |
| RN-13 | Fechamento da Comissão no dia 5; pagamento no dia 10 do mês seguinte. | Should | confirmado pela planilha | PLA | US-045 |
| RN-14 | O financeiro altera as regras de Comissão sem depender de TI; as regras são aprovadas anualmente pela diretoria. | Should | confirmado; MUD-01.1 é o primeiro caso de vigência; efeito retroativo pendente | ATA; R10; POL-5; MUD-01.1 | US-042 |
| RN-15 | Consentimento de marketing é marcado explicitamente pelo Cliente; a base atual da loja precisa ser reconfirmada. | Must | confirmado (Must derivado) | POL-6; R15; SQL-LOJA | US-017, US-018 |
| RN-16 | A emissão de NF-e permanece no VendaMax, inclusive em 2027. | Must | confirmado; data final desconhecida | ESC; ATA; R2; R3 | US-002, US-007, US-008, US-013, US-034 |
| RF-01 | Manter um cadastro único de Clientes. | Must | confirmado | ESC; R1 | US-011, US-012, US-016 |
| RF-02 | Consolidar e migrar os Clientes do VendaMax e da LojaB2B. | Must | derivado | ESC; SQL-ERP; SQL-LOJA; R12; R14 | US-014, US-015, US-016 |
| RF-03 | Disponibilizar a mesma Tabela de preços a todos os Canais. | Must | confirmado | ESC; POL-4 | US-009, US-020 |
| RF-04 | Aplicar alçadas de Desconto com fluxo de aprovação. | Must | confirmado | ESC; POL-1; R1; ATA | US-021, US-022, US-023 |
| RF-05 | Gerir campanhas de Cupom sob as mesmas alçadas. | Must | confirmado | R7; INT | US-024, US-025 |
| RF-06 | Registrar e consultar Pedidos de todos os Canais no mesmo lugar. | Must | confirmado | ESC; R1 | US-003, US-026, US-027, US-028, US-029 |
| RF-07 | Oferecer digitação de Pedido em web responsiva a Vendedores internos e, com internet, a representantes. | Must | confirmado; offline em RF-25; internos é premissa (PRE-01) | R13; ATA; MAN-1 | US-026 |
| RF-08 | Reservar e liberar estoque ao longo da vida do Pedido. | Must | confirmado | R1; R11; MAN-3; INT | US-029, US-031, US-032, US-033, US-034 |
| RF-09 | Mostrar o mesmo saldo disponível em todos os Canais. | Must | confirmado | ESC; INT | US-009, US-034, US-035 |
| RF-10 | Enviar Pedidos ao VendaMax por API para Faturamento e obter o resultado por consulta periódica. | Must | operações confirmadas pelo fornecedor, via Sérgio; homologação e triggers pendentes | R1; R2; R3; ATA; MUD-02.1; MUD-02.2; MUD-02.4; MUD-02.5 | US-001, US-002, US-007, US-008, US-025, US-041, US-061 |
| RF-11 | Expor falhas de integração com alerta e responsável. | Must | derivado | INT | US-010 |
| RF-12 | Encaminhar o Pedido à Análise de crédito conforme forma de pagamento e Limite de crédito. | Must | confirmado (Must derivado) | POL-3; R6; SQL-ERP | US-012, US-036 |
| RF-13 | Oferecer fila de Análise de crédito com controle do prazo de 1 dia útil. | Must | derivado da meta de sucesso | R1; POL-3; MAN-2; ATA | US-037 |
| RF-14 | Aprovar automaticamente Pedido de bom pagador dentro de 120% do Limite de crédito. | Should | confirmado; bloqueado por PEND-05 | R1; R5; ATA | US-038, US-039 |
| RF-15 | Calcular a Comissão automaticamente pelas regras da planilha. | Should | confirmado; ver CON-02 | ESC; R1; R8; PLA; ATA; MUD-01.1; MUD-01.2 | US-040, US-041, US-043 |
| RF-16 | Permitir ao financeiro configurar regras de Comissão com vigência. | Should | confirmado; primeira alteração real em março (MUD-01.1) | ATA; R10; POL-5 | US-042 |
| RF-17 | Registrar Devolução separada de cancelamento e estornar a Comissão. | Should | derivado | PLA; R9; ERD | US-044 |
| RF-18 | Apoiar o fechamento mensal da Comissão e substituir a planilha com segurança. | Should | confirmado | R1; PLA; ATA | US-045, US-046 |
| RF-19 | Oferecer painel de vendas por Canal. | Should | confirmado; indicadores pendentes | ATA; R1; R11 | US-047 |
| RF-20 | Registrar e reconfirmar o consentimento de marketing. | Must | derivado | POL-6; R15 | US-017, US-018 |
| RF-21 | Controlar o acesso por perfil. | Must | derivado | POL-1; POL-3; R15; ATA | US-005, US-012, US-028, US-059 |
| RF-22 | Conduzir a transição dos Canais sem interromper vendas. | Must | derivado | R2; R3; ATA; INT | US-003, US-030 |
| RF-23 | Reduzir o risco da operação atual até a migração. | Should | derivado | ATA; INT | US-048 |
| RF-24 | Alinhar o limite de Desconto do VendaMax à Política (15%), se viável, antes da v1. | Could | proposta | POL-1; SQL-ERP; ATA; MUD-01.3 | US-049 |
| RF-25 | Permitir a representantes consultar dados e registrar Pedidos sem internet, em app, com sincronização posterior. | Must | alterado por MUD-01.4; classificação Must é inferência; regras em PEND-13 | MUD-01.4; ATA | US-055, US-056, US-057, US-058, US-060 |
| RNF-01 | Suportar 400 Pedidos/dia e pico de 900/dia em novembro, 4 mil Clientes ativos, 12 mil SKUs, 8 Vendedores internos e 22 representantes. | Must | confirmado | R14; R13; MUD-02.3 | US-001, US-004, US-015, US-026 |
| RNF-02 | Painel com atraso máximo de 5 minutos. | Should | confirmado | R11; ATA | US-047 |
| RNF-03 | Integração com o VendaMax por API, não por arquivo. | Must | API confirmada só para criar pedido e consultar status; demais operações pendentes (PEND-02) | ATA; R2; R3; MUD-02.1; MUD-02.2 | US-001, US-007, US-009, US-027 |
| RNF-04 | Integração idempotente: reenvio não duplica Pedido. | Must | derivado | SQL-ERP; INT | US-007, US-027, US-058 |
| RNF-05 | Reservas concorrentes não podem vender o mesmo saldo duas vezes. | Must | derivado | MAN-3; R11 | US-032, US-058 |
| RNF-06 | Trilha de auditoria para aprovações de Desconto, decisões de crédito e alterações de regras de Comissão. | Must | derivado | POL-1; POL-3; POL-5 | US-006, US-022, US-024, US-037, US-039, US-042 |
| RNF-07 | Interface de digitação utilizável em celular. | Must | confirmado | R13 | US-026 |
| RNF-08 | Tratamento de dados pessoais conforme LGPD; retenção e acesso a dados de PF a definir com jurídico externo. | Must | parcial (PEND-09) | POL-6; R15 | US-005, US-017, US-019, US-059 |
| RNF-09 | Monitoramento e alerta das integrações. | Must | derivado | INT | US-010, US-048, US-061 |
| RNF-10 | Backup com restauração testada para os dados do novo sistema e da LojaB2B enquanto ela operar. | Must | derivado | ATA | US-004, US-048 |
| RNF-11 | Consumo da API do VendaMax limitado a 60 requisições por minuto, somando criação de pedido e consulta de status, sem bloquear a digitação. | Must | novo; escopo do limite pendente (PEND-14) | MUD-02.3; MUD-02.4; MUD-02.5 | US-061 |
| RNF-12 | Dados guardados no aparelho limitados à Carteira do representante, protegidos e removíveis. | Must | derivado; regras jurídicas em PEND-09 | MUD-01.4; POL-6; R15 | US-056, US-059 |

## 2. Fonte > requisito

Mostra a cobertura de cada fonte.

| Código | Fonte | Requisitos |
|---|---|---|
| ESC | escopo.md | RN-03, RN-16, RF-01, RF-02, RF-03, RF-04, RF-06, RF-09, RF-15 |
| ATA | fontes/geral/ata-kickoff.md | RN-04, RN-05, RN-09, RN-14, RN-16, RF-04, RF-07, RF-10, RF-13, RF-14, RF-15, RF-16, RF-18, RF-19, RF-21, RF-22, RF-23, RF-24, RF-25, RNF-02, RNF-03, RNF-10 |
| ERD | fontes/geral/erd-vendamax.md | RF-17 |
| POL-1 | politica-comercial.md, item 1 | RN-04, RF-04, RF-21, RF-24, RNF-06 |
| POL-2 | politica-comercial.md, item 2 | RN-02 |
| POL-3 | politica-comercial.md, item 3 | RN-07, RN-09, RF-12, RF-13, RF-21, RNF-06 |
| POL-4 | politica-comercial.md, item 4 | RN-03, RF-03 |
| POL-5 | politica-comercial.md, item 5 | RN-14, RF-16, RNF-06 |
| POL-6 | politica-comercial.md, item 6 | RN-15, RF-20, RNF-08, RNF-12 |
| MAN-1 | manual-pedido.md, seção 1 | RF-07 |
| MAN-2 | manual-pedido.md, seção 2 | RN-07, RF-13 |
| MAN-3 | manual-pedido.md, seção 3 | RF-08, RNF-05 |
| SQL-ERP | SIS-01-erp/schema.sql | RN-01, RF-02, RF-12, RF-24, RNF-04 |
| PLA | SIS-02-comissoes/regras-comissao.md | RN-11, RN-12, RN-13, RF-15, RF-17, RF-18 |
| INT | SIS-03-loja-b2b/integracao-erp.md | RN-01, RN-02, RN-06, RN-08, RF-05, RF-08, RF-09, RF-11, RF-22, RF-23, RNF-04, RNF-09 |
| SQL-LOJA | SIS-03-loja-b2b/schema.sql | RN-01, RN-06, RN-15, RF-02 |
| R1 | respostas.md, resposta 1 | RN-07, RN-10, RF-01, RF-04, RF-06, RF-08, RF-10, RF-13, RF-14, RF-15, RF-18, RF-19 |
| R2 | respostas.md, resposta 2 | RN-16, RF-10, RF-22, RNF-03 |
| R3 | respostas.md, resposta 3 | RN-16, RF-10, RF-22, RNF-03 |
| R4 | respostas.md, resposta 4 | sem requisito direto |
| R5 | respostas.md, resposta 5 | RN-09, RF-14 |
| R6 | respostas.md, resposta 6 | RN-08, RF-12 |
| R7 | respostas.md, resposta 7 | RN-05, RN-06, RF-05 |
| R8 | respostas.md, resposta 8 | RN-11, RF-15 |
| R9 | respostas.md, resposta 9 | RN-12, RF-17 |
| R10 | respostas.md, resposta 10 | RN-14, RF-16 |
| R11 | respostas.md, resposta 11 | RN-10, RF-08, RF-19, RNF-02, RNF-05 |
| R12 | respostas.md, resposta 12 | RN-01, RF-02 |
| R13 | respostas.md, resposta 13 | RF-07, RNF-01, RNF-07 |
| R14 | respostas.md, resposta 14 | RF-02, RNF-01 |
| R15 | respostas.md, resposta 15 | RN-15, RF-20, RF-21, RNF-08, RNF-12 |
| MUD-01.1 | mudancas/M-01-ata-diretoria.md, item 1 | RN-11, RN-14, RF-15 |
| MUD-01.2 | mudancas/M-01-ata-diretoria.md, item 2 | RN-11, RF-15 |
| MUD-01.3 | mudancas/M-01-ata-diretoria.md, item 3 | RN-04, RN-05, RN-06, RF-24 |
| MUD-01.4 | mudancas/M-01-ata-diretoria.md, item 4 | RN-10, RF-25, RNF-12 |
| MUD-02.1 | mudancas/M-02-email-ti.md | RF-10, RNF-03 |
| MUD-02.2 | mudancas/M-02-email-ti.md | RF-10, RNF-03 |
| MUD-02.3 | mudancas/M-02-email-ti.md | RNF-01, RNF-11 |
| MUD-02.4 | mudancas/M-02-email-ti.md | RF-10, RNF-11 |
| MUD-02.5 | mudancas/M-02-email-ti.md | RF-10, RNF-11 |

## 3. Diagnóstico > tratamento

| Divergência | Requisitos | Histórias |
|---|---|---|
| DIV-01 | RN-04, RF-04 | US-021, US-022, US-049 |
| DIV-02 | RN-06, RF-05 | US-024, US-025 |
| DIV-03 | RN-03, RF-03 | US-020 |
| DIV-04 | RN-11, RF-15 | US-043 |
| DIV-05 | RN-11 | US-040, US-043 |
| DIV-06 | RF-16, RF-15 | US-041, US-042 |
| DIV-07 | RN-09, RF-14 | US-038, US-039 |
| DIV-08 | RN-07, RF-13 | US-037 |
| DIV-09 | RF-12 | US-036, US-038 |
| DIV-10 | RN-08 | US-002, US-036 |
| DIV-11 | RN-01, RN-02, RF-01, RF-02 | US-011, US-013, US-014, US-015 |
| DIV-12 | RF-10, RN-16 | US-001, US-002, US-007 |
| DIV-13 | RN-15, RF-20 | US-017, US-018, US-019 |
| DIV-14 | RN-10, RF-08, RF-09 | US-031, US-032, US-034, US-035 |
| DIV-15 | RF-17 | US-044 |
| DIV-16 | RN-16 | US-001 |
| DIV-17 | Vários | US-003 |
| DIV-18 | RN-02 | Sem história própria: documentação é substituída pelo novo sistema |
| DIV-19 | RF-13, RF-14 | US-003, US-037, US-039 |
| DIV-20 | RF-15, RF-18 | US-003, US-043, US-046 |
| DIV-21 | RN-08, RN-09 | US-038 |
| DIV-22 | RF-07, RF-22 | US-003, US-026 |
| DIV-23 | RN-04, RN-06 | US-021, US-024 |
| DIV-24 | RF-25, RN-10 | US-055, US-058 |
| DIV-25 | RNF-03, RF-03, RF-09 | US-001, US-009 |

## 4. Pendência > backlog

Histórias que citam a pendência na própria ficha; o bloqueio também se propaga pelas dependências.

| Pendência | Responsável | Histórias |
|---|---|---|
| PEND-01 | Paulo | US-023, US-024 |
| PEND-02 | Sérgio, com fornecedor | US-001, US-002, US-007, US-009, US-013, US-025, US-041, US-044, US-049 |
| PEND-03 | Aline | US-003, US-016, US-026, US-027, US-030 |
| PEND-04 | Paulo | US-003 |
| PEND-05 | Paulo e Renata | US-036, US-038 |
| PEND-06 | Renata | US-040, US-041, US-042, US-043, US-044, US-045, US-046 |
| PEND-07 | Paulo | US-009, US-031, US-032, US-033, US-035, US-047 |
| PEND-08 | Aline | US-012, US-014, US-016 |
| PEND-09 | Sérgio, com jurídico externo | US-005, US-018, US-019, US-059 |
| PEND-10 | Sérgio | US-004 |
| PEND-11 | Renata, com diretoria | US-043 |
| PEND-12 | Paulo | US-055 |
| PEND-13 | Aline, com representantes | US-055, US-056, US-057, US-058, US-060 |
| PEND-14 | Sérgio, com fornecedor | US-001, US-008, US-061 |

## 5. Meta > backlog

| Meta | Descrição | Requisitos | Histórias |
|---|---|---|---|
| M-01 | Zero planilha | RF-15, RF-18 | US-043, US-045, US-046 |
| M-02 | Reclamações abaixo de 3/mês | RF-15, RF-18 | US-043, US-045, US-046 |
| M-03 | Cancelamentos abaixo de 5/mês | RF-08, RF-09 | US-032, US-033, US-034, US-035 |
| M-04 | Crédito em até 1 dia útil | RF-13, RN-07 | US-037 |

## 6. Fora da v1

| Item | Origem | Motivo |
|---|---|---|
| Integração com Serasa | MAN-2; R6 | Não solicitada |
| NF-e fora do VendaMax | ESC; R2; R3 | Permanece no ERP |
| Lançamento automático na folha | PLA; R10 | PRE-12 |

App offline saiu desta lista: R13 foi substituída por MUD-01.4.

## 7. Mudança > impacto

| Afirmação | Classificação | Requisitos | Histórias |
|---|---|---|---|
| MUD-01.1 | conflitante | RN-11, RN-14, RF-15, RF-16 | US-042, US-043, US-046 |
| MUD-01.2 | conflitante | RN-11, RF-15 | US-040, US-043, US-046 |
| MUD-01.3 | conflitante | RN-04, RN-05, RN-06, RF-24 | US-021, US-022, US-023, US-024, US-049 |
| MUD-01.3a | existente | RN-06 | US-024, US-025 |
| MUD-01.4 | conflitante | RF-25, RNF-12, RN-10 | US-055, US-056, US-057, US-058, US-059, US-060 |
| MUD-02.1 | complementar | RNF-03, RF-10 | US-001 |
| MUD-02.2 | complementar | RF-10, RNF-03 | US-001, US-007, US-008, US-009 |
| MUD-02.3 | novo | RNF-11, RNF-01 | US-001, US-009, US-061 |
| MUD-02.4 | novo | RNF-11, RF-10 | US-008, US-034, US-061 |
| MUD-02.5 | complementar | RF-10, RNF-11 | US-008, US-045, US-061 |
