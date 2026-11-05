# Diagnóstico do cenário atual — Vendas Unificado

Distribuidora Aurora. Versão 3, atualizada com `respostas.md` e `mudancas/`. O que mudou está nas seções 8 e 9; o texto das seções 2 a 6 descreve o cenário atual e permanece como evidência.

## 1. Conclusões principais

1. **A viabilidade depende do VendaMax, e isso só foi parcialmente esclarecido.** A API existe para criar pedido e consultar status, com limite e sem webhook (seção 9), mas não cobre o restante conhecido nem as regras do ERP. A NF-e fica no ERP, mas as regras dele recusam ou refazem o que o novo sistema decidir: desconto acima de 10%, CPF, crédito e comissão (DIV-12). Nenhuma fonte comprova que o VendaMax tem API (RIS-01).
2. **Crédito mudou de posição.** Era a "prioridade número 1" na ata e não aparece em `escopo.md`; em R1, o crédito automático virou Should. O critério de bom pagador foi definido (R5), mas ainda contraria a Política Comercial (DIV-07, DIV-19).
3. **Há quatro limites de desconto em vigor:** 8%, 10%, 12% e 15%, e o ERP está defasado em relação à Política (DIV-01).
4. **A comissão só pode ser automatizada depois de desambiguada.** A regra da planilha não define ordem de cálculo, e a base "líquida" não existe nos dados analisados (DIV-04, DIV-05).
5. **Não está demonstrado que o escopo cabe em 6 meses com 4 devs e 1 PO**, e o app offline entrou na v1 sem mudança de prazo ou equipe (seção 9). Comissão é Should, mas "zero planilha" é meta: é preciso um corte explícito (RIS-02, DIV-20).

### Fontes e limitações

| Fonte | Data | Natureza |
|---|---|---|
| `geral/erd-vendamax.md` | 2022 | Descritivo, do fornecedor |
| `SIS-01-erp/manual-pedido.md` | 2023 | Processo, anterior à Política |
| `geral/politica-comercial.md` | 10/02/2025 | Normativo |
| `SIS-02-comissoes/regras-comissao.md` | mar/2026 | Regra de fato usada para pagar |
| `SIS-01-erp/schema.sql` | 01/10/2026 | Comportamento implementado |
| `SIS-03-loja-b2b/schema.sql` e `integracao-erp.md` | sem data | Implementado e processo |
| `geral/ata-kickoff.md` | 15/10/2026 | Expectativas dos stakeholders |

**Critério adotado:** Política prevalece como norma; schema indica o que o sistema faz; planilha indica o que é pago. Conflitos entre eles são tratados como divergência a decidir.

**Limitações:**
- Os dumps trazem estrutura e poucos registros, sem volumes. Qualidade de dados não pôde ser medida.
- Não há tabelas de NF-e, impostos, frete, endereço, títulos a receber ou usuários/perfis no dump do ERP. Não dá para saber se elas não existem ou se o dump é parcial.
- O dump do ERP contém registros de clientes e vendedores, que não foram reproduzidos aqui.

Legenda: **[F]** fato com fonte; **[I]** inferência a partir das fontes; **[H]** hipótese a validar.

## 2. Divergências

### Desconto e preço

**DIV-01. Limites de desconto incompatíveis.** Mesmo percentual, resultado diferente em cada lugar:

| Faixa | Política | ERP (trigger) | Cupom da loja | Comissão (planilha) |
|---|---|---|---|---|
| até 8% | Vendedor | Aceita | Permitido | Integral |
| > 8% a 10% | Vendedor | Aceita | Permitido | Metade |
| > 10% a 12% | Vendedor | **Recusa** | Permitido; ERP recusa | Metade |
| > 12% a 15% | Gerente comercial | **Recusa** | Permitido; ERP recusa | Metade |
| > 15% a 20% | Gerente comercial | **Recusa** | Bloqueado (`CHECK`) | Metade |
| > 20% | Diretoria | **Recusa** | Bloqueado (`CHECK`) | Metade |

- [F] Fontes: Política item 1; `fn_valida_desconto`; `cupons.desconto_pct`; planilha.
- [I] O ERP (limite descrito no manual de 2023) não acompanhou a Política de 2025. É a causa provável da reclamação de desconto recusado citada por Paulo.
- [I] Nenhum desconto entre 10% e 20% consegue chegar ao faturamento com o valor aprovado: o ERP não tem fluxo nem campo de aprovação.
- [I] O Vendedor pode dar até 12% sem aprovação, mas perde metade da comissão acima de 8%. Não há como saber pelas fontes se esse incentivo é intencional.

