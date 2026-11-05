# Gabarito: caso hospital-compras

Uso restrito à avaliação. Data de referência dos dados: 30/09/2026.

Abreviações de arquivos, todos sob `fontes/`:

- **ERP**: `SIS-01-erp-compras/erp_suprimax_dump.sql`
- **MC**: `SIS-02-manutclin/manutclin_dump.sql`
- **CSV**: `SIS-03-planilha-contratos/controle_contratos.csv`
- **REG**: `SIS-03-planilha-contratos/regras_da_planilha.md`
- **MAN**: `geral/manual_processo_compras_v2_2019.md`
- **POL**: `geral/politica_compras_POL-SUP-004_rev3.md`
- **POR**: `geral/portaria_DG-017-2025_compras_emergenciais.md`
- **ATA**: `geral/ata_comite_contratos_2026-08-19.md`
- **FLX**: `geral/fluxo_contratacao_manutencao.md`
- **IND**: `geral/indicadores_manutencao_2025.md`

## Divergências

"Só cruzando" indica item visível apenas ao comparar DDL ou trigger com documento.

| ID | Conceito | Valores e evidência | Só cruzando |
|---|---|---|---|
| D1 | Alçada de ordem de compra do gerente | POL §2: até R$ 50.000. ERP `fn_valida_alcada_oc`: nível 1 até R$ 80.000. OC-2026-00388, R$ 72.500, aprovada pelo usuário 3. | Sim |
| D2 | Limite para três cotações | POL §3: acima de R$ 15.000. ERP `fn_valida_cotacoes`: a partir de R$ 25.000. OC-2026-00440, R$ 19.800, requisição 507 com uma cotação. | Sim |
| D3 | Base da alçada de contrato | POL §2.2: valor global. ERP `fn_valida_alcada_contrato`: `valor_mensal`, sem considerar moeda. CT-2025-0064 (R$ 528.000 em 24 meses) e CT-2025-0102 (R$ 163.200 em 24 meses) aprovados pelo usuário 3. | Sim |
| D4 | Fim de vigência do CT-2023-0088 | ERP: 31/12/2026, aditivo em 20/05/2026. CSV: 30/06/2026, status Vencido. | Não |
| D5 | Valor do CT-2024-0117 | ERP: R$ 11.040/mês (R$ 132.480/ano), reajuste em 01/05/2026. CSV: R$ 126.000/ano. | Não |
| D6 | SLA de atendimento do CT-2024-0117 | CSV: 4 h. MC `contrato_ref`: 8 h. | Não |
| D7 | Classificação de criticidade | POL §6.2: quatro níveis. MC `equipamento.criticidade`: ENUM A, B, C. REG e CSV: Crítico ou Não crítico. Monitor PAT-007731: B no MC; contrato CT-2023-0088 Crítico no CSV. | Sim |
| D8 | Antecedência da renovação | POL §4.2: 120 dias. FLX: 90 dias. REG: 60 dias. | Não |
| D9 | Índice do CT-2025-0064 | CSV: IPCA, coerente com POL §4.3. ERP: `IGPM`, que também é o DEFAULT da coluna `indice_reajuste`. | Não para o valor; Sim para a causa |
| D10 | Prazo de pagamento | POL §5.1: padrão de 45 dias, mínimo de 30. ERP `chk_prazo_pagamento`: entre 15 e 30, DEFAULT 30. | Sim |
| D11 | Preventiva de ventiladores da Central | CSV, CT-2023-0019: Semestral. MC `plano_preventivo` (VEN, CEN): 365 dias. | Não |
| D12 | Limite do parecer jurídico | POL §4.5: acima de R$ 30.000. FLX: acima de R$ 100.000. | Não |

## Gargalos

| ID | Gargalo | Evidência |
|---|---|---|
| G1 | Planilha de contratos com um único mantenedor, atualização semanal, sem histórico e parada nas férias | REG, "Quem mexe" |
| G2 | Parecer jurídico consome 23 dos 38 dias do ciclo de contratação | IND, "Tempos e volumes" |
| G3 | OS aguardando compra por 21 dias em média, com redigitação manual no ERP | IND; ATA item 5; FLX; MC `requisicao_erp` (OS 88190 e 88240); ERP `requisicao.origem_os` em texto livre |
| G4 | Conferência manual de OS contra medições: duas analistas, cerca de 6 dias úteis por mês | ATA item 4 |
| G5 | Alteração manual do vencimento de cerca de 140 títulos por mês | ATA item 6; associada a D10 |

