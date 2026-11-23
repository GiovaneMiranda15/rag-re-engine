# 07. Rastreabilidade

Liga requisitos, fontes e backlog. Abreviações: POL = POL-SUP-004 rev. 3; Portaria = DG-017/2025; Ata = Comitê de 19/08/2026 (número do item); R*n* = resposta à pergunta *n*; D-*n* = decisão a validar. RF e RN estão em `02-negocio.md`; RNF, em `03-tecnico.md`.

## 1. Requisitos, fontes e histórias

### Requisitos funcionais

| ID | Descrição | Fontes | Histórias |
|---|---|---|---|
| RF-01 | Manter cadastro único de contratos com número, unidade, fornecedor, objeto, vigência, moeda, valor mensal e global, índice, SLA de atendimento e solução, preventiva e gestor | Escopo; Ata 7; planilha; SupriMax `contrato`; ManutClin `contrato_ref`; R2, R4 | HU-001, HU-003, HU-004 |
| RF-02 | Manter cadastro único de fornecedores por CNPJ, com razão social e nome fantasia | SupriMax `fornecedor`; ManutClin `prestador`; planilha; R4 | HU-002, HU-042 |
| RF-03 | Manter unidades como cadastro, permitindo incluir novas sem desenvolvimento | Escopo; R15; M-01.1 | HU-040, HU-044 |
| RF-04 | Registrar aditivos com histórico e avisar o Jurídico | SupriMax `ultimo_aditivo_em`; regras da planilha; R4 | HU-005 |
| RF-05 | Registrar reajustes com histórico e sinalizar reajuste atrasado | POL 4.3, 4.4; SupriMax `dt_ultimo_reajuste`; R4 | HU-006 |
| RF-06 | Calcular a situação do contrato pelas datas e alertar a renovação em 120 dias | POL 4.2; regras da planilha; fluxo; R2, R3, R5 | HU-007, HU-008, HU-043 |
| RF-07 | Acompanhar a renovação, com responsável, etapa e atraso | POL 4.2; Ata 7; R5 | HU-009 |
| RF-08 | Registrar requisições com unidade, equipamento e origem | Escopo; SupriMax `requisicao`; Ata 1 | HU-011, HU-025 |
| RF-09 | Exigir cotações conforme a faixa de valor | POL 3; `fn_valida_cotacoes`; R3 | HU-012 |
| RF-10 | Encaminhar OC e contrato ao aprovador pela alçada | POL 2; `fn_valida_alcada_oc`, `fn_valida_alcada_contrato`; R2, R3 | HU-013, HU-014 |
| RF-11 | Impedir que o solicitante aprove | POL 2.3; OC-2026-00420 | HU-015 |
| RF-12 | Detectar possível fracionamento | POL 3.1; OC-2026-00301 a 00303 | HU-017 |
| RF-13 | Conduzir compra emergencial conforme a Portaria | Portaria arts. 1 a 4; OC-2026-00412; Ata 2 | HU-018 |
| RF-14 | Conduzir o parecer jurídico, com medição do tempo de cada etapa | POL 4.5; indicadores; R3, R5 | HU-020 |
| RF-15 | Manter trilha de auditoria das aprovações | R2, R14 | HU-021 |
| RF-16 | Manter regras e limites como parâmetros com vigência | R3 (ERP nunca revisto); proposta de R$ 200 mil; M-02.1 | HU-008, HU-016, HU-034 |
| RF-17 | Informar ao Comitê as compras emergenciais | Portaria art. 5; Ata 2 | HU-019 |
| RF-18 | Obter inventário e OS da Engenharia Clínica | Escopo; ManutClin; indicadores; R11 | HU-022, HU-023 |
| RF-19 | Gerar requisição a partir da OS, sem redigitação, com vínculo nos dois sentidos | Ata 5; fluxo; indicadores; R2; OS 88190, 88240 | HU-025, HU-026 |
| RF-20 | Gerar a medição mensal com as OS da competência | Ata 4; POL 5; SupriMax `medicao`; R2 | HU-027 |
| RF-21 | Registrar o ateste no sistema | POL 5.2; medição 9002; R2, R8 | HU-028 |
| RF-22 | Bloquear liberação sem ateste, sem contrato registrado ou com contrato vencido | POL 4.1, 5.2; `fn_libera_medicao`; medições 9001 e 9002; R6 | HU-004, HU-010, HU-029 |
| RF-23 | Calcular o vencimento conforme a Política e enviar a autorização ao Financeiro | POL 5.1; Portaria art. 4; `chk_prazo_pagamento`; Ata 6; OC-2026-00440 | HU-030, HU-031 |
| RF-24 | Sinalizar OS fechada sem teste ou liberação e equipamento em uso com calibração vencida | Fluxo; POL 6.3; `trg_os_fecha`; OS 88213; R10 | HU-024 |
| RF-25 | Apurar SLA de atendimento e solução por OS | POL 5.3; `contrato_ref`; OS 88170; R2, R4, R9 | HU-032, HU-033 |
| RF-26 | Calcular glosa sugerida, com teto, e registrar a decisão | POL 5.3; indicadores (glosa zero); R2, R9 | HU-034, HU-035 |
| RF-27 | Oferecer visão consolidada por contrato, fornecedor, equipamento e unidade | Escopo; Ata 1 | HU-036 |
| RF-28 | Medir os indicadores do processo | Indicadores; Ata 4 a 6; R2 | HU-037 |
| RF-29 | Calcular custo por equipamento (segunda fase) | Ata 1; indicadores; R2, R13 | HU-038 |
| RF-30 | Controlar acesso por perfil e unidade | POL 2; grants do ManutClin; R14 | HU-039 |
| RF-31 | Migrar contratos saneados e substituir a planilha | Regras da planilha; diagnóstico 3.1; R3 a R6; M-01.1 | HU-041, HU-042, HU-043, HU-044 |