**DIV-02. A Política não cobre cupom.** [F] As alçadas falam de "vendedor", gerente e diretoria, mas o pedido da loja não tem vendedor. O cupom BLACK15 está válido até 30/11/2026 e exigiria, por analogia, aprovação do gerente. [F] O comercial reduz o desconto à mão e o cliente reclama. [I] Isso pode deixar o valor do ERP diferente do valor combinado ou pago na loja; `pedido` não guarda referência ao cupom.

**DIV-03. "Preço próprio" no escopo x tabela única.** [F] O escopo diz que cada canal tem preço próprio; a Política diz que a tabela é única; a loja recebe `preco` do ERP via CSV uma vez por dia. [I] O problema evidenciado é defasagem de até um dia, não duas tabelas mantidas separadamente. [H] Pode haver preços paralelos não documentados. Além disso, não há histórico ou vigência de preço em nenhum dos schemas.

### Comissão

**DIV-04. Duas contas, por construção.**

| Caso | VendaMax (`fn_calcula_comissao`) | Planilha (a que é paga) |
|---|---|---|
| Base | Total do pedido | Líquido: total menos impostos e frete |
| Vendedor interno | 3% | 3% até a meta; 5% sobre o excedente |
| Representante | 3% | 4% fixo |
| Desconto > 8% | Sem efeito | Metade da comissão |
| Pedido da loja | Nada (`vendedor_id` nulo) | 1% ao vendedor da carteira |
| Devolução | Sem estorno | Estorno se no mês seguinte |

[F] A planilha informa que o valor do VendaMax não é usado para pagamento, e registra média de 15 reclamações de representantes por mês.

**DIV-05. Regras da planilha insuficientes para automatizar.** [I] As fontes não definem:
- ordem entre meta e redução de metade (a meta é mensal, a redução é por pedido);
- se a meta é apurada sobre líquido e se pedidos da loja contam para ela;
- se os 1% da loja também caem pela metade com cupom acima de 8%;
- quem recebe quando o cliente não tem carteira (`cliente.vendedor_id` é anulável, e clientes da loja não têm vendedor);
- devolução parcial ou no mesmo mês;
- qual vendedor vale se a carteira mudar, e a causa dos "vendedores trocados" corrigidos à mão.

**DIV-06. Dados e governança da comissão.**
- [F] `pedido` não tem impostos nem frete, então a base líquida não é calculável com os dados analisados.
- [F] `comissao` tem chave em `pedido_id` e é 1:1 com o pedido, o que não comporta estorno ou ajuste.
- [F] Política: regras definidas pelo financeiro e aprovadas pela diretoria anualmente. Ata: Renata quer configurar sem TI. São compatíveis, desde que haja vigência e aprovação. Não há evidência de que a versão de março/2026 tenha aprovação formal.
- [F] O pagamento é lançado "na folha". [H] Isso precisa de confirmação para representantes, que podem não ser empregados.

### Crédito

**DIV-07. Bom pagador x Política.** [F] Paulo: o pedido não pode travar quando o cliente é bom pagador. Política item 3: pedido acima do limite exige análise do financeiro. [F] "Bom pagador" não está definido, e não há histórico de pagamento nos schemas. É preciso alterar ou interpretar a Política; a ata não registra a posição do financeiro sobre isso.

**DIV-08. SLA descumprido.** [F] Política: até 1 dia útil. Manual: média de 2 dias úteis; pedidos de sexta só são vistos na terça. A consulta ao Serasa é feita fora do sistema.

**DIV-09. Lacunas na regra implementada.** [F] `fn_checa_credito`:
- compara só o total do pedido com o limite, sem somar pedidos em aberto. [I] Fracionar pedidos contorna o limite;
- roda apenas no `INSERT`, então um aumento posterior de total não é checado;
- não consulta `cliente.bloqueado`, nem há outra regra visível que use esse campo;
- com `limite_credito` padrão 0, [I] todo cliente novo vai para a fila.

**DIV-10. Cartão, pix e crédito.** [F] Segundo a integração, cartão não passa pela análise e boleto passa; pix não é mencionado. [I] Isso não se explica pelo schema: `pedido` não tem forma de pagamento e o trigger atua em todo `INSERT`. Há tratamento não documentado na importação ou o documento está impreciso.

