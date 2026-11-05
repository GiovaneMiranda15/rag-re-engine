# 01. Diagnóstico do cenário atual

Projeto: sistema único de compras e contratos de manutenção de equipamentos. Rede Hospitalar Aurora do Vale.

**Status:** atualizado em 04/11/2026 com `respostas.md`. As mudanças estão na seção 9. O que continua dependendo de confirmação segue marcado como hipótese.

## 1. Síntese

1. **Há uma situação de segurança do paciente para tratar agora, fora do projeto.** Um ventilador em uso na UTI (PAT-004512) teve evento adverso, a OS foi fechada sem teste de segurança elétrica e sem liberação, e a calibração está vencida desde 31/03/2026 (seção 4.1).
2. **Dados de saúde de pacientes estão expostos a prestadores externos.** O acesso do portal lê a tabela inteira de OS, que tem nome e prontuário, e pode alterar o horário de atendimento, que é a base de medição do SLA do próprio prestador (seção 4.2).
3. **Os sistemas não aplicam a política vigente.** Alçadas, cotações, prazo de pagamento e reajuste no ERP divergem da POL-SUP-004 rev. 3. A verificação de alçada de contrato usa o valor mensal, não o global, e por isso não barra nenhum contrato da base (seção 3.2).
4. **Nenhuma fonte tem o contrato completo.** ERP, planilha e ManutClin divergem em vigência, valor, índice, SLA e até na existência do contrato (seção 3.1).
5. **O controle de pagamento falha na amostra:** medição paga sem ateste, pagamento de contrato vencido há mais de um ano, atraso de SLA sem glosa e contrato pago por ordens avulsas (seção 3.3).
6. **O custo por equipamento pedido pela Diretora Geral não pode ser calculado hoje.** Ordem de compra não tem campo de equipamento, e 48,8% do gasto (avulsos e peças) só chega ao equipamento por texto livre, quando chega.
7. **O prazo é apertado pelo próprio negócio.** Faltam 238 dias para 30/06/2027, e 6 dos 8 contratos terminam antes disso (seção 4.4).

## 2. Base da análise

| Fonte | Natureza | Data | Limitação |
|---|---|---|---|
| POL-SUP-004 rev. 3 | Norma aprovada pela Diretoria | Vigência 01/01/2025 | A rev. 2 e versões anteriores não estão disponíveis |
| Portaria DG-017/2025 | Norma | Vigência 01/03/2025 | |
| Fluxo de contratação e manutenção | Processo descrito | Jun/2025 | Sem status de norma; diverge da POL |
| Manual de Compras v2 | Legado | Mar/2019 | Caps. 4 e 5 revogados; cita só Central e Norte, F-12, Compras+ |
| Indicadores 2025 | Consolidado da Controladoria | Datado de fev/2026 | Cita inventário concluído em jun/2026: data inconsistente |
| Ata do Comitê | Registro de reunião | 19/08/2026 | A ata de 21/10/2026 e a lista de setembro não estão nas fontes |
| SupriMax (ERP) | Dump | 30/09/2026 | `contrato` completo na categoria; demais tabelas são amostra |
| ManutClin | Dump | 30/09/2026 | `prestador` e `contrato_ref` completos; `equipamento` e `ordem_servico` são amostra |
| Planilha de contratos | CSV e regras | 25/09/2026 | Mantida por uma pessoa, sem histórico |

**Regras de leitura adotadas**

- Data de corte: 30/09/2026 para os sistemas. Janelas futuras também são comparadas com a data deste diagnóstico (04/11/2026).
- Quando há conflito, a POL rev. 3 e a Portaria são tratadas como referência, por serem as normas aprovadas. Essa precedência foi confirmada nos pontos da pergunta 3 (R3).
- Achados sobre amostra provam que o caso existe, não a sua frequência. Nenhum foi extrapolado.
- Os textos dos contratos não estão nas fontes. Nenhuma divergência de cláusula pode ser decidida só com este material.
- Pessoas são citadas por papel. Dados de pacientes não são reproduzidos.

## 3. Divergências

### 3.1 Contratos: ERP, planilha e ManutClin

