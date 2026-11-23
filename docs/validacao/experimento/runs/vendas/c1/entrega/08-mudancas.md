# Avaliação de mudanças — comunicações M-01 e M-02

**Fontes:** `mudancas/M-01-ata-diretoria.md` (20/01/2027) e `mudancas/M-02-email-ti.md` (sem data).

## 1. Resumo

- **10 afirmações:** 4 conflitantes, 4 complementares, 2 novas, nenhuma existente e nenhuma fora de escopo.
- **Maior impacto:** o app offline volta à v1 sem nada sair do escopo. Foi incluído no backlog como decisão da diretoria, mas prazo e capacidade **não** estão resolvidos (PA-22).
- **API confirmada só em parte:** criar pedido e consultar faturamento. Estoque, clientes e preço, necessários aos Musts, continuam sem confirmação.
- **Ação independente do sistema:** o financeiro precisa ajustar a planilha para os 6% a partir de março, porque a comissão automática é Should e pode não estar pronta.
- **Critério adotado:** a ata de diretoria prevalece sobre documentos e respostas anteriores, por ser posterior e de maior autoridade. Foi aplicado o que está definido. O que ela deixa em aberto virou pendência ou premissa identificada.

## 2. Classificação

| ID | Afirmação | Classificação | Em relação a | Decisão |
|---|---|---|---|---|
| M-01.1 | Interno acima da meta passa de 5% para 6% a partir de março | **conflitante** | RN-08, planilha, Resp. 4 | Aplicada, com vigência |
| M-01.2 | Representantes passam a ter bônus de meta igual ao dos internos | **conflitante** | RN-08, planilha ("4% fixo, sem bônus") | Aplicada como regra. Cálculo em espera (PA-20) |
| M-01.3 | Desconto sem aprovação sobe para 15%, para alinhar com a loja | **conflitante** | RN-01, RN-03, política 1, Resp. 2 e 3 | Aplicada. Vigência e formalização em PA-21 |
| M-01.4 | App offline para representantes entra na primeira versão | **conflitante** | Resp. 10 e 12, escopo da v1 | Aplicada ao escopo e ao backlog. Replanejamento em PA-22 |
| M-02.1 | VendaMax tem API REST | **complementar** | RNF-03, D-29, PA-01 | Aplicada. Falta documentação e teste |
| M-02.2 | API permite criar pedido | **complementar** | RF-16, PA-01 | Aplicada |
| M-02.3 | API permite consultar status de faturamento | **complementar** | RF-16, RF-15, PA-01 | Aplicada |
| M-02.4 | Limite de 60 requisições por minuto | **novo** | Nada anterior | Aplicada: RNF-12 |
| M-02.5 | API não tem webhook | **novo** | Nada anterior. Corrige a suposição de "evento" em D-31 e C-08 | Aplicada: RNF-14 |
| M-02.6 | Faturamento precisa de consulta periódica | **complementar** | RF-15, RF-16. O técnico já previa a hipótese | Aplicada: RNF-14 |

## 3. Impacto por afirmação

### M-01.1 — 6% para interno acima da meta

| Área | Impacto |
|---|---|
| Requisitos | RN-08 agora tem duas vigências: 5% e 6%. Comprova a necessidade de regra versionada (RF-22) |
| Backlog | US-037, US-039 (critério por vigência), US-048 (planilha) |
| Documentos | `02-negocio`, `03-tecnico` (8.4, 11), `01-diagnostico` |
| Em aberto | Ano e competência: tratados como março de 2027, para vendas a partir desse mês (PR-22). O fechamento de março paga vendas de fevereiro, então o texto admite outra leitura (PA-20). Combinação com a redução por desconto acima de 8% (PA-09) |

### M-01.2 — Bônus para representantes