### Cliente e dados

**DIV-11. Cadastros incompatíveis.**

| Aspecto | VendaMax | LojaB2B |
|---|---|---|
| Documento | `cnpj CHAR(14)`, único, sem máscara | `cpf_cnpj VARCHAR(18)`, com máscara, **sem unicidade** |
| Pessoa física | Não aceita | Aceita |
| Unicidade | CNPJ | E-mail |
| Crédito, bloqueio, carteira | Sim | Não |
| Login e consentimento | Não | Sim |

- [F] A Política admite PF desde 2025; o manual (2023) e o ERP não acompanharam. PF sempre cai em `erros/`.
- [I] Um mesmo CNPJ pode ter várias contas na loja, o que dificulta a deduplicação.
- [H] O recadastro manual de PF num campo de CNPJ pode ter gerado documentos artificiais no ERP, com efeito na migração e na NF-e. O processo real não está documentado.

**DIV-12. O ERP contraria o sistema novo.** [I] Conflito central entre "sistema único" e "NF-e continua no ERP":

| Regra do VendaMax | Efeito se pedido do novo sistema entrar no ERP |
|---|---|
| `fn_valida_desconto` (> 10%, em `INSERT` e `UPDATE`) | Pedido aprovado na alçada correta é recusado |
| `fn_checa_credito` (em `INSERT`) | Pedido liberado volta a `aguardando_credito` |
| `fn_calcula_comissao` | Continua gravando 3%, mantendo a segunda conta |
| `cnpj CHAR(14)` | PF não entra para faturamento |
| Baixa de estoque no faturamento | Estoque do ERP não enxerga reservas do novo sistema |

**DIV-13. LGPD.** [F] Política item 6: marketing só com consentimento explícito. Loja: `aceita_marketing DEFAULT 1`, sem data ou evidência do aceite. [I] O padrão marcado contraria a Política e torna não confiável o consentimento já registrado. Há PF na base desde 2025.

### Estoque, canais e prazo

**DIV-14. "Estoque atualizado para todos" x baixa no faturamento.** [F] O ERP baixa só no faturamento, e dois vendedores podem vender o mesmo item. A loja recebe estoque uma vez por dia, com média de 20 cancelamentos por mês. [I] Não basta sincronizar mais rápido: falta o conceito de reserva, e o mestre do estoque precisa ser definido.

**DIV-15. Devolução sem modelo.** [F] ERD: devolução é lançada como pedido cancelado. [I] Não há como representar devolução parcial nem distinguir cancelamento de devolução, dado que a planilha precisa para estornar.

**DIV-16. Prazo do VendaMax.** [F] Sérgio: não pode ser desligado "neste ano". Escopo: faturamento no ERP "por enquanto". Primeira versão em 6 meses: se contados do kickoff, cerca de abril/2027. [I] O VendaMax precisa continuar depois de 2026, e a data real de saída não está definida.

**DIV-17. Demandas fora do escopo escrito.** [F] Estão na ata, mas não em `escopo.md`: regra de crédito, painel em tempo real, comissão configurável, app offline. Nas fontes, mas sem menção no escopo: PF, devolução, LGPD e migração de dados.

**DIV-18. Documentação defasada.** [F] Manual (2023) e ERD (2022) são anteriores à Política de 2025. Não documentam PF nem as alçadas vigentes. [F] O ERD diz que todo cliente pertence a um vendedor, mas `cliente.vendedor_id` é anulável e sem chave estrangeira.

## 3. Gargalos

| ID | Gargalo | Evidência | Efeito |
|---|---|---|---|
| GAR-01 | Fila de crédito manual | 2 dias úteis em média; sexta só na terça | Pedido travado; SLA descumprido |
| GAR-02 | Lote noturno | Pedido logo após as 02:00 só chega ao ERP no dia seguinte, ~25 h depois [I] | Inviabiliza visão em tempo real |
| GAR-03 | Recadastro de PF | ~1 h/dia do comercial | Trabalho recorrente evitável |
| GAR-04 | Ajuste manual de desconto | Cupom de 15% rejeitado | Retrabalho e reclamação de cliente |
| GAR-05 | Fechamento de comissão | Excel, correção à mão, e-mail; fechamento dia 5, pagamento dia 10 | 15 reclamações/mês |
| GAR-06 | Tratamento de `erros/` | Pasta sem alerta | Pedido parado sem dono [I] |

