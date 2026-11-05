# Diagnóstico do cenário atual — Sistema de Vendas Unificado

**Status:** revisado depois de `respostas.md` e `mudancas/`. As seções 9 e 10 resumem o que mudou, e prevalecem sobre o texto anterior. As referências P1 a P15 apontam para `perguntas.md`, e as pendências PA e premissas PR estão em `02-negocio.md`.

**Legenda:** **[F]** fato documentado nas fontes · **[I]** inferência a partir das fontes, ainda não confirmada · **Severidade:** Alta, Média ou Baixa.

Dados de registros das fontes (clientes, vendedores, documentos) não foram reproduzidos. Pessoas são citadas pelo cargo.

## 1. Síntese

1. **O maior risco técnico é manter o VendaMax como emissor da NF-e.** O novo sistema vai depender de um ERP que recusa desconto acima de 10%, não aceita CPF e altera o status do pedido por triggers. O fornecedor confirmou, por e-mail da TI, API para criar pedido e consultar faturamento, com limite de 60 requisições por minuto e sem webhook. O restante não foi confirmado.
2. **A causa do "desconto recusado" é conhecida.** Política (12%/20%), ERP (10%), loja (cupom até 15%) e comissão (8%) usam limites diferentes, e o ERP não tem fluxo de aprovação.
3. **A comissão não é só uma fórmula a automatizar.** A planilha é a regra de fato, mas a base líquida, a devolução e a meta mensal dependem de dados ausentes no dump do ERP. Várias combinações de regras também estão indefinidas.
4. **O conflito no crédito persiste em parte.** "Bom pagador" agora tem critério: sem atraso em 12 meses, até 120% do limite. Porém, a política ainda exige análise acima do limite, a fonte do histórico é desconhecida, e o tema caiu de "prioridade nº 1" no kickoff para Should.
5. **Estoque unificado exige decidir quando reservar.** Hoje a baixa só ocorre no faturamento, portanto integrar mais rápido não elimina a venda duplicada.
6. **O escopo foi priorizado, mas não confirmado como viável.** Comissão, crédito automático e painel viraram Should, mas a diretoria incluiu o app offline na v1 em 20/01/2027. Os Musts ainda dependem de capacidades da API e de mudanças no ERP não confirmadas, e não há data de início nem definição entre prazo e escopo. Portanto, 6 meses continuam sem validação **[I]**.

## 2. Fontes e confiabilidade

| Fonte | Data | Uso recomendado |
|---|---|---|
| `fontes/geral/erd-vendamax.md` | 2022 | Visão conceitual. Está defasado e tem inconsistências (D-09, D-24) |
| `fontes/SIS-01-erp/manual-pedido.md` | 2023 | Processo operacional. Anterior à política vigente |
| `fontes/geral/politica-comercial.md` | 10/02/2025 | Regra de negócio aprovada pela diretoria |
| `fontes/SIS-02-comissoes/regras-comissao.md` | 03/2026 | Regra de comissão efetivamente paga. Não há registro da aprovação da diretoria |
| `fontes/SIS-01-erp/schema.sql` | 01/10/2026 | Melhor evidência do comportamento real do ERP. Pode não conter todas as tabelas |
| `fontes/SIS-03-loja-b2b/schema.sql` | Sem data | Estrutura real da loja |
| `fontes/SIS-03-loja-b2b/integracao-erp.md` | Sem data | Integração e problemas conhecidos. Traz as métricas de operação da loja |
| `fontes/geral/ata-kickoff.md` | 15/10/2026 | Expectativas dos patrocinadores. Não são requisitos validados |
| `escopo.md` | Sem data | Objetivo, prazo e equipe |

**Critério provisório para divergências:** política aprovada para desconto, crédito e preço; planilha para comissão; dump para o comportamento atual do sistema.

**Não foram ouvidos:** gerente comercial, analista de crédito, faturamento, representantes, a pessoa do comercial que faz o recadastro, desenvolvedor terceirizado da loja, fornecedor do VendaMax e jurídico/encarregado de dados. Cada um conhece parte crítica do processo.

## 3. Divergências entre sistemas e documentos

### 3.1 Desconto: quatro limites para a mesma decisão

