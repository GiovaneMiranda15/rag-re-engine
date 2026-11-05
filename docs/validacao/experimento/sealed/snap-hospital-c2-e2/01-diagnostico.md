# Diagnóstico do cenário atual: compras e contratos de manutenção de equipamentos

Rede Hospitalar Aurora do Vale. Patrocínio: Diretoria Geral. Etapa 1, atualizado na Etapa 2 com `respostas.md`.

## O que as respostas mudaram

| Assunto | Antes | Agora | Fonte |
|---|---|---|---|
| Regras em conflito | Hierarquia suposta | **Confirmado:** a Política vale para alçadas, cotações, parecer de R$ 30 mil e renovação em 120 dias. O ERP está desatualizado por falta de revisão; fluxo e planilha terão de se adequar. Exceção formal segue desconhecida | R3, R4, R5 |
| CT-2023-0088 | Inferência de aditivo | **Resolvido:** aditivo 2 assinado em 20/05/2026, vigência até 31/12/2026. Suprimentos lançou no ERP sem avisar o Jurídico. A planilha está errada; "Vencido" não procede. **Novo:** se este é o aditivo 2, houve um aditivo 1, sem nenhum registro nas fontes | R6 |
| CT-2024-0117 | SLA e valor em dúvida | **Resolvido:** SLA de atendimento de 4 h (ManutClin errado) e R$ 11.040,00/mês após reajuste (planilha defasada). A OS 88170 viola o SLA | R6 |
| CT-2025-0064 | Índice em dúvida | **Resolvido:** IPCA. O ERP está errado | R6 |
| CT-2026-0021 | Inferência | **Confirmado e ampliado:** assinado localmente pela unidade Litoral, nunca registrado, pago por avulsas. **Novo risco:** unidades podem assinar contrato fora do fluxo central | R8 |
| Preventiva de ventiladores | Divergente | **Resolvido:** semestral. O plano de 365 dias do ManutClin está errado | R13 |
| Criticidade | Sem correspondência | **Parcial:** quatro níveis oficiais; A = 1, B = 2 ou 3, C = 4. B não se converte automaticamente. Crítico/Não crítico segue sem correspondência | R13 |
| Retorno ao uso | Regra do fluxo | **Confirmado:** teste e assinatura obrigatórios. Desfecho da OS 88213 segue desconhecido | R14 |
| Prioridade | Suposta | **Definida** pela Diretora Geral; custo por equipamento pode ir para a fase 2; portal fora da fase 1 | R2, R15 |
| Interlocutores | Ausentes | **Novos:** Gerência de Qualidade e Segurança do Paciente e encarregado de dados (DPO), ainda não consultados | R14, R15 |

**Sem resposta, e por isso ainda abertos:** o que "sistema único" substitui e quem responde tecnicamente (P1, integralmente), contrato vencido (P7), segregação e fracionamento (P9), sistema financeiro e causa dos 140 títulos (P10, que continua **inferência**) e regras de medição e glosa (P11). As suposições de `perguntas.md` para esses pontos **não foram validadas**. Lista completa: `02-negocio.md`, seção 8.

## 1. Resumo executivo

O processo está dividido entre ERP SupriMax (compras, contrato, medição), ManutClin (OS, inventário, SLA) e a planilha do Jurídico. Nenhum dos três tem a visão completa, e **as regras gravadas no ERP não são as da política vigente**. O problema, portanto, não é só de integração: um sistema novo que migrasse as regras atuais reproduziria as falhas.

Principais achados:

