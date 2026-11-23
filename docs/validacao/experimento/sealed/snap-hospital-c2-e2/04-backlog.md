# Backlog ágil

Rede Hospitalar Aurora do Vale. Resultado das fases Spec e Breakdown, a partir de `02-negocio.md`. Cada história implementa o requisito de mesmo número (US-07 implementa RF-07).

## Como ler

- **Prioridade:** segue a ordem da Diretora Geral: 1 cadastro de contratos, 2 aprovações, 3 ligação OS-requisição-medição, 4 glosa. São recomendações minhas, a validar: visão consolidada (4), exceções técnicas (2, por ser risco assistencial) e criticidade (3).
- **Ordem:** posição na fila por prioridade. A dependência técnica prevalece: US-22 (prioridade 3) precisa vir antes de US-03 (prioridade 1).
- **Modo:** AFK pode seguir sem nova decisão de negócio além das listadas; HITL exige decisão humana durante o trabalho. **História com decisão pendente só entra em desenvolvimento quando a decisão vier.** O texto "provisório" nos critérios mostra o que pode mudar.
- **Sem estimativas:** ainda não há time nem arquitetura (DP-01).
- **Fora:** portal do prestador, medicamentos, OPME, obras prediais e prontuário.

## Resumo

| Épico | Maior prioridade | Histórias |
|---|---|---|
| EP-01 Cadastro único de contratos | 1 | US-01, US-02, US-03, US-04, US-05, US-06, US-07, US-08, US-09, US-10, US-11, US-36 |
| EP-02 Aprovações conforme a Política | 2 | US-12, US-13, US-14, US-15, US-16, US-17, US-18, US-19, US-20, US-21 |
| EP-03 Ligação entre OS, requisição e medição | 3 | US-22, US-23, US-24, US-25, US-26, US-27, US-28 |
| EP-04 Glosa por SLA | 4 | US-29, US-30 |
| EP-05 Visão consolidada e conformidade técnica | 2 | US-31, US-32, US-33, US-34 |
| EP-06 Segunda fase | 4 | US-35 |

## Fila priorizada

| Ordem | História | Título | Prior. | Fase | Modo | Decisões pendentes | Depende de |
|---|---|---|---|---|---|---|---|
| 1 | US-01 | Cadastrar contrato com vigência, valor e SLA | 1 | F1 | AFK | DP-08 | - |
| 2 | US-02 | Manter fornecedor único por CNPJ | 1 | F1 | AFK | - | - |
| 3 | US-03 | Vincular contrato a equipamentos e unidade | 1 | F1 | AFK | - | US-01, US-22 |
| 4 | US-04 | Registrar contrato em moeda estrangeira | 1 | F1 | AFK | DP-14 | US-01 |
| 5 | US-05 | Calcular a vigência por data | 1 | F1 | AFK | - | US-01 |
| 6 | US-06 | Avisar sobre renovação a partir de 120 dias | 1 | F1 | AFK | DP-07 | US-05 |
| 7 | US-07 | Conduzir a renovação | 1 | F1 | HITL | DP-06, DP-07 | US-05, US-17 |
| 8 | US-08 | Registrar aditivos com histórico | 1 | F1 | AFK | DP-06, DP-08 | US-01, US-20 |
| 9 | US-10 | Carregar os contratos saneados | 1 | F1 | HITL | DP-04, DP-05, DP-08 | US-01, US-02, US-03 |
| 10 | US-11 | Levantar contratos fora do registro | 1 | F1 | HITL | DP-10 | - |
| 11 | US-36 | Adequar fluxo e planilha à Política na transição | 1 | F1 | HITL | DP-07 | - |
| 12 | US-09 | Registrar e agendar reajustes | 2 | F1 | HITL | DP-07 | US-01 |
| 13 | US-12 | Abrir requisição | 2 | F1 | AFK | DP-11 | - |
| 14 | US-13 | Exigir cotações por faixa | 2 | F1 | AFK | - | US-12, US-14 |
| 15 | US-14 | Manter os limites da Política como parâmetros | 2 | F1 | AFK | DP-05 | - |
| 16 | US-15 | Aprovar OC pela alçada | 2 | F1 | AFK | DP-05, DP-10 | US-13, US-14, US-20 |
| 17 | US-16 | Impedir autoaprovação | 2 | F1 | HITL | DP-11 | US-15 |
| 18 | US-17 | Aprovar contrato por valor global, com parecer | 2 | F1 | AFK | DP-05, DP-06 | US-01, US-14, US-20 |
| 19 | US-18 | Alertar possível fracionamento | 2 | F1 | HITL | DP-11 | US-15 |
| 20 | US-19 | Tratar compra emergencial conforme a Portaria | 2 | F1 | AFK | - | US-13, US-20 |
| 21 | US-20 | Registrar trilha de auditoria | 2 | F1 | AFK | DP-18 | - |
| 22 | US-21 | Controlar acesso por função e unidade | 2 | F1 | AFK | DP-18 | US-20 |
| 23 | US-34 | Monitorar exceções técnicas de equipamento | 2 | F1 | HITL | DP-16, DP-17 | US-22 |
| 24 | US-22 | Consultar OS e inventário do ManutClin sem dados de paciente | 3 | F1 | HITL | DP-01, DP-17, DP-18 | - |
| 25 | US-23 | Abrir requisição a partir da OS | 3 | F1 | AFK | DP-01 | US-12, US-22 |
| 26 | US-24 | Gerar medição por contrato e competência | 3 | F1 | AFK | - | US-01 |
| 27 | US-25 | Conferir medição com as OS da competência | 3 | F1 | HITL | DP-13 | US-22, US-24, US-29 |
| 28 | US-26 | Atestar medição | 3 | F1 | AFK | - | US-20, US-24 |
| 29 | US-27 | Liberar para pagamento com vencimento calculado | 3 | F1 | HITL | DP-01, DP-12 | US-14, US-26 |
| 30 | US-28 | Tratar pagamento de contrato vencido | 3 | F1 | HITL | DP-09 | US-05, US-27 |
| 31 | US-33 | Classificar criticidade oficial do equipamento | 3 | F1 | HITL | DP-15 | US-22 |
| 32 | US-29 | Calcular atendimento de SLA por OS | 4 | F1 | HITL | DP-13 | US-01, US-22 |
| 33 | US-30 | Sugerir e decidir glosa | 4 | F1 | HITL | DP-13 | US-26, US-27, US-29 |
| 34 | US-31 | Consultar visão consolidada | 4 | F1 | AFK | DP-14 | US-03, US-05, US-22, US-24 |
| 35 | US-32 | Acompanhar indicadores do processo | 4 | F1 | HITL | DP-03 | US-17, US-26 |
| 36 | US-35 | Apurar custo por equipamento | 4 | F2 | HITL | DP-14 | US-23, US-31 |