| Faixa | Política | ERP (trigger) | Loja (cupom) | Comissão (planilha) |
|---|---|---|---|---|
| Até 8% | Livre | Aceita | Aceita | Integral |
| Acima de 8% até 10% | Livre | Aceita | Aceita | Metade |
| Acima de 10% até 12% | Livre | **Recusa** | Aceita na loja, ERP rejeita | Metade |
| Acima de 12% até 15% | Gerente | **Recusa** | **Sem aprovação**, ERP rejeita | Metade |
| Acima de 15% até 20% | Gerente | **Recusa** | Não permitido (`CHECK <= 15`) | Metade |
| Acima de 20% | Diretoria | **Recusa** | Não permitido | Metade |

| ID | Divergência | Impacto | Sev. |
|---|---|---|---|
| D-01 | **[F]** O ERP limita o desconto a 10% em inserção e alteração. A política de 2025 permite 12% sem aprovação e mais com alçada | Desconto legítimo é impossível de registrar, o que é causa direta da reclamação citada no kickoff | Alta |
| D-02 | **[F]** O ERP não tem status nem campo de aprovação de desconto. **[I]** As alçadas da política não têm registro sistêmico, e não se sabe como são cumpridas hoje | Falta fluxo e trilha de auditoria (P2) | Alta |
| D-03 | **[F]** O cupom BLACK15 dá 15% na loja, faixa que a política condiciona a aprovação do gerente, e o ERP o rejeita. O comercial reduz o desconto à mão | O cliente é informado de um valor e o pedido é alterado depois. **[I]** Em pedido já pago no cartão, a diferença de valor precisa de tratamento (P3) | Alta |
| D-04 | **[F]** A comissão cai pela metade acima de 8%, patamar que não aparece na política | O vendedor é penalizado dentro da própria alçada. Pode ser decisão intencional, mas precisa ser confirmada (P4) | Média |
| D-05 | **[F]** A política não define substituto do gerente nas férias (pendência do kickoff). **[I]** Também não define prazo de resposta nem se o desconto vale por pedido ou por item. O ERP guarda o percentual no pedido | Aprovação pode travar pedido, efeito oposto ao pretendido | Média |

### 3.2 Crédito

| ID | Divergência | Impacto | Sev. |
|---|---|---|---|
| D-06 | **[F]** A política exige análise em até 1 dia útil. O manual indica média de 2 dias úteis, e pedidos de sexta só são vistos na terça | SLA da política descumprido | Alta |
| D-07 | **[F]** A diretoria comercial quer que o pedido de bom pagador não trave, mas a política manda analisar todo pedido acima do limite. **[I]** Atender ao pedido exige mudar a política ou criar uma regra de exceção aprovada | Conflito de requisito entre comercial e financeiro (P1) | Alta |
| D-08 | **[F]** "Bom pagador" não está definido, e o dump não tem títulos, pagamentos ou atrasos. **[I]** Sem a fonte desse histórico, a regra não pode ser automatizada | Requisito prioritário sem dados de apoio confirmados (P1) | Alta |
| D-11 | **[F]** O trigger compara só o total do pedido com o limite e não considera saldo em aberto. Roda apenas na inserção e ignora o campo `bloqueado`. **[I]** Vários pedidos abaixo do limite podem somar exposição maior, e cliente bloqueado não é barrado no banco | Risco de crédito. Ao replicar a regra, ela seria mantida com falhas (P13) | Alta |
| D-12 | **[F]** A integração afirma que pedido no cartão não passa pelo crédito do ERP. Contudo, o trigger roda em toda inserção e a tabela `pedido` não tem forma de pagamento. A documentação não diz como o Pix é tratado | **[I]** Documentação e banco não se explicam mutuamente: pode haver desvio na importação ou pedido pago retido na fila (P7, P13) | Média |
| D-13 | **[F]** `limite_credito` tem valor padrão 0. **[I]** Cliente recadastrado sem limite definido sempre cairia na fila, inclusive pessoa física | Pode inflar a fila de crédito. Precisa de medição (P13) | Média |

### 3.3 Clientes e carteira

