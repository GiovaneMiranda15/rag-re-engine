# Requisitos

> Gerado por `recop.py render` a partir de `.re/modelo/requisitos.json`. Não edite à mão.

## Requisitos funcionais

### RF-001 — Cadastro único de clientes (v2)

- **Enunciado:** O sistema deve manter um cadastro único de clientes usado por todos os canais.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:escopo.md, doc:SIS-03/integracao-erp.md#0, entrevista:gestao-pmo Q-011
- **Perfis:** comercial
- **deriva de:** DIV-003, GAR-002, OPO-003
- **Critérios de aceite:**
  - Dado um cliente cadastrado, quando acessado por qualquer canal, então os dados são os mesmos.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  respostas da rodada 1

### RF-002 — Pedidos de todos os canais (v2)

- **Enunciado:** O sistema deve registrar os pedidos de todos os canais em um só lugar, com canal e vendedor.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:escopo.md, doc:geral/ata-kickoff.md#0, entrevista:gestao-pmo Q-011
- **Perfis:** comercial
- **deriva de:** GAR-004, OPO-006
- **Critérios de aceite:**
  - Dado um pedido da loja e um do vendedor, quando consultados, então aparecem na mesma lista, com o canal.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  respostas da rodada 1

### RF-003 — Aprovação de desconto (v3)

- **Enunciado:** O sistema deve encaminhar o desconto acima de 15% ao aprovador da faixa e registrar a decisão.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/politica-comercial.md#0, doc:geral/ata-kickoff.md#0, entrevista:comercial Q-001, entrevista:gestao-pmo Q-011, doc:geral/M-01-ata-diretoria.md#0
- **Perfis:** comercial
- **deriva de:** DIV-001, GAR-006, OPO-001
- **Critérios de aceite:**
  - Dado um desconto de 18%, quando a gerente aprova, então o pedido segue e guarda aprovador e data.
  - Dado um desconto de 18%, quando a gerente recusa, então o pedido não é confirmado.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  substituto retirado do enunciado: sem resposta (Q-016); v3 2026-11-03 CR-003 limite ajustado para 15%

### RF-004 — Comissão automática (v2)

- **Enunciado:** O sistema deve calcular automaticamente a comissão por pedido e por vendedor, sem uso da planilha.
- **Prioridade:** Should
- **Status:** confirmado
- **Fontes:** doc:escopo.md, doc:geral/ata-kickoff.md#0, doc:geral/politica-comercial.md#0, doc:SIS-02/regras-comissao.md#0, entrevista:financeiro Q-004, entrevista:gestao-pmo Q-011, entrevista:negocio Q-013
- **Perfis:** financeiro
- **deriva de:** DIV-002, DIV-012, GAR-003, RIS-008, RIS-011, OPO-002
- **Critérios de aceite:**
  - Dado um pedido faturado, quando a apuração roda, então a comissão aparece por pedido, com a regra aplicada.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  fora do Must literal do PO, mas exigido pela meta de zero planilha (DIV-014); configuração separada em RF-010

### RF-005 — Fila de crédito no sistema (v2)

- **Enunciado:** O sistema deve manter a fila de análise de crédito com prazo, responsável e decisão registrados.
- **Prioridade:** Should
- **Status:** confirmado
- **Fontes:** doc:SIS-01/manual-pedido.md#0, doc:geral/politica-comercial.md#0, entrevista:financeiro Q-008, entrevista:negocio Q-013
- **Perfis:** financeiro
- **deriva de:** DIV-004, GAR-001, OPO-005
- **Critérios de aceite:**
  - Dado um pedido na fila, quando se aproxima 1 dia útil, então o prazo restante fica visível ao analista.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  Should: fora do Must, mas ligado à meta de 1 dia útil (DIV-014)

### RF-006 — Estoque compartilhado (v2)

- **Enunciado:** O sistema deve disponibilizar o mesmo saldo de estoque a todos os canais.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:escopo.md, doc:SIS-03/integracao-erp.md#0, doc:SIS-01/manual-pedido.md#0, entrevista:gestao-pmo Q-011, entrevista:operacoes Q-012
- **Perfis:** operacoes
- **deriva de:** DIV-007, RIS-007, OPO-004
- **Critérios de aceite:**
  - Dado um pedido confirmado, quando outro canal consulta o saldo, então vê o saldo já sem a reserva.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  respostas da rodada 1

