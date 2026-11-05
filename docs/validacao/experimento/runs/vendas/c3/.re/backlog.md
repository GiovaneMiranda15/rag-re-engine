# Backlog

## EP-001 — Cadastro único de clientes [proposto]

Um cadastro para todos os canais, com PF, PJ e consentimento.

Prioridade: Must

### FT-001 — Cadastro PF e PJ [proposto]

Cadastro PF e PJ

Prioridade: Must · Requisitos: RF-001, RN-003

#### US-001 — Cadastrar cliente por CPF ou CNPJ [proposto]

Como vendedor interno, quero cadastrar cliente por CPF ou CNPJ, para vender a PF e PJ.

Prioridade: Must · Requisitos: RN-003, RF-001

- Dado um CNPJ já cadastrado, com ou sem máscara, quando se tenta novo cadastro, então o sistema recusa a duplicidade.
- Dado um CPF válido, quando o cliente é cadastrado, então o cadastro é aceito.

#### US-002 — Usar o mesmo cadastro em todos os canais [proposto]

Como cliente da loja, quero usar o mesmo cadastro em todos os canais, para não precisar repetir dados.

Prioridade: Must · Requisitos: RF-001

- Dado um cliente cadastrado, quando acessado por qualquer canal, então os dados são os mesmos.

### FT-002 — Consentimento de marketing [proposto]

Consentimento de marketing

Prioridade: Must · Requisitos: RF-013, RN-007

#### US-003 — Dar consentimento explícito [proposto]

Como cliente da loja, quero marcar eu mesmo o consentimento de marketing, para decidir o uso dos meus dados.

Prioridade: Must · Requisitos: RN-007

- Dado um novo cadastro, quando o formulário abre, então o consentimento vem desmarcado.
- Dado um cliente sem consentimento, quando se gera lista de marketing, então ele fica de fora.

#### US-004 — Reconfirmar consentimento da base da loja [proposto]

Como cliente atual da loja, quero reconfirmar meu consentimento, para que só valha o que autorizei.

Prioridade: Must · Requisitos: RF-013, RN-007

- Dado cliente migrado da loja, quando ainda não reconfirmou, então é tratado como sem consentimento.

## EP-002 — Pedido multicanal [proposto]

Pedidos de todos os canais no mesmo lugar, com preço único.

Prioridade: Must

### FT-003 — Registro de pedidos [proposto]

Registro de pedidos

Prioridade: Must · Requisitos: RF-002, RF-011, RNF-006

#### US-005 — Registrar pedido como vendedor interno [proposto]

Como vendedor interno, quero registrar pedido no sistema, para que ele fique junto dos demais canais.

Prioridade: Must · Requisitos: RF-002

- Dado um pedido da loja e um do vendedor, quando consultados, então aparecem na mesma lista, com o canal.

#### US-006 — Registrar pedido na web responsiva [revisar]

Como representante, quero registrar pedido pelo celular, com conexão, para atender no cliente.

Prioridade: Must · Requisitos: RF-011, RF-002

- Dado um representante no celular, quando abre o sistema, então consegue registrar um pedido.

#### US-007 — Receber pedido da loja sem lote noturno [proposto]

Como vendedor responsável pela carteira, quero ver o pedido da loja junto dos demais, sem esperar o lote da noite.

Prioridade: Must · Requisitos: RF-002

- Dado um pedido na loja, quando é confirmado, então aparece no sistema com canal loja, sem esperar o lote noturno.

#### US-008 — Suportar o pico de pedidos [revisar]

Como PO, quero validar a carga de 900 pedidos por dia, para atravessar novembro sem falha.

Prioridade: Must · Requisitos: RNF-006

- Dado o teste de carga, quando 900 pedidos entram em um dia, então todos são registrados sem erro.
- Dado o mesmo teste, quando os pedidos são enviados ao VendaMax, então nenhum minuto passa de 60 requisições.

### FT-004 — Preço único [proposto]

Preço único

Prioridade: Must · Requisitos: RN-008

#### US-009 — Aplicar tabela única de preço [proposto]