| Área | Impacto |
|---|---|
| Requisitos | RN-08 e C-11. "Igual" admite duas leituras, listadas abaixo |
| Backlog | US-037, US-039 (sem valor fixo), US-048 |
| Documentos | `02-negocio`, `03-tecnico` (8.4), `01-diagnostico` |
| Em aberto | Fórmula, meta aplicável e início. Ao contrário do item 1, o item 2 não dá vigência (PA-20). Possível efeito contratual (PA-16) |

| Leitura de "bônus igual" | Representante acima da meta |
|---|---|
| Mesma taxa dos internos | 6% sobre o excedente |
| Mesmo acréscimo sobre a taxa-base (de 3% para 6%, logo 3 pontos) | 7% sobre o excedente |

**Decisão:** não escolher uma leitura. O bônus vai à conferência manual até a definição (PR-21).

### M-01.3 — 15% sem aprovação

| Área | Impacto |
|---|---|
| Requisitos | RN-01 passa a 15%, 20% e acima de 20%. RN-03 é ajustada por derivação, porque cupom segue a mesma política (Resp. 2 e 3) e o patamar de autorização sobe de 12% para 15% |
| Backlog | US-025 (casos 15,00% e 15,01%, limites como parâmetro), US-028, US-030 |
| Documentos | `02-negocio`, `03-tecnico` (8.2, 11, ADR-09), `01-diagnostico` |
| Em aberto | Início, revisão formal da política e confirmação de que vale para todos os canais, porque a justificativa cita apenas a loja (PR-20, PA-21). Impacto na margem não foi informado |

**Efeitos a considerar:**

- O ERP continua recusando acima de 10%, então o novo limite não funciona no VendaMax hoje e PA-02 fica mais crítica.
- Desconto de 8% a 15% é livre, mas reduz a comissão à metade. Essa distância precisa ser confirmada pelo financeiro (PA-09).

### M-01.4 — App offline na v1

| Área | Impacto |
|---|---|
| Requisitos | Novos RF-30, RF-31, RF-32 e RNF-13. RF-08 (web) permanece. Inverte a decisão das respostas 10 e 12 (C-09) |
| Backlog | Novo épico E10 com 7 histórias (US-054 a US-060). Ajustes em US-018, US-032, US-052 |
| Documentos | Escopo em `02-negocio`, arquitetura, estados e plano em `03-tecnico`, D-33 e R-02 em `01-diagnostico` |
| Em aberto | Tudo o que a resposta 12 deixou sem saber: frequência sem internet, necessidades, pré-pedido e dispositivo (PA-19). Prioridade, prazo e o que sai (PA-22) |

**Decisões provisórias:**

- **Must** (PR-18), pois a ata fala em primeira versão sem indicar prioridade.
- **Pré-pedido** (PR-19): sem internet não há como validar estoque, crédito e alçada. A reserva ocorre ao confirmar na sincronização, o que mantém RN-10.

**Não aplicado:** nenhum outro item foi retirado, nem o prazo alterado, porque isso cabe à diretoria. Com 4 devs e 1 PO, considerar que tudo cabe em 6 meses seria uma afirmação sem base. US-055 trata esse replanejamento.

### M-02.1 a M-02.3 — API existente, criar pedido e consultar faturamento

| Área | Impacto |
|---|---|
| Requisitos | Reduz PA-01, sem encerrá-la. Reduz R-01 |
| Backlog | US-001 em andamento. US-003 e US-004 deixam de ser bloqueadas por PA-01, mas US-003 ainda depende de US-002. US-034 depende da leitura de saldo |
| Documentos | `02-negocio` (resumo, PA-01, C-07), `03-tecnico` (7.1, 7.3) |

| Ainda sem confirmação | Efeito |
|---|---|
| Saldo de estoque | Bloqueia US-031 e a reserva Must |
| Clientes | Bloqueia US-006 |
| Preço | Bloqueia US-007 |
| Número da NF-e | Limita US-004 |
| Impostos, frete, devoluções | Bloqueiam comissão automática |
| Alteração dos triggers | PA-02 sem resposta: pedido pela API pode ser recusado acima de 10% ou voltar à fila de crédito |

