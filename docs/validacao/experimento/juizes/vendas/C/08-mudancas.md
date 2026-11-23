# Avaliação de mudanças — Vendas Unificado

Comunicações avaliadas: `mudancas/M-01-ata-diretoria.md` (20/01/2027) e `mudancas/M-02-email-ti.md` (sem data).

## 1. Resumo

- **Foram aplicadas às entregas:** 6% do interno, alçada de 15%, app na v1 e as características da API.
- **Aplicada só em parte:** bônus do representante. O fato foi registrado, mas o valor não é calculado porque a ata não define a forma.
- **Exigem decisão de Paulo:** o que muda em prazo, equipe ou escopo com o app (235 pontos contra 201; nenhuma comunicação altera prazo ou equipe).
- **Continua crítico:** a API confirmada cobre só criar pedido e consultar status. Produto, preço, estoque, Cliente, CPF, impostos, frete e regras do ERP seguem sem confirmação.

Critério: comunicação mais recente, da instância competente, prevalece sobre a anterior, e o conflito fica registrado. Sem competência ou clareza, não se aplica como regra.

## 2. Classificação das afirmações

| ID | Afirmação | Classificação | Em relação a | Aplicação |
|---|---|---|---|---|
| MUD-01.1 | Comissão do interno acima da meta passa de 5% para 6% a partir de março | **conflitante** | RN-11, PLA (5%) | Aplicada |
| MUD-01.2 | Representantes passam a ter bônus de meta igual ao dos internos | **conflitante** | RN-11, PLA ("4% fixo, sem bônus de meta") | Parcial |
| MUD-01.3 | Desconto sem aprovação sobe para 15% | **conflitante** | RN-04, POL-1 e R7 (12%) | Aplicada; Política a revisar |
| MUD-01.3a | Motivo: alinhar com as campanhas da loja web | **existente** | INT, SQL-LOJA, R7 (Cupons até 15%) | Sem alteração |
| MUD-01.4 | App offline para representantes entra na primeira versão | **conflitante** | R13 ("não entra na v1, decisão atual"), R11 | Aplicada; decisões abertas |
| MUD-02.1 | VendaMax tem API REST, confirmada pelo fornecedor | **complementar** | RF-10, RNF-03, PEND-02 (R3 = Não sei) | Aplicada |
| MUD-02.2 | A API cria pedido e consulta status de faturamento | **complementar** | RF-10; cobre parte do contrato | Aplicada, só para essas operações |
| MUD-02.3 | Limite de 60 requisições por minuto | **novo** | Nenhum requisito anterior | RNF-11, US-061 |
| MUD-02.4 | Sem webhook | **novo** | Nenhum requisito anterior | RF-10, RNF-11, ADR-04 |
| MUD-02.5 | Para saber se foi faturado, será preciso consultar periodicamente | **complementar** | RF-10, US-008; consequência de MUD-02.4 | US-008 |

Nenhuma afirmação foi classificada como **fora_escopo**: todas atingem Comissão, Desconto, canais ou integração.

## 3. Impacto por afirmação

### MUD-01.1. Comissão de 6%

- **Requisitos:** RN-11 alterado, com 5% até fevereiro e 6% a partir de março. RN-14 e RF-16 ganham o primeiro caso real de vigência. Diretoria é a instância competente (POL-5).
- **Backlog:** US-042 (cadastro da alteração), US-043 (exemplo fictício: 4.000 com 5%; 4.200 com 6%), US-046 (paralelo na mesma versão).
- **Documentos:** `02-negocio.md`, `03-tecnico.md` seção 6, `07-rastreabilidade.md`.
- **Atenção:**
  - O ano é inferido: março/2027.
  - Não se sabe se vale pela data do Pedido ou do Faturamento. Mantida PRE-10 (data do Pedido), a confirmar com Renata (PEND-06). Muda o valor de Pedidos que cruzarem a virada.
  - Sob PRE-03, março vem antes da v1: a planilha precisa ser ajustada pelo financeiro, independentemente do sistema.

### MUD-01.2. Bônus de representante