Como vendedor interno, quero que o preço venha da tabela única, para vender igual em todos os canais.

Prioridade: Must · Requisitos: RN-008

- Dado um produto, quando consultado em qualquer canal, então o preço de tabela é o mesmo.

## EP-003 — Desconto com alçada [proposto]

Mesma política de desconto em todos os canais, com aprovação registrada.

Prioridade: Must

### FT-005 — Alçada por faixa [proposto]

Alçada por faixa

Prioridade: Must · Requisitos: RF-003, RN-001

#### US-010 — Aplicar faixas de desconto [revisar]

Como vendedor interno, quero saber na hora se o desconto exige aprovação, para negociar com o cliente.

Prioridade: Must · Requisitos: RN-001

- Dado um pedido com 15% de desconto, quando é confirmado, então não exige aprovação.
- Dado um pedido com 15,01% ou 20%, quando é confirmado, então aguarda a gerente comercial.
- Dado um pedido com 20,01%, quando é confirmado, então aguarda a diretoria.

#### US-011 — Aprovar ou recusar desconto [revisar]

Como gerente comercial, quero aprovar ou recusar desconto da minha faixa, para cumprir a política.

Prioridade: Must · Requisitos: RF-003, RN-001

- Dado um desconto de 18%, quando a gerente aprova, então o pedido segue e guarda aprovador e data.
- Dado um desconto de 18%, quando a gerente recusa, então o pedido não é confirmado.

#### US-012 — Aprovar desconto acima de 20% [proposto]

Como diretor comercial, quero decidir os descontos acima de 20%, para cumprir a política.

Prioridade: Must · Requisitos: RF-003, RN-001

- Dado um desconto de 25%, quando a diretoria decide, então o pedido guarda decisão, aprovador e data.

### FT-006 — Cupons e campanhas [proposto]

Cupons e campanhas

Prioridade: Must · Requisitos: RF-014, RN-001, RN-009

#### US-013 — Criar cupom com validade [proposto]

Como gerente comercial, quero manter cupons com percentual e validade, para gerir campanhas.

Prioridade: Must · Requisitos: RF-014

- Dado um cupom vencido, quando o cliente o usa, então é recusado.

#### US-014 — Autorizar cupom acima de 15% [revisar]

Como gerente comercial, quero autorizar cupom acima de 15% na criação da campanha, para que o pedido não pare depois.

Prioridade: Must · Requisitos: RN-009, RN-001

- Dado cupom de 18% sem autorização, quando se ativa a campanha, então o sistema impede.
- Dado cupom de 15%, quando se ativa a campanha, então não exige autorização.

## EP-004 — Reserva de estoque [proposto]

Saldo único e reserva na confirmação do pedido.

Prioridade: Must

### FT-007 — Reserva e saldo [proposto]

Reserva e saldo

Prioridade: Must · Requisitos: RF-006, RN-006

#### US-015 — Reservar item na confirmação [revisar]

Como vendedor interno, quero que o item fique reservado ao confirmar o pedido, para não vender o que já foi vendido.

Prioridade: Must · Requisitos: RN-006

- Dado saldo de 1 unidade, quando dois canais confirmam pedidos desse item, então só um deles reserva a unidade.

#### US-016 — Consultar o mesmo saldo em todos os canais [revisar]

Como cliente da loja, quero ver o saldo atualizado, para não comprar item sem estoque.

Prioridade: Must · Requisitos: RF-006

- Dado um pedido confirmado, quando outro canal consulta o saldo, então vê o saldo já sem a reserva.

## EP-005 — Integração com o VendaMax [proposto]

Faturamento e NF-e continuam no VendaMax, integrados por API.

Prioridade: Must

### FT-008 — API com o VendaMax [proposto]

API com o VendaMax

Prioridade: Must · Requisitos: RF-007, RF-015, RNF-007

#### US-017 — Comprovar a API e os triggers do VendaMax [revisar]

Como Gerente de TI, quero comprovar com o fornecedor a API REST, sua cobertura e o efeito dos triggers, para confirmar a viabilidade antes do desenvolvimento.