## Riscos

| ID | Risco | Evidência |
|---|---|---|
| R1 | Segurança do paciente, escondido na estrutura: equipamento volta a `EM_USO` ao fechar a OS, sem teste nem liberação. Ventilador retornou após evento adverso. | MC `trg_os_fecha`; `teste_seg_eletrica` e `liberado_por` anuláveis; OS 88213 fechada com ambos nulos; PAT-004512 `EM_USO`. Comparar com FLX, regra das etapas F e G. |
| R2 | Regulatório e segurança do paciente: equipamento em uso com calibração vencida ou sem registro, sem bloqueio estrutural | MC: PAT-004512 validade 31/03/2026, `EM_USO`; PAT-016002 sem calibração; nenhum trigger ou constraint; POL §6.1 e §6.3 |
| R3 | LGPD, escondido na estrutura: nome e prontuário em OS, legíveis pelo usuário externo do prestador | MC `ordem_servico.paciente_nome` e `paciente_prontuario`; OS 88213; `GRANT SELECT` a `'prestador_portal'@'%'` |
| R4 | Tecnovigilância: evento adverso sem registro de notificação | MC `evento_adverso`, sem campo de protocolo ou tabela de notificação; OS 88213; POL §6.1 |
| R5 | Serviço prestado e pago com contrato vencido; ERP não confere data | ERP e CSV: CT-2022-0055 terminou em 31/08/2025; ERP `status` ATIVO; CSV Em renovação; `fn_libera_medicao` só verifica status; medição 9001 paga em 15/09/2026; OC-2026-00440 vinculada; ATA item 7 |
| R6 | Renovação de gases medicinais pode perder a janela: pela Política, deve começar em 03/10/2026; a planilha só avisará em 02/12/2026 | CSV e ERP: CT-2025-0064 termina em 31/01/2027; POL §4.2; REG, "Status" |
| R7 | Fracionamento de compra para ficar abaixo da alçada | ERP: requisição 501 (R$ 149.300) dividida em OC-2026-00301, 00302 e 00303, no mesmo dia, cada uma abaixo de R$ 50.000; POL §3.1 |
| R8 | Falta de segregação de funções | ERP: OC-2026-00420 com solicitante e aprovador iguais a 3; nenhuma validação em trigger; POL §2.3 |
| R9 | Pagamento sem ateste | ERP: medição 9002 PAGA, `ateste_por` nulo; coluna anulável; `fn_libera_medicao` não verifica; POL §5.2 |
| R10 | Contrato fora do ERP, pago como compra avulsa | CSV, CT-2026-0021: R$ 58.800/ano; MC `contrato_ref` e OS 88260; ausente em ERP `contrato`, cujo recorte é completo; OC-2026-00409, 00431 e 00452 tipo AVULSA, R$ 4.900, sem `contrato_id`; POL §4.1 |

## Pontos de apoio

| ID | Ponto de apoio | Evidência |
|---|---|---|
| P1 | CNPJ disponível nos três sistemas como chave de fornecedor | ERP `fornecedor.cnpj` UNIQUE; MC `prestador.cnpj`; CSV `cnpj`, com máscara |
| P2 | Número de patrimônio comum entre ERP e ManutClin | ERP `contrato_item.patrimonio`; MC `equipamento.tag`; IND, inventário etiquetado |
| P3 | Numeração de contrato CT-AAAA-NNNN comum aos três sistemas | ERP `contrato.numero`; MC `contrato_ref.numero`; CSV `numero_contrato` |
| P4 | Política recente e explícita, com exceções formais, como base normativa | POL; POR |
| P5 | Inventário completo da rede concluído em 2026 | IND, 4.812 equipamentos etiquetados |

## Oportunidades