- **Requisitos:** RN-11 alterado; "4% fixo, sem bônus" deixa de valer.
- **Ambiguidade:** "igual" pode significar 6% sobre o excedente, ou 4% mais a diferença do interno (3 pontos, totalizando 7%), entre outras leituras. A ata também não informa vigência; "a partir de março" está escrito só no item 1.
- **Decisão tomada:** não escolher uma leitura, porque afeta valor pago. Representante acima da meta vai a revisão manual em US-043 até PEND-11.
- **Backlog:** US-040, US-043, US-046.
- **Ponto de apoio:** `vendedor.meta_mensal` existe também para representantes no dump. A validade dessas metas para esse uso precisa ser confirmada.

### MUD-01.3. Alçada de 15%

- **Requisitos:** RN-04 (até 15%; acima de 15% até 20%, gerente; acima de 20%, diretoria), RN-05 (faixa da ausência do gerente), RN-06 (PRE-15), RF-24 (10% para 15%).
- **Backlog:** US-021, US-022, US-023, US-024, US-049, US-002 (teste passou de 15% para 20%).
- **Documentos:** `02-negocio.md`, `03-tecnico.md`, `01-diagnostico.md` seção 9, `CONTEXT.md`.
- **Atenção:**
  - **Efeito no Cupom:** R7 dizia "acima de 12%", mas também que o Cupom segue a mesma política. Assumido limiar de 15% (PRE-15). Com o limite atual de Cupom em 15%, a autorização nunca seria acionada: Paulo confirma se o limite sobe.
  - **Política:** POL-1 precisa de revisão formal; a ata não informa data de vigência (CON-10).
  - **ERP:** o VendaMax segue recusando acima de 10%. A ata não resolve a reclamação sozinha; depende de US-002 ou US-049.
  - **Comissão:** a regra de pagar metade acima de 8% não foi alterada. Vendedor pode conceder 15% sem aprovação e receber metade. A ata não indica se é intencional (PEND-01).
  - **Margem:** sem dados nas fontes para estimar o efeito.

### MUD-01.3a. Campanhas da loja

Já levantado. Nota: os Cupons do dump (BLACK15 e PRIMEIRA10) têm validade anterior à data da ata; campanhas atuais não foram informadas.

### MUD-01.4. App offline na v1

- **Requisitos:** novos RF-25 e RNF-12. RF-07 limitado à digitação com internet. RN-10 recebe PRE-14.
- **Backlog:** novo EP-10, com FE-19 e FE-20, histórias US-055 a US-060, 29 pontos preliminares. Prioridade Must, por inferência de "entra na primeira versão".
- **Documentos:** `02-negocio.md` (escopo, conflitos, riscos), `03-tecnico.md` (ADR-05, segurança, testes), PRD, `CONTEXT.md`.
- **Conflitos não resolvidos pela ata:**
  - **CON-08:** nenhuma mudança de prazo, equipe ou escopo. Sob PRE-03, a ata cai no 4º mês de 6 [inferência]. Se nada mudar, os Should são os primeiros ameaçados, incluindo a Comissão e, portanto, as metas M-01 e M-02.
  - **CON-09:** sem internet, não há reserva, crédito ou aprovação. Assumido que o Pedido só é confirmado ao sincronizar, e pode ser recusado.
- **Ainda desconhecido (R13):** frequência sem internet, mínimo offline, aceitação da confirmação posterior. Também não se sabe se a equipe tem competência em app (PEND-10).
- **Decisão tomada:** manter a web responsiva (US-026) para quem tem internet e para internos.

### MUD-02.1 e MUD-02.2. API confirmada

- **Requisitos:** RF-10 e RNF-03 mudam de "não comprovado" para "confirmado para duas operações".
- **Backlog:** US-001 foi redirecionada para provar essas operações e verificar o restante. US-007 e US-008 mantêm o escopo.
- **Atenção:**
  - É confirmação indireta do fornecedor, sem documentação ou homologação.
  - **Não cobre:** Cliente e CPF (US-013), produto, preço e estoque (US-009, US-020, US-035), impostos e frete (US-041), Devolução (US-044). Sem produto e estoque, o CSV das 04:00 não pode ser desligado, o que contraria a ATA e RF-09 (DIV-25).
  - **Não responde R4:** não se sabe se o pedido criado pela API passa pelos triggers de Desconto e crédito. US-002 segue necessária.
  - O assunto do e-mail cita "API de NF-e", mas o texto não descreve emissão de NF-e pela API. NF-e continua no fluxo do VendaMax.

### MUD-02.3. Limite de 60 requisições por minuto