### RF-007 — Integração com o VendaMax por API (v3)

- **Enunciado:** O sistema deve integrar-se ao VendaMax por API, para o faturamento e a NF-e, sem troca de arquivos.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/ata-kickoff.md#0, doc:escopo.md, entrevista:software-architect Q-010, entrevista:gestao-pmo Q-011, doc:geral/M-02-email-ti.md#0
- **Perfis:** software-architect, backend-engineer
- **deriva de:** GAR-004, RIS-001, RIS-002, RIS-007, OPO-007
- **Critérios de aceite:**
  - Dado um pedido aprovado, quando enviado ao VendaMax, então é criado pela API REST.
  - Dado um pedido com desconto acima de 10%, dentro da alçada, quando enviado, então não é recusado pelo ERP.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  existência da API não confirmada (Q-023); v3 2026-11-03 CR-005 API REST confirmada para criar pedido e consultar faturamento; demais fluxos sem confirmação

### RF-008 — Migração e saneamento de clientes (v2)

- **Enunciado:** O sistema deve importar clientes do ERP e da loja, identificando duplicidades por documento.
- **Prioridade:** Should
- **Status:** hipótese
- **Fontes:** doc:escopo.md, sql:SIS-01/schema.sql:cliente, sql:SIS-03/schema.sql:clientes, entrevista:juridico-compliance Q-014
- **Perfis:** dba
- **deriva de:** RIS-010
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  segue hipótese: dono e precedência sem resposta (Q-003)

### RF-009 — App de pedido para representante, inclusive offline (v3)

- **Enunciado:** O sistema deve permitir ao representante tirar pedido no cliente sem internet.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/ata-kickoff.md#0, entrevista:gestao-pmo Q-011, doc:geral/M-01-ata-diretoria.md#0
- **Perfis:** comercial, gestao-pmo
- **deriva de:** RIS-004, OPO-008
- **Critérios de aceite:**
  - Dado um representante sem internet, quando registra um pedido, então o pedido fica salvo no aparelho.
  - Dado o aparelho reconectado, quando sincroniza, então o pedido chega ao sistema e não é duplicado.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  fora da v1 (decisão atual); v3 2026-11-03 CR-004 entra na primeira versão por decisão da diretoria; substitui a decisão de Q-011

### RF-010 — Regra de comissão configurável pelo Financeiro (v2)

- **Enunciado:** O sistema deve permitir ao Financeiro alterar regras de comissão sem depender da TI, com data de início de vigência.
- **Prioridade:** Should
- **Status:** confirmado
- **Fontes:** doc:geral/ata-kickoff.md#0, entrevista:financeiro Q-006, doc:geral/M-01-ata-diretoria.md#0
- **Perfis:** financeiro
- **deriva de:** DIV-012, RIS-011
- **Critérios de aceite:**
  - Dado um usuário do Financeiro, quando altera um percentual, então a mudança é salva sem intervenção da TI, com autor e data.
  - Dado um percentual com vigência em março, quando se calcula fevereiro, então vale o percentual anterior.
- **Histórico:** v1 2026-11-03  criado (respostas da rodada 1); v2 2026-11-03 CR-001 regra precisa de data de vigência; a mudança de março é o primeiro caso

### RF-011 — Pedido do representante na web responsiva (v2)

- **Enunciado:** O sistema deve permitir ao representante registrar pedidos pelo navegador do celular, com conexão.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** entrevista:gestao-pmo Q-011, doc:geral/M-01-ata-diretoria.md#0
- **Perfis:** comercial
- **deriva de:** OPO-008
- **Critérios de aceite:**
  - Dado um representante no celular, quando abre o sistema, então consegue registrar um pedido.
- **Histórico:** v1 2026-11-03  criado (respostas da rodada 1); v2 2026-11-03 CR-004 permanece até Q-032 dizer se a web continua junto do app

### RF-012 — Painel de vendas (v1)

