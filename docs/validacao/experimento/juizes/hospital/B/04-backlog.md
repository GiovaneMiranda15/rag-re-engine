# 04. Backlog ágil

Primeira fase, com entrada em operação até 30/06/2027. Sem estimativas: a equipe e a estratégia de construção não estão definidas (R1, R2).

- **Prioridade:** 1 a 4 segue a ordem da patrocinadora (R2). O EP-06 é prioridade 1 por habilitar os demais.
- **Corte, se faltar prazo:** sai primeiro o EP-04, depois o F-05.1. O custo por equipamento já está na fase 2.
- **"A validar":** a história depende de uma decisão D-*n* de `02-negocio.md`, seção 9, e pode mudar.
- **Ordem de construção sugerida:** F-06.1 e F-06.2; EP-01, com F-06.3 em paralelo; EP-02; EP-03; F-05.1; EP-04.
- **Antes de começar:** decidir D-01 e D-04. Validar D-10 antes de F-03.4 e D-08 antes de EP-04.
- **Versão:** atualizado com `mudancas/` (ver `08-mudancas.md`): inclui HU-044 e ajusta HU-016, HU-020, HU-034, HU-041 e HU-042.
- **Importação:** o Jira padrão não tem o tipo Feature, por isso `05-jira.csv` traz a feature em `Components` de cada história. No assistente de importação, use `Parent` (projetos gerenciados pela equipe) ou `Epic Name` e `Epic Link` (gerenciados pela empresa), e não os dois. `06-azure-devops.csv` usa a hierarquia Epic, Feature e User Story do processo Agile.

## Resumo

| Épico | Título | Prioridade | Features | Histórias |
|---|---|---:|---:|---:|
| EP-01 | Cadastro único de contratos e renovação | 1 | 3 | 10 |
| EP-02 | Aprovações conforme a Política, com trilha de auditoria | 2 | 6 | 11 |
| EP-03 | Ligação entre OS, requisição, medição e ateste | 3 | 4 | 10 |
| EP-04 | Glosa por SLA | 4 | 2 | 4 |
| EP-05 | Visão consolidada e custo por equipamento | 3 | 2 | 3 |
| EP-06 | Fundação: acesso, unidades e migração | 1 | 3 | 6 |
| **Total** | | | **20** | **44** |

## EP-01. Cadastro único de contratos e renovação

Fonte única de contratos, com vigência, valor, SLA, aditivos, reajustes e alertas de renovação. Prioridade 1 da patrocinadora (R2).

### F-01.1. Contratos e fornecedores

**HU-001. Cadastrar contrato com dados completos** (prioridade 1)

Como analista do Jurídico, quero registrar cada contrato em um único lugar, para que as áreas deixem de depender de planilha e cópias em PDF.

Critérios de aceite:

- Dado um contrato novo, quando salvo sem vigência, valor, moeda, índice, SLA de atendimento ou SLA de solução, então o sistema recusa e indica o campo faltante.
- Dado um número de contrato já existente, quando salvo, então o sistema recusa a duplicidade.
- Dado um contrato de R$ 6.800,00 mensais por 24 meses, quando salvo, então o valor global exibido é R$ 163.200,00.

Requisitos: RF-01, RN-20, RNF-01.

**HU-002. Manter fornecedor único por CNPJ** (prioridade 1)

Como comprador, quero ter um único cadastro por fornecedor, para que contratos da mesma empresa sejam consolidados.

Critérios de aceite:

- Dado o fornecedor MTS Engenharia Biomédica, quando pesquiso por "BioVolt" ou "MTS", então encontro o mesmo cadastro.
- Dado um CNPJ já cadastrado, quando tento novo cadastro, então o sistema recusa.
- Dado um CNPJ com máscara, quando salvo, então guarda 14 dígitos.

Requisitos: RF-02, RN-19.

**HU-003. Registrar contrato em moeda estrangeira** (prioridade 1)

Como Diretor Financeiro, quero registrar o contrato em sua moeda e definir o câmbio de referência, para que o controle orçamentário não misture moedas.

Critérios de aceite:

- Dado o CT-2025-0031, quando registrado, então guarda US$ 9.800,00 mensais, sem índice de reajuste.
- Dado um perfil que não seja o de Diretor Financeiro, quando tenta alterar o câmbio de referência, então é recusado.
- Dado um câmbio de 5,40, quando consultado o valor anual, então mostra US$ 117.600,00 e R$ 635.040,00, identificado como valor de referência.

Requisitos: RF-01, RN-11, RNF-06.

**HU-004. Exigir registro central de contrato assinado na unidade** (prioridade 1)

Como gestor de Suprimentos, quero que nenhum contrato fique fora do cadastro, para que não se repita o caso de contrato pago só por ordens avulsas.

Critérios de aceite:

- Dado um serviço continuado sem contrato registrado, quando se tenta liberar pagamento, então o sistema bloqueia e pede o registro.
- Dado o registro de contrato já assinado na unidade, quando salvo, então fica marcado como "a regularizar" até ter a aprovação e o parecer exigidos.

Requisitos: RF-01, RF-22, RN-08.

### F-01.2. Aditivos e reajustes

**HU-005. Registrar aditivo com histórico e aviso ao Jurídico** (prioridade 1)

Como comprador, quero lançar o aditivo com o que mudou, para que o Jurídico saiba na hora e a vigência fique correta em toda a Rede.

Critérios de aceite:

- Dado um aditivo confirmado, então guarda sequência, data, documento, valores antes e depois, e o histórico permanece.
- Dado um aditivo confirmado, então o Jurídico é notificado no mesmo momento.
- Dado um aditivo que mude a faixa do valor global, então exige nova aprovação na alçada e parecer correspondentes.
- Dado o CT-2023-0088 com o aditivo 2, quando consultado, então o fim é 31/12/2026 e a situação não é "Vencido".

Requisitos: RF-04, RN-02, RN-07, RNF-01.

**HU-006. Registrar reajuste e sinalizar atraso** (prioridade 1; a validar: D-11)

Como analista financeiro, quero aplicar o índice correto e ver reajustes atrasados, para que o valor do contrato fique correto.

Critérios de aceite:

- Dado contrato em moeda nacional assinado desde 01/01/2024, quando cadastrado, então o índice proposto é IPCA.
- Dado contrato anterior a essa data, quando cadastrado, então mantém o índice original.
- Dado contrato em moeda estrangeira, quando cadastrado, então não aceita índice.
- Dada a periodicidade parametrizada vencida sem registro de reajuste, quando consultado, então o contrato é sinalizado.

Requisitos: RF-05, RN-10, RN-11.

### F-01.3. Renovação

**HU-007. Calcular a situação do contrato pelas datas** (prioridade 1)

Como gestor de contratos, quero ver a situação real, sem digitação, para que contrato vencido não pareça vigente.

Critérios de aceite:

- Dada a data de fim já passada e sem aditivo, quando consultado, então a situação é "Vencido", mesmo com renovação em andamento.
- Dado um aditivo prorrogando a vigência, quando salvo, então a situação é recalculada no mesmo momento.
- A situação não pode ser editada manualmente por nenhum perfil.

Requisitos: RF-06.

**HU-008. Alertar renovação 120 dias antes do fim** (prioridade 1)

Como gestor da área e Jurídico, quero receber o aviso de início da renovação, para que a renovação comece no prazo da Política.

Critérios de aceite:

- Dado um contrato com fim em 31/01/2027, quando chega 03/10/2026, então área gestora e Jurídico recebem o alerta.
- Dado um alerta não tratado, quando passa o intervalo parametrizado (proposta: 7 dias), então é repetido aos dois e à Gerente de Suprimentos.
- Dado o parâmetro de antecedência alterado com nova vigência, quando salvo, então os próximos cálculos usam o novo valor.

Requisitos: RF-06, RF-16, RN-09.

**HU-009. Acompanhar renovações em andamento** (prioridade 1)

Como Jurídico, quero ver responsável, etapa e atraso de cada renovação, para que o Comitê saiba o que está em risco.

Critérios de aceite:

- Dada uma renovação, quando consultada, então mostra responsável, etapa e dias até o fim.
- Dado um contrato na janela sem renovação iniciada, quando vejo o painel, então aparece como atrasado.
- Dado um contrato vencido com serviço em andamento, quando vejo o painel, então aparece em destaque.

