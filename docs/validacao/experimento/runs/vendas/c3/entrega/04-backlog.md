# Backlog ágil

- **Projeto:** Sistema de Vendas Unificado
- **Data:** 03/11/2026
- **Baseline:** sem baseline (documentos ainda não validados pelos stakeholders)
- **Revisão:** inclui CR-001 a CR-005 (ver `08-mudancas.md`)
- **Fontes:** `escopo.md`; `fontes/SIS-01-erp/` (manual-pedido.md, schema.sql); `fontes/SIS-02-comissoes/regras-comissao.md`; `fontes/SIS-03-loja-b2b/` (integracao-erp.md, schema.sql); `fontes/geral/` (ata-kickoff.md, erd-vendamax.md, politica-comercial.md); `entrega/respostas.md`; `mudancas/` (M-01, M-02)

## Resumo

9 épicos, 13 features e 33 histórias: 23 Must e 10 Should. Sem estimativa: a equipe ainda não avaliou. Status: 12 itens em `revisar`, os demais em `proposto`.

- **Bloqueadas (14):** US-002, US-005, US-007, US-017, US-018, US-019, US-030, US-020, US-021, US-022, US-023, US-031, US-032, US-033. Dependem de resposta para serem iniciadas.
- **Com detalhe pendente (10):** US-011, US-015, US-016, US-029, US-020, US-021, US-022, US-024, US-025, US-027. O núcleo pode avançar, com a pendência indicada no label.
- **Label `conflito-prioridade`:** épicos EP-006, EP-007 e EP-008 estão como Should, conforme a lista do PO. A meta de 6 meses exige pelo menos EP-006 (DIV-014, Q-025).
- **Label `conflito-prazo`:** EP-009 (app offline) é Must por decisão da diretoria, mas sem plano de prazo e equipe (DIV-015, Q-032).
- **Status `revisar`:** histórias alteradas por CR, com label `revisar-CR-00X`. Novas têm label `novo-CR-00X`.
- **Comece por US-017:** ela comprova a cobertura da API e o efeito dos triggers, dos quais dependem as regras de desconto no ERP.

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

Prioridade: Should

### FT-009 — Cálculo de comissão [proposto]

Cálculo de comissão

Prioridade: Should · Requisitos: RF-004, RN-002, RN-011, RN-012, RN-013, RN-014, RN-015

#### US-019 — Calcular comissão por tipo de vendedor [revisar]

Como Coordenadora Financeira, quero que o sistema calcule a comissão, para abandonar a planilha.

Prioridade: Should · Requisitos: RF-004, RN-002

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

Prioridade: Should

### FT-011 — Análise de crédito [proposto]

Análise de crédito

Prioridade: Should · Requisitos: RF-005, RN-004, RN-010

#### US-025 — Trabalhar a fila com prazo [proposto]

Como analista de crédito, quero uma fila com prazo, para decidir em até 1 dia útil.

Prioridade: Should · Requisitos: RF-005, RN-004

- Dado um pedido em boleto acima do limite, quando é confirmado, então entra na fila com prazo de 1 dia útil.
- Dado um pedido na fila, quando se aproxima 1 dia útil, então o prazo restante fica visível ao analista.

#### US-026 — Dispensar análise em cartão e pix [proposto]

Como cliente da loja, quero que o pagamento em cartão ou pix siga sem análise, para não esperar.

Prioridade: Should · Requisitos: RN-010

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


## Pendências (sem história)

Hipóteses e conflitos não viram história até serem confirmados.

| ID | Status | Enunciado proposto | Por que está pendente |
|---|---|---|---|
| RN-005 | conflito | O sistema deve aprovar automaticamente o pedido de até 120% do limite de crédito de cliente sem atraso nos últimos 12 meses. | critério definido; contraria a política vigente, e o histórico não foi localizado (Q-021) |
| RF-008 | hipótese | O sistema deve importar clientes do ERP e da loja, identificando duplicidades por documento. | segue hipótese: dono e precedência sem resposta (Q-003) |
| RNF-001 | hipótese | O sistema deve confirmar cada troca com o ERP, reprocessar falhas e alertar um responsável, nos limites a definir. | sem confirmação humana; evidência só do problema |
| RNF-002 | hipótese | O sistema deve registrar quem alterou preço, regra de comissão, limite de crédito e aprovações, e quando. | sem confirmação humana; evidência só do problema |
| RNF-003 | hipótese | O sistema deve tratar dados pessoais conforme a LGPD, com finalidade, controle de acesso e retenção definidos. | segue hipótese: retenção e direitos dependem de jurídico externo (Q-028) |
| RNF-004 | hipótese | O sistema deve ter backup com restauração testada, com RPO e RTO a definir. | segue hipótese: RPO/RTO a levantar (Q-029) |

## Perguntas abertas

