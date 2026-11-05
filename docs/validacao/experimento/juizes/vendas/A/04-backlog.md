# Backlog ágil — Sistema de Vendas Unificado

Prioridade conforme a resposta 10, atualizada pelas comunicações avaliadas em `08-mudancas.md`. "Situação" indica se a história pode começar ou o que a bloqueia (IDs PA em `02-negocio.md`). Sem estimativas: pontuar é tarefa da equipe, depois da prova técnica. Critérios que usam uma premissa (PR) devem ser revistos quando ela for confirmada.

**Importação:** `05-jira.csv` e `06-azure-devops.csv` trazem as mesmas histórias e critérios.

- **Jira:** não tem nível nativo de feature, então a feature vai em rótulo (`F1-1`) e na descrição. As prioridades são High (Must) e Medium (Should). Mapeie `Epic Name` e `Epic Link` em projetos company-managed ou `Parent` em team-managed. Selecione UTF-8 no assistente.
- **Azure DevOps:** usa hierarquia Epic, Feature e User Story do processo Agile, com `Title 1`, `Title 2` e `Title 3`. Prioridade 1 é Must e 2 é Should. No processo Scrum, troque `User Story` por `Product Backlog Item`.

## E1 — Integração com o VendaMax
**Prioridade:** Must
**Objetivo:** Substituir o CSV por integração por API, mantendo a NF-e no VendaMax.

### F1.1 — Viabilidade da integração
**Objetivo:** Confirmar se a integração é possível antes de comprometer prazo.

#### US-001 — Comprovar a API do VendaMax
- **Prioridade:** Must
- **História:** Como Gerente de TI, quero uma prova técnica da API do VendaMax, para decidir a arquitetura com base em evidência.
- **Requisitos:** RF-16, RF-17, RNF-03
- **Situação:** Em andamento: criar pedido e consultar faturamento confirmados por e-mail (M-02); restante em PA-01
- **Critérios de aceite:**
  - Há matriz indicando, para pedido, faturamento, NF-e, impostos, frete, estoque, clientes, preço e devoluções, se a API cobre, com evidência de teste.
  - O limite de 60 requisições por minuto está detalhado: abrangência, cotas, resposta ao exceder, possibilidade de ampliação e consulta em lote ou por período.
  - A completude do dump e o motivo de cartão ou Pix não passarem pelo crédito na importação estão esclarecidos.
  - Prazo e custo do fornecedor para cobrir as lacunas estão registrados.
  - Se não houver API suficiente, a decisão é levada à TI e à diretoria, sem adotar CSV ou acesso direto ao banco por conta própria.

#### US-002 — Definir o tratamento dos triggers do ERP
- **Prioridade:** Must
- **História:** Como Gerente de TI, quero que o ERP não refaça decisões do novo sistema, para que pedidos aprovados cheguem à NF-e.
- **Requisitos:** RF-10, RF-16, RF-19, RF-20
- **Situação:** Bloqueada por PA-02
- **Critérios de aceite:**
  - Em homologação, pedido com desconto aprovado acima de 10% é aceito com o percentual real.
  - Em homologação, pedido liberado pelo novo sistema não retorna para `aguardando_credito`.
  - A mudança é aceita pelo fornecedor e não afeta a emissão de NF-e.
  - O valor de comissão gravado pelo ERP permanece fora de qualquer cálculo de pagamento.

### F1.2 — Pedidos e faturamento
**Objetivo:** Levar pedidos ao ERP e trazer o resultado de volta.

#### US-003 — Enviar pedido liberado ao VendaMax
- **Prioridade:** Must
- **História:** Como setor de Faturamento, quero receber no VendaMax os pedidos liberados de todos os canais, para emitir a NF-e.
- **Requisitos:** RF-16, RF-28, RNF-03, RNF-10, RNF-12
- **Situação:** Depende de US-001 e US-002; criar pedido confirmado (M-02)
- **Critérios de aceite:**
  - O pedido liberado é enviado com cliente, itens, preço, desconto real, vendedor e origem.
  - Reenvios do mesmo pedido não geram duplicidade.
  - O pedido não é enviado antes de ser liberado.
  - O envio respeita 60 requisições por minuto: o excedente aguarda em fila, sem perda ou erro para o vendedor.

#### US-004 — Receber faturamento e NF-e
- **Prioridade:** Must
- **História:** Como vendedor, quero ver a situação de faturamento e a NF-e do pedido, para informar o cliente sem consultar o ERP.
- **Requisitos:** RF-09, RF-16, RNF-12, RNF-14
- **Situação:** Depende de US-003; consulta de faturamento confirmada (M-02); número da NF-e em PA-01
- **Critérios de aceite:**
  - O sistema consulta periodicamente os pedidos em aberto, pois a API não tem webhook, e para de consultar estados finais.
  - Pedido faturado no ERP passa a faturado no novo sistema, com o número da NF-e, se a API o fornecer.
  - O tempo entre faturamento e detecção é medido e exposto.
  - Cancelamento no ERP é refletido com a origem identificada.
  - Respostas repetidas ou fora de ordem não corrompem a situação do pedido.