1. **Risco assistencial:** um ventilador de criticidade A estava em uso com calibração vencida há 142 dias quando teve um evento adverso (OS 88213), e a OS foi fechada sem teste de segurança elétrica nem liberação. O fechamento devolve o equipamento a `EM_USO` automaticamente, sem checar nada.
2. **Dados de paciente expostos:** a tabela de OS guarda nome e prontuário, e o usuário `prestador_portal` tem `SELECT` nela inteira. O mesmo usuário pode alterar `atendimento`, o campo que mede o SLA do próprio prestador.
3. **Controles do ERP desalinhados:** na amostra de 10 OCs, só a emergencial está integralmente conforme. Há fracionamento (3 OCs somando R$ 149.300,00), alçada abaixo da exigida, falta de cotações e solicitante aprovando a própria compra.
4. **Contratos fora de controle:** o CT-2022-0055 venceu há 395 dias e segue pago; o CT-2026-0021 não existe no ERP e é pago por OC avulsa; o CT-2023-0088 consta como vencido na planilha, embora tenha aditivo válido até 31/12/2026, que o Jurídico não recebeu.
5. **Medição e glosa não funcionam:** a glosa foi R$ 0,00 em 2025; há medição paga sem ateste e violação de SLA paga sem glosa.
6. **Custo por equipamento hoje é inviável:** o gasto real é de R$ 3,03 mi, não R$ 1,55 mi (que cobre só contratos), e chamados e peças não têm vínculo estruturado com o equipamento.
7. **Prazo:** 7 dos 8 contratos já venceram ou vencem antes da entrada em operação (30/06/2027). A renovação desses contratos ocorrerá no processo atual, e a migração pegará vários em andamento.

### Ações que não devem esperar o projeto

Estas recomendações vêm de dados extraídos em 30/09/2026 e devem ser checadas antes, pois a situação pode ter mudado.

| # | Ação | Dono sugerido |
|---|---|---|
| 1 | Verificar calibração e liberação do PAT-004512 e a varredura de equipamentos com calibração vencida em uso | Engenharia Clínica, Diretor Técnico |
| 2 | Revogar o acesso do `prestador_portal` aos dados de paciente e restringir a alteração de `atendimento` | TI, responsável por privacidade |
| 3 | Regularizar o CT-2022-0055 e decidir o tratamento dos pagamentos após o vencimento | Jurídico, Financeiro |
| 4 | Obter valor e parecer do aditivo 2 do CT-2023-0088, corrigir a planilha e iniciar a renovação (janela de 120 dias aberta desde 02/09/2026) | Jurídico, Engenharia Clínica |
| 5 | Registrar o CT-2026-0021 no ERP (POL-SUP-004, item 4.1) | Suprimentos, Jurídico |
| 6 | Avaliar as OC-2026-00301/302/303 e a OC-2026-00388 | Diretor Financeiro |

## 2. Base da análise

### Fontes e confiabilidade

| Fonte | Data | Cobertura | Uso |
|---|---|---|---|
| POL-SUP-004 rev. 3 | vigência 01/01/2025 | quatro unidades | **Regra vigente** de compras e contratos (exclui medicamentos e OPME) |
| Portaria DG-017/2025 | vigência 01/03/2025 | compra emergencial | Regra específica; prevalece no seu tema (POL, item 3.2) |
| Fluxo de contratação e manutenção | jun/2025 | Eng. Clínica e Suprimentos | Processo descrito; diverge da política em dois pontos, apesar de posterior a ela |
| Manual de Compras v2 | mar/2019 | só Central e Norte | Legado; capítulos 4 e 5 revogados. Os capítulos 1 a 3 (F-12 em papel, Compras+, fax) não foram revogados formalmente |
| ERP SupriMax | extração 30/09/2026 | `contrato`: todas as linhas da categoria. `contrato_item`, `medicao`, `requisicao`, `ordem_compra`: **amostra** | Registro transacional |
| ManutClin 4.2 | extração 30/09/2026 | `prestador`, `contrato_ref`: completos. `equipamento`, `ordem_servico`: **amostra** | OS, SLA, inventário |
| Planilha de contratos | atualizada em 25/09/2026 | 8 contratos | Controle manual do Jurídico |
| Indicadores 2025 | fev/2026 (inventário de jun/2026) | rede | Números agregados |
| Ata do Comitê | 19/08/2026 | | Dores e decisões declaradas |

**Convenções:** *Fato* é o que está escrito na fonte. *Inferência* é conclusão minha, a confirmar. *Não verificável* é o que as fontes não permitem conferir. As contagens em amostras mostram que o problema existe, **não a sua frequência**.

**Hierarquia:** Portaria (no tema emergencial) > POL-SUP-004 > fluxo > configuração de sistemas > manual de 2019. Confirmada nos pontos respondidos (R3 a R5); o contrato assinado define SLA, índice e preventiva do contrato (R6, R13).

### Números de referência