| ID | Oportunidade | Evidência |
|---|---|---|
| O1 | Alertas automáticos de renovação a partir da data de fim, substituindo o aviso manual | ERP `contrato.data_fim`; REG; POL §4.2; relaciona-se a G1 e R6 |
| O2 | Glosa automática comparando tempos da OS com SLA. A OS 88170 levou 14h10 para atendimento e a medição 9003 tem glosa 0. | MC, OS 88170 e `contrato_ref`; ERP medição 9003; POL §5.3; IND, glosas de R$ 0 |
| O3 | Consolidar contratos da mesma classe de equipamento: R$ 78,89, R$ 115,00 e R$ 170,00 por equipamento/mês | ERP `valor_mensal` e CSV `qtd_equip`: CT-2023-0088 (14.200/180), CT-2024-0117 (11.040/96), CT-2022-0055 (7.480/44) |
| O4 | Gerar requisição a partir da OS, sem redigitação | ATA item 5; FLX; MC `requisicao_erp`; ERP `requisicao.origem_os`; relaciona-se a G3 |
| O5 | Custo total por equipamento para decidir entre manter e substituir | ATA item 1; IND; P2 |

## Armadilhas: parecem problema, mas não são

| ID | Tipo | O que parece | Por que não é | Evidência |
|---|---|---|---|---|
| T1 | Documento revogado | Alçadas de R$ 20 mil e R$ 100 mil, três cotações acima de R$ 8 mil, aviso de 30 dias e pagamento em 28 dias conflitam com a Política | Os capítulos 4 e 5 do Manual foram revogados | MAN cap. 4 e 5; POL §1.3 |
| T2 | Total × subconjunto | R$ 3,03 mi × R$ 1,55 mi de gasto; 4.812 × 393 equipamentos | Contratos são parte do gasto total; equipamentos sob contrato são parte do inventário | IND; ATA item 1; soma de CSV `qtd_equip` = 393 |
| T3 | Contextos diferentes | Helvion com 6 h × 48 h de SLA | 6 h é início do atendimento; 48 h é solução | CSV e REG; ATA item 3; MC `contrato_ref` CT-2025-0031 (6 e 48); OS 88271 |
| T4 | Moeda distinta | CT-2025-0031 com 9.800 × 635.040 | US$ 9.800/mês × 12 × 5,40 = R$ 635.040/ano | ERP `moeda` USD; CSV `cambio_ref`; REG; POL §4.4 |
| T5 | Unidade distinta | CT-2023-0019 com 31.500 × 378.000 | Mensal × anual: 31.500 × 12 = 378.000 | ERP `valor_mensal`; CSV `valor_anual_brl`; REG |
| T6 | Regra com exceção formal | OC-2026-00412: R$ 92.000, uma cotação, aprovada dois dias depois pelo Diretor Técnico, com prazo de pagamento de 15 dias | Compra emergencial dentro do limite e do prazo da Portaria | ERP OC-2026-00412 e cotação 7007; POR art. 2º a 4º; POL §3.2; ATA item 2 |
| T7 | Nome diferente para a mesma coisa | MTS Engenharia Biomédica × BioVolt; filial 01 × CEN × Central | Mesmo CNPJ (00111222000101) e mesma unidade | ERP `fornecedor` e `filial`; MC `prestador` e `site`; CSV |
| T8 | Regra com exceção formal | CT-2022-0055, CT-2023-0019 e CT-2023-0088 com IGP-M, contrariando o IPCA | Contratos anteriores a 01/01/2024 mantêm o índice original | POL §4.3; ERP; CSV |

## Classificação das mudanças

| ID | Afirmação | Classe esperada | Temas impactados |
|---|---|---|---|
| A1 | M-01, item 1: incorporação do Hospital Aurora Serra em janeiro de 2027, com dois contratos próprios | novo | Escopo de unidades, cadastro de filiais, migração de contratos, volumes |
| A2 | M-01, item 2: contratos acima de R$ 250 mil de valor global são aprovados pela Diretora Geral | existente | POL §2 e §2.2; relaciona-se a D3 |
| A3 | M-01, item 3: controle de validade de lotes de medicamentos | fora do escopo | `escopo.md`; POL §1.2 |
| A4 | M-02, item 1: parecer jurídico obrigatório só acima de R$ 200 mil | conflitante | POL §4.5; D12; G2 |
| A5 | M-02, item 2: soma das glosas limitada a 10% do valor mensal por competência | complementar | POL §5.3; O2 |
