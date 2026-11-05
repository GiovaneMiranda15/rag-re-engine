# Oráculo — Distribuidora Aurora (stakeholders simulados)

Fatos que os stakeholders sabem. Responda só com base nisto. Fora disto: "não sei".

## Quem é quem
- Paulo, Diretor Comercial: patrocinador; decide política comercial.
- Renata, Coordenadora Financeira: dona das regras de comissão e crédito.
- Sérgio, Gerente de TI: dono de integrações e infraestrutura.
- Aline, PO: prioriza o backlog e representa o projeto.
- Gerente comercial: Marta. Ela aprova descontos na faixa intermediária.

## Decisões
- Desconto: vale a Política Comercial (até 12% sem aprovação; 12–20% gerente; acima de 20% diretoria). O limite de 10% do ERP é antigo. Cupons da loja seguem a mesma política; cupom acima de 12% precisa ser autorizado pela gerente ao criar a campanha.
- Comissão: vale a regra da planilha do financeiro. O cálculo do ERP será abandonado. Renata quer poder alterar as regras sem TI.
- Base de comissão: valor líquido. Estorno de comissão em devolução: mantém a regra da planilha.
- Clientes: o novo cadastro aceita PF e PJ. CNPJ/CPF é a chave do cliente, sem máscara.
- Crédito: meta de 1 dia útil. Cliente sem atraso nos últimos 12 meses e pedido dentro de 120% do limite é aprovado automaticamente. Pedido no cartão ou pix não precisa de análise de crédito; boleto precisa.
- Estoque: reservar na confirmação do pedido, em qualquer canal. Baixa continua no faturamento do VendaMax.
- Preço: tabela única para todos os canais; cadastrada no novo sistema.
- VendaMax: continua emitindo NF-e em 2027; novo sistema integra por API.
- "Tempo real" para o Paulo significa painel com atraso máximo de 5 minutos.
- App offline: não entra na v1 (decisão atual). Representantes usarão a web responsiva.
- Marketing: consentimento precisa ser marcado explicitamente pelo cliente; a base atual da loja precisa ser reconfirmada.

## Números
- 4 mil clientes ativos; 8 vendedores internos; 22 representantes; 12 mil SKUs.
- 400 pedidos/dia (pico de 900 em novembro); 60% ERP, 40% loja.
- Sucesso em 6 meses: zero planilha de comissão, reclamações de comissão abaixo de 3/mês, cancelamentos por falta de estoque abaixo de 5/mês, crédito em até 1 dia útil.
- MoSCoW v1 — Must: cadastro único, pedido multicanal, política de desconto com alçada, reserva de estoque, integração com VendaMax. Should: motor de comissão, crédito automático, painel. Could: portal de autoatendimento. Won't v1: app offline, marketplace.

## Não sabem responder
- Quem aprova desconto de 12–20% quando a gerente está de férias: "ainda não definimos; pergunte ao Paulo depois".
- Base legal detalhada de LGPD: "não sei; precisamos do jurídico externo".
- RPO/RTO: "não sei; Sérgio precisa levantar".
- Qualquer dado não listado aqui: "não sei".