Requisitos: RF-07, RN-09.

**HU-010. Tratar exceção de contrato vencido com serviço em andamento** (prioridade 1; a validar: D-06)

Como Diretora Geral, quero aprovar exceção justificada, para que serviço crítico continue, sem pagamento sem controle.

Critérios de aceite:

- Dado um contrato vencido, quando se tenta liberar pagamento, então o sistema bloqueia.
- Dada uma exceção com justificativa, prazo e aprovação da Diretora Geral, quando ativa, então o pagamento é permitido só naquele prazo e fica na trilha.

Requisitos: RF-22, RN-18, RNF-01.

## EP-02. Aprovações conforme a Política, com trilha de auditoria

Requisição, cotação, alçada, parecer e emergencial aplicando POL-SUP-004 rev. 3 e Portaria DG-017/2025. Prioridade 2 da patrocinadora (R2).

### F-02.1. Requisição e cotação

**HU-011. Criar requisição com unidade e equipamento** (prioridade 2; a validar: D-12)

Como solicitante, quero registrar a necessidade com o equipamento, para que o custo possa ser ligado ao equipamento.

Critérios de aceite:

- Dada uma requisição de manutenção, quando salva sem unidade ou equipamento, então é recusada, salvo serviço marcado como "sem etiqueta" com justificativa.
- Dada uma categoria de medicamento, OPME, obra predial ou prontuário, quando escolhida, então o sistema não permite o registro.

Requisitos: RF-08.

**HU-012. Exigir cotações conforme a faixa** (prioridade 2)

Como comprador, quero saber quantas cotações são necessárias, para que a compra siga a Política.

Critérios de aceite:

- Dado R$ 5.000,00, então a compra dispensa cotação.
- Dado R$ 5.000,01 ou R$ 15.000,00, então exige duas cotações.
- Dado R$ 15.000,01, então exige três, e um caso como a OC-2026-00440 (R$ 19.800,00, uma cotação) é bloqueado.
- A regra vale para todos os tipos de compra, exceto emergencial.

Requisitos: RF-09, RN-04.

### F-02.2. Alçadas e segregação

**HU-013. Encaminhar ordem de compra pela alçada** (prioridade 2)

Como Gerente de Suprimentos, quero receber só o que está na minha alçada, para que aprovações sigam a Política.

Critérios de aceite:

- Dado R$ 50.000,00, então aprova a Gerente de Suprimentos.
- Dado R$ 50.000,01 ou R$ 72.500,00, então aprova o Diretor Financeiro.
- Dado R$ 250.000,00, então aprova o Diretor Financeiro; dado R$ 250.000,01, a Diretora Geral.
- Um aprovador vazio ou sem alçada não permite concluir a aprovação.

Requisitos: RF-10, RN-01, RN-02.

**HU-014. Aprovar contrato pelo valor global** (prioridade 2)

Como Diretor Financeiro, quero aprovar contratos pelo valor de toda a vigência, para que contratos de valor alto não passem como mensalidade baixa.

Critérios de aceite:

- Dado R$ 6.800,00 mensais por 24 meses (global R$ 163.200,00), então aprova o Diretor Financeiro, e não a Gerente de Suprimentos.
- Dado contrato em USD, então a alçada usa o valor global convertido pelo câmbio de referência.

Requisitos: RF-10, RN-01, RN-02, RN-11.

**HU-015. Impedir que o solicitante aprove** (prioridade 2; a validar: D-05)

Como auditor, quero garantir a segregação de funções, para que ninguém aprove a própria compra.

Critérios de aceite:

- Dado que o solicitante é o aprovador da alçada, quando chega à aprovação, então o sistema impede e encaminha à alçada seguinte.
- A tentativa fica registrada na trilha.

Requisitos: RF-11, RN-03.

**HU-016. Parametrizar regras com vigência** (prioridade 2)

Como administrador de regras, quero alterar limites por nova vigência, para que o sistema não fique defasado da Política.

Critérios de aceite:

- Dado um limite novo com data de início, quando salvo, então vale só para processos iniciados a partir dela.
- Dado um processo aprovado, quando consultado, então mostra a versão da regra aplicada.
- O limite de parecer inicial é R$ 30.000,00; a mudança para R$ 200.000,00 (proposta em R3, Memorando 2026/14) só entra por nova versão, depois de comprovada a aprovação da Diretoria.