| Item | Valor |
|---|---|
| Gasto 2025 | R$ 3.025.880,00: contratos 51,2% (R$ 1.550.440,00), chamados avulsos 33,5% (R$ 1.012.300,00), peças 15,3% (R$ 463.140,00) |
| Inventário | 4.812 equipamentos em 4 unidades; **393 sob contrato (8,2%)** |
| Volumes | cerca de 640 OS/mês; 1.460 OCs de manutenção/ano; cerca de 140 títulos alterados/mês |
| Tempos | contratação 38 dias (23 aguardando parecer jurídico); OS corretiva em AGUARDANDO_COMPRA 21 dias |
| Medição | 2 analistas, cerca de 6 dias úteis/mês cada (cerca de 12 pessoa-dia/mês, se forem 6 dias de cada uma: inferência) |

Os totais conferem: a soma dos componentes dá o gasto total, `qtd_equip` da planilha soma 393, e as unidades somam 4.812 equipamentos.

### Papel de cada sistema

| Conceito | ERP SupriMax | ManutClin | Planilha |
|---|---|---|---|
| Unidade | `filial` 01 a 04 | `site` CEN, NOR, LIT, SUL | texto (Central, Norte, Litoral) |
| Fornecedor | `fornecedor` | `prestador` | `credor` |
| Equipamento | `contrato_item.patrimonio` | `equipamento.tag` | só `qtd_equip` |
| Contrato | `contrato` (7) | `contrato_ref` (8; sem datas nem valor) | linha (8) |
| SLA | ausente | atendimento e solução | só atendimento |
| Reajuste, valor | sim | não | sim |
| Câmbio de referência | **ausente** | não | `cambio_ref` |
| Aditivo | só a data do último | não | só via data fim |
| OS | só `origem_os` em texto | `ordem_servico` | não |
| Nota fiscal, título | **não aparece no recorte** | não | não |

## 3. Divergências

### 3.1 Regras: documentos versus sistemas

| ID | Regra | POL-SUP-004 rev. 3 / Portaria (vigente) | Fluxo 2025 | Manual 2019 (revogado) | ERP / planilha |
|---|---|---|---|---|---|
| DIV-01 | Alçada: nível intermediário | Gerente até R$ 50 mil; Dir. Financeiro até R$ 250 mil; Dir. Geral acima | "conforme alçada" | R$ 20 mil / R$ 100 mil | **Trigger: R$ 80 mil** / R$ 250 mil |
| DIV-02 | Base da alçada de contrato | Valor global da vigência (2.2) | | | **Trigger compara `valor_mensal`** e sem converter moeda: nenhum contrato atual chegaria perto do limite |
| DIV-03 | Cotações | Dispensa até R$ 5 mil; 2 até R$ 15 mil; 3 acima | "faz as cotações" | 3 acima de R$ 8 mil | **Trigger: 3 a partir de R$ 25 mil; faixa de 2 inexiste** |
| DIV-04 | Parecer jurídico | Global **acima de R$ 30 mil** (4.5) | **Acima de R$ 100 mil** | | Sem controle no ERP |
| DIV-05 | Início da renovação | **120 dias**, área gestora + Jurídico (4.2) | **90 dias**, Suprimentos | 30 dias, Compras | Planilha: **60 dias**, aviso do Jurídico; ERP: nada |
| DIV-06 | Prazo de pagamento | Padrão 45 dias da emissão; mínimo 30, salvo emergencial (5.1) | | 28 dias | **`CHECK` 15 a 30, padrão 30: 45 dias é impossível de registrar** |
| DIV-07 | Reajuste padrão | IPCA para assinados desde 01/01/2024; anteriores mantêm o original (4.3) | | | **Padrão da coluna: IGPM** |
| DIV-08 | Criticidade | 4 níveis: Suporte à vida, Alto, Médio, Baixo (6.2) | | | ManutClin A/B/C; planilha Crítico/Não crítico, sem correspondência documentada |
| DIV-09 | Tipos de OC | Regular e emergencial | | | ERP tem também **AVULSA**, sem definição em documento |
| DIV-10 | Retorno ao uso | Teste aprovado e liberação assinada (fluxo); calibração válida (POL 6.3) | Obrigatórios | | **`trg_os_fecha` põe `EM_USO` sem checar nada** |
| DIV-11 | Medição | Paga só após ateste (5.2) | Ateste antes do pagamento | | **`fn_libera_medicao` só checa `status = ATIVO`**; nem ateste, nem vigência |
| DIV-12 | Segregação e fracionamento | Solicitante não aprova (2.3); vedado fracionar (3.1) | | | **Nenhum trigger verifica** |
| DIV-13 | Emergencial | Até R$ 100 mil; Diretor Técnico aprova em até 72 h; aviso ao Comitê | | | Trigger só isenta; não valida limite, aprovador nem prazo |