#### US-005 — Tratar falhas de integração
- **Prioridade:** Must
- **História:** Como analista de TI, quero ver e reprocessar falhas de integração, para que nenhum pedido se perca em silêncio.
- **Requisitos:** RF-18, RNF-07, RNF-10, RNF-12
- **Situação:** Depende de US-001
- **Critérios de aceite:**
  - Toda rejeição aparece em fila com motivo e pode ser reprocessada.
  - Indisponibilidade ou rejeição gera alerta ao responsável definido.
  - Há conciliação diária entre pedidos liberados e pedidos recebidos no ERP.
  - O consumo do limite de requisições é monitorado, com alerta antes de saturar.
  - Logs não trazem dados pessoais.

### F1.3 — Dados mestres e encerramento do CSV
**Objetivo:** Manter o ERP alinhado com o novo sistema e encerrar os arquivos.

#### US-006 — Sincronizar clientes PJ com o ERP
- **Prioridade:** Must
- **História:** Como setor de Faturamento, quero os dados do cliente no ERP, para emitir a NF-e sem recadastro.
- **Requisitos:** RF-17, RNF-10
- **Situação:** Bloqueada por PA-01 e PA-12
- **Critérios de aceite:**
  - Cliente PJ novo ou alterado é refletido no ERP pela chave de documento, sem máscara.
  - Campos exigidos para a NF-e estão identificados e têm origem definida.
  - Falhas seguem o tratamento de US-005.

#### US-007 — Publicar a tabela de preços no ERP
- **Prioridade:** Must
- **História:** Como setor de Faturamento, quero os preços vigentes no ERP, para que a NF-e reflita o valor do pedido.
- **Requisitos:** RF-06, RF-17, RNF-12
- **Situação:** Bloqueada por PA-01
- **Critérios de aceite:**
  - Alteração de preço é publicada no ERP por SKU, dentro do limite de requisições, inclusive em reajuste amplo.
  - Falha de publicação gera alerta.
  - Em homologação, a NF-e reflete o preço do pedido, inclusive em pedido feito antes de um reajuste.

#### US-008 — Encerrar o CSV noturno
- **Prioridade:** Must
- **História:** Como Gerente de TI, quero encerrar os arquivos noturnos depois do corte, para eliminar a integração frágil.
- **Requisitos:** RF-27, RNF-03
- **Situação:** Bloqueada por PA-15
- **Critérios de aceite:**
  - Depois do corte de cada canal, seus arquivos deixam de ser gerados e importados.
  - Há procedimento de reversão aprovado durante a estabilização.
  - Arquivos residuais, inclusive `erros/`, têm destino definido com o jurídico.

## E2 — Cadastro único de clientes
**Prioridade:** Must
**Objetivo:** Ter um único cadastro de clientes PJ e PF para todos os canais.

### F2.1 — Cadastro e carteira
**Objetivo:** Representar cliente, acessos e responsável comercial.

#### US-009 — Cadastrar cliente PJ ou PF
- **Prioridade:** Must
- **História:** Como vendedor ou cliente da loja, quero um cadastro único por CPF ou CNPJ, para não haver duplicidade entre os canais.
- **Requisitos:** RF-01, RN-16
- **Situação:** Pronta
- **Critérios de aceite:**
  - O documento é validado e armazenado sem máscara, com indicação de tipo.
  - Um documento já cadastrado não gera segundo cliente.
  - O cadastro feito em um canal aparece nos demais.
  - O acesso a CPF é restrito conforme o perfil.

#### US-010 — Vincular usuários de acesso ao cliente
- **Prioridade:** Must
- **História:** Como cliente da loja, quero que mais de um comprador acesse a mesma empresa, para comprar sem criar outro cadastro.
- **Requisitos:** RF-02
- **Situação:** Pronta
- **Critérios de aceite:**
  - Um cliente pode ter vários usuários, com e-mail único por usuário.
  - O usuário vê apenas os dados e pedidos do cliente ao qual está vinculado.

#### US-011 — Manter responsável pela carteira
- **Prioridade:** Must
- **História:** Como Coordenadora Financeira, quero o histórico de carteira do cliente, para saber quem respondia por ele em cada data.
- **Requisitos:** RF-03, RNF-04
- **Situação:** Pronta; regra para cliente sem carteira em PA-09
- **Critérios de aceite:**
  - Toda alteração registra vendedor, vigência, autor e motivo.
  - É possível consultar o responsável em uma data.
  - Cliente sem responsável fica identificado em lista de exceções.

### F2.2 — Pessoa física no faturamento
**Objetivo:** Levar a venda a pessoa física até a NF-e sem recadastro manual.

#### US-012 — Faturar pedido de pessoa física
- **Prioridade:** Must
- **História:** Como cliente pessoa física, quero que meu pedido chegue à NF-e sem correção manual, para receber a compra sem atraso.
- **Requisitos:** RF-01, RF-17, RN-16
- **Situação:** Bloqueada por PA-02 e PA-03
- **Critérios de aceite:**
  - O caminho atual de cadastro e NF-e para CPF está documentado com Faturamento.
  - Em homologação, pedido com CPF é faturado sem recadastro manual.
  - Se a alteração no ERP não vier a tempo, a decisão sobre o canal PF é tomada formalmente antes do corte.

### F2.3 — Migração
**Objetivo:** Trazer as bases sem duplicidade.