Requisitos: RF-16, RN-07, RNF-04.

### F-02.3. Fracionamento

**HU-017. Detectar possível fracionamento** (prioridade 2; a validar: D-05)

Como Diretor Financeiro, quero ver compras possivelmente divididas, para que a Política não seja contornada.

Critérios de aceite:

- Dadas três OCs da mesma requisição que somam R$ 149.300,00, então a alçada considera a soma e a aprovação vai ao Diretor Financeiro.
- Dadas OCs de mesmo fornecedor e objeto em 30 dias, com soma que mude a faixa, então o sistema alerta e exige justificativa.
- Alertas e justificativas ficam em relatório.

Requisitos: RF-12, RN-05.

### F-02.4. Compra emergencial

**HU-018. Registrar compra emergencial** (prioridade 2)

Como Gerente de Eng. Clínica, quero abrir compra emergencial com uma proposta, para que o equipamento parado volte logo, conforme a Portaria.

Critérios de aceite:

- Dada uma compra acima de R$ 100.000,00 por ocorrência, então não pode ser emergencial.
- Dada uma compra emergencial, então exige uma proposta e a OS do equipamento parado.
- Só o Diretor Técnico aprova, em até 72 h da emissão; ao fim do prazo sem aprovação, gera alerta à Diretora Geral.
- Um caso como a OC-2026-00412 (R$ 92.000,00, aprovada em 2 dias) é aceito.

Requisitos: RF-13, RN-06.

**HU-019. Listar compras emergenciais para o Comitê** (prioridade 2)

Como Gerente de Suprimentos, quero obter a lista para a próxima reunião, para que o Comitê seja informado.

Critérios de aceite:

- Dada a data da reunião anterior, quando gero a lista, então vêm as compras emergenciais do período, com valor, OS, aprovador e prazo.
- Cada item fica marcado como informado, com a data da reunião.

Requisitos: RF-17, RN-06.

### F-02.5. Parecer jurídico

**HU-020. Conduzir parecer jurídico** (prioridade 2)

Como Jurídico, quero receber, emitir e devolver pareceres na ferramenta, para que se saiba onde o tempo é gasto.

Critérios de aceite:

- Com o limite vigente de R$ 30.000,00, contrato de R$ 30.000,00 de valor global não exige parecer; de R$ 30.000,01, exige.
- Dado parecer exigido e não emitido, então a aprovação fica bloqueada.
- Dado um parecer, então o tempo em fila, em análise e com o fornecedor são medidos separadamente.

Requisitos: RF-14, RN-07.

### F-02.6. Auditoria

**HU-021. Manter trilha de auditoria das aprovações** (prioridade 2)

Como auditor, quero saber quem aprovou o quê, quando e por qual regra, para que aprovações sejam comprováveis.

Critérios de aceite:

- Dada uma aprovação ou recusa, então guarda autor, data e hora, valor, versão da regra e justificativa.
- Nenhum perfil edita ou apaga registros da trilha.
- A trilha pode ser exportada por período, contrato ou OC.

Requisitos: RF-15, RNF-01.

## EP-03. Ligação entre OS, requisição, medição e ateste

Integração com ManutClin, requisição a partir da OS, medição e ateste no sistema e liberação para pagamento. Prioridade 3 da patrocinadora (R2).

### F-03.1. Integração com ManutClin

**HU-022. Obter inventário da Engenharia Clínica** (prioridade 3; a validar: D-12)

Como gestor de contratos, quero ver os equipamentos pela etiqueta, para que contrato, OS e custo se liguem ao mesmo equipamento.

Critérios de aceite:

- Dado o inventário, quando sincronizado, então os equipamentos aparecem com etiqueta e unidade, conferindo com o total de 4.812 da base inicial.
- Dado criticidade A ou C, então converte para 1 ou 4.
- Dado B, então fica "2 ou 3, a classificar", tratado como 2, até classificação da Eng. Clínica.
- Falha de sincronização gera alerta.

Requisitos: RF-18, RN-17, RNF-05.

**HU-023. Obter OS sem dados de paciente** (prioridade 3; a validar: D-13)