Outras brechas nos triggers (fato do código, sem ocorrência observada):

- `aprovador_id` nulo passa sem validação.
- A alçada da OC só é reavaliada em `INSERT` ou mudança de aprovador. Aumentar `valor_total` depois não dispara nova checagem.
- O Diretor Técnico tem nível 2, o que lhe permite aprovar OC regular de até R$ 250 mil, sem base na política.
- Não há restrição de unicidade em `medicao` para contrato e competência: nada impede duas medições iguais.

### 3.2 Contratos: comparação entre os três sistemas

| Contrato | Fornecedor / unidade | ERP | Planilha | ManutClin | Situação |
|---|---|---|---|---|---|
| CT-2022-0055 | Litoral Eletromédica / Litoral | fim 31/08/2025, **ATIVO** | **Em renovação** | SLA 12/72 h | Vencido há 395 dias em 30/09/2026; serviço e pagamento continuam (ata, medição 9001). O status de nenhum dos sistemas diz que está vencido |
| CT-2023-0019 | Clarivent / Central | fim 28/02/2027 | igual | SLA 4/24 h | Dados coincidem. Preventiva divergente (DIV-15) |
| CT-2023-0088 | BioVolt / Central | **fim 31/12/2026**, aditivo 20/05/2026, ATIVO | **fim 30/06/2026, Vencido** | SLA 8/48 h | **Confirmado:** aditivo 2 válido, não informado ao Jurídico. Valor do aditivo e parecer desconhecidos. O ERP mantém o aprovador original |
| CT-2024-0117 | BioVolt / Norte | **R$ 132.480,00/ano** (11.040,00/mês), reajuste em 01/05/2026 | **R$ 126.000,00/ano; SLA 4 h** | **SLA 8 h**/48 h | **Confirmado:** vale o ERP para valor e 4 h para SLA. A planilha não recebeu o reajuste de 5,14%, e o ManutClin está errado |
| CT-2025-0031 | Helvion / Central | USD 9.800,00/mês, sem índice | R$ 635.040,00/ano a 5,40 | SLA 6/48 h | Coerentes entre si. Criticidade: "Não crítico" / B, no maior contrato da rede |
| CT-2025-0064 | NorteGás / Norte | **IGPM** | **IPCA** | SLA 2/12 h | **Confirmado:** IPCA. O ERP está errado (inferência: ficou no padrão da coluna) |
| CT-2025-0102 | Termolab / Central | IPCA | igual | SLA 48/120 h | Coincide. Cobre instrumentos (`qtd_equip` 0), sem ligação com equipamento |
| CT-2026-0021 | Hemofix / Litoral | **Inexistente** (tabela completa) | R$ 58.800,00/ano, vigente | SLA 24/72 h | Viola o item 4.1. Pago por OCs AVULSA de R$ 4.900,00 "competência junho/julho/agosto"; 4.900 × 12 = 58.800. **Confirmado:** assinado localmente pela unidade |

Mais divergências de dados:

- **DIV-14, identidade:** o mesmo CNPJ aparece como "MTS Engenharia Biomédica" no ERP e "BioVolt" no ManutClin e na planilha. Só o CNPJ é confiável para unir fornecedores (formatos diferentes; no ManutClin é opcional). O nome "Litoral" designa tanto uma unidade quanto um fornecedor.
- **DIV-15, preventiva:** ventiladores têm periodicidade semestral na planilha, mas o plano `VEN/CEN` é de 365 dias. **Confirmado:** vale a semestral, logo o plano está errado e o equipamento pode estar recebendo menos preventiva do que a contratada. O plano também não tem `DEF/CEN` nem `DEF/LIT`, embora haja contratos para desfibriladores nessas unidades. A tabela não é marcada como amostra; a ausência é inferência a confirmar.
- **DIV-16, criticidade:** o PAT-016002 (autoclave) é B no ManutClin, com contrato "Crítico" na planilha. O PAT-007731 (monitor) é B, com contrato "Crítico". A planilha classifica o contrato, e o ManutClin, o equipamento.
- **DIV-17, modelo equipamento-contrato:** no ManutClin cada equipamento tem um único `contrato_numero`; no ERP a relação admite vários. Um equipamento com contrato de manutenção e de calibração não cabe no modelo do ManutClin.
- **DIV-18, ligação OS-compra:** o par `requisicao_erp` e `origem_os` é texto livre ("REQ 507", "OS 88190"). A OS 88240 está em AGUARDANDO_COMPRA há 12 dias sem requisição informada, e a requisição 504 (módulos para ventiladores) não cita OS.

### 3.3 Indicadores

- **DIV-19:** a ata cita R$ 1,55 mi como "gasto com contratos de manutenção"; o gasto total é de R$ 3,03 mi. Quase metade está fora de contrato, e só 8,2% do parque está sob contrato.
- **Reconciliação (inferência):** R$ 1.550.440,00 é reproduzido exatamente ao proratear os meses de 2025 dos sete contratos ativos naquele ano e usar R$ 126.000,00 para o CT-2024-0117, o valor anterior ao reajuste. O número é coerente, portanto, mas parte de câmbio de referência, não do valor efetivamente pago em reais.
- O total anualizado atual é de **R$ 1.803.600,00** na planilha e R$ 1.751.280,00 no ERP (sem o Hemofix, com USD a 5,40). Essa soma não é comparável com o gasto de 2025.
- O CT-2026-0021 pago como avulso tende a classificar gasto de contrato como chamado avulso nos números de 2026 (inferência).

## 4. Conformidade observada

### 4.1 Ordens de compra (amostra de 10, regras da rev. 3)

| OC | Valor | Achado | Regra |
|---|---|---|---|
| 00301, 00302, 00303 | 49.800 + 49.700 + 49.800 = **149.300** | Mesma requisição, data e fornecedor; aprovadas pela Gerente. O total exigiria o Diretor Financeiro | 3.1 e 2.1 |
| 00388 | 72.500 | Aprovada pela Gerente; exigiria o Diretor Financeiro. Passa pelo trigger de R$ 80 mil | 2 |
| 00409, 00431, 00452 | 4.900 cada | Avulsas recorrentes de contrato não registrado. Cada uma cabe na dispensa e na alçada da Gerente; o contrato (R$ 58.800) exigiria o Diretor Financeiro e parecer | 4.1, 2.2, 4.5 |
| 00420 | 8.400 | Mesma pessoa solicita e aprova. Cotações corretas (2) | 2.3 |
| 00440 | 19.800 | 1 cotação (exige 3; passa pelo trigger de R$ 25 mil); prazo de 28 dias (mínimo 30); vinculada a contrato vencido | 3, 5.1, 4 |
| 00412 | 92.000 | **Conforme:** emergencial, dentro do limite, aprovada pelo Diretor Técnico em 2 dias, prazo de 15 dias permitido, informada ao Comitê | Portaria |

Em 6 das 8 requisições da amostra, o solicitante é o Analista de Compras, não a área que precisa do serviço. A segregação formal é cumprida, mas o sistema esconde o verdadeiro demandante (inferência: efeito da redigitação).

### 4.2 Alçada de contratos pelo valor global

| Contrato | Global estimado (R$) | Exigiria | Aprovou no ERP | Leitura |
|---|---|---|---|---|
| CT-2025-0031 | 1.905.120,00 (a 5,40) | Dir. Geral | Dir. Geral | Conforme |
| CT-2025-0064 | 528.000,00 | Dir. Geral | Gerente | **Não conforme** |
| CT-2025-0102 | 163.200,00 | Dir. Financeiro | Gerente | **Não conforme** |
| CT-2022-0055, CT-2023-0019, CT-2023-0088, CT-2024-0117 | 269.280 a 1.512.000 | | Gerente ou Dir. Financeiro | Anteriores à rev. 3; a alçada da época não está nas fontes. O aditivo de 2026 do CT-2023-0088 já deveria seguir a rev. 3 |

