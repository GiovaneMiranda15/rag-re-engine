# Perguntas aos stakeholders

Estão em ordem de impacto dentro de cada tema. Como serão respondidas uma única vez, cada uma traz a premissa que será adotada se ficar sem resposta. As referências D-xx e R-xx são do `01-diagnostico.md`.

## Decisões comerciais

**1. Para: Diretor Comercial e Coordenadora Financeira.**
Qual critério objetivo define "bom pagador" (por exemplo, tempo de relacionamento, atrasos, valor em aberto) e qual o teto de exposição acima do limite? Esse cliente segue sem análise, com a política alterada, ou o pedido segue e o financeiro analisa em paralelo? De onde vem o histórico de pagamentos?
*Sem resposta: nenhuma exceção é automatizada; a v1 aplica a análise com SLA de 1 dia útil. (D-07, D-08, R-07)*

**2. Para: Diretor Comercial.**
Os limites de 12% e 20% da política seguem válidos para todos os canais? Quem substitui o gerente em ausências, em quanto tempo o aprovador deve responder e o que acontece se não responder? O desconto vale por pedido, por item ou ambos?
*Sem resposta: limites da política, por pedido; substituto é o diretor comercial; pedido fica pendente até decisão, com alerta após 1 dia útil. (D-01, D-02, D-05)*

**3. Para: Diretor Comercial.**
Cupom é desconto pré-aprovado, fora do fluxo do gerente? Quem autoriza a criação, qual o limite e pode somar com outro desconto? Até o fim de novembro, o BLACK15 (15%, válido até 30/11/2026) continua, e como tratar a diferença em pedido já pago quando o comercial reduz o desconto?
*Sem resposta: na v1, cupom é campanha aprovada pela diretoria, com limite de 15% e não cumulativo. Tratamento do BLACK15 fica registrado como risco em aberto. (D-03, R-13)*

**4. Para: Coordenadora Financeira.**
As regras da planilha (março/2026) estão aprovadas pela diretoria e são a referência oficial, inclusive o corte de 8%? Como calcular estes casos: (a) excedente de meta com desconto acima de 8%; (b) pedido da loja com cupom acima de 8%; (c) pedido da loja conta para a meta; (d) cliente da carteira de representante comprando na loja; (e) cliente sem carteira; (f) meta alterada no mês? Se puder, envie exemplos reais anonimizados do cálculo.
*Sem resposta: a planilha é a referência; cada combinação sem definição fica como bloqueio do cálculo automático daquele caso, e o pedido vai para conferência manual. (D-04, D-09, D-25, D-26)*

**5. Para: Coordenadora Financeira.**
De onde vêm os impostos e o frete da base líquida e qual data define o mês da comissão? Devolução parcial estorna proporcionalmente? E devolução no mesmo mês ou após mais de um mês? Como se reconhece hoje uma devolução, se ela aparece como pedido cancelado? Por que ocorrem os "vendedores trocados" corrigidos à mão?
*Sem resposta: competência pela data de faturamento; estorno proporcional no mês em que a devolução for registrada; correção de vendedor exige ajuste com justificativa e trilha. (D-23, D-24, D-27)*

**6. Para: Coordenadora Financeira.**
Quem pode alterar uma regra de comissão, e toda alteração precisa de aprovação da diretoria antes de vigorar? A aprovação mensal por e-mail continua? Como o pagamento chega à folha, inclusive para representantes? Qual diferença é aceitável, e por quantos fechamentos, em paralelo com a planilha, antes de aposentá-la?
*Sem resposta: financeiro edita, diretoria aprova, com vigência e versão; aprovação mensal mantida no sistema; exportação para a folha; dois fechamentos em paralelo sem diferença inexplicada. (D-28, R-06)*

## Integração e dados

**7. Para: Gerente de TI (com o fornecedor do VendaMax).**
O VendaMax tem API documentada? Ela cobre criar pedido, status de faturamento, número da NF-e, impostos, frete, estoque, clientes e devoluções? O fornecedor pode alterar ou desativar os triggers de desconto, crédito e comissão, e com qual prazo e custo? O dump está completo? Como a importação faz o pedido no cartão ou Pix não passar pelo crédito?
*Sem resposta: a existência de API não será presumida; o tema fica como bloqueador de arquitetura e a primeira atividade do projeto é uma prova técnica de integração. (D-12, D-23, D-29, D-30, R-01, R-14)*