#### US-013 — Avaliar a qualidade das bases
- **Prioridade:** Must
- **História:** Como PO, quero conhecer duplicidades e divergências das bases, para definir regras de união.
- **Requisitos:** RF-05
- **Situação:** Pronta
- **Critérios de aceite:**
  - Há contagem de duplicados, documentos inválidos, clientes sem carteira e clientes presentes em uma só base.
  - O relatório não traz dados pessoais identificáveis além do necessário à correção, e tem acesso restrito.
  - As regras de união são aprovadas pela PO e pela Coordenação Financeira.

#### US-014 — Migrar clientes
- **Prioridade:** Must
- **História:** Como PO, quero migrar os cerca de 4 mil clientes ativos com conciliação, para iniciar sem perda de dados.
- **Requisitos:** RF-05, RNF-02
- **Situação:** Bloqueada por PA-12
- **Critérios de aceite:**
  - A contagem de origem e destino é conciliada, com todas as rejeições explicadas.
  - Limite de crédito e carteira são preservados conforme as regras aprovadas.
  - A migração é ensaiada em homologação antes do corte.

### F2.4 — Consentimento
**Objetivo:** Usar dados em marketing somente com consentimento explícito.

#### US-015 — Registrar consentimento explícito
- **Prioridade:** Must
- **História:** Como cliente, quero decidir se aceito marketing, para controlar o uso dos meus dados.
- **Requisitos:** RF-04, RN-13, RNF-05
- **Situação:** Pronta; texto validado com jurídico (PA-16)
- **Critérios de aceite:**
  - A opção aparece desmarcada por padrão.
  - O sistema registra decisão, data, origem e versão do texto.
  - O cliente pode revogar, e a revogação vale para os próximos usos.

#### US-016 — Reconfirmar a base atual
- **Prioridade:** Must
- **História:** Como responsável por marketing, quero reconfirmar o consentimento da base, para só contatar quem aceitou de forma explícita.
- **Requisitos:** RF-04, RN-13, RNF-05
- **Situação:** Pronta; forma da campanha validada com jurídico (PA-16)
- **Critérios de aceite:**
  - Nenhum `aceita_marketing = 1` migrado conta como consentimento.
  - Clientes da loja têm um caminho de reconfirmação.
  - Quem não reconfirmar, ou existir apenas no ERP, fica sem consentimento para marketing (PR-11).

## E3 — Pedidos unificados
**Prioridade:** Must
**Objetivo:** Reunir pedidos de internos, representantes e loja com preço único.

### F3.1 — Captura de pedidos
**Objetivo:** Receber pedidos dos três canais por um único contrato.

#### US-017 — Decidir o destino da loja
- **Prioridade:** Must
- **História:** Como PO, quero decidir se a loja é adaptada ou substituída, para dimensionar a v1 e tratar o servidor antigo.
- **Requisitos:** RF-07, RF-29
- **Situação:** Bloqueada por PA-15
- **Critérios de aceite:**
  - A decisão registra opções, custo, riscos e o papel do desenvolvedor terceirizado.
  - O tratamento de credenciais e do servidor antigo está definido.
  - A decisão é aprovada por PO, Diretor Comercial e Gerente de TI.

#### US-018 — Digitar pedido na web responsiva
- **Prioridade:** Must
- **História:** Como vendedor interno ou representante, quero tirar pedido pela web em computador ou celular, para vender sem depender do VendaMax.
- **Requisitos:** RF-07, RF-08, RNF-08
- **Situação:** Pronta
- **Critérios de aceite:**
  - O fluxo completo funciona em computador, tablet e celular.
  - O vendedor seleciona apenas clientes permitidos por seu perfil.
  - O preço vem da tabela vigente e o sistema mostra a disponibilidade.
  - Sem conexão, a web informa que o pedido não foi enviado. A operação sem internet é coberta pelo épico E10.

#### US-019 — Receber pedidos da loja
- **Prioridade:** Must
- **História:** Como cliente da loja, quero que meu pedido entre diretamente no sistema de vendas, para não esperar o lote noturno.
- **Requisitos:** RF-07, RF-27
- **Situação:** Depende de US-017
- **Critérios de aceite:**
  - O pedido da loja usa o mesmo contrato dos outros canais e registra canal e forma de pagamento.
  - O pedido fica visível no sistema sem depender do lote noturno.
  - O cliente da loja vê a situação do próprio pedido.

### F3.2 — Preço
**Objetivo:** Aplicar a tabela única em todos os canais.

#### US-020 — Manter a tabela de preços única
- **Prioridade:** Must
- **História:** Como responsável pela tabela de preços, quero cadastrar preços no novo sistema, para que todos os canais usem o mesmo valor.
- **Requisitos:** RF-06, RN-04, RNF-02
- **Situação:** Pronta; responsável e exceções em PA-12
- **Critérios de aceite:**
  - Os 12 mil SKUs são carregados a partir da base atual, com conciliação.
  - Um SKU tem o mesmo preço vigente em todos os canais.
  - Alterações registram autor, vigência e valor anterior.
  - O pedido guarda o preço aplicado, sem efeito de reajuste posterior.

### F3.3 — Ciclo de vida e consulta
**Objetivo:** Dar uma situação clara a cada pedido.

#### US-021 — Controlar o ciclo de vida do pedido
- **Prioridade:** Must
- **História:** Como operador comercial, quero estados e histórico do pedido, para saber onde ele está e por quê.
- **Requisitos:** RF-09, RNF-04
- **Situação:** Pronta; revisão em PA-13
- **Critérios de aceite:**
  - O pedido segue apenas transições permitidas.
  - Cada mudança registra autor ou sistema, data e motivo.
  - Cancelamento é distinto de devolução no modelo.