- **Requisitos:** novo RNF-11.
- **Backlog:** nova US-061 (5 pontos), da qual US-007 passa a depender. US-009 ganha critério do limite.
- **Documentos:** `03-tecnico.md` (ADR-04 e cálculos).
- **Análise:**
  - Criar 900 Pedidos/dia no pico consome cerca de 1% de 86.400 requisições/dia. O limite não impede o volume.
  - Rajadas exigem fila: envio ao ERP não pode ser síncrono com a confirmação do usuário.
  - Carga de 12 mil SKUs por item levaria 200 minutos usando todo o limite (se essa operação existir).
- **Em aberto (PEND-14):** limite por chave ou global.

### MUD-02.4 e MUD-02.5. Sem webhook; consulta periódica

- **Requisitos:** RF-10 reescrito; RNF-11 soma consultas e criações.
- **Backlog:** US-008 (consulta só de Pedidos não finalizados), US-034 (atraso na conciliação da reserva), US-045 (status atualizado antes do fechamento), US-061 (prioridade da criação).
- **Análise:** com 50 requisições por minuto para consulta, um ciclo sobre 900 Pedidos pendentes leva 18 minutos, supondo consulta por Pedido.
- **Efeito:** painel (RNF-02) não é afetado para Pedidos do novo sistema, mas o status faturado chega com atraso.
- **Em aberto (PEND-14):** consulta em lote e atraso aceitável.

## 4. Decisões necessárias

| Pendência | Pergunta | Responsável | Prioridade |
|---|---|---|---|
| PEND-12 | Com o app na v1, o que muda: prazo, equipe ou itens cortados? | Paulo | Imediata |
| PEND-11 | Como se calcula o bônus do representante, desde quando e sobre qual meta? | Renata, com diretoria | Antes de março |
| PEND-06 | 6% vale por data do Pedido ou do Faturamento? | Renata | Antes de março |
| PEND-01, CON-10 | Quando vale a alçada de 15%? Quando a Política será revisada? Limite do Cupom sobe? A regra de 8% continua? | Paulo | Alta |
| PEND-02 | Quais outras operações a API tem, e o que acontece com os triggers? | Sérgio, com fornecedor | Imediata |
| PEND-14 | Limite por chave ou global? Há consulta em lote? Qual atraso é aceitável? | Sérgio, com fornecedor | Alta |
| PEND-13 | Regras do app e tecnologia; a confirmação ao sincronizar é aceita? | Aline, com representantes | Antes de construir |

## 5. O que mudou nas entregas

| Entrega | Alterações |
|---|---|
| `01-diagnostico.md` | Versão 3: conclusões; seção 9; DIV-23 a DIV-25; RIS-18 a RIS-23 |
| `02-negocio.md` | Versão 2: RN-04, RN-05, RN-06, RN-10, RN-11, RN-14; RF-07, RF-10, RF-16, RF-24; novo RF-25; escopo; CON-04, CON-07; novos CON-08 a CON-10; PEND-01, PEND-02, PEND-10; novas PEND-11 a PEND-14; PRE-14, PRE-15; riscos |
| `03-tecnico.md` | Versão 2: novos RNF-11, RNF-12; RNF-03; ADR-04, ADR-05; contrato da API com situação; cálculo do limite; regras de Desconto e Comissão; segurança e testes |
| `04-backlog.md` | Versão 2: EP-10, FE-19, FE-20; novas US-055 a US-061; alteradas US-001, 002, 007, 008, 009, 013, 021, 022, 023, 024, 026, 032, 034, 042, 043, 045, 046, 049. De 49 para 56 histórias; de 201 para 235 pontos (Must de 153 para 187) |
| `05-jira.csv`, `06-azure-devops.csv` | Regenerados a partir do mesmo backlog |
| `07-rastreabilidade.md` | Versão 2: fontes MUD, seção 7 e novas pendências |
| `[método]/` | PRD, `feature.json`, `state.json`, `CONTEXT.md`, `ARCHITECTURE.md`, `STACK.md`, `plan-notes.md`, `backlog-source.json` |

Sem alteração: `perguntas.md`, `respostas.md`, `fontes/`. Os números US-050 a US-054 não são usados, porque correspondem a itens cancelados no ponytail gate em `feature.json`. Pontos seguem preliminares.