### Regras de negócio

| ID | Descrição | Fontes | Histórias |
|---|---|---|---|
| RN-01 | Alçada: até R$ 50.000,00, Gerente de Suprimentos; de R$ 50.000,01 a R$ 250.000,00, Diretor Financeiro; acima, Diretora Geral | POL 2; R3; M-01.2 | HU-013, HU-014 |
| RN-02 | Base da alçada: valor total da OC; valor global de toda a vigência no contrato | POL 2.1, 2.2 | HU-005, HU-013, HU-014 |
| RN-03 | Quem solicita não pode aprovar | POL 2.3 | HU-015 |
| RN-04 | Cotações: até R$ 5.000,00, dispensa; de R$ 5.000,01 a R$ 15.000,00, duas; acima, três | POL 3; R3 | HU-012 |
| RN-05 | É vedado dividir a mesma necessidade para enquadrá-la em alçada inferior | POL 3.1 | HU-017 |
| RN-06 | Emergencial: evitar interrupção imediata da assistência por parada de equipamento; até R$ 100.000,00 por ocorrência; uma proposta; Diretor Técnico aprova em até 72 h após a emissão; pagamento pode ser inferior a 30 dias; informe ao Comitê na reunião seguinte | Portaria arts. 1 a 5 | HU-018, HU-019, HU-030 |
| RN-07 | Contrato com valor global acima de R$ 30.000,00 exige parecer antes da aprovação | POL 4.5; R3; M-02.1 (conflito, não aplicado; D-16) | HU-005, HU-016, HU-020 |
| RN-08 | Contrato é registrado antes do primeiro pagamento, inclusive se assinado na unidade | POL 1.1, 4.1; R6 | HU-004, HU-029, HU-044 |
| RN-09 | Renovação começa 120 dias antes do fim, pela área gestora e pelo Jurídico | POL 4.2; R3, R5 | HU-008, HU-009 |
| RN-10 | Reajuste: IPCA em contratos assinados desde 01/01/2024; anteriores mantêm o índice até o fim da vigência | POL 4.3; R4 | HU-006 |
| RN-11 | Moeda estrangeira: registrar na moeda do contrato, sem índice; câmbio de referência definido pelo Diretor Financeiro | POL 4.4; planilha; R13 | HU-003, HU-006, HU-014 |
| RN-12 | Pagamento: padrão de 45 dias da emissão da nota, mínimo de 30, salvo emergencial | POL 5.1; Portaria art. 4 | HU-030 |
| RN-13 | Medição só é paga após ateste da Engenharia Clínica; a decisão é da Gerente | POL 5.2; R8 | HU-028, HU-029 |
| RN-14 | Descumprimento de SLA gera glosa de 2% do valor mensal por evento, limitada a 10% por competência | POL 5.3; R9; M-02.2 | HU-034 |
| RN-15 | Nenhum equipamento volta ao uso sem teste aprovado e liberação assinada | Fluxo; R10 | HU-024 |
| RN-16 | Equipamento com calibração vencida não deve permanecer em uso | POL 6.3 | HU-024 |
| RN-17 | Criticidade em 4 níveis por equipamento; no ManutClin, A = 1, B = 2 e 3, C = 4 | POL 6.2; R11 | HU-022 |
| RN-18 | Contrato vencido não recebe pagamento, salvo exceção registrada | D-06; Ata 7 | HU-010, HU-029 |
| RN-19 | Fornecedor é único por CNPJ, com razão social e nome fantasia | SupriMax; ManutClin; R4 | HU-002 |
| RN-20 | SLA de atendimento e de solução são os do contrato assinado | R4; `contrato_ref` | HU-001, HU-032, HU-041 |