Como encarregado de dados, quero garantir que nenhum dado de paciente entre no sistema, para que se cumpra a LGPD.

Critérios de aceite:

- Dada a sincronização de OS, então as colunas de paciente e a descrição livre não são lidas.
- Uma verificação automática após cada carga confirma a ausência dessas colunas.
- Dada uma OS, então estão disponíveis etiqueta, tipo, datas, status, contrato, teste, liberação e indicador de evento adverso.

Requisitos: RF-18, RNF-02.

**HU-024. Sinalizar pendências de segurança** (prioridade 3; a validar: D-07)

Como Gerente de Eng. Clínica, quero ver OS fechada sem liberação e calibração vencida em uso, para que o equipamento não siga em uso indevido.

Critérios de aceite:

- Dada uma OS corretiva fechada sem teste aprovado ou sem liberação, então gera alerta à Eng. Clínica e ao Diretor Técnico e a OS fica pendente na medição.
- Dado equipamento em uso com calibração vencida, então gera alerta aos mesmos papéis.
- Dada uma OS com indicador de evento adverso, então avisa a Qualidade e Segurança do Paciente, sem detalhes clínicos.

Requisitos: RF-24, RN-15, RN-16.

### F-03.2. Requisição a partir da OS

**HU-025. Gerar requisição a partir da OS** (prioridade 3; a validar: D-01)

Como analista de Eng. Clínica, quero abrir a requisição sem redigitar, para que a OS não fique parada em compras.

Critérios de aceite:

- Dada uma OS aguardando compra, quando gero a requisição, então etiqueta, unidade, contrato e OS vêm preenchidos.
- A OS e a requisição ficam ligadas, nos dois sentidos, por chave e não por texto livre.
- O tempo em cada etapa, até a entrega, fica disponível.

Requisitos: RF-19, RF-08.

**HU-026. Registrar decisão de cobertura contratual** (prioridade 3; a validar: D-01)

Como analista de Eng. Clínica, quero registrar se a peça é coberta, para que não se compre o que o contrato já cobre.

Critérios de aceite:

- Dada uma requisição a partir de OS sob contrato, então exige o registro "coberta" ou "não coberta", com autor.
- Se coberta, a compra não prossegue sem justificativa.

Requisitos: RF-19.

### F-03.3. Medição e ateste

**HU-027. Gerar medição mensal com as OS da competência** (prioridade 3)

Como analista de Eng. Clínica, quero ver a medição junto das OS, para que a conferência não seja manual.

Critérios de aceite:

- Dado um contrato vigente, quando abre a competência, então a medição traz valor, moeda e OS do período.
- Dada uma OS de outro contrato, então ela não entra.
- Dado o CT-2026-0021 registrado, então a medição substitui as ordens avulsas mensais.

Requisitos: RF-20, RNF-06.

**HU-028. Atestar a medição** (prioridade 3; a validar: D-09)

Como Gerente de Eng. Clínica, quero atestar no sistema, para que o Financeiro só receba o que foi conferido.

Critérios de aceite:

- Só o perfil de atestador pode atestar; o ato registra autor e data.
- Dada uma OS pendente de segurança na medição, então o ateste exige ciência explícita.
- Sem substituto definido, o sistema não permite delegação até que seja configurada.

Requisitos: RF-21, RN-13, RNF-01.

### F-03.4. Liberação para pagamento

**HU-029. Bloquear pagamento sem requisitos** (prioridade 3)

Como Diretor Financeiro, quero que só seja liberado o que atende a Política, para que não se pague sem ateste ou contrato.

Critérios de aceite:

- Dada medição sem ateste, então não é liberada.
- Dado contrato não registrado, ou vencido sem exceção, então não é liberada.
- Cada bloqueio informa o motivo.

Requisitos: RF-22, RN-08, RN-13, RN-18.

**HU-030. Calcular vencimento conforme a Política** (prioridade 3; a validar: D-10)

Como analista financeiro, quero receber o título com o prazo correto, para que não seja preciso ajustar à mão.

Critérios de aceite:

- Dada uma nota emitida, então o vencimento padrão é 45 dias da emissão.
- Dado prazo inferior a 30 dias em compra não emergencial, então é recusado.
- Dada compra emergencial, então aceita menos de 30 dias.