| Contrato | Campo | ERP | Planilha | ManutClin | Leitura |
|---|---|---|---|---|---|
| CT-2023-0088 | Fim e status | 31/12/2026, ATIVO, aditivo em 20/05/2026 | 30/06/2026, Vencido | Sem data | **Vigente até 31/12/2026.** Aditivo 2 confirmado (R4); Suprimentos lançou no ERP e não avisou o Jurídico |
| CT-2023-0088 e CT-2024-0117 | Fornecedor | MTS Engenharia Biomédica | BioVolt | BioVolt | Mesmo CNPJ. BioVolt é o nome fantasia da MTS (R4) |
| CT-2024-0117 | Valor | R$ 11.040,00/mês (R$ 132.480,00/ano) | R$ 126.000,00/ano | | Vale o ERP: R$ 11.040,00 após o reajuste de 01/05/2026 (R4). Planilha desatualizada |
| CT-2024-0117 | SLA de atendimento | | 4 h | 8 h | Vale 4 h, do contrato (R4). ManutClin incorreto |
| CT-2025-0064 | Índice | IGPM | IPCA | | Vale IPCA, do contrato (R4). ERP incorreto; o valor padrão IGPM é a provável causa |
| CT-2026-0021 | Existência | **Ausente** | Vigente, R$ 58.800,00/ano | Presente | **Viola a POL 4.1.** Assinado pela unidade e nunca registrado no ERP (R6) |
| CT-2022-0055 | Status | ATIVO | Em renovação | Em uso em OS | **Vencido desde 31/08/2025** (395 dias no corte), com serviço e pagamento continuando |
| CT-2025-0031 | Valor | US$ 9.800,00/mês | R$ 635.040,00/ano (câmbio 5,40) | | Coerente entre si. Ver risco de moeda na seção 3.3 |
| CT-2023-0019 | Preventiva | | Semestral | Plano VEN/CEN: 365 dias | Vale semestral, do contrato (R4). Plano do ManutClin (365 dias) abaixo do contratado |

Pontos que **conferem**: número do contrato e CNPJ batem nas três bases; os demais valores da planilha equivalem a mensal do ERP × 12; os outros SLAs de atendimento são iguais. Isso sustenta a migração (seção 6).

Lacunas de modelo:

- Só o ManutClin tem SLA de solução; a planilha tem só atendimento e o ERP não tem nenhum.
- O ERP guarda apenas a data do último aditivo, sem histórico de aditivos.
- O ManutClin não guarda a vigência, então OS são abertas contra contrato vencido.
- A unidade tem código diferente em cada base: `01..04` no ERP, `CEN/NOR/LIT/SUL` no ManutClin e texto na planilha.

### 3.2 Regras: norma contra documentos e sistemas

| Regra | POL rev. 3 / Portaria (referência) | ERP | Fluxo 2025 | Planilha | Manual 2019 (revogado) |
|---|---|---|---|---|---|
| Alçada de nível 1 | Até R$ 50.000,00 | Até **R$ 80.000,00** | | | Até R$ 20.000,00 |
| Alçada da Diretora Geral | Acima de R$ 250.000,00 | Igual | | | Acima de R$ 100.000,00 |
| Base da alçada de contrato | **Valor global** | **`valor_mensal`** | | | |
| Três cotações | Acima de R$ 15.000,00 | A partir de **R$ 25.000,00** e só tipo REGULAR | | | Acima de R$ 8.000,00 |
| Duas cotações | R$ 5.000,01 a R$ 15.000,00 | Sem verificação | | | |
| Parecer jurídico | Acima de **R$ 30.000,00** | Sem verificação | Acima de **R$ 100.000,00** | | |
| Início da renovação | **120 dias**, área gestora e Jurídico | Sem controle | **90 dias**, Suprimentos | **60 dias**, aviso do Jurídico | 30 dias, Compras |
| Prazo de pagamento | Padrão 45, mínimo 30 dias, da emissão da nota | **CHECK de 15 a 30**, padrão 30 | | | 28 dias, do recebimento |
| Reajuste | IPCA desde 01/01/2024; moeda estrangeira sem índice | Padrão IGPM | | | |
| Criticidade | **4 níveis** (1 a 4) | | | **Crítico / Não crítico**, por contrato (e **A/B/C** por equipamento, no ManutClin) | |