### Requisitos não funcionais

| ID | Descrição | Fontes | Histórias |
|---|---|---|---|
| RNF-01 | Auditabilidade | R2, R14; POL 2 | HU-001, HU-005, HU-010, HU-021, HU-028, HU-035 |
| RNF-02 | Privacidade | Escopo; `ordem_servico`; R14; D-13 | HU-023, HU-042 |
| RNF-03 | Controle de acesso | Grants do ManutClin; R14 | HU-039 |
| RNF-04 | Parametrização | R3; R15 | HU-016, HU-040 |
| RNF-05 | Integridade das integrações | Grants do ManutClin; R15 | HU-022, HU-031, HU-033 |
| RNF-06 | Moeda | POL 4.4; `medicao` | HU-003, HU-027, HU-036 |
| RNF-07 | Capacidade | Indicadores; R15 | Aceite geral (nota) |
| RNF-08 | Disponibilidade e recuperação | Proposta; sem fonte | Aceite geral (nota) |
| RNF-09 | Usabilidade da aprovação | Portaria art. 3; proposta | Aceite geral (nota) |
| RNF-10 | Tempo e fuso | `ordem_servico`; D-08 | HU-032 |

**Nota:** RNF-07, RNF-08 e RNF-09 valem para toda a solução e são verificados no aceite das entregas, não em história própria.

## 2. Backlog para requisitos