| ID | Para | Pergunta aberta | Achados |
|---|---|---|---|
| Q-003 | Diretor Comercial (reenviar) | Quem será o dono do cadastro único e qual dado prevalece quando ERP e loja divergirem? Todo cliente precisa ter vendedor de carteira, inclusive pessoa física da loja, e quem define e troca essa carteira? O que causa os vendedores trocados? | DIV-003, DIV-010, RIS-010 |
| Q-009 | Setor de Faturamento, com a Coordenadora Financeira (reenviar) | Como exatamente esses clientes são cadastrados no ERP hoje, e como sai a NF-e deles? Há impacto fiscal ou de contabilização que o novo fluxo deva corrigir? | DIV-003, RIS-003, GAR-002 |
| Q-016 | Diretor Comercial | Quem aprova desconto de 12% a 20% nas férias da gerente, e o que acontece se ninguém responder? | GAR-006, DIV-001 |
| Q-017 | Diretor Comercial | Existe hoje preço diferente por canal, cliente ou representante? Há exceção à tabela única na v1? | DIV-011 |
| Q-018 | Coordenadora Financeira | A aba Leia-me é a regra completa? De onde vêm impostos e frete por pedido? Qual data define o mês e a meta? Como é o arredondamento? | RIS-008, DIV-002 |
| Q-019 | Coordenadora Financeira | Como as regras de comissão se combinam (cupom e loja, loja na meta, carteira de representante, metade sobre 5%)? Como fica devolução parcial, no mesmo mês ou depois de mais de um mês? Há casos reais para teste? | DIV-009, DIV-010 |
| Q-020 | Coordenadora Financeira e diretoria | Quais itens da regra de comissão o Financeiro altera sozinho, quem aprova, com que vigência e retroatividade? A aprovação mensal continua? | DIV-012, RIS-011 |
| Q-021 | Diretor Comercial e Coordenadora Financeira | A política será revisada para permitir a aprovação automática até 120% do limite? Onde está o histórico de atraso e quem assume o risco? | DIV-005 |
| Q-022 | Coordenadora Financeira | O limite considera saldo em aberto ou só o pedido? O que fazer com cliente bloqueado e cliente novo? Quem cobre o analista? Serasa entra na v1? | RIS-009 |
| Q-023 | Gerente de TI e fornecedor | O VendaMax tem API? Se não, quem cria, com que custo e prazo? O fornecedor ajusta os triggers e aceita CPF? Qual a data final de uso? | RIS-001, RIS-002, DIV-003 |
| Q-024 | PO | Vendedores deixam de digitar no VendaMax? A LojaB2B é substituída ou reconectada? Há paralelo da planilha, por quantos ciclos? Qual a data de início e a equipe de QA, UX e DevOps? | RIS-004, RIS-007 |
| Q-025 | PO e Diretor Comercial | Comissão automática, fila de crédito e painel fazem parte da v1? O Must de cinco itens não os inclui, mas as metas de 6 meses dependem deles. | DIV-014 |
| Q-026 | Responsável por Operações/Estoque (a indicar) | O que é 'confirmação do pedido'? Por quanto tempo vale a reserva, ela vale durante a análise de crédito, há mais de um depósito, venda sem saldo é permitida, quem faz o estorno ao cliente, e quem é a fonte do saldo enquanto o ERP baixa no faturamento? | DIV-007, RIS-007, RIS-014 |
| Q-027 | Diretor Comercial | Quais metas para 3 meses e quais indicadores do painel? Venda é pedido criado ou faturado? | OPO-006, RIS-015 |
| Q-028 | Jurídico externo (a indicar) | Quais prazos de retenção e direitos do titular o sistema atende? Consentimento dos clientes só no ERP precisa de reconfirmação? Os contratos de representantes alteram a comissão? Validar o que o PO respondeu. | RIS-012, RIS-013, RIS-014 |
| Q-029 | Gerente de TI | Quais RPO e RTO, total mensal de pedidos e horário de operação? Há stack ou hospedagem obrigatória? Quem responde pela loja e pelo backup até a virada? | RIS-005, RIS-006 |
| Q-030 | Diretoria e Coordenadora Financeira | Qual o valor do bônus de meta do representante: 6% sobre o excedente, 7%, ou outro? Vale desde março? 'A partir de março' é venda faturada em março ou pagamento em março? O Financeiro revisou a mudança? | DIV-016, DIV-017 |
| Q-031 | Diretoria | Desde quando vale o limite de 15%? A faixa da gerente passa a ser acima de 15% até 20%? Cupom só exige autorização acima de 15%? O redutor de comissão acima de 8% permanece? Quem revisa a política? | DIV-001, DIV-017 |
| Q-032 | Diretoria e PO | Para o app offline na v1, o que sai, quanto o prazo aumenta ou quem entra na equipe? Offline, como ficam reserva, alçada, crédito e preço? A web responsiva continua? Qual o tempo máximo sem sincronizar? | DIV-015, RIS-004 |
| Q-033 | Gerente de TI e fornecedor | O limite de 60/min é por chave ou global? A consulta aceita vários pedidos em uma chamada? A API cobre cliente com CPF, produto, preço, estoque, imposto, frete, data de faturamento e devolução? O que ela retorna ao exceder o limite? | RIS-015, RIS-016, RIS-008 |