## 4. Riscos

| ID | Risco | Prob. | Impacto | Resposta sugerida |
|---|---|---|---|---|
| RIS-01 | VendaMax sem API adequada, ou mudança dependente do fornecedor (custo e prazo) | Não avaliada | Crítico | Prova técnica logo no início; contato com fornecedor; plano alternativo a decidir |
| RIS-02 | Escopo maior que a capacidade de 4 devs e 1 PO em 6 meses | Alta [I] | Alto | Corte e ordem de entrega explícitos; comissão e estoque por fases |
| RIS-03 | Regras do ERP rejeitam ou refazem decisões do novo sistema (DIV-12) | Alta | Crítico | Decidir a alteração das regras antes de desenhar pedidos |
| RIS-04 | Servidor da loja antigo, sem backup testado, mantido por 1 terceirizado | Média [H] | Alto | Testar restauração já, independentemente do projeto |
| RIS-05 | Falha silenciosa do lote noturno | [F] ocorre se o servidor cair às 02:00 | Médio | Alerta simples, antes da integração nova |
| RIS-06 | Importação sem chave de origem: `pedido` não guarda o id de `pedidos_web` | Média [I] | Médio | Chave de idempotência na integração nova |
| RIS-07 | Liberar crédito automaticamente aumenta a inadimplência | Média [H] | Alto | Critério aprovado pelo financeiro, teto de exposição e trilha de auditoria |
| RIS-08 | Comissão automática erra e aumenta as reclamações | Média | Alto | Rodada paralela contra a planilha, antes de substituir |
| RIS-09 | Migração de clientes: duplicados e documentos irregulares | Alta [H] | Alto | Perfilar os dados reais e definir regra de consolidação e responsável |
| RIS-10 | Tratamento irregular de dados pessoais (DIV-13) | Média | Alto | Consentimento explícito, com data e origem; validar com jurídico |
| RIS-11 | App offline conflita com estoque, crédito e aprovação online | Alta [I] | Alto | Decidir à parte; offline, a confirmação do pedido é posterior |
| RIS-12 | Papéis ausentes na equipe (QA, DevOps, DBA, UX) e sem dono identificado de estoque/operação | Não avaliada | Médio | Confirmar competências e responsáveis |
| RIS-13 | PostgreSQL 13 fora do suporte da comunidade desde nov/2025 (informação externa às fontes; confirmar) | Baixa a média | Médio | Verificar suporte com o fornecedor |

## 5. Pontos de apoio

- **Regra normativa aprovada:** a Política define alçadas, tabela única e SLA de crédito.
- **SKU comum:** `produto.sku` e `produtos.sku` são únicos nos dois sistemas, base confiável para produtos.
- **CNPJ** é chave natural para casar clientes PJ, depois de normalizar a máscara.
- **Regras escritas:** planilha ("Leia-me") e triggers documentam o comportamento, e podem virar casos de teste.
- **Dados já existentes:** `meta_mensal`, `tipo` de vendedor, `origem` do pedido, carteira, `limite_credito`, `aceita_marketing` e máquina de status do pedido.
- **Linhas de base** para medir sucesso: 15 reclamações/mês, 20 cancelamentos/mês, 1 h/dia, 2 dias úteis.
- **Patrocínio:** direção comercial, financeiro, TI e PO participaram do kickoff.
- **Histórico de fechamentos da planilha** [H]: se preservado, serve de oráculo para testar a comissão.

## 6. Oportunidades

| ID | Oportunidade | Ganho | Observação |
|---|---|---|---|
| OPO-01 | Corrigir já o limite do ERP para a Política (10% para 12%), se o fornecedor permitir | Reduz a reclamação principal sem esperar a v1 | Não resolve 12% a 20% sem fluxo de aprovação |
| OPO-02 | Alerta e dono para falhas do lote e `erros/`; teste de restauração da loja | Reduz risco imediato com baixo esforço | Lote continua até a integração nova |
| OPO-03 | Consolidar a regra de comissão antes de automatizar | Reduz divergências, mesmo ainda na planilha | Depende do financeiro, não de TI |
| OPO-04 | Fila de crédito com visibilidade, prazo e alerta do SLA, inclusive sextas-feiras | Ataca a prioridade nº 1 sem mudar a Política | Pode preceder a liberação automática |
| OPO-05 | Transparência da comissão para vendedores e representantes | Reduz as 15 reclamações/mês [H] | Depende de regra consolidada |
| OPO-06 | Aprovação de desconto com delegação e registro | Resolve a pendência da ata e cria auditoria | Depende de RIS-03 |
| OPO-07 | Entrega por etapas: cadastro e regras primeiro, canais depois | Reduz risco de corte único e retorna valor antes | A confirmar com a fronteira da v1 |
| OPO-08 | Ajustar o padrão de `aceita_marketing` para desmarcado | Adequa à Política com mudança pequena | A base já existente segue em aberto |