## Detalhamento

### EP-01: Cadastro único de contratos

#### F-01: Contrato e fornecedor

**US-01: Cadastrar contrato com vigência, valor e SLA** (prioridade 1, F1, AFK)

Como Jurídico, quero registrar cada contrato em um único lugar, para todas as áreas consultarem a mesma informação.

Critérios de aceite:

1. Dado um contrato novo, quando salvo sem número, unidade, fornecedor, vigência, valor, índice ou SLA de atendimento e solução, então o sistema recusa e aponta o campo.
2. Dado um número já cadastrado, quando tento repeti-lo, então o sistema recusa.
3. Dado um contrato com data de fim anterior ao início, quando salvo, então o sistema recusa.
4. Dado um contrato salvo, quando consulto, então vejo o documento assinado, a periodicidade de preventiva e, por campo, a origem e se foi confirmado.

Requisito: RF-01. Regras: RN-08, RN-18. Pendências: DP-08.

**US-02: Manter fornecedor único por CNPJ** (prioridade 1, F1, AFK)

Como Gerente de Suprimentos, quero um cadastro por CNPJ, com nomes alternativos, para consolidar contratos sem duplicar empresas.

Critérios de aceite:

1. Dado um CNPJ existente, quando tento outro cadastro, então o sistema recusa e mostra o existente.
2. Dado o fornecedor com razão social MTS e nome BioVolt, quando busco por qualquer nome, então encontro o mesmo cadastro e seus dois contratos.
3. Dado um CNPJ inválido, quando salvo, então o sistema recusa.

Requisito: RF-02.

**US-03: Vincular contrato a equipamentos e unidade** (prioridade 1, F1, AFK)

Como Gerente de Engenharia Clínica, quero saber quais equipamentos cada contrato cobre, para conferir cobertura e chamados.

Critérios de aceite:

1. Dado um patrimônio do inventário, quando o vinculo a um contrato de manutenção e a um de calibração, então os dois vínculos ficam registrados.
2. Dado um patrimônio inexistente, quando vinculo, então o sistema recusa.
3. Dado um contrato de calibração sem lista de itens, quando consulto, então ele aparece como cobertura por instrumentos, sem quantidade inventada.

Requisito: RF-03. Depende de: US-01, US-22.

**US-04: Registrar contrato em moeda estrangeira** (prioridade 1, F1, AFK)