| ID | Divergência | Impacto | Sev. |
|---|---|---|---|
| D-14 | **[F]** Desde 2025 a política permite pessoa física, e a loja aceita CPF. O ERP exige `cnpj` (`CHAR(14) NOT NULL`), e pedidos com CPF sempre vão para `erros/`, gerando cerca de 1h/dia de recadastro | **[I]** Como a NF-e continua no ERP, o cadastro único não resolve o problema sozinho. Não há fonte explicando como um CPF é recadastrado nem como a NF-e é emitida (P8) | Alta |
| D-15 | **[F]** A loja guarda documento com máscara e sem `UNIQUE`, com `email` único. O ERP guarda sem máscara e com CNPJ único. **[I]** Um mesmo CNPJ pode ter várias contas na loja | A migração exige deduplicação e separar cliente de usuário de acesso (P9) | Média |
| D-09 | **[F]** O ERD diz que todo cliente tem um único vendedor, mas `cliente.vendedor_id` aceita nulo e não tem chave estrangeira. O ERD também mostra pedido com vendedor obrigatório, e sua própria nota diz que pedidos da loja não têm vendedor | Regra de carteira não é confiável, e ela define a comissão de 1% da loja (P4) | Média |
| D-16 | **[F]** Os atributos são complementares: limite e carteira só no ERP; e-mail, senha e consentimento só na loja. Endereço e inscrição estadual não aparecem em nenhum dump | **[I]** O modelo único precisa unir as bases e confirmar de onde vêm os dados exigidos para NF-e (P7, P9) | Média |
| D-17 | **[F]** `aceita_marketing` tem padrão 1 na loja, enquanto a política exige consentimento explícito. O ERP não tem campo de consentimento | Não conformidade potencial com a política e a LGPD. A base atual pode não servir como prova de consentimento (P14) | Alta |

### 3.4 Preço e estoque

| ID | Divergência | Impacto | Sev. |
|---|---|---|---|
| D-18 | **[F]** O escopo diz que cada canal tem preço próprio. A política exige tabela única, e a loja recebe preço do ERP por CSV. **[I]** A diferença documentada é defasagem de até um dia, não uma segunda tabela | Pode reduzir o trabalho de "política de preço única". Falta confirmar se há exceções fora das fontes (P9) | Média |
| D-19 | **[F]** O ERP baixa estoque só no faturamento, permitindo que dois vendedores vendam o mesmo item | O problema é de regra, não apenas de integração (P11) | Alta |
| D-20 | **[F]** A loja recebe estoque 1x/dia e tem média de 20 cancelamentos/mês. **[I]** O arquivo das 04:00 sai depois da importação das 03:00, mas pedidos ainda não faturados não reduzem o estoque, então o saldo pode nascer superestimado | Mesmo atualizado, o saldo atual não representa o disponível (P11) | Alta |

### 3.5 Comissão

| Caso | ERP (trigger) | Planilha (o que é pago) |
|---|---|---|
| Base de cálculo | Total do pedido | Líquido: total menos impostos e frete |
| Vendedor interno | 3% | 3% até a meta, 5% sobre o excedente |
| Representante | 3% | 4% fixo |
| Desconto acima de 8% | Sem efeito | Metade da comissão |
| Pedido da loja | Nenhum registro (sem vendedor) | 1% ao responsável pela carteira |
| Devolução | Sem estorno no trigger | Estorno se ocorrer no mês seguinte |

| ID | Divergência | Impacto | Sev. |
|---|---|---|---|
| D-21 | **[F]** O cálculo do ERP diverge da planilha em todas as linhas da tabela acima | São as "duas contas" citadas no kickoff, com média de 15 reclamações/mês de representantes | Alta |
| D-22 | **[F]** O manual diz que o financeiro "confere" a comissão do ERP na planilha. A planilha diz que o valor do ERP não é usado para pagamento | O manual está defasado. A planilha é a referência provisória (P4) | Baixa |
| D-23 | **[F]** Não há impostos, frete nem data de faturamento no dump. **[I]** A base líquida e a competência não podem ser calculadas com o que foi visto. Os dados podem estar em tabelas ausentes ou no relatório exportado | Bloqueia o cálculo automático até achar a fonte (P5, P7) | Alta |
| D-24 | **[F]** Não há entidade de devolução: ela é registrada como pedido cancelado, igual ao cancelamento comum. **[I]** Devolução parcial e distinção entre cancelamento e devolução não são representáveis | Bloqueia o estorno automático (P5) | Alta |
| D-25 | **[F]** A tabela `comissao` tem uma linha por pedido, enquanto o bônus depende do acumulado mensal por vendedor. `meta_mensal` não tem histórico | **[I]** O modelo atual não suporta a regra. Recálculo com meta antiga seria incorreto (P4) | Média |
| D-26 | **[F]** A planilha não define combinações, por exemplo excedente de meta com desconto acima de 8%, cupom de loja, ou se pedido da loja conta para a meta. **[I]** Sem resposta, o sistema codificaria uma interpretação arbitrária | A comissão pode continuar sem bater (P4) | Alta |
| D-27 | **[F]** O financeiro corrige "vendedores trocados" à mão. A causa não está documentada | Automatizar sem atacar a causa só moveria o erro (P5) | Média |
| D-28 | **[F]** O financeiro quer regra configurável sem TI. A política exige aprovação anual da diretoria, e a planilha também vai à diretoria para aprovar o pagamento. **[I]** Configuração precisa de vigência, versão e aprovação | Sem governança, a autonomia pode violar a política (P6) | Média |