#### US-022 — Consultar pedidos de todos os canais
- **Prioridade:** Must
- **História:** Como gestor comercial, quero consultar pedidos de todos os canais no mesmo lugar, para acompanhar a operação.
- **Requisitos:** RF-07, RF-09, RNF-05
- **Situação:** Pronta
- **Critérios de aceite:**
  - É possível filtrar por canal, situação, cliente, vendedor e período.
  - Vendedores e representantes veem apenas o permitido ao seu perfil.
  - A consulta responde adequadamente com o volume de referência, inclusive no pico.

### F3.4 — Crédito na entrada do pedido
**Objetivo:** Cumprir a política de crédito no fluxo unificado.

#### US-023 — Conduzir a análise manual de crédito
- **Prioridade:** Must
- **História:** Como analista de crédito, quero uma fila com prazo, para analisar pedidos acima do limite em até 1 dia útil.
- **Requisitos:** RF-19, RN-05, RNF-04
- **Situação:** Pronta; regras abertas em PA-08
- **Critérios de aceite:**
  - Pedido acima do limite vai para a fila com o prazo calculado e o motivo.
  - Pedido perto de vencer ou vencido gera alerta.
  - O analista libera ou cancela com justificativa, e o sistema registra autor e data.
  - Cliente bloqueado não confirma pedido (PR-05).
  - Tempo de fila pode ser medido por período.

#### US-024 — Dispensar análise em cartão e Pix
- **Prioridade:** Must
- **História:** Como cliente que paga por cartão ou Pix, quero seguir sem análise de crédito, para receber o pedido mais rápido.
- **Requisitos:** RF-20, RN-07
- **Situação:** Pronta; integração de pagamento e PR-09 em PA-08
- **Critérios de aceite:**
  - Pedido em cartão ou Pix, com pagamento aprovado, é liberado sem passar pela fila.
  - Falha ou expiração de pagamento não libera o pedido e encerra a reserva.
  - O pedido não volta à fila de crédito depois de chegar ao ERP.

## E4 — Alçadas de desconto
**Prioridade:** Must
**Objetivo:** Aplicar a política de desconto igualmente em todos os canais, com aprovação registrada.

### F4.1 — Faixas e aprovação
**Objetivo:** Encerrar a recusa indevida de desconto.

#### US-025 — Aplicar as faixas de desconto
- **Prioridade:** Must
- **História:** Como vendedor, quero que o sistema aplique a alçada correta, para dar desconto permitido sem recusa indevida.
- **Requisitos:** RF-10, RN-01, RN-02
- **Situação:** Pronta; vigência do novo limite em PA-21; desconto por pedido é PR-01 (PA-05)
- **Critérios de aceite:**
  - Desconto de 15,00% não exige aprovação.
  - Descontos de 15,01% a 20,00% exigem gerente comercial.
  - Desconto de 20,01% exige diretoria.
  - O comportamento é igual em todos os canais.
  - O limite de 10% não é aplicado no novo sistema.
  - Os limites são parâmetros com vigência, e a troca não afeta pedidos já aprovados.

#### US-026 — Aprovar ou recusar desconto
- **Prioridade:** Must
- **História:** Como gerente comercial ou diretor, quero decidir solicitações pelo sistema, para responder rapidamente e deixar registro.
- **Requisitos:** RF-11, RN-01, RNF-04
- **Situação:** Pronta; prazo em PA-05
- **Critérios de aceite:**
  - O aprovador recebe solicitação com cliente, valor, percentual e vendedor.
  - O vendedor é avisado da decisão.
  - Autor, data, decisão e justificativa ficam registrados.
  - Sem resposta após 1 dia útil há alerta, e o pedido não é aprovado automaticamente (PR-02).

#### US-027 — Configurar aprovador substituto
- **Prioridade:** Must
- **História:** Como Diretor Comercial, quero definir o substituto da gerente nas ausências, para que aprovações não parem nas férias.
- **Requisitos:** RF-11, RNF-04
- **Situação:** Funcionalidade pronta; valor bloqueado por PA-04
- **Critérios de aceite:**
  - É possível indicar substituto com período de vigência.
  - No período, as solicitações vão ao substituto, e isso fica registrado.
  - Sem substituto definido, o pedido fica pendente com alerta, e o sistema não escolhe aprovador sozinho.
  - O substituto só é colocado em produção depois de definido pelo Diretor Comercial.

### F4.2 — Cupons
**Objetivo:** Submeter cupons à mesma política.

#### US-028 — Criar campanha de cupom com autorização
- **Prioridade:** Must
- **História:** Como gerente comercial, quero autorizar cupons acima do limite sem aprovação ao criar a campanha, para evitar aprovação pedido a pedido.
- **Requisitos:** RF-12, RN-03, RNF-04
- **Situação:** Pronta; limite próprio em PA-06; patamar de 15% em PA-21
- **Critérios de aceite:**
  - Cupom de até 15% pode ser criado sem autorização.
  - Cupom acima de 15% só fica ativo com autorização da gerente registrada.
  - Cupom acima de 20% exige diretoria, conforme a mesma política (a confirmar em PA-06).
  - Cada cupom registra validade, percentual e autorização.