O global foi estimado como valor mensal atual × meses de vigência; `data_inicio` foi usada como aproximação da assinatura.

### 4.3 Medição, SLA e glosa

| Evidência | Situação |
|---|---|
| Medição 9002 (CT-2023-0088, 08/2026) | **Paga sem ateste**, viola o item 5.2 |
| Medição 9001 (CT-2022-0055, 08/2026) | Paga para contrato vencido; o trigger passa porque o status é ATIVO |
| OS 88170 (CT-2024-0117) | Atendimento em **14h10**, acima do SLA contratual de 4 h (R6). Medição 9003 paga sem glosa. Glosa estimada: 2% × R$ 11.040,00 = R$ 220,80, se o evento for por OS (P11 sem resposta) |
| OS 88190 (CT-2022-0055) | Solução em 533,7 h (SLA 72 h), com espera de compra da placa. Haver glosa depende de a espera suspender o prazo, regra que não está nas fontes |
| OS 88240 (CT-2023-0019) | Ventilador de criticidade A parado havia 12 dias na extração (SLA de solução 24 h); peça não coberta; mesma dúvida |
| Demais OS da amostra (88213, 88260, 88271) | Dentro do SLA |
| Tomógrafo, parada de junho (ata) | **Não verificável:** a OS não está na amostra. O SLA citado de 48 h confere com o ManutClin |

A glosa em si é pequena em valor. O ganho principal está em liberar trabalho manual e dar poder de negociação com fornecedor; o projeto não deveria prometer retorno baseado em glosa.

Os pagamentos de medições de 08/2026 ocorreram em setembro. O prazo mínimo de 30 dias da emissão pode não estar sendo respeitado, mas é não verificável, porque a data da nota não aparece no recorte.

### 4.4 Segurança do paciente e calibração

- **OS 88213 (PAT-004512):** fechada com `teste_seg_eletrica` e `liberado_por` nulos e com `evento_adverso = 1`. Viola a regra do fluxo.
- **Calibração:** o mesmo equipamento venceu em 31/03/2026 e continua `EM_USO`, contra o item 6.3 da política.
- **Notificação:** as fontes não mostram como o evento adverso é tratado ou notificado. É lacuna, não prova de omissão.
- **Sem registro:** o PAT-016002 não tem calibração registrada; não se sabe se é aplicável.
- **Próximos vencimentos:** PAT-015530 (19/11/2026) e PAT-007731 (10/12/2026).

## 5. Gargalos

| ID | Gargalo | Evidência | Causa provável |
|---|---|---|---|
| GAR-01 | Parecer jurídico consome 23 dos 38 dias do ciclo (61%) | Indicadores | Uma pessoa concentra o controle; não há fila nem padrão observável (inferência). **Aplicar o limite de R$ 30 mil pode aumentar a fila** |
| GAR-02 | OS corretiva parada em média 21 dias por compra | Indicadores | Redigitação no ERP, sem integração; exigências de cotação também na compra de peça |
| GAR-03 | Conferência de medição: até 12 pessoa-dia/mês, raramente antes do pagamento | Ata | OS e medição sem chave comum |
| GAR-04 | Cerca de 140 títulos/mês com vencimento alterado à mão | Ata | Inferência forte: o `CHECK` limita a OC a 30 dias, e a política pede 45 |
| GAR-05 | Planilha depende de uma pessoa, de atualização semanal e não tem histórico; nas férias, para | Regras da planilha | Sistema de registro informal |
| GAR-06 | Pedidos de relatório consolidado exigem cruzamento manual | Ata: Comitê consolida à mão | Chaves distintas |

## 6. Riscos