Prioridade: Must · Requisitos: RF-007

- Dado o ambiente do VendaMax, quando a prova é executada, então criação de pedido e consulta de status ficam demonstradas.
- Dado pedido com desconto acima de 10% criado pela API, quando enviado na prova, então o resultado fica registrado.
- Dado cliente, produto, preço, estoque, imposto, frete e devolução, quando verificados, então cada um fica registrado como coberto ou não pela API.

#### US-018 — Enviar pedido aprovado para faturamento [revisar]

Como analista de faturamento, quero receber pedido aprovado no VendaMax, para emitir a NF-e sem redigitar.

Prioridade: Must · Requisitos: RF-007

- Dado um pedido aprovado, quando enviado ao VendaMax, então é criado pela API REST.
- Dado um pedido com desconto acima de 10%, dentro da alçada, quando enviado, então não é recusado pelo ERP.

#### US-028 — Enfileirar envios no limite da API [proposto]

Como Gerente de TI, quero que os envios respeitem 60 requisições por minuto, para que o pico não perca pedidos.

Prioridade: Must · Requisitos: RNF-007

- Dado um pico de envios, quando a fila excede 60 requisições em um minuto, então o restante espera, sem perda de pedido.

#### US-029 — Consultar periodicamente o faturamento [proposto]

Como vendedor interno, quero que o pedido mostre quando foi faturado, sem depender de aviso do ERP.

Prioridade: Must · Requisitos: RF-015

- Dado um pedido enviado, quando o ERP o fatura, então o sistema registra o faturamento em uma consulta seguinte, sem aviso do ERP.
- Dado um pedido já faturado, quando o ciclo roda, então ele não é mais consultado.

## EP-006 — Comissão automática [proposto]

Regra da planilha no sistema. Fora do Must literal; conflito em DIV-014.

Prioridade: Must

### FT-009 — Cálculo de comissão [proposto]

Cálculo de comissão

Prioridade: Must · Requisitos: RF-004, RN-002, RN-011, RN-012, RN-013, RN-014, RN-015

#### US-019 — Calcular comissão por tipo de vendedor [revisar]

Como Coordenadora Financeira, quero que o sistema calcule a comissão, para abandonar a planilha.

Prioridade: Must · Requisitos: RF-004, RN-002

- Dado vendedor interno com meta de 100.000 e base de 120.000 (exemplo fictício) em fevereiro de 2027, quando calculado, então o valor é 4.000.
- Dado o mesmo caso em março de 2027, quando calculado, então o valor é 4.200.
- Dado representante com meta de 100.000 e base de 80.000 (exemplo fictício), quando calculado, então o valor é 3.200.
- Dado um pedido faturado, quando a apuração roda, então a comissão aparece por pedido, com a regra aplicada.

#### US-030 — Aplicar bônus de meta ao representante [proposto]

Como representante, quero receber o bônus sobre o que exceder a meta, para ter o incentivo definido pela diretoria.

Prioridade: Should · Requisitos: RN-015

- Dado representante acima da meta, quando calculado, então o excedente recebe o percentual definido em Q-030.

#### US-020 — Aplicar redutor acima de 8% [proposto]

Como Coordenadora Financeira, quero aplicar a redução por desconto, para pagar como a regra manda.

Prioridade: Should · Requisitos: RN-011

- Dado pedido de representante com 9% de desconto e base de 100.000 (exemplo fictício), quando calculado, então a comissão é 2.000.
- Dado pedido com 8% de desconto, quando calculado, então não há redução.

#### US-021 — Pagar 1% em pedido da loja [proposto]

Como vendedor responsável pela carteira, quero receber 1% de pedido da loja, para ver essa venda na comissão.

Prioridade: Should · Requisitos: RN-012

- Dado pedido da loja sem desconto e base de 10.000 (exemplo fictício), de cliente com carteira, quando calculado, então o vendedor recebe 100.

#### US-022 — Estornar comissão por devolução [proposto]

Como Coordenadora Financeira, quero estornar comissão de pedido devolvido, para não pagar indevidamente.