| História | Título | Feature | Épico | Requisitos | Observação |
|---|---|---|---|---|---|
| HU-001 | Cadastrar contrato com dados completos | F-01.1 | EP-01 | RF-01, RN-20, RNF-01 |  |
| HU-002 | Manter fornecedor único por CNPJ | F-01.1 | EP-01 | RF-02, RN-19 |  |
| HU-003 | Registrar contrato em moeda estrangeira | F-01.1 | EP-01 | RF-01, RN-11, RNF-06 |  |
| HU-004 | Exigir registro central de contrato assinado na unidade | F-01.1 | EP-01 | RF-01, RF-22, RN-08 |  |
| HU-005 | Registrar aditivo com histórico e aviso ao Jurídico | F-01.2 | EP-01 | RF-04, RN-02, RN-07, RNF-01 |  |
| HU-006 | Registrar reajuste e sinalizar atraso | F-01.2 | EP-01 | RF-05, RN-10, RN-11 | A validar: D-11 |
| HU-007 | Calcular a situação do contrato pelas datas | F-01.3 | EP-01 | RF-06 |  |
| HU-008 | Alertar renovação 120 dias antes do fim | F-01.3 | EP-01 | RF-06, RF-16, RN-09 |  |
| HU-009 | Acompanhar renovações em andamento | F-01.3 | EP-01 | RF-07, RN-09 |  |
| HU-010 | Tratar exceção de contrato vencido com serviço em andamento | F-01.3 | EP-01 | RF-22, RN-18, RNF-01 | A validar: D-06 |
| HU-011 | Criar requisição com unidade e equipamento | F-02.1 | EP-02 | RF-08 | A validar: D-12 |
| HU-012 | Exigir cotações conforme a faixa | F-02.1 | EP-02 | RF-09, RN-04 |  |
| HU-013 | Encaminhar ordem de compra pela alçada | F-02.2 | EP-02 | RF-10, RN-01, RN-02 |  |
| HU-014 | Aprovar contrato pelo valor global | F-02.2 | EP-02 | RF-10, RN-01, RN-02, RN-11 |  |
| HU-015 | Impedir que o solicitante aprove | F-02.2 | EP-02 | RF-11, RN-03 | A validar: D-05 |
| HU-016 | Parametrizar regras com vigência | F-02.2 | EP-02 | RF-16, RN-07, RNF-04 |  |
| HU-017 | Detectar possível fracionamento | F-02.3 | EP-02 | RF-12, RN-05 | A validar: D-05 |
| HU-018 | Registrar compra emergencial | F-02.4 | EP-02 | RF-13, RN-06 |  |
| HU-019 | Listar compras emergenciais para o Comitê | F-02.4 | EP-02 | RF-17, RN-06 |  |
| HU-020 | Conduzir parecer jurídico | F-02.5 | EP-02 | RF-14, RN-07 |  |
| HU-021 | Manter trilha de auditoria das aprovações | F-02.6 | EP-02 | RF-15, RNF-01 |  |
| HU-022 | Obter inventário da Engenharia Clínica | F-03.1 | EP-03 | RF-18, RN-17, RNF-05 | A validar: D-12 |
| HU-023 | Obter OS sem dados de paciente | F-03.1 | EP-03 | RF-18, RNF-02 | A validar: D-13 |
| HU-024 | Sinalizar pendências de segurança | F-03.1 | EP-03 | RF-24, RN-15, RN-16 | A validar: D-07 |
| HU-025 | Gerar requisição a partir da OS | F-03.2 | EP-03 | RF-19, RF-08 | A validar: D-01 |
| HU-026 | Registrar decisão de cobertura contratual | F-03.2 | EP-03 | RF-19 | A validar: D-01 |
| HU-027 | Gerar medição mensal com as OS da competência | F-03.3 | EP-03 | RF-20, RNF-06 |  |
| HU-028 | Atestar a medição | F-03.3 | EP-03 | RF-21, RN-13, RNF-01 | A validar: D-09 |
| HU-029 | Bloquear pagamento sem requisitos | F-03.4 | EP-03 | RF-22, RN-08, RN-13, RN-18 |  |
| HU-030 | Calcular vencimento conforme a Política | F-03.4 | EP-03 | RF-23, RN-12, RN-06 | A validar: D-10 |
| HU-031 | Enviar autorização de pagamento ao Financeiro | F-03.4 | EP-03 | RF-23, RNF-05 | A validar: D-10 |
| HU-032 | Apurar SLA de atendimento e solução por OS | F-04.1 | EP-04 | RF-25, RN-20, RNF-10 | A validar: D-08 |
| HU-033 | Registrar alterações em dados de atendimento | F-04.1 | EP-04 | RF-25, RNF-05 |  |
| HU-034 | Calcular glosa sugerida com teto | F-04.2 | EP-04 | RF-26, RN-14, RF-16 | A validar: D-08 |
| HU-035 | Decidir e aplicar a glosa na medição | F-04.2 | EP-04 | RF-26, RNF-01 | A validar: D-08 |
| HU-036 | Ver visão consolidada da rede | F-05.1 | EP-05 | RF-27, RNF-06 |  |
| HU-037 | Medir indicadores do processo | F-05.1 | EP-05 | RF-28 |  |
| HU-038 | Calcular custo por equipamento | F-05.2 | EP-05 | RF-29 | Fase 2 |
| HU-039 | Controlar acesso por perfil e unidade | F-06.1 | EP-06 | RF-30, RNF-03 |  |
| HU-040 | Manter unidades por cadastro | F-06.2 | EP-06 | RF-03, RNF-04 | A validar: D-02 |
| HU-041 | Sanear contratos contra o documento assinado | F-06.3 | EP-06 | RF-31, RN-20 |  |
| HU-042 | Migrar contratos, fornecedores e reconciliar | F-06.3 | EP-06 | RF-31, RF-02, RNF-02 | A validar: D-14 |
| HU-043 | Encerrar a planilha no corte | F-06.3 | EP-06 | RF-31, RF-06 |  |
| HU-044 | Carregar os contratos do Hospital Aurora Serra | F-06.3 | EP-06 | RF-03, RF-31, RN-08 | A validar: D-15 |