| ID | Risco | Sev. | Evidência | Tratamento na fase 1 |
|---|---|---|---|---|
| RIS-01 | Dano ao paciente: equipamento em uso sem calibração ou liberação | **Crítica** | 4.4 | Painel de exceções (RF-34). Impedir ou alertar: sem resposta (DP-16) |
| RIS-02 | Vazamento de dado de paciente (LGPD) | **Crítica** | `GRANT SELECT` a conta `@'%'` compartilhada; campos de paciente na OS | Não trazer campos de paciente. **Excluir o portal da fase 1 não resolve o acesso existente**; levar ao DPO (DP-18) |
| RIS-03 | Adulteração da evidência de SLA | Alta | Prestador tem `UPDATE (atendimento, descricao)` | Trilha de auditoria; carimbo de tempo não editável |
| RIS-04 | Serviço crítico sem cobertura contratual | Alta | CT-2022-0055 | Vigência calculada por data; alertas; regra para pagamento |
| RIS-05 | Burla de alçada e de cotação não detectada | Alta | 4.1, 4.2 | Motor de regras parametrizado; alerta de fracionamento |
| RIS-06 | Pagamento indevido | Alta | Medição sem ateste; avulsas fora de contrato | Ateste obrigatório, vínculo de contrato |
| RIS-07 | Migrar dados errados como verdade | Alta | 3.2; não há contratos originais nas fontes | Saneamento com o contrato em mãos, antes da carga |
| RIS-08 | Prazo de 30/06/2027 com escopo amplo e contratos renovando no meio | Alta | Janelas abaixo | Faseamento e corte; processo-ponte para renovações |
| RIS-09 | Integração sem dono técnico: **TI não aparece** em nenhuma fonte e não está entre as áreas que puxam o projeto | Alta | Escopo, ata | P1 sem resposta: decisão mais urgente (DP-01) |
| RIS-10 | Consolidar real e dólar errado | Média | `medicao.valor` sem moeda; trigger não converte | Moeda e câmbio explícitos; critério consolidado sem resposta (DP-14) |
| RIS-11 | Maior rigor, mais demora: mais pareceres e aprovações | Média | DIV-01, DIV-04 | Medir a capacidade; minutas e pareceres padrão |
| RIS-12 | Reajustes não aplicados ou índice errado | Média | CT-2025-0064; `dt_ultimo_reajuste` antiga ou nula em vários contratos. Periodicidade não consta das fontes | Registro e agenda; periodicidade sem resposta (DP-07) |
| RIS-14 | Contrato assinado por unidade fora do fluxo central, sem registro nem controle | Alta | R8: CT-2026-0021 | Levantamento nas unidades (RF-11); registro antes do primeiro pagamento (RN-08) |
| RIS-13 | Fronteira com o escopo excluído: usina de oxigênio e gases podem ser tratados como predial | Baixa | CT-2025-0064 | P2 sem resposta (DP-04). Hipótese: dentro do escopo, pois está em `MANUT_EQUIP` e no inventário |

### Janelas de renovação contra a entrada em operação

| Contrato | Fim | 120 dias (política) | 60 dias (planilha) | Antes de 30/06/2027? |
|---|---|---|---|---|
| CT-2022-0055 | 31/08/2025 | vencido | vencido | Já vencido |
| CT-2023-0088 | 31/12/2026 (ERP) | 02/09/2026 | 01/11/2026 | Sim |
| CT-2025-0064 | 31/01/2027 | 03/10/2026 | 02/12/2026 | Sim |
| CT-2026-0021 | 14/02/2027 | 17/10/2026 | 16/12/2026 | Sim |
| CT-2023-0019 | 28/02/2027 | 31/10/2026 | 30/12/2026 | Sim |
| CT-2025-0102 | 28/02/2027 | 31/10/2026 | 30/12/2026 | Sim |
| CT-2024-0117 | 30/04/2027 | 31/12/2026 | 01/03/2027 | Sim |
| CT-2025-0031 | 31/03/2028 | 02/12/2027 | 31/01/2028 | Não |

Pelo critério da planilha, os alertas só sairão dois meses depois do que a política exige; os contratos com janela aberta até 31/10/2026 aparecem como "Vigente".

## 7. Pontos de apoio

- **Patrimônio único:** inventário concluído em jun/2026, com etiqueta em todos os equipamentos. Todas as tags de `contrato_item` da amostra existem no ManutClin, com o mesmo formato.
- **Número de contrato** idêntico nos três sistemas, e **CNPJ** confiável para fornecedores.
- **Regras escritas e recentes:** POL-SUP-004 e Portaria são claras; muitos conflitos se resolvem aplicando-as.
- **Compra emergencial** funcionando conforme a Portaria, inclusive a prestação de contas ao Comitê.
- **Fluxos já desenhados** e critérios de liberação definidos pela Engenharia Clínica.
- **Comitê de Contratos** ativo, com todas as áreas: fórum natural de decisões.
- **Dados já existentes** para SLA (tempos da OS) e classificação (plano preventivo por classe e unidade).
- **Patrocínio:** a Diretora Geral apresenta uma pergunta concreta de negócio.