Requisitos: RF-23, RN-12, RN-06.

**HU-031. Enviar autorização de pagamento ao Financeiro** (prioridade 3; a validar: D-10)

Como analista financeiro, quero receber a autorização com valor líquido e vencimento, para que o pagamento siga o que foi atestado.

Critérios de aceite:

- Dada a medição liberada, então envia fornecedor, valor líquido de glosa, moeda e vencimento ao destino definido.
- Falha no envio gera alerta e permite reprocessar sem duplicidade.
- Sem integração disponível, há exportação em arquivo como contingência.

Requisitos: RF-23, RNF-05.

## EP-04. Glosa por SLA

Apuração de SLA e cálculo de glosa com teto. Prioridade 4 da patrocinadora (R2).

### F-04.1. Apuração de SLA

**HU-032. Apurar SLA de atendimento e solução por OS** (prioridade 4; a validar: D-08)

Como analista de Eng. Clínica, quero ver o descumprimento de SLA automaticamente, para que não seja preciso conferir à mão.

Critérios de aceite:

- Dada a OS 88170 no CT-2024-0117 (atendimento em 14h10; SLA de 4 h), então aponta descumprimento.
- O SLA usado é o do contrato no novo sistema, não o do ManutClin.
- Dada uma espera registrada de peça não coberta, então o relógio de solução é suspenso conforme parâmetro.

Requisitos: RF-25, RN-20, RNF-10.

**HU-033. Registrar alterações em dados de atendimento** (prioridade 4)

Como auditor, quero saber se o horário mudou depois da sincronização, para que a glosa não se apoie em dado alterado sem aviso.

Critérios de aceite:

- Dado um atendimento diferente da leitura anterior, então guarda valor antigo, novo e data de detecção.
- Dada uma OS com alteração, então ela fica sinalizada na conferência.

Requisitos: RF-25, RNF-05.

### F-04.2. Glosa

**HU-034. Calcular glosa sugerida com teto** (prioridade 4; a validar: D-08)

Como Gerente de Eng. Clínica, quero receber a glosa calculada, para que o valor siga a Política e o teto.

Critérios de aceite:

- Dado um evento em R$ 11.040,00 mensais, então a glosa é R$ 220,80.
- Dados 6 eventos na mesma competência, então a soma limita-se a R$ 1.104,00 (10% do valor mensal do contrato).
- Em contrato em USD, a glosa fica em USD.
- Percentual e teto são parâmetros com vigência.

Requisitos: RF-26, RN-14, RF-16.

**HU-035. Decidir e aplicar a glosa na medição** (prioridade 4; a validar: D-08)

Como Gerente de Eng. Clínica, quero aceitar ou ajustar a glosa com justificativa, para que o pagamento reflita a decisão.

Critérios de aceite:

- Dada uma glosa sugerida, então é preciso aceitar ou ajustar, com justificativa.
- Dada uma glosa decidida, então o valor líquido da medição é atualizado.
- Toda decisão fica na trilha.

Requisitos: RF-26, RNF-01.

## EP-05. Visão consolidada e custo por equipamento

Visão da rede exigida no escopo e indicadores do processo; custo por equipamento na fase 2 (R2).

### F-05.1. Visão consolidada e indicadores

**HU-036. Ver visão consolidada da rede** (prioridade 3)

Como Diretora Geral, quero consultar por contrato, fornecedor, equipamento e unidade, para que a Rede tenha uma só visão.

Critérios de aceite:

- Dados os filtros, então os resultados se somam por contrato, fornecedor, equipamento e unidade.
- Moedas nunca se somam sem indicar câmbio.
- BioVolt aparece como fornecedor único nos seus dois contratos.
- Uma nova unidade aparece sem desenvolvimento.

Requisitos: RF-27, RNF-06.

**HU-037. Medir indicadores do processo** (prioridade 3)

Como Diretora Geral, quero acompanhar tempos e bloqueios, para que se saiba se o projeto atingiu seu objetivo.

Critérios de aceite:

- Estão disponíveis ciclo total, tempo em parecer, tempo em compra, renovações em prazo, medições sem ateste e glosas.
- Cada indicador é filtrável por unidade e período.

Requisitos: RF-28.

