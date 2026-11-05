# Perguntas aos stakeholders — Vendas Unificado

Rodada única. Cada pergunta traz o que ela decide e a suposição que será usada se ficar sem resposta. Os códigos (DIV, RIS) remetem a `01-diagnostico.md`.

## Prioridade e fronteira

**1. Para: Paulo (Diretor Comercial)**
Se tudo não couber em 6 meses, o que é inegociável na primeira versão e em que ordem: crédito, desconto, pedidos unificados, cadastro único, comissão, estoque, painel? Qual resultado define sucesso (por exemplo, prazo de crédito, reclamações, cancelamentos), e os 6 meses contam a partir de quando?
- *Decide:* corte da v1 e metas (RIS-02).
- *Sem resposta:* ordem cadastro, preço e desconto, pedidos e crédito, estoque, comissão; prazo a partir do kickoff.

**2. Para: Aline (PO)**
O novo sistema substitui a digitação de pedidos no VendaMax e a LojaB2B, ou convive com eles apenas consolidando dados? Se substituir, a loja é refeita ou mantida com integração em tempo real, e quais canais migram primeiro?
- *Decide:* tamanho do projeto e arquitetura.
- *Sem resposta:* substitui a digitação; VendaMax só fatura; loja migra por último.

## VendaMax

**3. Para: Sérgio (Gerente de TI)**
O VendaMax tem API hoje? Quais operações existem (criar cliente e pedido, consultar status de faturamento e NF-e, preço, estoque, devolução), há documentação e ambiente de homologação, e quais são o contrato, o custo e o prazo do fornecedor para evoluções? Até quando o VendaMax seguirá em uso?
- *Decide:* viabilidade da integração (RIS-01, DIV-16).
- *Sem resposta:* não há API confirmada; a primeira entrega é uma prova técnica.

**4. Para: Sérgio (Gerente de TI)**
Os triggers de desconto (máx. 10%), crédito e comissão, e o campo de CNPJ de 14 posições, podem ser alterados ou desativados para pedidos vindos do novo sistema? Quem faz isso? Na importação atual, como o pedido em cartão escapa do crédito, e como a NF-e de pessoa física é emitida hoje?
- *Decide:* se o novo sistema pode ser dono das regras (DIV-10, DIV-11, DIV-12).
- *Sem resposta:* alterações são necessárias e ficam registradas como bloqueio de projeto.

## Crédito

**5. Para: Paulo (Diretor Comercial) e Renata (Coordenadora Financeira), em conjunto**
O que é "bom pagador" em critérios verificáveis (histórico, atraso, tempo de relação)? O pedido dele acima do limite é liberado automaticamente, até que teto, e a Política será alterada para isso? Quem aprova a mudança e quem responde pela inadimplência?
- *Decide:* conflito entre prioridade comercial e Política item 3 (DIV-07, RIS-07).
- *Sem resposta:* mantém a análise da Política e reduz a fila com priorização e alerta de SLA, sem liberação automática.

**6. Para: Renata (Coordenadora Financeira)**
O limite deve considerar a exposição acumulada (pedidos e títulos em aberto) ou apenas cada pedido? Onde estão os dados de títulos e pagamentos? Como tratar cliente bloqueado, cliente novo ou PF com limite zero, e pedidos em cartão, pix e boleto? A consulta ao Serasa deve ser integrada?
- *Decide:* regra de crédito e fontes de dados (DIV-09, DIV-10).
- *Sem resposta:* mantém a comparação por pedido; bloqueado impede o pedido; cartão e pix aprovados dispensam análise; Serasa continua manual.

## Desconto

**7. Para: Paulo (Diretor Comercial)**
Quem aprova descontos entre 12% e 20% quando o gerente está de férias, e qual o prazo até escalar? As alçadas valem igual para representantes? Cupom é "desconto" sujeito às alçadas: quem autoriza criar um cupom, e o limite de 15% continua? Os 8% que reduzem a comissão são intencionais diante dos 12% livres?
- *Decide:* pendência da ata e regra única de desconto (DIV-01, DIV-02).
- *Sem resposta:* substituto indicado pela diretoria; representantes seguem a mesma alçada; cupom é aprovado previamente na criação, conforme as alçadas.

## Comissão

**8. Para: Renata (Coordenadora Financeira)**
Pode fornecer a planilha de um mês fechado (e, se possível, de um mês com devolução), para servir de resultado esperado nos testes? Confirme também: a meta é apurada sobre o líquido; pedidos da loja contam para a meta; qual a ordem entre meta e redução pela metade; os 1% da loja também caem à metade com cupom acima de 8%; e quem recebe quando o cliente não tem carteira?
- *Decide:* algoritmo e aceite da comissão (DIV-05, RIS-08).
- *Sem resposta:* a automação não substitui a planilha até haver conferência; casos ambíguos ficam para revisão manual.