Como Diretor Financeiro, quero registrar o contrato na moeda original, com câmbio de referência, para controlar o orçamento sem misturar moedas.

Critérios de aceite:

1. Dado o CT-2025-0031, quando salvo em USD 9.800,00 por mês com referência de R$ 5,40, então vejo o valor em dólar e o valor de referência em reais, rotulado.
2. Dado um contrato em moeda estrangeira, quando tento informar índice de reajuste, então o sistema recusa.
3. Dado um contrato em moeda estrangeira, quando salvo sem câmbio de referência, então o sistema recusa.

Requisito: RF-04. Regras: RN-11. RNF: RNF-09. Pendências: DP-14. Depende de: US-01.

#### F-02: Vigência e renovação

**US-05: Calcular a vigência por data** (prioridade 1, F1, AFK)

Como Jurídico, quero ver a vigência calculada automaticamente, para nenhum contrato vencido parecer ativo.

Critérios de aceite:

1. Dado um contrato com fim em mais de 120 dias, quando consulto, então o status é Vigente.
2. Dado um contrato com 120 dias ou menos até o fim, quando consulto, então o status é A renovar.
3. Dado o CT-2022-0055 com minuta em discussão, quando consulto após o fim, então vejo Vencido e o andamento Em renovação.
4. Dado o CT-2023-0088 com aditivo 2, quando consulto em 30/09/2026, então o fim é 31/12/2026 e o status é A renovar.
5. Dado um usuário, quando tenta editar o status de vigência, então o sistema não oferece essa opção.

Requisito: RF-05. Regras: RN-09. Depende de: US-01.

**US-06: Avisar sobre renovação a partir de 120 dias** (prioridade 1, F1, AFK)

Como Gerente de Engenharia Clínica, quero receber aviso da renovação, para começar a tempo.

Critérios de aceite:

1. Dado um contrato que chega a 120 dias do fim, quando o sistema verifica os prazos, então avisa a área gestora e o Jurídico uma vez.
2. Dado que a renovação não começou, quando o prazo avança, então novos avisos são enviados em marcos parametrizados.
3. Dado um aditivo que prorroga o contrato, quando registrado, então os avisos pendentes deixam de valer.
4. Dado um aviso, quando enviado, então ele fica registrado no contrato.

Requisito: RF-06. Regras: RN-09. Pendências: DP-07. Depende de: US-05.

**US-07: Conduzir a renovação** (prioridade 1, F1, HITL)

Como Jurídico, quero acompanhar as etapas da renovação, para evitar serviço sem cobertura.

Critérios de aceite:

1. Dado um contrato A renovar, quando a área gestora inicia a renovação, então vejo etapas, responsáveis e datas.
2. Dado que o valor global passa de R$ 30.000,00, quando a renovação chega à aprovação sem parecer, então o sistema impede o avanço (provisório, DP-06).
3. Dado que a renovação é concluída, quando o novo contrato ou aditivo é registrado, então a vigência é atualizada.

Requisito: RF-07. Regras: RN-09, RN-07. Pendências: DP-06, DP-07. Depende de: US-05, US-17.

#### F-03: Aditivo e reajuste

**US-08: Registrar aditivos com histórico** (prioridade 1, F1, AFK)

Como Gerente de Suprimentos, quero registrar cada aditivo, para o histórico do contrato ficar completo e o Jurídico informado.

Critérios de aceite:

1. Dado um contrato, quando registro um aditivo, então ele recebe número, data, documento e os novos fim e valor, e o Jurídico é notificado.
2. Dado um aditivo, quando consulto, então vejo os valores anteriores e os novos.
3. Dado o CT-2023-0088, quando consulto, então vejo o aditivo 2 de 20/05/2026 e, como pendentes de informação, o valor, o parecer e o aditivo 1.
4. Dado um aditivo sem parecer em contrato acima de R$ 30.000,00, quando salvo, então o sistema sinaliza (provisório, DP-06).

Requisito: RF-08. Regras: RN-19, RN-07. Pendências: DP-06, DP-08. Depende de: US-01, US-20.

**US-09: Registrar e agendar reajustes** (prioridade 2, F1, HITL)

Como Diretor Financeiro, quero saber quando reajustar e com qual índice, para não pagar valor errado.

Critérios de aceite:

1. Dado um contrato assinado desde 01/01/2024 em reais, quando cadastro, então o índice sugerido é IPCA.
2. Dado um contrato anterior, quando cadastro, então o índice do contrato é mantido.
3. Dado um reajuste, quando registro data e percentual, então os valores anterior e novo ficam no histórico.
4. Dado um contrato com periodicidade informada, quando a data chega, então a área responsável é avisada.