### F-05.2. Custo por equipamento

**HU-038. Calcular custo por equipamento** (prioridade 4; fase 2)

Como Diretora Geral, quero somar contrato, chamados e peças por equipamento, para que se decida entre manter ou substituir.

Critérios de aceite:

- Dada a regra de rateio definida, então o custo é calculado por equipamento e período.
- Pré-requisito: regra de rateio, custos de equipe própria e critério de decisão, ainda não definidos (R13).

Requisitos: RF-29.

## EP-06. Fundação: acesso, unidades e migração

Habilitadores: perfis, unidades, saneamento e migração dos contratos.

### F-06.1. Perfis e acesso

**HU-039. Controlar acesso por perfil e unidade** (prioridade 1)

Como administrador, quero dar a cada um só o necessário, para que o princípio de menor privilégio seja seguido.

Critérios de aceite:

- Dado um perfil, então só acessa as funções previstas em 03-tecnico.
- Dada uma visão limitada por unidade, então não vê outras unidades.
- Fornecedores não têm acesso na primeira fase.
- Toda mudança de perfil fica registrada.

Requisitos: RF-30, RNF-03.

### F-06.2. Unidades

**HU-040. Manter unidades por cadastro** (prioridade 1; a validar: D-02)

Como administrador, quero incluir uma unidade sem desenvolvimento, para que o Hospital Aurora Serra possa entrar.

Critérios de aceite:

- Dada uma nova unidade com seus códigos de-para, quando salva, então fica disponível em todos os cadastros e consultas.
- Os códigos do ERP e do ManutClin ficam ligados às quatro unidades existentes.

Requisitos: RF-03, RNF-04.

### F-06.3. Saneamento e migração

**HU-041. Sanear contratos contra o documento assinado** (prioridade 1)

Como Jurídico, quero validar cada contrato antes da carga, para que o sistema nasça com dados corretos.

Critérios de aceite:

- Dados os 8 contratos da Rede e os 2 do Hospital Aurora Serra, então cada um tem validação do Jurídico com data e autor.
- Pendências conhecidas (SLA de solução do CT-2024-0117, aditivos do CT-2023-0088, regularização do CT-2026-0021) ficam registradas e visíveis.

Requisitos: RF-31, RN-20.

**HU-042. Migrar contratos, fornecedores e reconciliar** (prioridade 1; a validar: D-14)

Como gestor do projeto, quero carregar os dados e comprovar que batem, para que a transição seja confiável.

Critérios de aceite:

- Dada a carga, então constam os 8 contratos da Rede, atualizados pelas renovações até o corte, e os 2 do Hospital Aurora Serra, com a carteira anual reconciliada a R$ 1.810.080,00 mais os 2 novos, ou ao valor atualizado.
- MTS e BioVolt resultam em um só fornecedor.
- Uma verificação confirma zero dado de paciente.
- Histórico de 24 meses fica disponível para consulta.

Requisitos: RF-31, RF-02, RNF-02.

**HU-043. Encerrar a planilha no corte** (prioridade 1)

Como Jurídico, quero substituir a planilha sem dupla manutenção, para que não voltem as divergências.

Critérios de aceite:

- Dado o corte, então a planilha fica somente leitura, e as áreas recebem acesso de consulta.
- Os avisos de renovação vêm só do sistema, a partir do corte.

Requisitos: RF-31, RF-06.

**HU-044. Carregar os contratos do Hospital Aurora Serra** (prioridade 1; a validar: D-15)

Como Jurídico, quero registrar os dois contratos de manutenção do Hospital Aurora Serra, para que a unidade incorporada esteja na visão única desde a entrada em operação.

Critérios de aceite:

- Dados os 2 contratos, quando carregados, então têm todos os campos obrigatórios, unidade Aurora Serra e validação do Jurídico contra o documento assinado.
- Dado um contrato incorporado, então fica identificado com essa origem, sem exigir nova aprovação até a renovação ou o aditivo, que seguem a Política.
- Dado um equipamento coberto ainda sem etiqueta ou inventário, então o contrato é carregado e o vínculo fica pendente e visível.
- Dado um fornecedor com CNPJ já cadastrado, então o contrato usa o cadastro existente.

Requisitos: RF-03, RF-31, RN-08.