## 7. Temas perguntados

As perguntas em `perguntas.md` cobriram os temas abaixo; o que continua aberto está em `02-negocio.md`, seção 8:
- fronteira e corte da v1 (P1, P2);
- viabilidade do VendaMax (P3, P4);
- crédito (P5, P6);
- desconto (P7);
- comissão (P8, P9, P10);
- estoque e tempo real (P11);
- cadastro (P12);
- app offline (P13);
- operação e transição (P14);
- LGPD (P15).

## 8. Atualização após as respostas

### O que mudou

| Item | Resposta | Situação |
|---|---|---|
| DIV-02 Cupom | R7: Cupom segue a política; acima de 12%, autorização do gerente comercial ao criar a campanha | Resolvida em regra. Limite de 15% segue aberto; BLACK15 sem evidência de autorização |
| DIV-05, DIV-06 Comissão | R8, R9: vale a planilha, base líquida, estorno pela regra atual | Direção confirmada. Ordem de cálculo, impostos e frete seguem abertos; planilha de mês fechado não foi fornecida |
| DIV-06 Governança | R10: alterar sem TI | Confirmada. Vigência e aprovação abertas |
| DIV-07 Bom pagador | R5: sem atraso em 12 meses; automático até 120% do limite | Critério definido. Sem alteração da Política, aprovador nem fonte de dados de títulos |
| DIV-09 Exposição, bloqueio | R6: Não sei | Sem mudança |
| DIV-10 Cartão e pix | R6: dispensam análise; boleto precisa | Regra definida. Inconsistência com o schema continua sem explicação (R4) |
| DIV-11 Cadastro | R12: CPF/CNPJ sem máscara é a chave | Chave definida. Campo do ERP segue só com CNPJ; dono e consolidação abertos |
| DIV-12 Regras do ERP | R4: Não sei | **Sem mudança; segue crítica** |
| DIV-13 LGPD | R15: consentimento explícito e reconfirmação da base | Regra definida. Responsável, retenção e acesso abertos; jurídico externo necessário |
| DIV-14 Estoque | R11: reserva na confirmação, em qualquer Canal | Momento definido. Retenção, venda sem saldo e depósitos abertos |
| DIV-16 Prazo do VendaMax | R2, R3: NF-e no ERP em 2027 | Horizonte ampliado; data final desconhecida |
| Pendência da ata | R7: "Ainda não definimos" | **Aberta:** aprovador de 12% a 20% nas férias (PEND-01) |
| RIS-01 API | R3: integração por API é decisão, mas a existência não foi confirmada | **Sem redução** |
| RIS-02 Capacidade | R1: Must e Should definidos | Corte possível; estimativa preliminar de 201 pontos, sem velocidade conhecida |
| RIS-11 App offline | R13: fora da v1 (decisão atual), web responsiva | Encerrado para a v1 |
| RIS-12 Papéis | R14: Não sei | Sem mudança |
| Limitação de volumes | R14: 400 Pedidos/dia, pico 900 em novembro, 60% ERP e 40% loja, 4 mil Clientes, 12 mil SKUs, 8 internos, 22 representantes | Resolvida |

### Novas divergências

**DIV-19. Prioridade de crédito.** [F] Ata: não travar por crédito é "prioridade número 1". R1: crédito automático é Should; a lista de Must não cita crédito. Mas "crédito em até 1 dia útil" é meta de sucesso. [I] Tratamento: análise no prazo como Must derivado; automático como Should (CON-01).

**DIV-20. Comissão: Should com meta de sucesso.** [F] R1 põe Comissão em Should e, na mesma resposta, define "zero planilha" e menos de 3 reclamações por mês como sucesso em 6 meses. O escopo também pede Comissão automática. [I] Se a Comissão não couber, duas das quatro metas não serão atingidas (CON-02).