- **Enunciado:** O sistema deve mostrar em painel as vendas de todos os canais.
- **Prioridade:** Should
- **Status:** confirmado
- **Fontes:** doc:geral/ata-kickoff.md#0, entrevista:negocio Q-013
- **Perfis:** negocio
- **deriva de:** OPO-006, DIV-014
- **Critérios de aceite:**
  - Dado pedidos de ERP e loja, quando o diretor abre o painel, então vê as vendas por canal.
- **Histórico:** v1 2026-11-03  criado (respostas da rodada 1)

### RF-013 — Reconfirmação de consentimento da base da loja (v1)

- **Enunciado:** O sistema deve solicitar reconfirmação de consentimento aos clientes atuais da loja.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** entrevista:juridico-compliance Q-014
- **Perfis:** juridico-compliance
- **deriva de:** DIV-008
- **Critérios de aceite:**
  - Dado cliente migrado da loja, quando ainda não reconfirmou, então é tratado como sem consentimento.
- **Histórico:** v1 2026-11-03  criado (respostas da rodada 1)

### RF-014 — Cadastro de cupom e campanha (v1)

- **Enunciado:** O sistema deve manter cupons com percentual, validade e autorização.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** entrevista:comercial Q-001, sql:SIS-03/schema.sql:cupons
- **Perfis:** comercial
- **deriva de:** DIV-001
- **Critérios de aceite:**
  - Dado um cupom vencido, quando o cliente o usa, então é recusado.
- **Histórico:** v1 2026-11-03  criado (respostas da rodada 1)

### RF-015 — Consulta periódica de faturamento (v1)

- **Enunciado:** O sistema deve consultar periodicamente no VendaMax o status de faturamento dos pedidos enviados e ainda não faturados.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/M-02-email-ti.md#0
- **Perfis:** backend-engineer
- **deriva de:** RIS-015
- **Critérios de aceite:**
  - Dado um pedido enviado, quando o ERP o fatura, então o sistema registra o faturamento em uma consulta seguinte, sem aviso do ERP.
  - Dado um pedido já faturado, quando o ciclo roda, então ele não é mais consultado.
- **Histórico:** v1 2026-11-03 CR-005 criado por CR-005

## Requisitos não funcionais

### RNF-001 — Integração monitorada (v1)

- **Enunciado:** O sistema deve confirmar cada troca com o ERP, reprocessar falhas e alertar um responsável, nos limites a definir.
- **Categoria:** confiabilidade
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** doc:SIS-03/integracao-erp.md#0
- **Perfis:** devops
- **deriva de:** RIS-006, OPO-007
- **Histórico:** v1 2026-11-03  criado (diagnóstico)

### RNF-002 — Trilha de auditoria (v1)

- **Enunciado:** O sistema deve registrar quem alterou preço, regra de comissão, limite de crédito e aprovações, e quando.
- **Categoria:** segurança
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** doc:geral/politica-comercial.md#0, doc:geral/ata-kickoff.md#0, doc:SIS-02/regras-comissao.md#0
- **Perfis:** security, financeiro
- **deriva de:** RIS-011
- **Histórico:** v1 2026-11-03  criado (diagnóstico)

### RNF-003 — Proteção de dados pessoais (v2)

- **Enunciado:** O sistema deve tratar dados pessoais conforme a LGPD, com finalidade, controle de acesso e retenção definidos.
- **Categoria:** segurança
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** doc:geral/politica-comercial.md#0, entrevista:juridico-compliance Q-014
- **Perfis:** juridico-compliance, security
- **deriva de:** DIV-008, RIS-012
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  segue hipótese: retenção e direitos dependem de jurídico externo (Q-028)

### RNF-004 — Backup e recuperação (v2)

- **Enunciado:** O sistema deve ter backup com restauração testada, com RPO e RTO a definir.
- **Categoria:** confiabilidade
- **Prioridade:** Must
- **Status:** hipótese
- **Fontes:** doc:geral/ata-kickoff.md#0, entrevista:devops Q-015
- **Perfis:** devops
- **deriva de:** RIS-005
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  segue hipótese: RPO/RTO a levantar (Q-029)

### RNF-005 — Atualização da visão de vendas (v3)