Requisito: RF-09. Regras: RN-10. Pendências: DP-07. Depende de: US-01.

#### F-04: Carga e transição

**US-10: Carregar os contratos saneados** (prioridade 1, F1, HITL)

Como Jurídico, quero carregar os contratos conferidos, para o sistema começar com dados confiáveis.

Critérios de aceite:

1. Dado o CT-2024-0117, quando carregado, então o SLA de atendimento é 4 h e o valor é R$ 11.040,00 por mês.
2. Dado o CT-2025-0064, quando carregado, então o índice é IPCA.
3. Dado o CT-2023-0088, quando carregado, então o fim é 31/12/2026.
4. Dado o CT-2026-0021, quando carregado, então está registrado, com aviso de que foi assinado localmente.
5. Dado um campo não conferido com o documento, quando consulto, então ele aparece como não confirmado.
6. Dado o fim da carga, quando concilio, então os totais conferem com o relatório, incluindo os 393 equipamentos, ou a diferença é explicada.

Requisito: RF-10. Regras: RN-08. RNF: RNF-06. Pendências: DP-04, DP-05, DP-08. Depende de: US-01, US-02, US-03.

**US-11: Levantar contratos fora do registro** (prioridade 1, F1, HITL)

Como Gerente de Suprimentos, quero descobrir outros contratos não registrados, para nenhum contrato ser pago como OC avulsa.

Critérios de aceite:

1. Dado o histórico de OCs, quando analisado, então são listadas OCs recorrentes por fornecedor e objeto, começando pela Hemofix.
2. Dado que as unidades podem ter assinado localmente, quando cada uma responde ao levantamento, então a resposta fica registrada.
3. Dado um contrato encontrado, quando confirmado, então entra na carga.

Requisito: RF-11. Regras: RN-08. Pendências: DP-10.

**US-36: Adequar fluxo e planilha à Política na transição** (prioridade 1, F1, HITL)

Como Gerente de Engenharia Clínica, quero operar com as regras certas enquanto o sistema não chega, para não repetir os erros durante a transição.

Critérios de aceite:

1. Dado o fluxo, quando revisado, então prevê parecer acima de R$ 30.000,00 e renovação em 120 dias.
2. Dada a planilha, quando revisada, então "A renovar" é contado a 120 dias e as correções do CT-2023-0088 e do CT-2024-0117 constam dela.
3. Dado um contrato com vencimento antes de 30/06/2027, quando sua renovação é decidida, então o resultado é anotado para a carga.
4. Dada a entrada em operação, quando concluída, então a planilha fica somente leitura.

Requisito: RF-36. Regras: RN-07, RN-09. Pendências: DP-07.

### EP-02: Aprovações conforme a Política

#### F-05: Requisição e cotação

**US-12: Abrir requisição** (prioridade 2, F1, AFK)

Como Analista de Engenharia Clínica, quero abrir requisição com unidade, patrimônio e objeto, para Suprimentos não precisar redigitar.

Critérios de aceite:

1. Dada uma requisição, quando salvo sem unidade, descrição ou valor estimado, então o sistema recusa.
2. Dada uma requisição digitada por Suprimentos, quando salvo, então a área demandante e quem digitou ficam registrados separadamente.
3. Dada uma requisição com patrimônio inexistente, quando salvo, então o sistema recusa.

Requisito: RF-12. Regras: RN-03. Pendências: DP-11.

**US-13: Exigir cotações por faixa** (prioridade 2, F1, AFK)

Como Analista de Compras, quero saber quantas cotações são exigidas, para cumprir a Política.

Critérios de aceite:

1. Dada uma compra de R$ 5.000,00, quando encaminho, então a cotação é dispensada.
2. Dada uma compra de R$ 5.000,01 a R$ 15.000,00, quando encaminho com menos de duas cotações, então o sistema impede.
3. Dada uma compra acima de R$ 15.000,00, quando encaminho com menos de três, então o sistema impede; o caso da OC-2026-00440, de R$ 19.800,00 e uma cotação, é recusado.
4. Dada uma compra emergencial, quando encaminho com uma proposta, então o sistema aceita.

Requisito: RF-13. Regras: RN-04. Depende de: US-12, US-14.

#### F-06: Alçadas

**US-14: Manter os limites da Política como parâmetros** (prioridade 2, F1, AFK)

Como Diretor Financeiro, quero atualizar limites com data de vigência, para a próxima revisão não ficar esquecida no sistema.

Critérios de aceite:

1. Dado um limite, quando crio um novo valor com data futura, então o valor atual vale até essa data.
2. Dada uma aprovação passada, quando consulto, então vejo o limite vigente na época.
3. Dado um usuário sem perfil administrativo, quando tenta alterar, então o sistema impede, e toda mudança fica na trilha.
4. Dada a carga inicial, quando consulto, então os valores são os da Política e da Portaria.

Requisito: RF-14. Regras: RN-01, RN-02, RN-04, RN-06, RN-07, RN-09, RN-12, RN-14. Pendências: DP-05.

**US-15: Aprovar OC pela alçada** (prioridade 2, F1, AFK)

Como Gerente de Suprimentos, quero receber para aprovação só o que me cabe, para respeitar a Política.

Critérios de aceite:

1. Dada uma OC de até R$ 50.000,00, quando encaminho, então vai à Gerente de Suprimentos.
2. Dada a OC de R$ 72.500,00, quando encaminho, então vai ao Diretor Financeiro e a Gerente não consegue aprová-la.
3. Dada uma OC acima de R$ 250.000,00, quando encaminho, então vai à Diretora Geral.
4. Dada uma OC aprovada, quando o valor aumenta, então a aprovação é reaberta.
5. Dada uma OC sem aprovador, quando tento emiti-la como regular, então o sistema impede.

Requisito: RF-15. Regras: RN-01, RN-22. Pendências: DP-05, DP-10. Depende de: US-13, US-14, US-20.

**US-16: Impedir autoaprovação** (prioridade 2, F1, HITL)

Como Diretor Financeiro, quero impedir que o solicitante aprove a própria compra, para garantir a segregação.

Critérios de aceite:

1. Dada a OC em que solicitante e aprovador são a mesma pessoa, como a OC-2026-00420, quando tento aprovar, então o sistema impede.
2. Dado que o aprovador é o solicitante, quando a OC é encaminhada, então vai ao substituto definido (provisório: nível acima, DP-11).
3. Dada uma tentativa impedida, quando consulto a trilha, então ela está registrada.

Requisito: RF-16. Regras: RN-03. Pendências: DP-11. Depende de: US-15.

**US-17: Aprovar contrato por valor global, com parecer** (prioridade 2, F1, AFK)

Como Diretora Geral, quero aprovar contratos pelo valor total da vigência, para as decisões certas chegarem à alçada certa.

Critérios de aceite:

1. Dado um contrato assinado desde 01/01/2025, quando encaminho, então a alçada usa o valor global da vigência: R$ 528.000,00 vai à Diretora Geral e R$ 163.200,00, ao Diretor Financeiro.
2. Dado um contrato acima de R$ 30.000,00, quando encaminho sem parecer, então o sistema impede; com R$ 30.000,00, o parecer é dispensado.
3. Dado um contrato em moeda estrangeira, quando encaminho, então a alçada usa o câmbio de referência (suposição).
4. Dada uma aprovação, quando consulto, então vejo parecer, aprovador, data e valor considerado.

Requisito: RF-17. Regras: RN-02, RN-07, RN-22. Pendências: DP-05, DP-06. Depende de: US-01, US-14, US-20.

**US-18: Alertar possível fracionamento** (prioridade 2, F1, HITL)

Como Diretor Financeiro, quero ser alertado de possível fracionamento, para evitar burla de alçada.

Critérios de aceite:

1. Dadas as OCs 00301, 00302 e 00303 da mesma requisição, quando encaminhadas, então o sistema alerta e usa a alçada da soma, R$ 149.300,00.
2. Dadas OCs ao mesmo fornecedor e objeto dentro do período (provisório: 30 dias, DP-11), quando encaminhadas, então o sistema alerta.
3. Dado um alerta, quando o aprovador decide, então a justificativa fica na trilha.

Requisito: RF-18. Regras: RN-05. Pendências: DP-11. Depende de: US-15.

#### F-07: Compra emergencial

**US-19: Tratar compra emergencial conforme a Portaria** (prioridade 2, F1, AFK)

Como Diretor Técnico, quero aprovar compras emergenciais sem as alçadas comuns, para não parar a assistência.

Critérios de aceite:

1. Dada a OC-2026-00412, de R$ 92.000,00, com uma proposta e aprovação do Diretor Técnico em 2 dias, quando registrada, então é aceita.
2. Dada uma compra acima de R$ 100.000,00 por ocorrência, quando marcada como emergencial, então o sistema recusa.
3. Dada uma OC sem aprovação após 72 h da emissão, quando o prazo vence, então o sistema alerta o Diretor Técnico e Suprimentos.
4. Dada a reunião do Comitê, quando Suprimentos gera a lista, então constam as compras emergenciais desde a última reunião.