**8. Para: pessoa do Comercial que faz o recadastro e Setor de Faturamento.**
Como um cliente com CPF é registrado hoje no ERP, dado que o campo só aceita CNPJ, e como a NF-e dele é emitida? Quantos cadastros são feitos por dia, e há erros decorrentes?
*Sem resposta: tratar pessoa física como requisito que depende de alteração no ERP, sem assumir contorno. (D-14)*

**9. Para: Gerente de TI e PO.**
Por quanto tempo, de forma realista, o VendaMax continuará emitindo NF-e? Durante a convivência, qual sistema é mestre de cliente, preço, estoque e limite de crédito, e onde ocorre a entrada de mercadoria? Quanto histórico migrar? Há tabelas de preço ou exceções fora do ERP?
*Sem resposta: novo sistema é mestre de cliente, pedido, política de desconto e comissão; ERP é mestre de NF-e, tributos, tabela de preços e entrada de estoque; migram cadastros e pedidos em aberto. (D-15, D-16, D-18, D-32, R-10, R-11)*

## Escopo, prazo e operação

**10. Para: PO, Diretor Comercial e Gerente de TI.**
Qual a data de início e o que é inegociável na primeira versão, se não couber tudo: prazo ou escopo? Ordene: alçadas, crédito, cadastro único, pedidos unificados, estoque, comissão, painel e app. A loja atual é mantida com novo backend ou substituída? Em que ordem os canais migram? O terceirizado da loja faz parte dos 4 devs, e a equipe conta com QA, UX e DevOps?
*Sem resposta: prazo fixo de 6 meses a partir da aprovação, com escopo cortado; ordem: integração, cadastro, pedidos e desconto, crédito, estoque, comissão e painel básico. (D-34, R-02, R-05)*

**11. Para: Diretor Comercial e responsável pelo Estoque/Logística.**
Em qual momento o estoque é reservado (digitação, aprovação ou pagamento), por quanto tempo e quem tem prioridade na falta? Pedido em análise de crédito segura estoque? Há mais de um depósito? Qual atraso é aceitável para considerar estoque e painel "em tempo real", e quais indicadores o painel precisa ter?
*Sem resposta: reserva na confirmação do pedido, liberada no cancelamento ou por expiração a definir; um depósito; atualização em até 1 minuto. (D-19, D-20, D-31)*

**12. Para: PO, com representantes.**
Quantos representantes existem, com que frequência ficam sem internet durante a visita e o que precisariam fazer offline? É aceitável que o pedido offline seja apenas um pré-pedido, sujeito a estoque, crédito e desconto na sincronização? Quem fornece o dispositivo?
*Sem resposta: app offline fica fora da v1, com interface web responsiva para representantes. (D-33)*

**13. Para: Analista de Crédito e Coordenadora Financeira.**
O limite deve considerar o saldo em aberto do cliente, ou só o valor do pedido? Cliente bloqueado deve ser barrado? Cartão e Pix dispensam análise? Pessoa física tem limite? Quantos pedidos por dia vão para a fila, qual percentual é aprovado, e quem garante a cobertura para cumprir 1 dia útil? A consulta ao Serasa continua fora do sistema?
*Sem resposta: mantém a regra da política, barra cliente bloqueado, cartão e Pix aprovados dispensam análise e o Serasa segue fora do sistema na v1. (D-06, D-11, D-12, D-13)*

**14. Para: Jurídico / Encarregado de Dados.**
O que fazer com clientes marcados por padrão com `aceita_marketing = 1`: tratar como sem consentimento e pedir novamente? Quais prazos de retenção e controles se aplicam a CPF, inclusive em arquivos de erro? As regras de comissão, especialmente estorno, redução por desconto e pagamento de representantes pela folha, têm respaldo em contrato e na legislação?
*Sem resposta: base atual tratada como sem consentimento para marketing; retenção mínima definida com o jurídico antes da produção; regras de comissão ficam com ressalva de validação jurídica. (D-17, R-08, R-09)*

**15. Para: Gerente de TI.**
Quais são os volumes atuais e de pico (clientes, SKUs, pedidos/dia por canal, usuários, representantes)? Quais as metas de disponibilidade e tempo de recuperação? O servidor da loja aguenta até a migração? Quem responde por incidentes após a entrada em produção? Há restrição de hospedagem ou tecnologia?
*Sem resposta: requisitos não funcionais ficam como propostas a validar, sem números apresentados como fato. (R-03, R-04, D-31)*