O silêncio do e-mail foi tratado como falta de informação, não como ausência da capacidade. A origem é um relato por e-mail, então a prova técnica continua necessária.

### M-02.4 a M-02.6 — Limite de 60 por minuto, sem webhook, consulta periódica

| Área | Impacto |
|---|---|
| Requisitos | Novos RNF-12 e RNF-14. RNF-01 passa a ter ressalva para faturamento (C-12) |
| Backlog | US-001, US-003, US-004, US-005, US-007, US-031, US-034, US-044, US-053 |
| Documentos | `03-tecnico` (7.4, 7.5, 8.1, ADR-07), `02-negocio` (C-08, C-12), `01-diagnostico` (D-40, D-41) |

**Cálculo, supondo uma requisição por item e sem lote (a confirmar):**

| Operação | Tempo com o limite inteiro | Conclusão |
|---|---|---|
| Criar 900 pedidos (pico diário) | 15 min | Sem problema, com fila para rajadas |
| Verificar 300 pedidos pendentes | 5 min | Máximo para ciclo de 5 minutos, sem outro uso |
| Verificar 900 pedidos pendentes | 15 min | Não cumpre 5 minutos |
| Ler saldo de 12 mil SKUs | 200 min | Inviável para acompanhar item a item |

**Conclusões:**

- **O painel de pedidos segue viável em 5 minutos**, pois os pedidos nascem no novo sistema. A meta de faturamento em 5 minutos depende da quantidade pendente, dado ainda não disponível, e precisa de decisão (PA-14).
- **O risco maior é o estoque.** Sem lote ou consulta por período, a disponibilidade não acompanha o ERP com folga. A pergunta foi acrescentada a PA-01.
- **Consulta periódica cria uma janela** entre a baixa no ERP e o consumo da reserva, que pode subestimar a disponibilidade (US-034).
- **O intervalo não foi fixado**, porque depende de medir o tempo entre envio e faturamento.

## 4. Pendências novas

| ID | Pendência | Responsável |
|---|---|---|
| PA-20 | Bônus do representante: fórmula, meta e início. Competência dos 6% | Coord. Financeira, diretoria, jurídico |
| PA-21 | 15%: início, abrangência, revisão da política, patamar do cupom, margem | Diretor Comercial |
| PA-22 | App na v1: prioridade, o que sai, prazo ou equipe | Diretoria, PO, Gerente de TI |

PA-01, PA-14 e PA-19 foram atualizadas. PA-19 deixou de ser apenas insumo pós-v1 e passou a condicionar o épico E10.

## 5. Registro do que mudou

| Arquivo | Alteração |
|---|---|
| `01-diagnostico.md` | Síntese atualizada e nova seção 10, com D-40 a D-42 e R-16 a R-18 |
| `02-negocio.md` | RN-01, RN-03, RN-08, escopo, RF-30 a RF-32, C-06 a C-08 revistos, C-09 a C-12, PR-18 a PR-22, PA-20 a PA-22, riscos, histórico |
| `03-tecnico.md` | RNF-12 a RNF-14, arquitetura, estados, cobertura da API, orçamento de uso (7.4), reserva, faixas, comissão, segurança no app, validação, ADR-07 a ADR-09, plano |
| `04-backlog.md` | Novo E10 com US-054 a US-060. Revistas: US-001, 003, 004, 005, 007, 018, 025, 028, 030, 031, 032, 034, 037, 039, 044, 048, 052, 053 |
| `05-jira.csv`, `06-azure-devops.csv` | Regenerados a partir do backlog revisado |
| `07-rastreabilidade.md` | Regenerado, com a seção de comunicações novas |

**Não alterados:** `fontes/`, que são somente leitura. A política comercial e a planilha precisam ser atualizadas pelos seus responsáveis.

## 6. Limitações

- Os CSVs foram conferidos quanto à estrutura e à quantidade de linhas, mas não importados em um Jira ou Azure DevOps reais.
- Os tempos de uso da API são cálculos sobre hipóteses, não medições.