Requisito: RF-19. Regras: RN-06. Depende de: US-13, US-20.

#### F-08: Auditoria e acesso

**US-20: Registrar trilha de auditoria** (prioridade 2, F1, AFK)

Como Diretor Financeiro, quero consultar quem aprovou o quê, e quando, para haver prova de conformidade.

Critérios de aceite:

1. Dada uma aprovação, rejeição, exceção ou alteração de contrato, quando ocorre, então registra autor, data e hora, ação, valores anterior e novo e justificativa.
2. Dado um registro da trilha, quando qualquer usuário tenta alterá-lo ou apagá-lo, então o sistema impede.
3. Dado um filtro por contrato, OC ou usuário, quando consulto, então vejo os registros.
4. Dado um registro, quando inspecionado, então não contém dados de paciente.

Requisito: RF-20. Regras: RN-22. RNF: RNF-01, RNF-02, RNF-08. Pendências: DP-18.

**US-21: Controlar acesso por função e unidade** (prioridade 2, F1, AFK)

Como Encarregado de dados, quero que cada usuário veja só o necessário, para reduzir exposição.

Critérios de aceite:

1. Dado um usuário, quando acessa, então usa conta individual, sem conta compartilhada.
2. Dado um usuário de uma unidade, quando consulta, então vê apenas o permitido ao seu perfil.
3. Dado um prestador, quando tenta acessar na fase 1, então não há perfil para ele.
4. Dada a mudança de perfil, quando ocorre, então fica na trilha.

Requisito: RF-21. Regras: RN-21. RNF: RNF-03. Pendências: DP-18. Depende de: US-20.

### EP-03: Ligação entre OS, requisição e medição

#### F-09: Integração com ManutClin

**US-22: Consultar OS e inventário do ManutClin sem dados de paciente** (prioridade 3, F1, HITL)

Como Analista de Engenharia Clínica, quero ver OS e equipamentos no novo sistema, para não digitar de novo.

Critérios de aceite:

1. Dada a integração, quando executada, então só os campos da lista positiva são lidos; paciente_nome, paciente_prontuario e descricao ficam fora.
2. Dada uma falha, quando ocorre, então o erro e a data da última sincronização ficam visíveis.
3. Dada uma nova execução, quando reprocessa, então não há duplicidade.
4. Dada uma OS alterada na origem depois de lida, quando sincronizada, então a mudança fica registrada.

Requisito: RF-22. Regras: RN-21. RNF: RNF-02, RNF-04, RNF-05, RNF-06. Pendências: DP-01, DP-17, DP-18.

**US-23: Abrir requisição a partir da OS** (prioridade 3, F1, AFK)

Como Analista de Engenharia Clínica, quero gerar requisição a partir da OS, para acabar com a redigitação.

Critérios de aceite:

1. Dada uma OS em AGUARDANDO_COMPRA, quando peço a requisição, então unidade, patrimônio, OS e contrato vêm preenchidos.
2. Dada a requisição gerada, quando consulto a OS ou a requisição, então o vínculo é estruturado, não texto.
3. Dada uma OS em AGUARDANDO_COMPRA sem requisição, quando consulto a lista, então ela aparece, como a OS 88240.
4. Dada a compra concluída, quando consulto, então vejo OS, requisição e OC ligadas ao patrimônio.

Requisito: RF-23. Pendências: DP-01. Depende de: US-12, US-22.

#### F-10: Medição e ateste

**US-24: Gerar medição por contrato e competência** (prioridade 3, F1, AFK)

Como Analista de Engenharia Clínica, quero ter uma medição mensal por contrato, para controlar o pagamento.

Critérios de aceite:

1. Dado um contrato e competência com medição, quando tento criar outra, então o sistema recusa.
2. Dado o valor do contrato, quando a medição é criada, então usa o valor mensal vigente, em sua moeda.
3. Dado o contrato sem registro, quando tento criar a medição, então o sistema recusa, com orientação de registrar antes.

Requisito: RF-24. Regras: RN-13. RNF: RNF-09. Depende de: US-01.

**US-25: Conferir medição com as OS da competência** (prioridade 3, F1, HITL)

Como Analista de Engenharia Clínica, quero ver as OS da competência junto da medição, para reduzir o trabalho manual.

Critérios de aceite:

1. Dada uma medição, quando abro, então vejo as OS do contrato na competência, com tempos e SLA.
2. Dada uma OS que cita contrato diferente do equipamento, quando há conferência, então é indicada como divergente.
3. Dada uma integração incompleta, quando abro a medição, então a conferência é marcada como incompleta.
4. Dado o trabalho atual das analistas, quando DP-13 for respondida, então a lista de checagens é validada com elas.

Requisito: RF-25. Regras: RN-13, RN-14. RNF: RNF-04. Pendências: DP-13. Depende de: US-22, US-24, US-29.

**US-26: Atestar medição** (prioridade 3, F1, AFK)

Como Gerente de Engenharia Clínica, quero atestar no sistema, para o pagamento depender do ateste.

Critérios de aceite:

1. Dada uma medição, quando atesto, então autor, data e resultado são registrados.
2. Dado um usuário fora da Engenharia Clínica, quando tenta atestar, então o sistema impede.
3. Dada uma medição sem ateste, como a 9002, quando tentam liberá-la, então o sistema impede.
4. Dada uma medição atestada, quando há mudança posterior no valor, então o ateste é reaberto.

Requisito: RF-26. Regras: RN-13, RN-22. Depende de: US-20, US-24.

#### F-11: Liberação para pagamento

**US-27: Liberar para pagamento com vencimento calculado** (prioridade 3, F1, HITL)

Como Analista Financeiro, quero receber os títulos liberados com vencimento correto, para não alterar vencimentos à mão.

Critérios de aceite:

1. Dada uma medição atestada e a nota informada, quando libero, então o vencimento padrão é 45 dias da emissão.
2. Dado um prazo inferior a 30 dias, quando a compra não é emergencial, então o sistema impede.
3. Dada uma compra emergencial, quando informo prazo inferior a 30 dias, então o sistema aceita.
4. Dada a liberação, quando concluída, então o título segue ao Financeiro pelo meio definido em DP-12, com valor líquido de glosa.

Requisito: RF-27. Regras: RN-12, RN-13. RNF: RNF-06. Pendências: DP-01, DP-12. Depende de: US-14, US-26.

**US-28: Tratar pagamento de contrato vencido** (prioridade 3, F1, HITL)

Como Diretor Financeiro, quero decidir de forma justificada sobre pagamento de contrato vencido, para regularizar sem interromper a assistência.

Critérios de aceite:

1. Dado um contrato vencido, quando abro OS, então o atendimento não é impedido.
2. Dado um contrato vencido, quando a medição é enviada para liberação, então o sistema exige exceção justificada e aprovada (provisório, DP-09).
3. Dada uma exceção, quando concedida, então fica na trilha e entra em relatório ao Comitê.

Requisito: RF-28. Regras: RN-20. Pendências: DP-09. Depende de: US-05, US-27.

### EP-04: Glosa por SLA

#### F-12: SLA e glosa

**US-29: Calcular atendimento de SLA por OS** (prioridade 4, F1, HITL)

Como Analista de Engenharia Clínica, quero ver se cada OS cumpriu o SLA, para ter base objetiva para a glosa.

Critérios de aceite:

1. Dada a OS 88170, com atendimento em 14h10, e SLA de 4 h, quando calculada, então há violação.
2. Dada a OS 88271, com 5h30 e 32 h e SLA de 6 h e 48 h, quando calculada, então não há violação.
3. Dada uma OS com espera de peça, como a 88190, quando calculada, então fica pendente de decisão humana (provisório, DP-13).
4. Dado um horário alterado na origem, quando calculada, então é indicado.

Requisito: RF-29. Regras: RN-14. RNF: RNF-04. Pendências: DP-13. Depende de: US-01, US-22.

**US-30: Sugerir e decidir glosa** (prioridade 4, F1, HITL)

Como Gerente de Engenharia Clínica, quero receber a sugestão e decidir, para aplicar a Política.

Critérios de aceite:

1. Dada a violação da OS 88170, quando sugerida, então o valor é 2% de R$ 11.040,00: R$ 220,80 (provisório: por OS, DP-13).
2. Dada uma sugestão, quando decido aplicar ou rejeitar, então a justificativa é obrigatória e fica na trilha.
3. Dada uma glosa aplicada, quando libero, então o título sai com o valor líquido.
4. Dado um contrato em moeda estrangeira, quando calculo, então a glosa fica na moeda do contrato.

Requisito: RF-30. Regras: RN-14. RNF: RNF-09. Pendências: DP-13. Depende de: US-26, US-27, US-29.

### EP-05: Visão consolidada e conformidade técnica

#### F-13: Visão consolidada

**US-31: Consultar visão consolidada** (prioridade 4, F1, AFK)

Como Diretora Geral, quero ver a rede por contrato, fornecedor, equipamento e unidade, para acompanhar e decidir.