Consequências verificadas:

- **O prazo-padrão de 45 dias é impossível no ERP**, porque o CHECK limita a 30. Hipótese: esta é a causa dos cerca de 140 títulos alterados à mão por mês (o volume é próximo das cerca de 122 OCs por mês). A confirmar (pergunta 12).
- **Alçada de contrato:** o maior valor mensal da base é R$ 31.500,00, logo a verificação de R$ 80.000,00 nunca é acionada. O valor global exigiria Diretora Geral ou Diretor Financeiro:

| Contrato | Valor global (R$) | Alçada pela POL | Aprovador no ERP | Situação |
|---|---:|---|---|---|
| CT-2025-0031 | 1.905.120,00 (câmbio 5,40) | Diretora Geral | Diretora Geral | Conforme |
| CT-2023-0019 | 1.512.000,00 | Diretora Geral | Diretor Financeiro | Anterior à rev. 3: regra da época desconhecida |
| CT-2023-0088 | 596.400,00 (42 meses, com aditivo) | Diretora Geral | Gerente de Suprimentos | Original anterior à rev. 3; aditivo de 2026 já sob ela, sem nova verificação (o gatilho só atua se o aprovador mudar) |
| CT-2025-0064 | 528.000,00 | Diretora Geral | Gerente de Suprimentos | **Provável não conformidade** (início 02/2025; data de assinatura a confirmar) |
| CT-2024-0117 | 397.440,00 | Diretora Geral | Gerente de Suprimentos | Anterior à rev. 3 |
| CT-2022-0055 | 269.280,00 | Diretora Geral | Gerente de Suprimentos | Anterior à rev. 3 |
| CT-2025-0102 | 163.200,00 | Diretor Financeiro | Gerente de Suprimentos | **Provável não conformidade** (início 03/2025) |
| CT-2026-0021 | 58.800,00 | Diretor Financeiro | Sem registro no ERP | Aprovação desconhecida |

Valores globais calculados com o mensal atual × meses de vigência; o valor original assinado pode ser diferente.

- **Parecer jurídico:** pelo valor global, todos os 8 contratos passam de R$ 30.000,00. O limite do fluxo de 2025 só muda o resultado no CT-2026-0021 (R$ 58.800,00), em que apenas a POL exige parecer. Para contratos menores, fora desta base, o efeito é desconhecido.
- **Lacunas nos gatilhos:** aprovador nulo passa sem verificação. O tipo EMERGENCIAL passa sem verificar nem o limite de R$ 100.000,00 nem se o aprovador é o Diretor Técnico. O tipo AVULSA não existe na POL e não exige cotação. A liberação de medição verifica o status do contrato, não a vigência nem o ateste.
- **Manual 2019:** a POL revoga só os caps. 4 e 5. Os caps. 1 a 3 (papel, Compras+, fax) continuam formalmente em vigor, embora obsoletos. O prazo de 28 dias do manual revogado ainda aparece na OC-2026-00440.

### 3.3 Ordens de compra e medições: casos na amostra

