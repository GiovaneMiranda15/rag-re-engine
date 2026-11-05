# Cenários de teste

> Gerado dos critérios de aceite por `recop.py render`.

| Cenário | Item | Critério | Requisitos |
|---|---|---|---|
| US-001.1 | Controlar acesso por papel e unidade | Dado usuário de Suprimentos, quando abre um contrato, então pode ver e não pode aprovar acima de sua alçada. | RNF-004 |
| US-001.2 | Controlar acesso por papel e unidade | Dado usuário sem papel na unidade, quando tenta abrir uma medição, então o acesso é negado e registrado. | RNF-004 |
| US-001.3 | Controlar acesso por papel e unidade | Dado usuário com papel removido hoje, quando faz nova ação, então a permissão antiga já não vale. | RNF-004 |
| US-002.1 | Cadastrar contrato com vigência, valor e SLA | Dado contrato completo, quando salvo, então guarda número, unidade, fornecedor, início, fim, valor, moeda, índice, SLA de atendimento e de solução e preventiva. | RF-001, RN-009, RN-011 |
| US-002.2 | Cadastrar contrato com vigência, valor e SLA | Dado contrato sem fim de vigência, quando salvo, então o sistema recusa. | RF-001, RN-009, RN-011 |
| US-002.3 | Cadastrar contrato com vigência, valor e SLA | Dado número já cadastrado, quando salvo, então o sistema recusa a duplicidade. | RF-001, RN-009, RN-011 |
| US-003.1 | Validar índice e moeda do contrato | Dado contrato em BRL assinado em 01/01/2024 ou depois, quando salvo com IGP-M, então o sistema recusa. | RN-007, RN-019 |
| US-003.2 | Validar índice e moeda do contrato | Dado contrato assinado até 31/12/2023, quando salvo com IGP-M, então o sistema aceita. | RN-007, RN-019 |
| US-003.3 | Validar índice e moeda do contrato | Dado contrato em USD, quando salvo, então exige câmbio de referência e não aceita índice de reajuste. | RN-007, RN-019 |
| US-004.1 | Calcular status da vigência | Dado contrato com fim futuro, quando consultado, então aparece vigente. | RF-001 |
| US-004.2 | Calcular status da vigência | Dado CT-2022-0055 com fim em 31/08/2025, quando consultado depois disso, então aparece vigência encerrada, mesmo com renovação em andamento. | RF-001 |
| US-004.3 | Calcular status da vigência | Dado contrato no último dia da vigência, quando consultado, então ainda aparece vigente. | RF-001 |
| US-005.1 | Impedir pagamento de contrato não registrado | Dado contrato registrado, quando a medição é liberada, então o sistema aceita. | RN-021 |
| US-005.2 | Impedir pagamento de contrato não registrado | Dada cobrança sem contrato registrado, quando enviada a pagamento, então o sistema recusa. | RN-021 |
| US-005.3 | Impedir pagamento de contrato não registrado | Dado contrato registrado depois do primeiro pedido, quando o pedido é reenviado, então o sistema aceita. | RN-021 |
| US-006.1 | Bloquear medição de contrato vencido, com exceção | Dada medição com competência dentro da vigência, quando liberada, então o sistema aceita. | RN-008 |
| US-006.2 | Bloquear medição de contrato vencido, com exceção | Dada medição após o fim da vigência sem exceção, quando liberada, então o sistema recusa. | RN-008 |
| US-006.3 | Bloquear medição de contrato vencido, com exceção | Dada exceção aprovada com justificativa, quando liberada, então o sistema aceita e registra na trilha. | RN-008 |
| US-007.1 | Receber alerta de renovação | Dado CT-2025-0064 com fim em 31/01/2027, quando chega 03/10/2026 (120 dias), então os responsáveis recebem o alerta. | RF-008, RN-006 |
| US-007.2 | Receber alerta de renovação | Dado contrato com 121 dias para o fim, quando processada a rotina, então não há alerta. | RF-008, RN-006 |
| US-007.3 | Receber alerta de renovação | Dado alerta sem renovação aberta depois de 30 dias, quando processada a rotina, então o aviso é repetido. | RF-008, RN-006 |
| US-008.1 | Acompanhar a renovação | Dada renovação aberta, quando há minuta em discussão, então aparece a etapa e o responsável. | RF-015 |
| US-008.2 | Acompanhar a renovação | Dada renovação concluída, quando assinada, então a vigência é atualizada por aditivo ou novo contrato. | RF-015 |
| US-008.3 | Acompanhar a renovação | Dado contrato vencido, quando em renovação, então os dois estados aparecem juntos. | RF-015 |
| US-009.1 | Registrar aditivo com histórico | Dado aditivo que muda o fim, quando salvo, então a vigência muda e o valor anterior fica no histórico. | RF-018 |
| US-009.2 | Registrar aditivo com histórico | Dado aditivo salvo por outra área, quando concluído, então o Jurídico recebe aviso. | RF-018 |
| US-009.3 | Registrar aditivo com histórico | Dado aditivo sem documento de referência, quando salvo, então o sistema recusa. | RF-018 |
| US-010.1 | Importar renovações do legado | Dada renovação concluída no legado, quando importada, então o contrato mostra a nova vigência. | RF-014 |
| US-010.2 | Importar renovações do legado | Dado número inexistente, quando importado, então a linha é rejeitada com motivo. | RF-014 |
| US-010.3 | Importar renovações do legado | Dada a mesma renovação importada de novo, quando processada, então não há duplicidade. | RF-014 |
| US-011.1 | Exigir parecer acima de R$ 30.000,00 | Dado contrato de R$ 58.800,00 sem parecer, quando enviado à aprovação, então o sistema recusa. | RN-005, RN-028 |
| US-011.2 | Exigir parecer acima de R$ 30.000,00 | Dado contrato de R$ 30.000,00, quando enviado, então não exige parecer. | RN-005, RN-028 |
| US-011.3 | Exigir parecer acima de R$ 30.000,00 | Dado contrato de R$ 30.000,01, quando enviado, então exige parecer. | RN-005, RN-028 |
| US-012.1 | Ver fila de pareceres | Dado parecer em aberto, quando abro a fila, então vejo dias de espera e fim de vigência. | RF-003 |
| US-012.2 | Ver fila de pareceres | Dado parecer concluído, quando abro a fila, então ele sai da fila e entra na medição do ciclo. | RF-003 |
| US-013.1 | Registrar requisição com cotações | Dada compra de R$ 5.000,00 sem cotação, quando enviada, então o sistema aceita. | RF-017, RN-003 |
| US-013.2 | Registrar requisição com cotações | Dada compra de R$ 5.000,01 com uma cotação, quando enviada, então o sistema recusa; com duas, aceita. | RF-017, RN-003 |
| US-013.3 | Registrar requisição com cotações | Dada compra de R$ 15.000,01 com duas cotações, quando enviada, então o sistema recusa; com três, aceita. | RF-017, RN-003 |
| US-014.1 | Aprovar OC pela alçada | Dada OC de R$ 50.000,00, quando submetida, então vai ao Gerente de Suprimentos. | RF-016, RN-001 |
| US-014.2 | Aprovar OC pela alçada | Dada OC de R$ 72.500,00, quando o Gerente de Suprimentos tenta aprovar, então o sistema recusa e encaminha ao Diretor Financeiro. | RF-016, RN-001 |
| US-014.3 | Aprovar OC pela alçada | Dada OC de R$ 250.000,01, quando submetida, então vai à Diretora Geral. | RF-016, RN-001 |
| US-015.1 | Aprovar contrato pelo valor global | Dado contrato assinado desde 01/01/2025 de R$ 6.800,00/mês por 24 meses, quando submetido, então a base é R$ 163.200,00 e vai ao Diretor Financeiro. | RF-016, RN-002, RN-020 |
| US-015.2 | Aprovar contrato pelo valor global | Dado contrato de R$ 22.000,00/mês por 24 meses, quando submetido, então vai à Diretora Geral. | RF-016, RN-002, RN-020 |
| US-015.3 | Aprovar contrato pelo valor global | Dado contrato em USD, quando submetido, então a base usa o câmbio de referência e aditivos somam ao global. | RF-016, RN-002, RN-020 |
| US-016.1 | Impedir autoaprovação | Dada OC solicitada por X, quando X tenta aprovar, então o sistema recusa. | RN-014 |
| US-016.2 | Impedir autoaprovação | Dada OC solicitada por X, quando Y com alçada aprova, então o sistema aceita. | RN-014 |
| US-016.3 | Impedir autoaprovação | Dado único aprovador na faixa sendo o solicitante, quando submetida, então a OC sobe ao nível seguinte. | RN-014 |
| US-017.1 | Somar ordens da mesma requisição | Dadas três OCs de uma requisição somando R$ 149.300,00, quando a terceira é aprovada, então a alçada é a do Diretor Financeiro. | RN-016 |
| US-017.2 | Somar ordens da mesma requisição | Dada OC única de R$ 49.800,00, quando submetida, então a alçada é do Gerente de Suprimentos. | RN-016 |
| US-017.3 | Somar ordens da mesma requisição | Dada a soma exatamente em R$ 50.000,00, quando submetida, então a alçada não muda. | RN-016 |
| US-018.1 | Alertar compras recorrentes sem contrato | Dadas três OCs mensais do mesmo fornecedor e unidade sem contrato, quando emitida a terceira, então recebo alerta. | RN-025 |
| US-018.2 | Alertar compras recorrentes sem contrato | Dadas OCs vinculadas a contrato, quando emitidas, então não há alerta. | RN-025 |
| US-019.1 | Registrar trilha das aprovações | Dada aprovação concluída, quando consultada, então mostra usuário, data, valor anterior e valor novo. | RNF-002 |
| US-019.2 | Registrar trilha das aprovações | Dada recusa, quando consultada, então mostra usuário, data e motivo. | RNF-002 |
| US-019.3 | Registrar trilha das aprovações | Dado registro de trilha, quando há tentativa de alteração, então o sistema recusa. | RNF-002 |
| US-020.1 | Manter limites como parâmetros com vigência | Dado limite com vigência futura, quando chega a data, então passa a valer. | RNF-006 |
| US-020.2 | Manter limites como parâmetros com vigência | Dada compra anterior à vigência, quando consultada, então mantém o limite da época. | RNF-006 |
| US-021.1 | Registrar compra emergencial | Dada emergencial de R$ 92.000,00 com uma proposta, quando emitida, então o sistema aceita. | RF-020, RN-018 |
| US-021.2 | Registrar compra emergencial | Dada emergencial de R$ 100.000,01, quando emitida, então o sistema recusa como emergencial. | RF-020, RN-018 |
| US-021.3 | Registrar compra emergencial | Dada emergencial emitida, quando decorrerem 72 horas sem aprovação do Diretor Técnico, então o sistema alerta; emergenciais do período aparecem na lista do Comitê. | RF-020, RN-018 |
| US-022.1 | Conectar aos sistemas mantidos com monitoramento | Dada carga normal, quando concluída, então o registro de execução mostra lidos, aceitos e rejeitados. | RF-011, RNF-003, RNF-011 |
| US-022.2 | Conectar aos sistemas mantidos com monitoramento | Dada falha de integração, quando detectada, então o alerta sai em até 15 min. | RF-011, RNF-003, RNF-011 |
| US-022.3 | Conectar aos sistemas mantidos com monitoramento | Dado reprocessamento, quando executado, então não duplica registros. | RF-011, RNF-003, RNF-011 |
| US-023.1 | Receber inventário e calibração | Dado patrimônio no ManutClin, quando sincronizado, então aparece com os dados atuais. | RF-007 |
| US-023.2 | Receber inventário e calibração | Dado patrimônio sem contrato, quando consultado, então aparece sem cobertura contratual. | RF-007 |
| US-023.3 | Receber inventário e calibração | Dada alteração de validade, quando sincronizada em até 24 horas, então o valor é atualizado. | RF-007 |
| US-024.1 | Criar requisição a partir da OS | Dada OS em AGUARDANDO_COMPRA, quando gero a requisição, então ela recebe OS, patrimônio e unidade. | RF-004 |
| US-024.2 | Criar requisição a partir da OS | Dada OS já com requisição, quando tento gerar outra, então o sistema alerta. | RF-004 |
| US-024.3 | Criar requisição a partir da OS | Dada OS fechada, quando tento gerar, então o sistema recusa. | RF-004 |
| US-025.1 | Conferir medição contra OS | Dada medição de um contrato, quando aberta, então aparecem as OS da competência. | RF-005 |
| US-025.2 | Conferir medição contra OS | Dada OS sem contrato ligado, quando conferida, então aparece como divergência. | RF-005 |
| US-025.3 | Conferir medição contra OS | Dada OS de 31/08 fechada em 01/09, quando conferida, então entra pela regra de competência definida. | RF-005 |
| US-026.1 | Atestar medição no sistema | Dada medição conferida, quando atestada, então registra usuário e data e libera o pagamento. | RF-005, RN-013 |
| US-026.2 | Atestar medição no sistema | Dada medição sem ateste, quando enviada a pagamento, então o sistema recusa. | RF-005, RN-013 |
| US-026.3 | Atestar medição no sistema | Dada medição atestada e depois alterada, quando salva, então o ateste é invalidado. | RF-005, RN-013 |
| US-027.1 | Listar OS corretivas sem teste ou liberação | Dada OS 88213, fechada sem teste e liberação, quando recebida, então entra na lista. | RN-012 |
| US-027.2 | Listar OS corretivas sem teste ou liberação | Dada OS corretiva com teste APROVADO e liberação, quando recebida, então não entra. | RN-012 |
| US-027.3 | Listar OS corretivas sem teste ou liberação | Dada OS com teste REPROVADO, quando recebida, então entra na lista. | RN-012 |
| US-028.1 | Alertar calibração vencida | Dado PAT-004512 EM_USO com validade em 31/03/2026, quando processada a carga, então há alerta. | RN-015 |
| US-028.2 | Alertar calibração vencida | Dado equipamento com validade hoje, quando processada, então não há alerta de vencido. | RN-015 |
| US-028.3 | Alertar calibração vencida | Dado equipamento sem validade, quando processado, então aparece como sem informação, não como conforme. | RN-015 |
| US-029.1 | Classificar equipamentos em quatro níveis | Dado equipamento A, quando carregado, então recebe nível 1. | RN-010, RN-023, RN-022 |
| US-029.2 | Classificar equipamentos em quatro níveis | Dado equipamento C, quando carregado, então recebe nível 4. | RN-010, RN-023, RN-022 |
| US-029.3 | Classificar equipamentos em quatro níveis | Dado equipamento B, quando carregado, então fica pendente até eu escolher nível 2 ou 3. | RN-010, RN-023, RN-022 |
| US-029.4 | Classificar equipamentos em quatro níveis | Dado contrato com itens de vários níveis, quando consultado, então mostra o maior nível (premissa de RN-022). | RN-010, RN-023, RN-022 |
| US-030.1 | Conciliar preventiva do contrato e do plano | Dado contrato Semestral e plano de 365 dias, quando conciliados, então a diferença é sinalizada. | RF-013 |
| US-030.2 | Conciliar preventiva do contrato e do plano | Dado contrato Trimestral e plano de 90 dias, quando conciliados, então não há diferença. | RF-013 |
| US-031.1 | Apurar tempos de SLA por OS | Dada OS 88170, com 14,2 horas até o atendimento em contrato de 4 horas, quando apurada, então é evento fora do SLA. | RN-009 |
| US-031.2 | Apurar tempos de SLA por OS | Dada OS 88213, com 3,4 horas em contrato de 4 horas, quando apurada, então está dentro. | RN-009 |
| US-031.3 | Apurar tempos de SLA por OS | Dado atendimento exatamente no limite do SLA, quando apurado, então está dentro. | RN-009 |
| US-032.1 | Calcular glosa por evento | Dado um evento em contrato de R$ 11.040,00/mês, quando calculado, então a glosa é R$ 220,80. | RN-017 |
| US-032.2 | Calcular glosa por evento | Dados dois eventos no mês, quando calculado, então a glosa é R$ 441,60. | RN-017 |
| US-032.3 | Calcular glosa por evento | Dado mês sem evento, quando calculado, então a glosa é R$ 0,00. | RN-017 |
| US-032.4 | Calcular glosa por evento | Dados 5 eventos em contrato de R$ 11.040,00/mês, quando calculada a competência, então a glosa é R$ 1.104,00. | RN-017 |
| US-032.5 | Calcular glosa por evento | Dados 6 eventos no mesmo contrato e competência, quando calculada, então a glosa continua R$ 1.104,00. | RN-017 |
| US-033.1 | Aceitar ou justificar glosa no ateste e pausar relógio | Dada glosa proposta, quando aceita, então desconta da medição. | RN-026 |
| US-033.2 | Aceitar ou justificar glosa no ateste e pausar relógio | Dada glosa recusada, quando salva, então exige justificativa. | RN-026 |
| US-033.3 | Aceitar ou justificar glosa no ateste e pausar relógio | Dada OS em espera de item não coberto, quando apurada a solução, então o período é excluído. | RN-026 |
| US-034.1 | Gerar título com vencimento correto | Dada nota de 01/03/2027 em OC regular, quando gerado o título, então o vencimento é 45 dias depois. | RF-006, RN-004 |
| US-034.2 | Gerar título com vencimento correto | Dada OC regular com prazo de 29 dias, quando salva, então o sistema recusa; com 30, aceita. | RF-006, RN-004 |
| US-034.3 | Gerar título com vencimento correto | Dada OC emergencial com 15 dias, quando salva, então o sistema aceita. | RF-006, RN-004 |
| US-035.1 | Ver visão consolidada da rede | Dado filtro por unidade, quando aplicado, então os valores somam só a unidade. | RF-009 |
| US-035.2 | Ver visão consolidada da rede | Dado contrato em USD, quando consolidado, então usa o câmbio de referência e mostra a moeda original. | RF-009 |
| US-035.3 | Ver visão consolidada da rede | Dado fornecedor com dois nomes e um CNPJ, quando consolidado, então aparece uma só linha. | RF-009 |
| US-035.4 | Ver visão consolidada da rede | Dado o Hospital Aurora Serra cadastrado, quando aberta a visão da rede, então ele aparece como unidade própria. | RF-009 |
| US-036.1 | Acompanhar indicadores do processo | Dado mês encerrado, quando aberto o relatório, então mostra ciclo de contratação, espera de compra, títulos alterados e glosas. | RF-019 |
| US-036.2 | Acompanhar indicadores do processo | Dado indicador sem dado, quando aberto, então aparece como sem informação, não como zero. | RF-019 |
| US-037.1 | Consultar custo por equipamento | Dado equipamento com contrato e peça, quando consultado, então mostra os três componentes. | RF-010, RN-027 |
| US-037.2 | Consultar custo por equipamento | Dado contrato de R$ 1.000,00 com 2 equipamentos, quando rateado, então cada um recebe R$ 500,00 (premissa de RN-027). | RF-010, RN-027 |
| US-038.1 | Excluir dados de paciente da integração | Dada OS com nome de paciente, quando integrada, então o dado não é armazenado. | RNF-001 |
| US-038.2 | Excluir dados de paciente da integração | Dada migração histórica, quando concluída, então uma busca nos campos importados não acha nome ou prontuário. | RNF-001 |
| US-038.3 | Excluir dados de paciente da integração | Dada OS com evento adverso, quando integrada, então chega só o indicador, sem paciente (premissa de Q-017). | RNF-001 |
| US-039.1 | Registrar trilha de contrato, medição e título | Dada alteração de contrato, quando salva, então registra usuário, data, valores anteriores e novos. | RNF-007 |
| US-039.2 | Registrar trilha de contrato, medição e título | Dada alteração de vencimento, quando salva, então exige motivo e registra. | RNF-007 |
| US-039.3 | Registrar trilha de contrato, medição e título | Dado registro de trilha, quando há tentativa de alteração, então o sistema recusa. | RNF-007 |
| US-040.1 | Sanear e migrar contratos | Dados os oito contratos, quando migrados, então cada um tem vigência, valor e SLA conferidos com o documento assinado. | RF-002 |
| US-040.2 | Sanear e migrar contratos | Dado CT-2026-0021, ausente no ERP, quando migrado, então entra com origem na planilha e pendência de regularização. | RF-002 |
| US-040.3 | Sanear e migrar contratos | Dado fornecedor com mesmo CNPJ e dois nomes, quando migrado, então resulta em um só cadastro. | RF-002 |
| US-040.4 | Sanear e migrar contratos | Dados os dois contratos do Hospital Aurora Serra, quando recebidos, então entram na mesma conferência e carga. | RF-002 |
| US-041.1 | Conduzir convivência e treinamento | Dada área em entrada em operação, quando inicia o uso, então seus usuários concluíram o treinamento. | RF-012 |
| US-041.2 | Conduzir convivência e treinamento | Dada a entrada em operação, quando concluída, então a planilha fica somente leitura. | RF-012 |
| US-041.3 | Conduzir convivência e treinamento | Dado contrato renovado na convivência, quando importado, então aparece nos dois controles até o desligamento. | RF-012 |
| US-042.1 | Garantir capacidade, disponibilidade e recuperação | Dada carga de 4.812 equipamentos, 640 OS/mês e 1.460 OCs/ano, quando processada, então não há perda de registros. | RNF-005, RNF-008, RNF-009, RNF-010 |
| US-042.2 | Garantir capacidade, disponibilidade e recuperação | Dada medição mensal, quando calculada, então a disponibilidade é de pelo menos 99,5% e consultas abrem em até 3 s em 95% dos casos (valores propostos). | RNF-005, RNF-008, RNF-009, RNF-010 |
| US-042.3 | Garantir capacidade, disponibilidade e recuperação | Dado teste de restauração, quando executado, então conclui em até 8 horas (valor proposto). | RNF-005, RNF-008, RNF-009, RNF-010 |
| US-043.1 | Incorporar o Hospital Aurora Serra e seus contratos | Dada a unidade cadastrada, quando aberto o cadastro de contrato, então ela pode ser selecionada, com de-para próprio. | RF-021 |
| US-043.2 | Incorporar o Hospital Aurora Serra e seus contratos | Dado contrato da unidade sem vigência, valor ou SLA, quando carregado, então a linha é rejeitada com motivo. | RF-021 |
| US-043.3 | Incorporar o Hospital Aurora Serra e seus contratos | Dados os dois contratos carregados, quando aberta a visão da rede, então aparecem filtrados pela unidade. | RF-021 |
| RN-001.1 | Alçada de OC pela política | Dada OC de R$ 50.000,00, quando o Gerente de Suprimentos aprova, então o sistema aceita. | RN-001 |
| RN-001.2 | Alçada de OC pela política | Dada OC de R$ 50.000,01, quando o Gerente de Suprimentos tenta aprovar, então o sistema recusa e encaminha ao Diretor Financeiro. | RN-001 |
| RN-001.3 | Alçada de OC pela política | Dada OC de R$ 250.000,01, quando o Diretor Financeiro tenta aprovar, então o sistema recusa e encaminha à Diretora Geral. | RN-001 |
| RN-002.1 | Alçada de contrato pelo valor global | Dado contrato de R$ 22.000,00/mês por 24 meses, quando enviado à aprovação, então a alçada usa R$ 528.000,00 e vai à Diretora Geral. | RN-002 |
| RN-003.1 | Cotações pela política | Dada compra regular de R$ 19.800,00 com uma cotação, quando enviada à aprovação, então o sistema recusa. | RN-003 |
| RN-004.1 | Prazo de pagamento | Dada OC regular com 28 dias, quando salva, então o sistema recusa. | RN-004 |
| RN-005.1 | Parecer jurídico por valor | Dado contrato de R$ 58.800,00 sem parecer, quando enviado à aprovação, então o sistema recusa. | RN-005 |
| RN-005.2 | Parecer jurídico por valor | Dado contrato de exatamente R$ 30.000,00, quando enviado à aprovação, então o parecer não é exigido. | RN-005 |
| RN-006.1 | Início da renovação | Dado contrato com fim em 31/01/2027, quando chega 03/10/2026, então a renovação é aberta para os responsáveis. | RN-006 |
| RN-007.1 | Índice de reajuste | Dado contrato em BRL assinado em 2025, quando cadastrado com IGP-M, então o sistema recusa. | RN-007 |
| RN-008.1 | Pagamento depende de contrato vigente e registrado | Dada medição de contrato com fim anterior à competência, quando liberada sem exceção, então o sistema recusa. | RN-008 |
| RN-009.1 | Fonte única do SLA | Dado CT-2024-0117 migrado, quando consultado, então o SLA de atendimento é 4 horas, não 8. | RN-009 |
| RN-010.1 | Criticidade única | Dado equipamento sem classificação, quando incluído em contrato, então o sistema exige o nível. | RN-010 |
| RN-011.1 | Preventiva de ventiladores da Central | Dado CT-2023-0019 migrado, quando consultada a preventiva, então consta Semestral. | RN-011 |
| RN-012.1 | Retorno ao uso depende de teste e liberação | Dada OS corretiva fechada sem liberação, quando recebida, então entra na lista de irregularidades da Engenharia Clínica. | RN-012 |
| RN-012.2 | Retorno ao uso depende de teste e liberação | Dada OS corretiva com teste aprovado e liberação, quando recebida, então não entra na lista. | RN-012 |
| RN-013.1 | Pagamento depende de ateste | Dada medição sem ateste, quando enviada a pagamento, então o sistema recusa. | RN-013 |
| RN-014.1 | Segregação de funções | Dada OC solicitada pelo usuário X, quando X tenta aprovar, então o sistema recusa. | RN-014 |
| RN-015.1 | Calibração vencida | Dado equipamento EM_USO com validade passada, quando processada a carga, então um alerta é gerado. | RN-015 |
| RN-016.1 | Detecção de fracionamento | Dadas três OCs da mesma requisição somando R$ 149.300,00, quando aprovadas, então a alçada usa o total. | RN-016 |
| RN-017.1 | Glosa por descumprimento de SLA | Dado evento acima do SLA em contrato de R$ 11.040,00/mês, quando aberta a medição, então a proposta é de R$ 220,80. | RN-017 |
| RN-017.2 | Glosa por descumprimento de SLA | Dados 5 eventos em contrato de R$ 11.040,00/mês, quando calculada a competência, então a glosa é R$ 1.104,00. | RN-017 |
| RN-017.3 | Glosa por descumprimento de SLA | Dados 6 eventos no mesmo contrato e competência, quando calculada, então a glosa continua R$ 1.104,00. | RN-017 |
| RN-018.1 | Compra emergencial | Dada emergencial de R$ 120.000,00, quando registrada, então o sistema recusa como emergencial. | RN-018 |
| RN-019.1 | Moeda estrangeira | Dado contrato em USD, quando consolidado, então usa o câmbio de referência e exibe a moeda original. | RN-019 |
| RF-001.1 | Cadastro único de contratos | Dado aditivo registrado, quando consultado o contrato, então todas as áreas veem a nova vigência e o histórico. | RF-001 |
| RF-002.1 | Migração e de-para de chaves | Dado fornecedor com nomes diferentes e mesmo CNPJ, quando migrado, então resulta em um único cadastro. | RF-002 |
| RF-003.1 | Fila de parecer | Dado contrato em parecer, quando aberta a fila, então aparecem dias de espera e fim de vigência. | RF-003 |
| RF-004.1 | Requisição a partir de OS | Dada OS em AGUARDANDO_COMPRA, quando importada, então a requisição recebe OS, patrimônio e unidade. | RF-004 |
| RF-005.1 | Conferência assistida de medição | Dada medição mensal, quando aberta, então aparecem as OS do contrato e os eventos fora do SLA. | RF-005 |
| RF-006.1 | Título com vencimento correto | Dada nota de OC regular, quando gerado o título, então o vencimento é emissão + 45 dias. | RF-006 |
| RF-007.1 | Consulta de inventário e calibração | Dada alteração de validade no ManutClin, quando sincronizada, então o novo valor aparece no equipamento. | RF-007 |
| RF-008.1 | Alertas de renovação | Dado contrato que atinge a data de alerta, quando processada a rotina, então os responsáveis recebem o aviso. | RF-008 |
| RF-009.1 | Visão consolidada | Dado filtro por unidade, quando aplicado, então os valores somam os contratos da unidade com moeda normalizada. | RF-009 |
| RF-010.1 | Custo por equipamento | Dado equipamento com contrato e peça comprada, quando consultado, então aparecem os três componentes. | RF-010 |
| RF-011.1 | Integração com sistemas mantidos | Dada falha de integração, quando detectada, então um alerta é gerado e o reprocessamento não duplica registros. | RF-011 |
| RF-012.1 | Convivência e treinamento | Dada a entrada em operação, quando a área inicia o uso, então os usuários foram treinados e a planilha fica somente leitura. | RF-012 |
| RNF-001.1 | Dados de paciente fora do sistema | Dada OS com nome de paciente, quando integrada, então o dado não é armazenado nem exibido. | RNF-001 |
| RNF-002.1 | Trilha de auditoria | Dada aprovação de OC, quando concluída, então a trilha mostra os quatro dados. | RNF-002 |
| RNF-003.1 | Atualização da integração | Dada OS alterada, quando decorrido o prazo definido, então o novo status aparece. | RNF-003 |
| RNF-004.1 | Permissões por papel | Dado usuário de outra área, quando tenta aprovar sem papel, então é recusado. | RNF-004 |
| RNF-005.1 | Capacidade inicial | Dada carga com esses volumes, quando processada, então todos os registros são aceitos ou rejeitados com motivo. | RNF-005 |
| RNF-006.1 | Parâmetros versionados | Dada nova revisão da política, quando cadastrada, então o novo limite vale a partir da data de vigência. | RNF-006 |
| RN-020.1 | Valor global com aditivo e moeda | Dado contrato de 9.800 USD/mês por 36 meses com câmbio 5,40, quando enviado à aprovação, então a base é R$ 1.905.120,00. | RN-020 |
| RN-021.1 | Registro antes do primeiro pagamento | Dada medição sem contrato registrado, quando enviada a pagamento, então o sistema recusa. | RN-021 |
| RN-022.1 | Criticidade do contrato | Dado contrato com itens de nível 1 e 3, quando consultado, então a criticidade é nível 1. | RN-022 |
| RN-023.1 | Conversão de A, B, C | Dado equipamento B na carga, quando importado, então fica com classificação pendente entre 2 e 3. | RN-023 |
| RN-023.2 | Conversão de A, B, C | Dado equipamento A, quando importado, então recebe nível 1. | RN-023 |
| RN-024.1 | Bloqueio operacional | Dada OS sem liberação, quando há tentativa de fechar, então o ManutClin recusa. | RN-024 |
| RN-025.1 | Alerta de recorrência | Dadas três OCs mensais de R$ 4.900,00 ao mesmo fornecedor sem contrato, quando emitida a terceira, então Suprimentos recebe alerta. | RN-025 |
| RN-026.1 | Relógio do SLA e aceite da glosa | Dada OS em AGUARDANDO_COMPRA, quando apurado o SLA de solução, então o período é excluído. | RN-026 |
| RN-026.2 | Relógio do SLA e aceite da glosa | Dada glosa proposta, quando recusada, então exige justificativa. | RN-026 |
| RN-027.1 | Rateio do contrato | Dado contrato de R$ 1.000,00 com 2 equipamentos, quando calculado, então cada um recebe R$ 500,00. | RN-027 |
| RF-013.1 | Conciliação contrato x plano preventivo | Dado contrato semestral e plano de 365 dias, quando conciliados, então o sistema sinaliza a diferença. | RF-013 |
| RF-014.1 | Importação de renovações do legado | Dada renovação concluída no legado, quando importada, então o contrato mostra a vigência nova. | RF-014 |
| RF-015.1 | Fluxo de renovação | Dada renovação aberta, quando a minuta é enviada, então o status indica a etapa e o responsável. | RF-015 |
| RF-016.1 | Fluxo de aprovação | Dada OC submetida, quando calculada a alçada, então a pendência aparece só para o aprovador correto. | RF-016 |
| RF-017.1 | Requisição e cotações | Dada requisição de peça, quando registrada, então guarda o patrimônio do equipamento. | RF-017 |
| RF-018.1 | Aditivos com histórico | Dado aditivo salvo, quando concluído, então o Jurídico é avisado e o histórico mantém os valores anteriores. | RF-018 |
| RF-019.1 | Linha de base de indicadores | Dado mês encerrado, quando aberto o relatório, então mostra os indicadores com a linha de base de 2025. | RF-019 |
| RF-020.1 | Registro de compra emergencial | Dada emergencial emitida, quando decorrerem 72 horas sem aprovação, então Suprimentos e o Diretor Técnico são alertados. | RF-020 |
| RNF-007.1 | Auditoria de demais objetos | Dada alteração de vencimento, quando concluída, então a trilha mostra usuário, data e valores. | RNF-007 |
| RNF-008.1 | Disponibilidade | Dado um mês de operação, quando medida a disponibilidade, então é de pelo menos 99,5%. | RNF-008 |
| RNF-009.1 | Tempo de resposta | Dada a carga de RNF-005, quando medido, então o 95º percentil fica em até 3 s. | RNF-009 |
| RNF-010.1 | Recuperação | Dado teste de restauração, quando executado, então conclui em até 8 horas. | RNF-010 |
| RNF-011.1 | Monitoramento de integração | Dada falha na carga, quando detectada, então o alerta sai em até 15 min. | RNF-011 |
| RN-028.1 | Parecer jurídico acima de R$ 200 mil (memorando) | Dado contrato de R$ 163.200,00 sem parecer, quando enviado à aprovação, então o sistema aceita. | RN-028 |
| RN-028.2 | Parecer jurídico acima de R$ 200 mil (memorando) | Dado contrato de R$ 200.000,01 sem parecer, quando enviado à aprovação, então o sistema recusa. | RN-028 |
| RF-021.1 | Incorporação do Hospital Aurora Serra | Dada a incorporação, quando cadastrada a unidade, então os dois contratos aparecem na visão consolidada da rede. | RF-021 |