- **Enunciado:** O sistema deve atualizar a visão consolidada de vendas com atraso máximo de 5 minutos.
- **Categoria:** desempenho
- **Prioridade:** Should
- **Status:** confirmado
- **Fontes:** doc:geral/ata-kickoff.md#0, entrevista:negocio Q-013, doc:geral/M-02-email-ti.md#0
- **Perfis:** negocio
- **deriva de:** OPO-006
- **Critérios de aceite:**
  - Dado um pedido novo, quando se passam 5 minutos, então ele consta no painel.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  respostas da rodada 1; v3 2026-11-03 CR-005 meta em risco se 'venda' for faturado, pela consulta periódica (RIS-015, Q-027)

### RNF-006 — Capacidade no pico (v2)

- **Enunciado:** O sistema deve processar 900 pedidos por dia, volume do pico de novembro.
- **Categoria:** desempenho
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** entrevista:devops Q-015, doc:geral/M-02-email-ti.md#0
- **Perfis:** devops
- **deriva de:** RIS-004
- **Critérios de aceite:**
  - Dado o teste de carga, quando 900 pedidos entram em um dia, então todos são registrados sem erro.
  - Dado o mesmo teste, quando os pedidos são enviados ao VendaMax, então nenhum minuto passa de 60 requisições.
- **Histórico:** v1 2026-11-03  criado (respostas da rodada 1); v2 2026-11-03 CR-005 pico deve respeitar o limite da API

### RNF-007 — Limite de chamadas ao VendaMax (v1)

- **Enunciado:** O sistema deve manter as chamadas à API do VendaMax em até 60 requisições por minuto, enfileirando o excedente.
- **Categoria:** desempenho
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/M-02-email-ti.md#0
- **Perfis:** software-architect, devops
- **deriva de:** RIS-015
- **Critérios de aceite:**
  - Dado um pico de envios, quando a fila excede 60 requisições em um minuto, então o restante espera, sem perda de pedido.
- **Histórico:** v1 2026-11-03 CR-005 criado por CR-005

## Regras de negócio

### RN-001 — Alçada única de desconto (v3)

- **Enunciado:** O sistema deve exigir aprovação de desconto por faixa, em todos os canais: até 15% nenhuma; acima de 15% até 20% gerente comercial; acima de 20% diretoria.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/politica-comercial.md#0, doc:geral/ata-kickoff.md#0, entrevista:comercial Q-001, doc:geral/M-01-ata-diretoria.md#0
- **Perfis:** comercial
- **deriva de:** DIV-001, GAR-005
- **Critérios de aceite:**
  - Dado um pedido com 15% de desconto, quando é confirmado, então não exige aprovação.
  - Dado um pedido com 15,01% ou 20%, quando é confirmado, então aguarda a gerente comercial.
  - Dado um pedido com 20,01%, quando é confirmado, então aguarda a diretoria.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  respostas da rodada 1; v3 2026-11-03 CR-003 limite sem aprovação de 12% para 15%; faixa da diretoria mantida

### RN-002 — Percentual de comissão por tipo de vendedor (v3)

- **Enunciado:** O sistema deve calcular a comissão sobre o valor líquido faturado (total menos impostos e frete): vendedor interno 3% até a meta mensal e, sobre o excedente, 5% até fevereiro de 2027 e 6% a partir de março de 2027; representante 4% até a meta mensal.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:SIS-02/regras-comissao.md#0, doc:geral/ata-kickoff.md#0, entrevista:financeiro Q-004, doc:geral/M-01-ata-diretoria.md#0
- **Perfis:** financeiro
- **deriva de:** DIV-002, DIV-009, DIV-010
- **Critérios de aceite:**
  - Dado vendedor interno com meta de 100.000 e base de 120.000 (exemplo fictício) em fevereiro de 2027, quando calculado, então o valor é 4.000.
  - Dado o mesmo caso em março de 2027, quando calculado, então o valor é 4.200.
  - Dado representante com meta de 100.000 e base de 80.000 (exemplo fictício), quando calculado, então o valor é 3.200.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  respostas da rodada 1; v3 2026-11-03 CR-001 excedente do interno a 6% a partir de março; cláusula 'sem bônus' do representante retirada por CR-002

### RN-003 — Cliente identificado por CPF ou CNPJ (v2)