| Caso | Fato | Regra | Avaliação |
|---|---|---|---|
| OC-2026-00301, 00302, 00303 | R$ 49.800,00 + 49.700,00 + 49.800,00 = R$ 149.300,00. Mesma requisição, fornecedor, aprovador e data | POL 3.1 e 2.1 | **Fracionamento.** Exigia Diretor Financeiro; aprovado pela Gerente de Suprimentos |
| OC-2026-00388 | R$ 72.500,00, aprovada por nível 1 | POL 2 | **Viola a POL**, e o ERP aceita por usar R$ 80.000,00 |
| OC-2026-00420 | Solicitante e aprovador são a mesma pessoa | POL 2.3 | **Viola segregação de funções.** O ERP não verifica |
| OC-2026-00440 | R$ 19.800,00, 1 cotação, prazo de 28 dias, ligada a contrato vencido | POL 3 e 5.1 | **Viola cotação e prazo mínimo.** O ERP aceita por usar R$ 25.000,00 |
| OC-2026-00409, 00431, 00452 | R$ 4.900,00 por mês, AVULSA, Hemofix, sem cotação, "competência" | POL 4.1 e 5.2 | **Contrato CT-2026-0021 pago por OC avulsa**, sem medição nem ateste. O valor é o mensal do contrato e fica abaixo do limite de dispensa de cotação |
| **OC-2026-00412** | R$ 92.000,00, 1 proposta, aprovação em 2 dias pelo Diretor Técnico, prazo de 15 dias, informada ao Comitê | Portaria DG-017 | **Conforme.** Não é irregularidade. Falta só a ligação com a OS que comprove a parada (`origem_os` vazio) |
| Medição 9002 (CT-2023-0088, 08/2026) | PAGA sem ateste | POL 5.2 | **Viola a POL.** O ERP não exige ateste |
| Medição 9001 (CT-2022-0055, 08/2026) | Paga, com contrato vencido | Ata, item 7 | Pagamento sem cobertura contratual; ver risco 4.3 |
| OS 88170 e medição 9003 (CT-2024-0117) | Atendimento em 14h10, acima do SLA de 4 h (R4); medição com glosa 0, atestada e paga | POL 5.3 | **Glosa não aplicada**, de R$ 220,80 (2% de R$ 11.040,00) |
| OS 88190 (CT-2022-0055) | Solução em 533h40, SLA de 72 h, aguardou compra de peça | POL 5.3 | **Indefinido:** depende de o relógio parar durante a compra (pergunta 9) |
| OS 88240 (CT-2023-0019) | Em AGUARDANDO_COMPRA há 12 dias, sem requisição registrada no campo; item não coberto | Fluxo | Caso aberto de gargalo; ventilador parado |
| Medição 9004 (CT-2025-0031) | Valor 9.800,00 sem moeda na tabela | POL 4.4 | **Risco de somar USD como BRL** em relatório consolidado. Também o gatilho de alçada compara USD com limites em BRL |

As glosas de R$ 0,00 em 2025 são coerentes com a falta de cruzamento entre OS e medição. O caso da OS 88170 é de 2026, mas sugere falta de apuração, não ausência de descumprimento (hipótese).

Reajustes possivelmente atrasados (hipótese de reajuste anual, a confirmar em contrato): CT-2023-0019 (último em 03/2024), CT-2023-0088 (07/2024), CT-2025-0064 e CT-2025-0102 (nenhum registrado).

Sobre a Ata, item 3: a afirmação de que a Helvion cumpriu as 48 h na parada de junho **não pode ser verificada**, pois a OS de junho não está na amostra. A OS 88271, de setembro, cumpriu (atendimento 5h30 de 6 h; solução 32 h de 48 h). As 48 h são SLA de solução, e a planilha só registra o de atendimento (6 h).

### 3.4 Escopo: fronteiras ambíguas

- **"Sistema único" contra "se relacionar com as OS e o inventário":** o escopo não diz se o ManutClin é substituído ou integrado. O SupriMax atende outras categorias, então provavelmente permanece. Decisão estruturante (pergunta 1).
- **Pagamento:** não há fonte do módulo financeiro. Os títulos existem "depois de recebidos do ERP", e o sistema de destino não é identificado.
- **Obras prediais:** a usina de oxigênio e a central de gases (CT-2025-0064) têm contrato de manutenção e etiqueta, mas tocam infraestrutura predial.
- **Calibração:** CT-2025-0102 tem `qtd_equip` = 0. Os instrumentos podem não estar no inventário de 4.812.
- **Prontuário:** está fora do escopo, mas o ManutClin guarda campos de paciente. O novo sistema não deve herdá-los.
- **Hospital Aurora Serra:** entra em janeiro de 2027 (R15). Não aparece no escopo, na POL 1.1 nem em nenhuma base. Ver seção 9.
- **CDI Aurora Sul:** 402 equipamentos, nenhum contrato continuado e nenhum plano preventivo nas fontes. Pode ser coerente ou uma lacuna.

### 3.5 Números