#### US-029 — Aplicar cupom no pedido
- **Prioridade:** Must
- **História:** Como cliente da loja, quero que o desconto do cupom seja o que recebo no fim, para não ter o pedido alterado depois da compra.
- **Requisitos:** RF-12, RN-02, RF-16
- **Situação:** Depende de US-002; soma de descontos em PA-06
- **Critérios de aceite:**
  - Cupom válido e autorizado é aplicado sem nova aprovação no pedido.
  - Cupom vencido ou sem autorização é recusado com mensagem clara.
  - Cupom não soma com outro desconto (PR-03).
  - Em homologação, o desconto chega ao ERP sem ajuste manual.

#### US-030 — Regularizar cupons ativos no corte
- **Prioridade:** Must
- **História:** Como Diretor Comercial, quero revisar cupons ativos antes do corte, para que nenhum fique fora da política.
- **Requisitos:** RF-12, RF-29
- **Situação:** Bloqueada por PA-06
- **Critérios de aceite:**
  - Há lista de cupons ativos na data do corte, com situação da autorização.
  - Cupons acima do limite vigente sem autorização não migram como ativos.
  - O tratamento de pedidos pagos com diferença de desconto está decidido e documentado.

## E5 — Reserva de estoque
**Prioridade:** Must
**Objetivo:** Evitar venda duplicada, com disponibilidade igual para todos os canais.

### F5.1 — Disponibilidade
**Objetivo:** Mostrar o mesmo número a todos.

#### US-031 — Exibir disponibilidade única
- **Prioridade:** Must
- **História:** Como vendedor ou cliente da loja, quero ver o saldo realmente disponível, para não vender o que já está reservado.
- **Requisitos:** RF-14, RNF-02, RNF-11, RNF-12
- **Situação:** Bloqueada por PA-01, PA-12 e PA-13
- **Critérios de aceite:**
  - Disponível é o saldo físico do ERP menos as reservas abertas.
  - Todos os canais mostram o mesmo valor para o mesmo SKU.
  - O atraso máximo definido em PA-13 é medido e monitorado.
  - A leitura de saldo respeita o limite de requisições. Para 12 mil SKUs, a abordagem é validada na prova técnica, pois a leitura item a item levaria cerca de 200 minutos.

### F5.2 — Reserva
**Objetivo:** Reservar e liberar conforme o ciclo do pedido.

#### US-032 — Reservar na confirmação
- **Prioridade:** Must
- **História:** Como vendedor ou cliente da loja, quero reservar o item ao confirmar o pedido, para garantir a entrega do que foi vendido.
- **Requisitos:** RF-13, RN-10, RNF-09
- **Situação:** Pronta; sentido de "confirmação" em PA-13
- **Critérios de aceite:**
  - Pedido confirmado em qualquer canal gera reserva por item.
  - Em confirmações simultâneas da última unidade, somente uma reserva é aceita, e a outra recebe aviso.
  - A reserva é mantida durante análises de desconto e crédito (PR-08).
  - Pré-pedido do app offline só reserva ao ser confirmado na sincronização (PR-19).

#### US-033 — Liberar reserva
- **Prioridade:** Must
- **História:** Como gestor comercial, quero que reservas sem uso sejam liberadas, para o estoque voltar à venda.
- **Requisitos:** RF-13
- **Situação:** Bloqueada por PA-13 quanto ao prazo
- **Critérios de aceite:**
  - Cancelamento, recusa ou falha de pagamento liberam a reserva.
  - O prazo de expiração é parâmetro, sem valor padrão presumido.
  - A liberação registra motivo e data.

#### US-034 — Conciliar reserva e baixa do faturamento
- **Prioridade:** Must
- **História:** Como responsável pelo estoque, quero que o faturamento consuma a reserva, para o saldo não ficar em dobro.
- **Requisitos:** RF-15, RN-11, RNF-14
- **Situação:** Depende de US-004; leitura de saldo em PA-01
- **Critérios de aceite:**
  - A baixa continua sendo feita no faturamento do VendaMax.
  - O faturamento detectado por consulta consome a reserva correspondente.
  - O atraso de detecção não gera contagem dupla persistente, e a janela é medida.
  - Divergências entre reserva e faturamento geram alerta e são tratáveis.

## E6 — Crédito automático
**Prioridade:** Should
**Objetivo:** Não travar pedidos de bons pagadores dentro da tolerância aprovada.

### F6.1 — Aprovação automática
**Objetivo:** Automatizar a exceção com regra e dados confiáveis.

#### US-035 — Obter histórico de pagamentos
- **Prioridade:** Should
- **História:** Como Coordenadora Financeira, quero o histórico de atrasos disponível no sistema, para classificar bons pagadores sem conferência manual.
- **Requisitos:** RF-21, RN-06
- **Situação:** Bloqueada por PA-07
- **Critérios de aceite:**
  - A fonte do histórico é identificada e validada com o financeiro.
  - Há uma definição escrita de atraso e do tratamento de cliente sem 12 meses de histórico.
  - A atualização tem frequência e monitoramento definidos.

#### US-036 — Aprovar automaticamente o bom pagador
- **Prioridade:** Should
- **História:** Como Diretor Comercial, quero aprovar automaticamente pedidos de bons pagadores até 120% do limite, para não travar quem paga em dia.
- **Requisitos:** RF-21, RN-06, RNF-04
- **Situação:** Bloqueada por PA-07 e US-035
- **Critérios de aceite:**
  - Cliente sem atraso em 12 meses e com pedido de até 120% do limite é aprovado automaticamente.
  - Pedido acima de 120%, ou cliente com atraso, vai para a análise manual.
  - Cliente sem limite definido vai para a análise manual (PR-10).
  - A aprovação registra a regra e os dados usados.
  - A função só é ligada depois de alterar formalmente a política ou registrar a exceção.