**9. Para: Renata (Coordenadora Financeira)**
De onde vêm os impostos e o frete usados na base líquida? Como tratar devolução parcial e devolução no mesmo mês? O que causa os "vendedores trocados", e vale o vendedor do pedido ou o da carteira na data do pedido?
- *Decide:* dados necessários do ERP, modelo de estorno e atribuição (DIV-05, DIV-06, DIV-15).
- *Sem resposta:* impostos e frete vêm do faturamento do VendaMax; estorno proporcional; vale o vendedor do pedido.

**10. Para: Renata (Coordenadora Financeira)**
Quem pode alterar as regras de comissão, com que vigência, e as mudanças valem para pedidos já feitos? A aprovação mensal da diretoria permanece e passa para o sistema? O pagamento continua lançado à mão na folha, inclusive para representantes? Vendedores e representantes podem consultar o cálculo? Aceita um período de cálculo paralelo antes de desligar a planilha?
- *Decide:* governança, configurabilidade e transição (DIV-06).
- *Sem resposta:* financeiro configura, diretoria aprova; regras valem só para novos pedidos; pagamento segue fora do sistema; dois fechamentos em paralelo.

## Estoque, cadastro e canais

**11. Para: Paulo (Diretor Comercial), indicando o responsável por estoque/operações, que não consta da ata**
Em que momento o estoque deve ser reservado (digitação, aprovação ou pagamento), e por quanto tempo fica retido num pedido parado no crédito ou em aprovação? Pode vender sem saldo? Há mais de um depósito? E o que é "tempo real" na prática: qual atraso máximo aceitável no estoque e no painel de vendas, e quais indicadores o painel precisa mostrar?
- *Decide:* regra de reserva, requisito de latência e painel (DIV-14).
- *Sem resposta:* reserva na digitação, com expiração configurável; não vende sem saldo; atraso de até 1 minuto; painel de vendas por canal.

**12. Para: Aline (PO), com apoio da pessoa do comercial que faz o recadastro**
Quem é o dono do cadastro único e qual dado prevalece quando ERP e loja divergem? O que fazer com várias contas da loja no mesmo CNPJ? Como PF é recadastrada hoje no ERP? PF tem carteira e limite de crédito?
- *Decide:* regra de consolidação e migração (DIV-11, RIS-09).
- *Sem resposta:* comercial é o dono; ERP prevalece para dados fiscais e de crédito, loja para login; um cliente com várias contas de acesso; PF sem carteira.

**13. Para: Aline (PO), a partir do pedido dos representantes**
Quantos representantes usam ou usariam o app, com que frequência ficam sem internet, e qual o mínimo necessário: consulta de catálogo offline ou pedido completo? Aceitam que o pedido offline só seja confirmado (estoque, crédito, desconto) ao sincronizar? Uma versão web responsiva online atende na primeira versão?
- *Decide:* entrada do app na v1 (RIS-11).
- *Sem resposta:* web responsiva online na v1; app offline fica fora da v1 e é reavaliado depois.

## Operação e LGPD

**14. Para: Sérgio (Gerente de TI)**
Quais os volumes atuais (pedidos por dia e pico, clientes, SKUs, usuários por perfil)? Há restrição de hospedagem, tecnologia ou orçamento? Os 4 devs incluem o terceirizado da loja, e quem cobre QA, banco e infraestrutura? O servidor da loja aguenta até a migração? Quanto histórico de pedidos precisa ser migrado?
- *Decide:* requisitos não funcionais, stack, capacidade e transição (RIS-02, RIS-04, RIS-12).
- *Sem resposta:* stack fica a definir; 4 devs generalistas dedicados; migrar clientes e pedidos em aberto; histórico fica disponível para consulta.

**15. Para: Sérgio (Gerente de TI), encaminhando ao encarregado de dados/jurídico, que não consta da ata**
Quem responde pela LGPD na empresa? Como tratar o consentimento já marcado por padrão na loja: pedir novamente ou desconsiderar? Quais são as regras de retenção e de acesso a dados de pessoas físicas, inclusive pelos representantes?
- *Decide:* conformidade na migração e no novo cadastro (DIV-13, RIS-10).
- *Sem resposta:* consentimento antigo não é usado para marketing até novo aceite; acesso limitado à carteira; retenção a definir com o jurídico.

---

## Suposições registradas no bootstrap (sem necessidade de resposta)

A skill pede respostas interativas na inicialização. Sem ninguém disponível, foi adotado:
- produto "Vendas Unificado", idioma pt-BR, e usuário identificado pelo papel;
- produto novo sobre sistemas existentes, pois não há código no diretório;
- stack não escolhida (depende da pergunta 14);
- nove papéis ativos, sem Head of Marketing, porque não há go-to-market no escopo.

Detalhes em `[método]/artifacts/vendas-unificado/plan-notes.md`.