**DIV-21. Exceções ausentes da Política.** [F] Política item 3 exige análise de Pedido acima do limite, sem exceção. R5 cria aprovação automática até 120%, e R6 dispensa cartão e pix. [I] Precisa de revisão formal; não se sabe quem aprova (CON-03). Também não está claro se "boleto precisa" vale para todo boleto ou só acima do limite (PRE-06).

**DIV-22. Fronteira implícita.** [F] R2 não define se a digitação sai do VendaMax. R11 pede reserva em qualquer Canal, e R13 coloca os representantes em web responsiva. [I] As duas respostas só se sustentam se os Pedidos passarem pelo novo sistema na confirmação (CON-05, PRE-01).

### Novos riscos

| ID | Risco | Prob. | Impacto | Resposta |
|---|---|---|---|---|
| RIS-14 | Reserva feita antes de crédito e aprovação prende saldo em Pedidos parados, com tempo de retenção indefinido | Média [I] | Médio | Histórias 31, 33 e 37 |
| RIS-15 | Durante a coexistência, reserva parcial entre Canais impede atingir a meta de cancelamentos | Média [I] | Médio | Medir M-03 depois da migração completa |
| RIS-16 | Bom pagador não calculável sem dados de títulos, que não aparecem nos dumps | Alta [I] | Médio | História 38 antes da 39 |
| RIS-17 | Virada coincidir com o pico de 900 Pedidos/dia em novembro | Baixa, se a v1 sair no prazo | Alto | História 30 |

## 9. Atualização após `mudancas/`

Detalhes em `08-mudancas.md`. As tabelas das seções 2 e 8 ficam como histórico; a regra vigente está em `02-negocio.md`.

| Item | Mudança | Situação |
|---|---|---|
| DIV-01 | Alçada livre sobe de 12% para 15% | ERP segue em 10%: **distância aumentou**. Comissão pela metade começa em 8%, 7 pontos abaixo da alçada livre |
| DIV-02, CON-07 | Cupom de 15% fica dentro da alçada, se o limiar acompanhar (PRE-15) | ERP segue recusando. BLACK15 e PRIMEIRA10 do dump já venceram na data da ata |
| DIV-04, DIV-05 | Interno passa a 6% no excedente; representante ganha bônus | Forma do bônus do representante indefinida (PEND-11) |
| DIV-12 | E-mail de TI nada diz sobre regras do ERP | **Segue crítica** |
| RIS-01 | API confirmada parcialmente | Reduzido, não eliminado: produto, preço, estoque, Cliente e impostos não confirmados |
| RIS-02 | App adiciona 29 pontos, e a integração adiciona 5, total de 235 | **Aumentou.** Pela premissa PRE-03, a ata ocorre no 4º mês dos 6 [inferência] |
| RIS-11 | App reentra na v1 | **Reaberto** |

### Novas divergências

**DIV-23. Ata x Política e resposta anterior.** [F] A ata eleva a alçada para 15%; POL-1 e R7 falam em 12%. Sem data de vigência nem revisão formal da Política (CON-10).

**DIV-24. App x decisões anteriores.** [F] A ata inclui o app na v1; R13 o excluía; R11 exige reserva na confirmação. [I] Offline, não há como reservar, checar crédito ou aprovar (CON-08, CON-09).

**DIV-25. E-mail x escopo de integração.** [F] A API confirmada cobre duas operações; o escopo exige estoque atualizado para todos, e a ata pede integração sem arquivo. [I] Sem operação de produto e estoque, o CSV das 04:00 não pode ser desligado.

### Novos riscos

| ID | Risco | Prob. | Impacto | Resposta |
|---|---|---|---|---|
| RIS-18 | Limite da API compartilhado com outros consumidores | Não avaliada | Médio | PEND-14 |
| RIS-19 | Atraso na informação de Faturamento afeta status, reserva e fechamento | Média [I] | Médio | US-008, US-034, US-045, US-061 |
| RIS-20 | Pedido offline recusado ao sincronizar, após promessa ao Cliente | Média [I] | Alto | US-055, US-058 |
| RIS-21 | Dados pessoais em aparelhos de representantes | Média [I] | Alto | US-059, PEND-09 |
| RIS-22 | Planilha precisa aplicar 6% em março, antes do sistema, com bônus sem regra | Alta [I] | Médio | Renata atualiza a planilha; US-046 compara na mesma versão |
| RIS-23 | Alçada de 15% reduz margem, sem estudo nas fontes | Não avaliada | Médio | Diretoria acompanha |