## E7 — Comissão automática
**Prioridade:** Should
**Objetivo:** Calcular comissão igual à que o financeiro paga, com regras sob sua gestão.

### F7.1 — Regras
**Objetivo:** Fechar e configurar as regras.

#### US-037 — Fechar a especificação da comissão
- **Prioridade:** Should
- **História:** Como Coordenadora Financeira, quero as regras e combinações escritas com casos de teste, para o sistema pagar o valor correto.
- **Requisitos:** RF-23, RN-08, RN-09
- **Situação:** Bloqueada por PA-09, PA-10, PA-16 e PA-20
- **Critérios de aceite:**
  - Os casos (a) a (f), o corte de 8% e a situação de aprovação da planilha estão definidos.
  - Vigência dos 6% e fórmula, meta e início do bônus do representante estão definidos.
  - Fonte de impostos, frete e data de competência estão identificadas.
  - Há casos de teste anonimizados, aprovados pelo financeiro.
  - O jurídico se manifestou sobre as regras.

#### US-038 — Configurar regras sem TI
- **Prioridade:** Should
- **História:** Como Coordenadora Financeira, quero alterar as regras de comissão sem depender de TI, para reagir a mudanças aprovadas.
- **Requisitos:** RF-22, RN-14, RNF-04
- **Situação:** Bloqueada por PA-11
- **Critérios de aceite:**
  - Percentuais, corte de desconto, fator e regras de meta podem ser alterados sem implantação.
  - Cada versão tem vigência e não altera comissões já fechadas.
  - A versão só vigora com a aprovação da diretoria registrada (PR-12).
  - O financeiro pode simular a nova regra antes de ativá-la.

### F7.2 — Cálculo e estorno
**Objetivo:** Automatizar o cálculo com rastreabilidade.

#### US-039 — Calcular a comissão
- **Prioridade:** Should
- **História:** Como vendedor ou representante, quero a comissão calculada pelas regras vigentes, para receber o valor correto.
- **Requisitos:** RF-23, RN-08
- **Situação:** Bloqueada por US-037 e PA-20
- **Critérios de aceite:**
  - O interno recebe 3% até a meta e, sobre o excedente, 5% antes da vigência e 6% a partir de março, na base líquida.
  - O representante recebe 4% na base líquida. O bônus de meta entra conforme PA-20 e, até lá, vai à conferência manual (PR-21).
  - Desconto acima de 8% reduz a comissão à metade, conforme especificação.
  - Pedido da loja gera 1% para o responsável da carteira na data aplicável.
  - Caso sem regra definida vai à conferência manual (PR-13).
  - Cada lançamento mostra base, percentual, versão da regra e motivo.

#### US-040 — Estornar comissão por devolução
- **Prioridade:** Should
- **História:** Como Coordenadora Financeira, quero estornar a comissão de devoluções, para que o pagamento reflita a venda final.
- **Requisitos:** RF-24, RN-09
- **Situação:** Bloqueada por PA-10
- **Critérios de aceite:**
  - Devolução identificada no mês seguinte gera estorno, segundo a regra da planilha.
  - Devolução parcial ou de outro período vai à conferência manual até haver regra.
  - Cancelamento comum não é tratado como devolução.

### F7.3 — Fechamento
**Objetivo:** Substituir a planilha com segurança.

#### US-041 — Apurar o fechamento mensal
- **Prioridade:** Should
- **História:** Como Coordenadora Financeira, quero o fechamento no sistema, para cumprir o dia 5 sem colar dados à mão.
- **Requisitos:** RF-25, RN-15
- **Situação:** Bloqueada por PA-11
- **Critérios de aceite:**
  - O fechamento consolida lançamentos, ajustes e estornos do período.
  - Ajuste manual exige justificativa e fica registrado.
  - A etapa de aprovação e o formato para a folha seguem a definição de PA-11.
  - Período fechado não é alterado sem reabertura registrada.

#### US-042 — Exibir extrato de comissão
- **Prioridade:** Should
- **História:** Como representante, quero um extrato por pedido, para entender o valor sem abrir reclamação.
- **Requisitos:** RF-25, RNF-05
- **Situação:** Depende de US-039
- **Critérios de aceite:**
  - O extrato mostra pedido, base, percentual, regra e estorno.
  - Cada vendedor só acessa o próprio extrato.
  - O número de reclamações é acompanhado depois da entrega.

#### US-043 — Rodar em paralelo com a planilha
- **Prioridade:** Should
- **História:** Como Coordenadora Financeira, quero comparar sistema e planilha, para aposentar a planilha com segurança.
- **Requisitos:** RF-25, RF-28
- **Situação:** Bloqueada por US-039 e PA-11
- **Critérios de aceite:**
  - A comparação mostra as diferenças por pedido e vendedor, com causa.
  - A planilha só é aposentada depois de dois fechamentos sem diferença inexplicada (PR-14).
  - A decisão é aprovada pela Coordenação Financeira.

## E8 — Painel de vendas
**Prioridade:** Should
**Objetivo:** Dar visão unificada dos canais, com atraso máximo de 5 minutos.