### 3.6 Integração, escopo e prazo

| ID | Divergência | Impacto | Sev. |
|---|---|---|---|
| D-29 | **[F]** A TI exige API, mas as fontes só documentam CSV. Nada comprova API no VendaMax. O ERD é do fornecedor | Bloqueador potencial de toda a arquitetura (P7) | Alta |
| D-30 | **[I]** Se os triggers continuarem ativos, o ERP pode recusar desconto aprovado acima de 10%, voltar pedido liberado para `aguardando_credito` e gravar comissão de 3% | Decisões do novo sistema seriam desfeitas ou recusadas no ERP (P7) | Alta |
| D-31 | **[F]** O painel "em tempo real" foi pedido, mas o faturamento fica no ERP e o pedido da loja hoje pode levar cerca de 25h para chegar ao ERP. "Tempo real" não tem tolerância definida | A integração precisa ser bidirecional e por evento, e o requisito precisa de número (P11, P15) | Média |
| D-32 | **[F]** A restrição de manter o VendaMax foi descrita como "neste ano", enquanto o escopo diz "por enquanto", e a v1 ficaria para 2027 **[I]** | O horizonte de convivência com o ERP não está definido e muda o investimento na integração (P9) | Média |
| D-33 | **[F]** O app offline para representantes está "a avaliar". **[I]** Pedido offline não tem acesso a estoque, crédito e alçada atualizados, tensionando os demais objetivos | Grande impacto em esforço, e o escopo não o menciona (P12) | Alta |
| D-34 | **[F]** O escopo fala em sistema único, mas não diz se a loja atual ganha novo backend ou é substituída, nem quando vendedores param de digitar no VendaMax | Define a estratégia de corte e o tamanho da v1 (P9, P10) | Alta |
| D-35 | **[F]** `pedidos_web` não tem status do pedido nem do pagamento, e não há documentação do meio de pagamento. **[I]** A loja não recebe de volta o andamento do pedido no ERP | Pedidos unificados exigem ciclo de vida e integração de pagamento ainda não descritos (P7) | Média |

## 4. Gargalos

| Gargalo | Medida disponível | Causa | Fonte |
|---|---|---|---|
| Fila de crédito | Média de 2 dias úteis, contra 1 da política. Sexta vista só na terça | Análise manual, consulta ao Serasa fora do sistema, sem cobertura ou alerta documentados | Manual, política |
| Recadastro de pessoa física | Cerca de 1h/dia | ERP sem CPF, CSV rejeitado | Integração |
| Pedido da loja até o ERP | Até cerca de 25h **[I]**, para pedido logo após as 02:00 | Lote noturno único | Integração |
| Atualização de preço e estoque da loja | 1x/dia | Lote noturno único | Integração, schema da loja |
| Ajuste manual de cupom | Sem medida | Limite de 10% no ERP | Integração |
| Fechamento de comissão | Sem medida de horas. Média de 15 reclamações/mês | Exportar, colar, corrigir à mão, aprovar por e-mail | Planilha |
| Vendas sem estoque | 20 cancelamentos/mês na loja. Sem dado para os canais internos | Sem reserva, estoque defasado | Integração, manual |

**Medidas que faltam para a linha de base:** volume de pedidos e clientes, percentual e valor de pedidos que vão para crédito, descontos recusados e custo por hora do fechamento (P15).

## 5. Riscos