Critérios de aceite:

1. Dada uma consulta por qualquer das quatro dimensões, quando filtro, então vejo contratos, vigência, valor, OS e medições relacionados.
2. Dados valores em moedas diferentes, quando somados, então o total em reais é rotulado como câmbio de referência.
3. Dada a visão por equipamento, quando consulto na F1, então ela não mostra custo total (F2).
4. Dado um dado não confirmado, quando aparece, então vem sinalizado.

Requisito: RF-31. Regras: RN-11. RNF: RNF-09. Pendências: DP-14. Depende de: US-03, US-05, US-22, US-24.

**US-32: Acompanhar indicadores do processo** (prioridade 4, F1, HITL)

Como Diretor Financeiro, quero ver os indicadores essenciais, para saber se o sistema melhorou o processo.

Critérios de aceite:

1. Dado o período, quando consulto, então vejo ciclo de contratação, espera por parecer, medições sem ateste e glosas.
2. Dado um novo indicador definido em DP-03, quando aprovado, então é incluído na lista.
3. Dado um número, quando consulto, então vejo a regra de cálculo e o período.

Requisito: RF-32. Pendências: DP-03. Depende de: US-17, US-26.

#### F-14: Conformidade técnica

**US-33: Classificar criticidade oficial do equipamento** (prioridade 3, F1, HITL)

Como Gerente de Engenharia Clínica, quero registrar o nível oficial de cada equipamento, para usar uma única classificação.

Critérios de aceite:

1. Dado um equipamento A, quando carregado, então fica no nível 1; C, no nível 4.
2. Dado um equipamento B, quando carregado, então fica pendente de reclassificação, sem valor padrão, e aceita apenas 2 ou 3.
3. Dada a lista de pendentes, quando filtro por unidade, então acompanho a reclassificação.
4. Dado o Crítico/Não crítico da planilha, quando consulto, então aparece apenas como dado histórico.

Requisito: RF-33. Regras: RN-17. Pendências: DP-15. Depende de: US-22.

**US-34: Monitorar exceções técnicas de equipamento** (prioridade 2, F1, HITL)

Como Diretor Técnico, quero ver equipamentos com exceções, para agir antes de novo incidente.

Critérios de aceite:

1. Dada uma OS fechada sem teste aprovado ou liberação, como a 88213, quando sincronizada, então aparece no painel, sem dados de paciente.
2. Dado um equipamento EM_USO com calibração vencida, quando sincronizado, então aparece no painel, com prioridade por nível oficial.
3. Dada uma calibração a vencer, quando faltar o prazo definido, então a Engenharia Clínica é avisada.
4. Dada uma exceção, quando tratada, então o responsável registra a providência.

Requisito: RF-34. Regras: RN-15, RN-16. RNF: RNF-02. Pendências: DP-16, DP-17. Depende de: US-22.

### EP-06: Segunda fase

#### F-15: Custo por equipamento

**US-35: Apurar custo por equipamento** (prioridade 4, F2, HITL)

Como Diretora Geral, quero saber quanto custa manter cada equipamento, para decidir entre manter e substituir.

Critérios de aceite:

1. Dado um equipamento, quando consulto, então vejo contrato rateado, chamados e peças, conforme a regra definida em DP-14.
2. Dado um gasto sem patrimônio, quando apurado, então aparece como não alocado, nunca rateado silenciosamente.
3. Dado um contrato em dólar, quando apurado, então o critério de câmbio de DP-14 é informado.

Requisito: RF-35. Pendências: DP-14. Depende de: US-23, US-31.

## Revisão de minimalismo (ponytail)

Três candidatas foram descartadas: portal do prestador (fora da fase 1, por decisão da Diretora Geral), motor genérico de workflow e regras (bastam parâmetros com vigência, US-14) e busca automática de índices econômicos (basta registro e agenda, US-09). Histórias pedidas, segurança, auditoria e ateste não foram cortados. Registro em `.product-team/artifacts/sistema-unico-manutencao/feature.json`.

## Importação

- **`05-jira.csv`:** o Jira não tem Feature por padrão, então cada feature vai em `Component/s` e em um rótulo. Mapeie `Parent Id` para a hierarquia e `Acceptance Criteria` para um campo personalizado; os critérios também estão em `Description`.
- **`06-azure-devops.csv`:** hierarquia por `Title 1`, `Title 2` e `Title 3`, com Epic, Feature e User Story (processo Agile) e prioridades de 1 a 4.
- Os dois arquivos foram validados quanto a estrutura e conteúdo, mas não testados em uma instância real.