- **R$ 1,55 milhão (Ata) não é o gasto de manutenção.** É só a parcela de contratos, 51,2% do total de R$ 3.025.880,00. Chamados avulsos são 33,5% e peças 15,3%.
- **O R$ 1.550.440,00 foi reconstruído exatamente** como cálculo teórico: valores da planilha, proporcionais aos meses de 2025, e câmbio de referência 5,40 no contrato em USD. Logo, **parece valor contratado, não valor pago**. O efetivamente pago em reais do CT-2025-0031 é desconhecido.
- Os demais totais conferem: componentes do gasto, leitos (640), equipamentos (4.812). Os 393 equipamentos sob contrato são a soma de `qtd_equip` da planilha, ou 8,2% do inventário, e incluem contrato iniciado em 2026.
- Valor anual da carteira: R$ 1.803.600,00 na planilha e R$ 1.751.280,00 no ERP. A diferença é o CT-2026-0021 ausente e o reajuste do CT-2024-0117.

## 4. Riscos

### 4.1 Segurança do paciente: ação imediata, fora do projeto

**PAT-004512 (ventilador, UTI, criticidade A), no corte de 30/09/2026:**

- OS 88213: evento adverso registrado, com falha de alarme durante o uso.
- OS fechada **sem teste de segurança elétrica e sem liberação**, contra a regra do fluxo. O gatilho devolveu o equipamento para EM_USO.
- **Calibração vencida desde 31/03/2026**, em uso, contra a POL 6.3.
- Causa técnica: `trg_os_fecha` passa para EM_USO qualquer OS fechada, mesmo com teste REPROVADO ou nulo. O problema pode alcançar outros equipamentos.
- Também: PAT-016002 (autoclave) está em uso sem calibração registrada, a confirmar se ela se aplica. PAT-015530 vence em 19/11/2026 e PAT-007731 em 10/12/2026.
- As fontes não mostram se houve investigação ou notificação do evento à vigilância sanitária.

**Recomendação:** o Diretor Técnico e a Engenharia Clínica devem verificar a situação atual do equipamento, a tratativa do evento e o escopo do problema do gatilho, sem esperar o projeto.

### 4.2 Privacidade e integridade: ação imediata, fora do projeto

- `ordem_servico` guarda nome e prontuário de paciente, dado sensível de saúde pela LGPD.
- O usuário `prestador_portal`, de qualquer host, tem SELECT em toda a tabela `ordem_servico`, sem filtro por prestador. No nível do banco, cada prestador pode ler os pacientes e os chamados dos outros; um eventual filtro na aplicação não está nas fontes.
- Ele tem UPDATE em `atendimento` e `descricao`: **o prestador pode alterar o horário usado para medir o seu próprio SLA**, sem trilha de auditoria visível no dump.
- O trecho de grants não mostra a autenticação. A confirmar.

**Recomendação:** TI e encarregado de dados devem restringir colunas e linhas e rever as permissões de escrita, independentemente do projeto.

### 4.3 Conformidade e financeiro

| Risco | Evidência | Efeito |
|---|---|---|
| Serviço e pagamento sem contrato vigente | CT-2022-0055, vencido e cobrindo 44 equipamentos críticos | Exposição jurídica; SLA e glosa sem base; regularização necessária |
| Controles contornáveis | Fracionamento, avulsas, segregação, alçada, ateste | Migrar sem mudar a regra perpetua as falhas |
| Glosa não aplicada | R$ 0,00 em 2025; caso OS 88170 | Perda financeira de valor desconhecido |
| Moeda sem tratamento | Medição sem moeda; indicador a câmbio de referência | Consolidado incorreto, em contrato de R$ 1,9 milhão |
| Dado alterável pelo medido | Grant do portal | Glosa contestável |

### 4.4 Projeto

| Risco | Evidência | Efeito |
|---|---|---|
| Renovações antes do go-live | Ver tabela abaixo | Migração de contratos em mudança; processo antigo ainda em uso |
| Janela de 120 dias já perdida | 5 contratos com início da janela já passado em 04/11/2026 | Novos casos como o CT-2022-0055, inclusive ventiladores e gases |
| Dependência de uma pessoa | Planilha mantida só pelo Jurídico, parado nas férias; todos os contratos com a mesma responsável | A fonte da migração tem atraso e risco de indisponibilidade |
| Decisão de fronteira tardia | Substituir ou integrar o ManutClin | Prazo de 238 dias não comporta retrabalho |
| Mudança de regra sem gestão | Aplicar parecer acima de R$ 30.000,00 eleva a carga no gargalo de 23 dias | O sistema pode piorar o ciclo se o Jurídico não for redesenhado |
| Conflito de fonte na migração | Seção 3.1 | Sem saneamento, o novo sistema nasce com erro |
| Integração desconhecida | Sem informação sobre API ou fornecedor do ERP e do ManutClin | Risco técnico e de contrato |