- **Enunciado:** O sistema deve aceitar cliente pessoa física e jurídica, com um único cadastro por documento (CPF ou CNPJ) normalizado.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/politica-comercial.md#0, sql:SIS-03/schema.sql:clientes, doc:SIS-03/integracao-erp.md#0
- **Perfis:** comercial, financeiro
- **deriva de:** DIV-003, RIS-003
- **Critérios de aceite:**
  - Dado um CNPJ já cadastrado, com ou sem máscara, quando se tenta novo cadastro, então o sistema recusa a duplicidade.
  - Dado um CPF válido, quando o cliente é cadastrado, então o cadastro é aceito.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  confirmado pela política; envio de PF ao ERP segue pendente (Q-009, Q-023)

### RN-004 — Análise de crédito em 1 dia útil (v2)

- **Enunciado:** O sistema deve encaminhar à análise do Financeiro, com prazo de até 1 dia útil, o pedido a prazo acima do limite de crédito.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/politica-comercial.md#0, doc:SIS-01/manual-pedido.md#0, entrevista:financeiro Q-008
- **Perfis:** financeiro
- **deriva de:** DIV-004, DIV-006, RIS-009
- **Critérios de aceite:**
  - Dado um pedido em boleto acima do limite, quando é confirmado, então entra na fila com prazo de 1 dia útil.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  respostas da rodada 1

### RN-005 — Critério de bom pagador (v2)

- **Enunciado:** O sistema deve aprovar automaticamente o pedido de até 120% do limite de crédito de cliente sem atraso nos últimos 12 meses.
- **Prioridade:** Should
- **Status:** conflito
- **Fontes:** doc:geral/ata-kickoff.md#0, entrevista:negocio Q-007
- **Perfis:** negocio, financeiro
- **deriva de:** DIV-005, OPO-005, RIS-009
- **conflita com:** RN-004
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  critério definido; contraria a política vigente, e o histórico não foi localizado (Q-021)

### RN-006 — Momento de reserva de estoque (v2)

- **Enunciado:** O sistema deve reservar o estoque do item na confirmação do pedido, em qualquer canal.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:SIS-01/manual-pedido.md#0, doc:SIS-03/integracao-erp.md#0, doc:escopo.md, entrevista:operacoes Q-012
- **Perfis:** operacoes
- **deriva de:** DIV-007
- **Critérios de aceite:**
  - Dado saldo de 1 unidade, quando dois canais confirmam pedidos desse item, então só um deles reserva a unidade.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  respondido pelo PO, na ausência de Operações; validar em Q-026

### RN-007 — Consentimento explícito para marketing (v2)

- **Enunciado:** O sistema deve usar dados de clientes para marketing somente com consentimento explícito registrado.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/politica-comercial.md#0, entrevista:juridico-compliance Q-014
- **Perfis:** juridico-compliance
- **deriva de:** DIV-008, OPO-009
- **Critérios de aceite:**
  - Dado um novo cadastro, quando o formulário abre, então o consentimento vem desmarcado.
  - Dado um cliente sem consentimento, quando se gera lista de marketing, então ele fica de fora.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  respondido pelo PO, na ausência do jurídico; validar em Q-028

### RN-008 — Tabela de preços única (v2)

- **Enunciado:** O sistema deve usar uma única tabela de preços em todos os canais.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** doc:geral/politica-comercial.md#0, doc:escopo.md, entrevista:comercial Q-002
- **Perfis:** comercial
- **deriva de:** DIV-011
- **Critérios de aceite:**
  - Dado um produto, quando consultado em qualquer canal, então o preço de tabela é o mesmo.
- **Histórico:** v1 2026-11-03  criado (diagnóstico); v2 2026-11-03  respostas da rodada 1

### RN-009 — Autorização de cupom acima de 15% (v2)

- **Enunciado:** O sistema deve exigir autorização da gerente comercial na criação de campanha com cupom acima de 15%.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** entrevista:comercial Q-001, doc:geral/M-01-ata-diretoria.md#0
- **Perfis:** comercial
- **deriva de:** DIV-001, GAR-005
- **Critérios de aceite:**
  - Dado cupom de 18% sem autorização, quando se ativa a campanha, então o sistema impede.
  - Dado cupom de 15%, quando se ativa a campanha, então não exige autorização.