## 8. Oportunidades

| ID | Oportunidade | Base |
|---|---|---|
| OPO-01 | Abrir requisição a partir da OS, sem redigitar | Pedido da ata; 21 dias de espera |
| OPO-02 | Pré-conferência automática de medição (OS × SLA × contrato), com sugestão de glosa | Até 12 pessoa-dia/mês |
| OPO-03 | Regras parametrizadas (valores e vigência), para que a próxima revisão não dependa de alterar trigger | DIV-01 a DIV-07 |
| OPO-04 | Calendário único de vencimentos, renovação e reajuste, com alertas a 120 dias | DIV-05 |
| OPO-05 | Custo total por equipamento (TCO) para decidir entre manter e substituir | Pedido da Diretora Geral |
| OPO-06 | Consolidar contratos de monitores e desfibriladores: custo por equipamento/mês varia de R$ 78,89 (Central) a R$ 115,00 (Norte) e R$ 170,00 (Litoral). O mix pode explicar parte da diferença; há também dois contratos com o mesmo fornecedor | Planilha, ERP |
| OPO-07 | Avaliar contrato para despesa recorrente fora de contrato: R$ 1,01 mi em chamados avulsos; calibração avulsa do CDI (OC-00420) com o fornecedor que tem contrato só para a Central. O CDI Aurora Sul tem 402 equipamentos e nenhum contrato | Indicadores, ERP |
| OPO-08 | Fila, minutas e pareceres padrão para reduzir os 23 dias do Jurídico, sem baixar o controle | GAR-01 |
| OPO-09 | Trocar o `prazo` fixo por vencimento calculado da emissão da nota | GAR-04 |

## 9. Lacunas das fontes

- **Contratos originais e aditivos** não estão nas fontes, e são eles que resolvem SLA, valor, índice e periodicidade. O Jurídico os consultou para três contratos; a disponibilização deles segue sem resposta. O caso do CT-2024-0117 mostra que o SLA do ManutClin pode estar errado.
- **Sistema financeiro:** o recorte não mostra nota fiscal, título ou baixa; o Financeiro recebe títulos do ERP, mas o destino não é descrito.
- **Histórico de status da OS:** não existe no dump, e o indicador de 21 dias vem de método desconhecido.
- **Dados para decidir manter ou substituir:** o inventário do dump não tem valor de aquisição, idade, fabricante ou modelo.
- **Custo da equipe própria:** fora do gasto de 2025, apesar de atender grande parte dos 4.419 equipamentos sem contrato.
- **Interlocutores:** TI não soube responder às perguntas feitas a ela; o DPO e a Gerência de Qualidade e Segurança do Paciente foram indicados e ainda não consultados.
- **Alçadas anteriores à rev. 3** e a revisão 2 da política (citada no item 4.3).
- **Reunião do Comitê de 21/10/2026** e a lista atualizada prometida para setembro.

## 10. Implicações para os requisitos

Desenvolvidas em `02-negocio.md` e `03-tecnico.md`. Os itens 1, 6 e 7 foram confirmados em parte pelas respostas; os demais seguem como decisão de projeto ou hipótese.

1. A POL-SUP-004 rev. 3 e a Portaria são a base das regras; o comportamento do ERP não é requisito.
2. Vigência, status e alertas são calculados por data, não digitados.
3. Regras são parâmetros versionados, com a data de vigência de cada um.
4. A chave de integração é contrato (número), fornecedor (CNPJ), equipamento (patrimônio) e unidade (tabela de equivalência).
5. Campos de paciente não entram no novo sistema; a OS só leva dados técnicos e o indicador de evento adverso.
6. Antes da carga, os 8 contratos passam por saneamento com o documento original.
7. Controle de escopo: medicamentos, OPME, obras prediais e prontuário ficam fora.
8. A entrega deve priorizar o controle (contrato, alçada, ateste) e deixar o TCO completo para quando os vínculos existirem.