### F8.1 — Painel unificado
**Objetivo:** Acompanhar vendas de todos os canais.

#### US-044 — Exibir o painel multicanal
- **Prioridade:** Should
- **História:** Como Diretor Comercial, quero ver vendas de todos os canais em um painel, para acompanhar a operação em tempo real.
- **Requisitos:** RF-26, RNF-01
- **Situação:** Bloqueada por PA-14 quanto aos indicadores
- **Critérios de aceite:**
  - O painel mostra os indicadores definidos em PA-14, com filtro por canal.
  - Um pedido registrado aparece em até 5 minutos.
  - O indicador de faturamento mostra o horário da última consulta, e sua tolerância segue PA-14.
  - O painel informa o horário da última atualização.

#### US-045 — Alertar atraso do painel
- **Prioridade:** Should
- **História:** Como analista de TI, quero um alerta de atraso do painel, para garantir que a informação é confiável.
- **Requisitos:** RF-26, RNF-01, RNF-07
- **Situação:** Depende de US-044
- **Critérios de aceite:**
  - Atraso acima de 5 minutos gera alerta.
  - O painel sinaliza quando os dados estão atrasados.

## E9 — Transição e operação
**Prioridade:** Must
**Objetivo:** Proteger a operação atual e implantar sem interromper as vendas.

### F9.1 — Proteção da operação atual
**Objetivo:** Reduzir riscos que existem antes da v1.

#### US-046 — Alertar falha do lote noturno
- **Prioridade:** Must
- **História:** Como analista de TI, quero ser avisado quando o lote falhar, para corrigir antes de a operação ser afetada.
- **Requisitos:** RF-29, RNF-07
- **Situação:** Pronta
- **Critérios de aceite:**
  - A ausência ou erro de qualquer etapa do lote gera alerta ao responsável.
  - O alerta não contém dados pessoais.
  - O monitoramento vale até o encerramento do CSV.

#### US-047 — Testar a restauração da loja
- **Prioridade:** Must
- **História:** Como Gerente de TI, quero um backup testado da loja, para poder recuperar a operação se o servidor falhar.
- **Requisitos:** RF-29, RNF-06
- **Situação:** Pronta
- **Critérios de aceite:**
  - O backup é restaurado em ambiente isolado, com evidência.
  - O tempo de restauração medido é registrado.
  - Os backups têm acesso restrito por conter dados pessoais.

### F9.2 — Continuidade e requisitos operacionais
**Objetivo:** Fechar condições para operar.

#### US-048 — Manter a planilha viável
- **Prioridade:** Must
- **História:** Como Coordenadora Financeira, quero continuar fechando pela planilha enquanto a comissão não entra, para o pagamento não parar.
- **Requisitos:** RF-28, RN-08
- **Situação:** Depende de US-003; regras em PA-20
- **Critérios de aceite:**
  - O relatório de faturados continua trazendo vendedor, desconto real, origem e demais colunas usadas.
  - O pedido da loja permite identificar o responsável pela carteira.
  - Um fechamento é simulado com pedidos do novo fluxo antes do corte.
  - O financeiro aplica na planilha os 6% a partir da vigência e o bônus do representante quando definido, sem esperar o sistema.

#### US-049 — Definir disponibilidade e recuperação
- **Prioridade:** Must
- **História:** Como Gerente de TI, quero definir disponibilidade, RPO e RTO, para orientar arquitetura e operação.
- **Requisitos:** RNF-06, RNF-07
- **Situação:** Bloqueada por PA-17
- **Critérios de aceite:**
  - Os valores estão aprovados com o negócio.
  - O responsável por incidentes está definido.
  - A recuperação é testada antes da produção.

#### US-050 — Definir retenção e controles de dados pessoais
- **Prioridade:** Must
- **História:** Como responsável pela privacidade, quero prazos e controles definidos, para tratar CPF de forma adequada.
- **Requisitos:** RF-04, RNF-05
- **Situação:** Bloqueada por PA-16
- **Critérios de aceite:**
  - O jurídico externo define prazos, base legal e descarte.
  - As permissões e logs são revisados com base nessa definição.
  - Dados antigos da loja, arquivos e backups estão incluídos.

### F9.3 — Implantação
**Objetivo:** Migrar canais com segurança.

#### US-051 — Planejar o corte por canal
- **Prioridade:** Must
- **História:** Como PO, quero um plano de corte com critérios e reversão, para migrar sem interromper vendas.
- **Requisitos:** RF-29, RF-27
- **Situação:** Bloqueada por PA-15
- **Critérios de aceite:**
  - O plano define ordem, critérios de entrada e saída e reversão.
  - O corte não ocorre perto do pico de novembro.
  - A convivência considera a demanda dos canais não migrados na disponibilidade.

#### US-052 — Capacitar os usuários
- **Prioridade:** Must
- **História:** Como gestor comercial, quero capacitar os usuários, para o novo fluxo ser adotado sem queda nas vendas.
- **Requisitos:** RF-29
- **Situação:** Depende de US-051
- **Critérios de aceite:**
  - Os 8 vendedores internos e os 22 representantes são capacitados, inclusive no app offline.
  - Aprovadores, crédito, financeiro e Faturamento também são capacitados.
  - Há canal de suporte definido para o início da operação.