| ID | Risco | Prob. | Impacto | Resposta sugerida |
|---|---|---|---|---|
| R-01 | VendaMax sem API adequada, ou fornecedor sem prazo para alterar triggers e CPF | Média a alta **[I]** | Alto | Validar com o fornecedor antes de fechar a arquitetura. Avaliar camada de integração isolada e alternativa técnica aprovada pela TI |
| R-02 | Escopo excede a capacidade da equipe em 6 meses | Alta **[I]** | Alto | Definir o corte da v1 por valor e dependências. Tratar app offline, painel completo e substituição da loja como decisões explícitas |
| R-03 | Servidor da loja falhar antes da migração: é antigo e sem backup testado | Média | Alto | Testar restauração e alertar falha do lote já, independentemente da v1 |
| R-04 | Falha silenciosa do lote: se o servidor cair às 02:00, ninguém é avisado | Média | Médio | Monitorar a geração e a importação dos arquivos |
| R-05 | Dependência de um único desenvolvedor terceirizado na loja | Média | Alto | Documentar e transferir conhecimento. Confirmar se ele faz parte da equipe (P10) |
| R-06 | Comissão automática não bater e aumentar a insegurança dos representantes | Média | Alto | Fechar regras por escrito, usar casos de teste aprovados pelo financeiro e rodar em paralelo com a planilha antes do corte (P6) |
| R-07 | Afrouxar o crédito de "bom pagador" elevar a inadimplência | Média | Alto | Critério objetivo aprovado, teto de exposição, auditoria e acompanhamento (P1) |
| R-08 | Tratamento inadequado de dados pessoais: CPF de autônomos, consentimento por padrão, arquivos em `erros/` e, se houver app, dados em dispositivo móvel | Média | Alto | Avaliação com o jurídico, consentimento versionado, retenção e controle de acesso (P14) |
| R-09 | Regras de comissão terem risco trabalhista ou contratual, como estorno, redução por desconto e pagamento na folha para representante | A avaliar | Alto | Revisão jurídica antes de codificar. Este diagnóstico aponta a dúvida, sem conclusão legal (P14) |
| R-10 | Migração com duplicidade de clientes e carteira incorreta | Alta **[I]** | Médio | Perfilar dados, definir regra de união e tratar exceções com responsável de negócio (P9) |
| R-11 | Convivência entre sistemas gerar dois donos do mesmo dado | Média | Alto | Definir sistema mestre por dado e por fase (P9) |
| R-12 | Baixa adesão de vendedores e representantes ao novo processo | Média | Médio | Envolver representantes e o gerente comercial cedo, e planejar treinamento |
| R-13 | Pico de novembro (até 900 pedidos/dia) com BLACK15 válido até 30/11/2026, antes de qualquer entrega. A continuidade do cupom ficou sem resposta | Alta **[I]** | Médio | Decidir tratamento provisório do cupom agora (PA-06) |
| R-14 | PostgreSQL 13 no ERP. Pelo que se sabe externamente, o suporte da comunidade terminou em 2025. Confirmar com o fornecedor | A confirmar | Médio | Verificar versão suportada e impacto na integração (P7) |
| R-15 | O limite continuar comparado só com o valor do pedido, com aprovação até 120%, permitindo exposição acumulada acima do limite | Média **[I]** | Alto | Decidir entre pedido e saldo em aberto (PA-08) |

## 6. Pontos de apoio

- **Regras escritas:** política aprovada, planilha com regras explícitas e triggers que documentam o comportamento do ERP.
- **Chaves de integração:** SKU é único nas duas bases e tem o mesmo formato. O CNPJ é único no ERP, e já existe rotina de casamento sem máscara.
- **Preço:** a política exige tabela única, e a loja já recebe preço do ERP.
- **NF-e estável no ERP**, fora da mudança inicial.
- **Estruturas aproveitáveis:** `origem` e status no pedido, `exportado_erp` na loja e tipo de vendedor.
- **Métricas iniciais:** há medidas de crédito, recadastro, cancelamentos e reclamações.
- **Patrocínio:** diretoria comercial, financeiro, TI e PO participaram do kickoff com objetivos claros.
- **Cadastro da loja já preparado** para CPF, e-mail e consentimento, ainda que o padrão de consentimento precise mudar.

## 7. Oportunidades

Em ordem aproximada de valor, sujeita a validação:

1. **Motor de alçadas de desconto** com aprovador substituto e trilha de auditoria. Ataca a reclamação prioritária.
2. **Fila de crédito com SLA e regra de exceção aprovada**, reduzindo tempo de espera sem perder controle.
3. **Cadastro único com CPF e CNPJ**, eliminando o recadastro diário.
4. **Reserva de estoque na venda**, com disponibilidade comum a todos os canais.
5. **Comissão versionada, com simulação e extrato por vendedor**, para reduzir reclamações e fechamento manual.
6. **Substituir o CSV por integração monitorada**, removendo a falha silenciosa e a dependência do servidor antigo.
7. **Consentimento explícito versionado**, corrigindo a não conformidade e organizando a base para marketing.
8. **Painel unificado de vendas**, que pode começar com os indicadores essenciais.

Medidas imediatas, independentes da v1: alerta de falha do lote noturno, teste de restauração do servidor da loja e decisão sobre o BLACK15.

## 8. Premissas iniciais: situação depois das respostas

| # | Premissa inicial | Situação |
|---|---|---|
| 1 | Limites da política valem para todos os canais, e cupom é tratado conforme decisão da diretoria | **Confirmada** (Resp. 2 e 3) |
| 2 | A planilha, e não o ERP, define a regra de comissão | **Confirmada** (Resp. 4). Aprovação e combinações seguem pendentes |
| 3 | NF-e, tributos e baixa fiscal continuam no VendaMax na v1 | **Confirmada** para NF-e e baixa (Resp. 9). Tributos seguem como premissa PR-06 |
| 4 | O app offline fica fora da v1 até decisão com base em dados | **Confirmada** (Resp. 10 e 12) |
| 5 | Nenhuma exceção de crédito é automatizada sem critério aprovado | **Alterada:** critério dado (Resp. 1). A ativação depende da política e da fonte de dados (PA-07) |

## 9. Atualização depois das respostas

### 9.1 Achados alterados

| Achado | Mudança |
|---|---|
| D-01, D-02, D-03 | A política vale para todos os canais. Cupom acima de 12% é autorizado pela gerente na criação da campanha. A rejeição pelo ERP segue até resolver PA-02 |
| D-05 | Continua aberto. O substituto da gerente segue sem definição, e a resposta pede para perguntar ao Diretor Comercial depois (PA-04) |
| D-07, D-08 | Critério definido, mas a alteração da política e a fonte do histórico são desconhecidas (PA-07) |
| D-12 | Regra definida: cartão e Pix dispensam análise. A discrepância técnica segue sem explicação (PA-01) |
| D-14 | Continua aberto. Ninguém soube explicar o caminho de CPF no ERP (PA-03) |
| D-17 | Consentimento explícito e reconfirmação da base confirmados. Retenção e controles dependem do jurídico externo (PA-16) |
| D-18 | Tabela de preços única confirmada, e agora cadastrada no novo sistema (ver D-38) |
| D-19, D-20 | Reserva na confirmação decidida, e a baixa permanece no faturamento. Detalhes em PA-13 |
| D-26 | Continua aberto. A planilha é a referência, mas os casos (a) a (f) não foram respondidos (PA-09) |
| D-29, D-30 | Continuam abertos. A API é decisão da TI, mas sua existência e a alteração dos triggers são desconhecidas (PA-01, PA-02) |
| D-31 | Painel: máximo de 5 minutos. O atraso aceitável de estoque não foi definido |
| D-32 | VendaMax permanece emitindo NF-e em 2027. O período posterior é desconhecido (PA-18) |
| D-33 | App offline fora da v1, com web responsiva para os 22 representantes. Os dados para reavaliar seguem em aberto (PA-19) |
| D-34 | Prioridades Must e Should definidas. Destino da loja e ordem de migração seguem em aberto (PA-15) |
| R-02 | Reduzido pelo corte, mas não resolvido: sem data de início, definição entre prazo e escopo, ou composição da equipe |
| R-08 | Base da loja será reconfirmada. Falta a orientação do jurídico |
| R-09 | Sem resposta. A PO respondeu na ausência do jurídico, e o tema segue aberto |

### 9.2 Novos achados