| Contrato | Fim | Início da janela (120 dias) | Situação em 04/11/2026 |
|---|---|---|---|
| CT-2022-0055 | 31/08/2025 | Passado | **Vencido** |
| CT-2023-0088 | 31/12/2026 (ERP) | 02/09/2026 | Janela passada; faltam 57 dias; planilha o trata como vencido |
| CT-2025-0064 | 31/01/2027 | 03/10/2026 | Janela passada; faltam 88 dias |
| CT-2026-0021 | 14/02/2027 | 17/10/2026 | Janela passada; faltam 102 dias |
| CT-2023-0019 | 28/02/2027 | 31/10/2026 | Janela passada; faltam 116 dias |
| CT-2025-0102 | 28/02/2027 | 31/10/2026 | Janela passada; faltam 116 dias |
| CT-2024-0117 | 30/04/2027 | 31/12/2026 | Antes do go-live |
| CT-2025-0031 | 31/03/2028 | 02/12/2027 | Depois do go-live |

Não há nas fontes evidência de início dessas renovações. Pela regra da planilha, todos continuam "Vigente", o que oculta o problema.

## 5. Gargalos

| Gargalo | Medida | Causa aparente |
|---|---|---|
| Parecer jurídico | 23 dos 38 dias do ciclo (60,5%) | Fila concentrada; limite de parecer indefinido na prática |
| OS parada em compras | 21 dias em média | Redigitação em sistemas que não se falam; vínculo em texto livre |
| Conferência de medição | 2 analistas, cerca de 6 dias úteis por mês; raramente termina antes do pagamento | Cruzamento manual; 640 OS por mês |
| Ajuste de título | Cerca de 140 por mês | Prazo do ERP incompatível com a POL (hipótese) |
| Atualização de contratos | Semanal, por e-mail, cópia em PDF | Fonte única em planilha |
| Consolidação | Sem visão de rede por contrato, fornecedor, equipamento e unidade | Chaves e cadastros diferentes |

## 6. Pontos de apoio

- **Chaves comuns:** número do contrato nas três bases, CNPJ nas três e etiqueta patrimonial igual entre `contrato_item` e `equipamento`.
- **Inventário concluído em jun/2026**, 4.812 equipamentos etiquetados.
- **Norma clara:** POL rev. 3 e Portaria definem os parâmetros necessários.
- **Exemplo de processo que funciona:** a OC-2026-00412 cumpriu a Portaria e foi ao Comitê.
- **Regras já codificadas:** gatilhos do ERP e ManutClin mostram onde colocar os controles, ainda que com valores errados.
- **Dados de SLA e tempo:** `contrato_ref`, datas de abertura, atendimento e fechamento, teste e liberação existem no ManutClin.
- **Governança:** Comitê de Contratos ativo, Diretora Geral patrocinando e as quatro áreas engajadas.
- **Vínculos iniciais:** `origem_os` e `requisicao_erp` existem, ainda que em texto livre e pouco preenchidos.

## 7. Oportunidades para a primeira fase

| Oportunidade | Ganho esperado |
|---|---|
| Regras da POL e da Portaria parametrizadas e com vigência | Elimina divergências da seção 3.2 e bloqueia fracionamento, segregação e alçada |
| Requisição gerada a partir da OS, com equipamento e origem | Ataca os 21 dias e viabiliza o custo por equipamento |
| Apuração automática de SLA e sugestão de glosa | Ataca os 6 dias de conferência e a glosa de R$ 0,00 |
| Pagamento condicionado a contrato vigente e ateste | Cumpre POL 4.1 e 5.2 |
| Alerta de renovação em 120 dias com responsável | Evita novos casos como o CT-2022-0055 |
| Prazo de pagamento conforme a POL, com exceção emergencial | Pode eliminar os cerca de 140 ajustes mensais |
| Trilha de parecer jurídico com triagem e prazo | Ataca os 23 dias |
| Contrato com moeda, aditivos e histórico de reajuste | Fonte única e consolidado correto |
| Custo total por equipamento (contrato, chamados, peças) | Decisão de manter ou substituir, pedida pela Diretora Geral |
| Bloqueio de retorno ao uso sem teste, liberação e calibração válida (se o ManutClin for abrangido) | Corrige a falha de segurança na raiz |