#### US-053 — Validar carga no pico
- **Prioridade:** Must
- **História:** Como Gerente de TI, quero testar o volume de pico, para evitar falha em novembro.
- **Requisitos:** RNF-02, RNF-09, RNF-12
- **Situação:** Depende de US-032; perfil por hora a medir
- **Critérios de aceite:**
  - O teste reproduz 900 pedidos/dia com o perfil horário medido.
  - Não há reserva acima do disponível nem pedido duplicado no ERP.
  - O limite de 60 requisições por minuto não é excedido, e o tempo de detecção de faturamento no pico é registrado.
  - O resultado é aceito pelo Gerente de TI.

## E10 — App de pedidos offline
**Prioridade:** Must
**Objetivo:** Permitir que representantes registrem pedidos sem internet, por decisão da diretoria de 20/01/2027. A classificação como Must é provisória (PR-18).

### F10.1 — Definição e replanejamento
**Objetivo:** Entender a necessidade e decidir o efeito na v1.

#### US-054 — Levantar a necessidade offline
- **Prioridade:** Must
- **História:** Como PO, quero conhecer como os representantes trabalham sem internet, para construir apenas o que eles precisam.
- **Requisitos:** RF-30, RF-31
- **Situação:** Pronta; resolve PA-19
- **Critérios de aceite:**
  - Uma amostra dos 22 representantes foi ouvida sobre frequência sem internet, tarefas e dispositivos.
  - O pré-pedido, ou o que o substitua, foi validado com representantes e Diretor Comercial.
  - Fica definido quem fornece o dispositivo.

#### US-055 — Replanejar a primeira versão
- **Prioridade:** Must
- **História:** Como Diretor Comercial, quero saber o efeito do app no prazo e no escopo, para decidir o que muda de forma consciente.
- **Requisitos:** RF-30, RF-29
- **Situação:** Bloqueada por PA-22; depende de US-001 e US-054
- **Critérios de aceite:**
  - A equipe estimou Musts e app depois da prova técnica.
  - Há opções comparadas: aumentar prazo, aumentar equipe, retirar escopo ou entregar o app em etapas.
  - A diretoria registrou a escolha, sem retirada silenciosa de outros Musts.

### F10.2 — Operação sem internet
**Objetivo:** Consultar e registrar pedidos em campo.

#### US-056 — Consultar catálogo e preços sem internet
- **Prioridade:** Must
- **História:** Como representante, quero consultar catálogo, preço e clientes sem internet, para atender durante a visita.
- **Requisitos:** RF-30, RNF-13
- **Situação:** Depende de US-054 e US-020
- **Critérios de aceite:**
  - Catálogo, preços e clientes da própria carteira ficam disponíveis sem conexão.
  - O app mostra a data da última sincronização.
  - A disponibilidade aparece como referência, e não como garantia.

#### US-057 — Registrar pré-pedido sem internet
- **Prioridade:** Must
- **História:** Como representante, quero registrar o pedido sem internet, para não perder a venda em campo.
- **Requisitos:** RF-30, RN-10
- **Situação:** Depende de US-054; premissa PR-19 (PA-19)
- **Critérios de aceite:**
  - O pré-pedido é registrado sem conexão e sobrevive ao fechamento do app.
  - A tela deixa claro que estoque, desconto e crédito ainda serão validados.
  - O pré-pedido não gera reserva nem aprovação antes de sincronizar.

### F10.3 — Sincronização
**Objetivo:** Levar pré-pedidos ao fluxo normal sem burlar regras.

#### US-058 — Sincronizar pré-pedidos
- **Prioridade:** Must
- **História:** Como representante, quero que os pré-pedidos sejam enviados ao voltar a conexão, para não precisar digitar de novo.
- **Requisitos:** RF-31, RN-10, RNF-10
- **Situação:** Depende de US-057 e US-018
- **Critérios de aceite:**
  - A sincronização é retomada sozinha com a volta da conexão.
  - Reenvios não duplicam pedidos.
  - O pedido passa por preço, alçada, crédito e reserva do fluxo normal, e a reserva ocorre na confirmação.
  - O representante vê o resultado de cada pré-pedido.

#### US-059 — Tratar divergências da sincronização
- **Prioridade:** Must
- **História:** Como representante, quero saber o que mudou em relação ao pré-pedido, para acertar com o cliente antes de seguir.
- **Requisitos:** RF-31
- **Situação:** Depende de US-058; regra em PA-19
- **Critérios de aceite:**
  - Preço alterado, falta de estoque, desconto com aprovação ou crédito pendente deixam o pedido em pendência, com motivo.
  - O sistema não altera valor combinado sem aceite do representante.
  - O pré-pedido pode ser ajustado ou cancelado com registro.

### F10.4 — Segurança no dispositivo
**Objetivo:** Proteger dados de clientes em campo.

#### US-060 — Proteger dados no dispositivo
- **Prioridade:** Must
- **História:** Como responsável pela privacidade, quero proteger os dados guardados no app, para reduzir o risco de vazamento em caso de perda.
- **Requisitos:** RF-32, RNF-05, RNF-13
- **Situação:** Bloqueada por PA-16
- **Critérios de aceite:**
  - O app guarda apenas dados da carteira do representante.
  - Os dados locais ficam protegidos, e o acesso exige autenticação.
  - O acesso pode ser revogado em perda do aparelho ou desligamento.
  - O jurídico externo validou o tratamento.