Prioridade: Should · Requisitos: RN-013

- Dado pedido comissionado devolvido no mês seguinte, quando a apuração roda, então o valor é estornado.

#### US-023 — Fechar comissão no calendário [proposto]

Como Coordenadora Financeira, quero fechar no dia 5 e pagar no dia 10, para manter o calendário.

Prioridade: Should · Requisitos: RN-014

- Dado o dia 5, quando o fechamento roda, então a apuração do mês anterior fica pronta para pagamento no dia 10.

### FT-010 — Regra configurável [proposto]

Regra configurável

Prioridade: Should · Requisitos: RF-010

#### US-024 — Alterar regra de comissão sem TI [revisar]

Como Coordenadora Financeira, quero alterar a regra sem a TI, para acompanhar as mudanças.

Prioridade: Should · Requisitos: RF-010

- Dado um usuário do Financeiro, quando altera um percentual, então a mudança é salva sem intervenção da TI, com autor e data.
- Dado um percentual com vigência em março, quando se calcula fevereiro, então vale o percentual anterior.

## EP-007 — Crédito [proposto]

Fila com prazo e dispensa por forma de pagamento. Fora do Must literal; conflito em DIV-014.

Prioridade: Must

### FT-011 — Análise de crédito [proposto]

Análise de crédito

Prioridade: Must · Requisitos: RF-005, RN-004, RN-010

#### US-025 — Trabalhar a fila com prazo [proposto]

Como analista de crédito, quero uma fila com prazo, para decidir em até 1 dia útil.

Prioridade: Must · Requisitos: RF-005, RN-004

- Dado um pedido em boleto acima do limite, quando é confirmado, então entra na fila com prazo de 1 dia útil.
- Dado um pedido na fila, quando se aproxima 1 dia útil, então o prazo restante fica visível ao analista.

#### US-026 — Dispensar análise em cartão e pix [proposto]

Como cliente da loja, quero que o pagamento em cartão ou pix siga sem análise, para não esperar.

Prioridade: Must · Requisitos: RN-010

- Dado um pedido em pix acima do limite, quando é confirmado, então não entra na fila de crédito.

## EP-008 — Visão de vendas [proposto]

Painel consolidado. Fora do Must literal; conflito em DIV-014.

Prioridade: Should

### FT-012 — Painel [proposto]

Painel

Prioridade: Should · Requisitos: RF-012, RNF-005

#### US-027 — Ver vendas de todos os canais [revisar]

Como diretor comercial, quero ver as vendas de todos os canais em até 5 minutos, para acompanhar o dia.

Prioridade: Should · Requisitos: RF-012, RNF-005

- Dado pedidos de ERP e loja, quando o diretor abre o painel, então vê as vendas por canal.
- Dado um pedido novo, quando se passam 5 minutos, então ele consta no painel.

## EP-009 — App offline do representante [proposto]

Decisão da diretoria para a v1 (M-01), com prazo e regras em aberto (DIV-015).

Prioridade: Must

### FT-013 — Pedido sem internet [proposto]

Pedido no aparelho e sincronização.

Prioridade: Must · Requisitos: RF-009

#### US-031 — Definir as regras do pedido offline [proposto]

Como PO, quero definir reserva, alçada, crédito e preço no pedido offline, para o app não violar as regras.

Prioridade: Must · Requisitos: RF-009

- Dado cada regra online, quando o pedido é feito sem internet, então o comportamento está decidido e registrado.

#### US-032 — Registrar pedido sem internet [proposto]

Como representante, quero tirar pedido no cliente sem internet, para não perder a venda.

Prioridade: Must · Requisitos: RF-009

- Dado um representante sem internet, quando registra um pedido, então o pedido fica salvo no aparelho.

#### US-033 — Sincronizar pedido ao reconectar [proposto]

Como representante, quero que o pedido suba ao reconectar, sem duplicar, para ele seguir o fluxo normal.

Prioridade: Must · Requisitos: RF-009

- Dado o aparelho reconectado, quando sincroniza, então o pedido chega ao sistema e não é duplicado.