- **Histórico:** v1 2026-11-03  criado (respostas da rodada 1); v2 2026-11-03 CR-003 derivado de Q-001 (cupons seguem a política); confirmar em Q-031

### RN-010 — Cartão e pix dispensam análise de crédito (v1)

- **Enunciado:** O sistema deve dispensar da análise de crédito o pedido pago com cartão ou pix.
- **Prioridade:** Must
- **Status:** confirmado
- **Fontes:** entrevista:financeiro Q-008, doc:SIS-03/integracao-erp.md#0
- **Perfis:** financeiro
- **deriva de:** DIV-006
- **Critérios de aceite:**
  - Dado um pedido em pix acima do limite, quando é confirmado, então não entra na fila de crédito.
- **Histórico:** v1 2026-11-03  criado (respostas da rodada 1)

### RN-011 — Redutor por desconto acima de 8% (v1)

- **Enunciado:** O sistema deve pagar metade da comissão em pedido com desconto acima de 8%.
- **Prioridade:** Should
- **Status:** confirmado
- **Fontes:** doc:SIS-02/regras-comissao.md#0, entrevista:financeiro Q-004
- **Perfis:** financeiro
- **deriva de:** DIV-002
- **Critérios de aceite:**
  - Dado pedido de representante com 9% de desconto e base de 100.000 (exemplo fictício), quando calculado, então a comissão é 2.000.
  - Dado pedido com 8% de desconto, quando calculado, então não há redução.
- **Histórico:** v1 2026-11-03  criado (respostas da rodada 1)

### RN-012 — Comissão de pedido da loja (v1)

- **Enunciado:** O sistema deve pagar 1% do pedido da loja ao vendedor responsável pela carteira do cliente.
- **Prioridade:** Should
- **Status:** confirmado
- **Fontes:** doc:SIS-02/regras-comissao.md#0, entrevista:financeiro Q-004
- **Perfis:** financeiro
- **deriva de:** DIV-002, DIV-010
- **Critérios de aceite:**
  - Dado pedido da loja sem desconto e base de 10.000 (exemplo fictício), de cliente com carteira, quando calculado, então o vendedor recebe 100.
- **Histórico:** v1 2026-11-03  criado (respostas da rodada 1)

### RN-013 — Estorno de comissão por devolução (v1)

- **Enunciado:** O sistema deve estornar a comissão de pedido devolvido no mês seguinte.
- **Prioridade:** Should
- **Status:** confirmado
- **Fontes:** doc:SIS-02/regras-comissao.md#0, entrevista:financeiro Q-005
- **Perfis:** financeiro
- **deriva de:** DIV-009
- **Critérios de aceite:**
  - Dado pedido comissionado devolvido no mês seguinte, quando a apuração roda, então o valor é estornado.
- **Histórico:** v1 2026-11-03  criado (respostas da rodada 1)

### RN-014 — Calendário de comissão (v1)

- **Enunciado:** O sistema deve fechar a comissão no dia 5 e indicar pagamento no dia 10 do mês seguinte.
- **Prioridade:** Should
- **Status:** confirmado
- **Fontes:** doc:SIS-02/regras-comissao.md#0, entrevista:financeiro Q-004
- **Perfis:** financeiro
- **deriva de:** DIV-002
- **Critérios de aceite:**
  - Dado o dia 5, quando o fechamento roda, então a apuração do mês anterior fica pronta para pagamento no dia 10.
- **Histórico:** v1 2026-11-03  criado (respostas da rodada 1)

### RN-015 — Bônus de meta do representante (v1)

- **Enunciado:** O sistema deve aplicar ao representante, sobre o que exceder a meta mensal, o bônus de meta igual ao do vendedor interno.
- **Prioridade:** Should
- **Status:** confirmado
- **Fontes:** doc:geral/M-01-ata-diretoria.md#0
- **Perfis:** financeiro, comercial
- **deriva de:** DIV-016
- **Critérios de aceite:**
  - Dado representante acima da meta, quando calculado, então o excedente recebe o percentual definido em Q-030.
- **Histórico:** v1 2026-11-03 CR-002 criado por CR-002