| ID | Achado | Impacto | Sev. |
|---|---|---|---|
| D-36 | **[F]** Crédito de bom pagador era "prioridade número 1" no kickoff e virou Should na resposta 10 | Pode sair da v1 contra a expectativa inicial (C-01) | Alta |
| D-37 | **[F]** O escopo pede comissão automática, que virou Should. **[I]** Se ela sair da v1, a planilha continua dependendo de vendedor e desconto corretos no ERP | Exige manter a planilha viável (RF-28) | Média |
| D-38 | **[F]** Preço será cadastrado no novo sistema, mas o ERP mantém `preco_tabela` e emite a NF-e | É preciso publicar preço no ERP (C-04) | Média |
| D-39 | **[F]** Reserva no novo sistema e baixa no ERP. **[I]** Sem evento confiável de faturamento, a disponibilidade fica errada | Reserva Must depende de PA-01 (C-08) | Alta |

### 9.3 Volumes agora conhecidos

Fonte: Resp. 15. São 4 mil clientes ativos, 12 mil SKUs, 400 pedidos/dia com pico de 900 em novembro (60% ERP, 40% loja), 8 vendedores internos e 22 representantes. Continuam faltando os dados da fila de crédito, descontos recusados e horas de fechamento.

### 9.4 Confiança nas respostas

Nas respostas 8 e 14, a PO respondeu na ausência das áreas citadas, e a 8 ficou sem conteúdo. Por isso, Faturamento e jurídico externo ainda precisam ser ouvidos. Grande parte das respostas traz "Não sei": esses pontos foram mantidos como pendência ou premissa identificada, e não como fato.

## 10. Atualização depois das comunicações M-01 e M-02

Avaliação completa em `08-mudancas.md`. A seção 3 descreve as fontes como estão: a política e a planilha ainda não foram revisadas.

### 10.1 Achados alterados

| Achado | Mudança |
|---|---|
| D-01, D-03 | O limite sem aprovação passa a 15% pela ata. A distância para o limite de 10% do ERP aumenta, assim como a dependência de PA-02 |
| D-04 | Vendedor pode dar até 15% sem aprovação, mas perde metade da comissão acima de 8% |
| D-21, D-26 | Interno passa a 6% acima da meta e representante ganha bônus. A distância entre ERP e regra paga aumenta, e surgem novas combinações |
| D-25 | O bônus do representante também precisa de meta mensal. A tabela `vendedor` já a comporta |
| D-29 | API confirmada em parte por e-mail, sem documentação. Estoque, clientes, preço, impostos, frete, devoluções e número da NF-e continuam abertos |
| D-31 | A ideia de integração "por evento" é substituída por consulta periódica |
| D-33 | App offline **volta à v1**, por decisão da diretoria. O conflito com estoque, crédito e alçada atualizados permanece e é tratado com pré-pedido (PR-19) |
| D-39 | Reserva e baixa dependem de detecção por consulta, com janela de atraso |
| R-01 | Probabilidade reduzida para média: a API existe, mas a cobertura segue incerta |
| R-02 | **Agravado:** o app entrou sem nada sair do escopo |
| R-08 | Dados de clientes no dispositivo passam a fazer parte da v1 |
| R-09 | Bônus e novos percentuais entram na revisão jurídica |
| R-13 | Pela data da ata, o BLACK15 já venceu conforme o dump. Resta o tratamento de pedidos com diferença de desconto |

### 10.2 Novos achados

| ID | Achado | Impacto | Sev. |
|---|---|---|---|
| D-40 | **[F]** API limitada a 60 requisições por minuto. **[I]** Em chamadas por item, saldo de 12 mil SKUs levaria 200 minutos | Estoque depende de operação em lote ou por período, ainda não confirmada | Alta |
| D-41 | **[F]** Sem webhook. **[I]** Com uma chamada por pedido, só 300 pedidos pendentes podem ser verificados a cada 5 minutos | Indicador de faturamento pode não cumprir 5 minutos (C-12) | Média |
| D-42 | **[F]** A ata não indica vigência dos itens 2 e 3, e o item 2 não dá a fórmula do bônus | Bloqueia configuração final (PA-20, PA-21) | Média |

### 10.3 Novos riscos

| ID | Risco | Prob. | Impacto | Resposta |
|---|---|---|---|---|
| R-16 | Limite de requisições atrasar faturamento, estoque e cargas no pico | Média | Alto | Limitador, prioridade, medição e operação em lote, se houver |
| R-17 | App offline consumir a capacidade dos demais Musts | Alta | Alto | Decidir PA-22 antes de nova estimativa |
| R-18 | Pré-pedido gerar promessa ao cliente sem estoque, crédito ou alçada | Média | Médio | Comunicação clara no app e tratamento de divergências |