## 3. Achados do diagnóstico para tratamento

| Achado | Evidência | Tratamento |
|---|---|---|
| Vigência divergente | CT-2023-0088: ERP, planilha, R4 | RF-04, RF-06, RF-31 |
| SLA divergente | CT-2024-0117: planilha, ManutClin, R4 | RF-01, RF-31; correção no ManutClin |
| Índice divergente | CT-2025-0064: ERP, planilha, R4 | RF-05, RF-31; correção no ERP |
| Preventiva divergente | CT-2023-0019: plano do ManutClin, R4 | RF-01; correção no ManutClin |
| Nome do fornecedor | MTS e BioVolt, R4 | RF-02 |
| Contrato sem registro | CT-2026-0021, R6 | RF-01, RF-22, RF-31 |
| Contrato vencido | CT-2022-0055, Ata 7 | RF-06, RF-07, RF-22, RN-18 |
| Alçada, cotação e parecer divergentes | ERP, fluxo, POL, R3 | RF-09, RF-10, RF-14, RF-16 |
| Alçada de contrato no valor mensal | `fn_valida_alcada_contrato` | RF-10 |
| Fracionamento | OC-2026-00301 a 00303 | RF-12 |
| Sem segregação | OC-2026-00420 | RF-11 |
| Prazo de pagamento | `chk_prazo_pagamento`, POL 5.1, OC-2026-00440 | RF-23 |
| Medição sem ateste | Medição 9002 | RF-21, RF-22 |
| Glosa não aplicada | OS 88170, medição 9003 | RF-25, RF-26 |
| Moeda misturada | Medição 9004 | RF-01, RNF-06 |
| Retorno ao uso sem liberação | OS 88213, `trg_os_fecha` | RF-24; ação imediata |
| Calibração vencida em uso | PAT-004512 | RF-24; ação imediata |
| Dado de paciente exposto | Grants, `ordem_servico` | RNF-02; ação imediata |
| SLA alterável pelo prestador | Grant de UPDATE | HU-033; ação imediata |
| Redigitação de OS | Ata 5 | RF-19 |
| Custo por equipamento | Ata 1, R2 | RF-08 (dado), RF-29 (fase 2) |
| Renovação tardia | R5, POL 4.2 | RF-06, RF-07; ação imediata |
| Quinta unidade | R15, M-01.1 | RF-03, RF-31; D-02, D-15; HU-044 |
| Criticidade em três escalas | POL 6.2, ManutClin, planilha, R11 | RF-18, RN-17 |

## 4. Lacunas

- **Sem documento assinado:** os textos dos contratos não foram fornecidos (R4). Os dados de contrato vêm das bases e de R4.
- **Fora do backlog por decisão:** portal do prestador (R14), condução de evento adverso (D-07), pagamento efetivo (D-10).
- **RN-14:** o teto de 10% vem de R9 e M-02.2, sem norma aprovada pela Diretoria.
- **RN-07:** M-02.1 conflita com a norma; decisão pendente (D-16).
- **Pedido da Farmácia (M-01.3):** fora do escopo, sem requisito.
- **RN-18:** decisão minha (D-06), sem fonte normativa direta.
- **Sem resposta:** itens da seção 9 de `02-negocio.md`.

## 5. Mudanças

| Afirmação | Classificação | Requisitos | Histórias |
|---|---|---|---|
| M-01.1a | existente | RF-03 | HU-040 |
| M-01.1b | complementar | RF-03, RF-31, RN-08 | HU-041, HU-042, HU-044 |
| M-01.2 | existente | RN-01, RN-02 | HU-014 |
| M-01.3 | fora_escopo | Nenhum | Nenhuma |
| M-02.1 | conflitante | RN-07, RF-16 | HU-016, HU-020 |
| M-02.2 | complementar | RN-14 | HU-034 |