## 8. Decisões tomadas nesta etapa

- POL rev. 3 e Portaria são a referência até confirmação em contrário. O fluxo de 2025 é tratado como descrição de prática, e o Manual 2019 como legado.
- CT-2023-0088 é tratado como vigente até 31/12/2026, confirmado em R4; o documento do aditivo ainda não foi visto.
- OC-2026-00412 é tratada como conforme.
- As decisões assumidas para o que ficou sem resposta estão em `02-negocio.md`, seção 9.

## 9. O que mudou com as respostas (04/11/2026)

### Confirmado ou resolvido

| Item | Antes | Agora | Origem |
|---|---|---|---|
| Precedência | POL como hipótese | POL vale para parecer, renovação, alçada de OC e cotações; a configuração do ERP é antiga e nunca foi revista | R3 |
| CT-2023-0088 | Hipótese de vigência | Aditivo 2 assinado em 20/05/2026; vigente até 31/12/2026. Aprovador desconhecido | R4 |
| CT-2024-0117 | SLA de 4 h ou 8 h; valor em dúvida | 4 h; R$ 11.040,00 | R4 |
| CT-2025-0064 | IPCA ou IGPM | IPCA | R4 |
| CT-2023-0019 | Semestral ou anual | Semestral | R4 |
| MTS e BioVolt | Hipótese | Mesma empresa | R4 |
| CT-2026-0021 | Talvez em outra categoria | Assinado na unidade, nunca registrado | R6 |
| OS 88170 | Acima do SLA nos dois valores | Glosa de R$ 220,80 não aplicada, sujeita à definição de "evento" | R4, POL 5.3 |
| Custo por equipamento | Objetivo | Desejável; pode ir para a fase 2 | R2 |
| Gasto de 2025 | Fontes | Confirmado: R$ 3,03 milhões, sendo R$ 1,55 milhão em contratos. Se é contratado ou pago continua sem resposta | R13 |

### Novo

- **Hospital Aurora Serra em janeiro de 2027 (R15):** quinta unidade, sem dado em nenhuma fonte. Mudança de escopo a formalizar.
- **Teto de glosa de 10% por competência (R9):** não está na POL. Falta formalização e base de cálculo.
- **Proposta do Jurídico de limite de parecer de R$ 200.000,00 (R3):** não aprovada; a Política continua valendo. A resposta fala em "reduzir", mas o valor é maior que os R$ 30.000,00 atuais: reduziria a quantidade de pareceres, e não o limite.
- **Causa da renovação tardia (R5):** o Jurídico só inicia quando a planilha muda para "A renovar", a 60 dias. O **CT-2025-0064 (usina de oxigênio) não iniciou**, com a janela de 120 dias vencida em 03/10/2026.
- **De-para de criticidade (R11):** A = 1, B = 2 e 3, C = 4. B não se resolve automaticamente: é preciso classificar os equipamentos.
- **Portal do prestador fora da fase 1 (R14):** o acesso atual no ManutClin continua existindo, com os riscos da seção 4.2.
- **Novos interlocutores:** Qualidade e Segurança do Paciente, encarregado de dados e coordenador de TI, ainda não ouvidos.
- **Aditivo "2" do CT-2023-0088 (R4):** implica um aditivo 1, do qual não há registro.

### Continua sem resposta

Fronteira do sistema e estratégia (R1) é o principal bloqueio. Também seguem abertos: sistema financeiro e motivo dos 140 títulos (R12, **a causa continua sendo hipótese**), divisão dos 21 e dos 23 dias (R5, R7), regras de apuração de SLA (R9), conferência de medição (R8), tratamento dos riscos 4.1 e 4.2 (R10, R14) e APIs (R15). Decisões assumidas e responsáveis estão em `02-negocio.md`, seção 9.
