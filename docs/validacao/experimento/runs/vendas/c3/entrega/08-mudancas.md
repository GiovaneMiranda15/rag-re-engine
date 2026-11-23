# Avaliação de mudanças

- **Projeto:** Sistema de Vendas Unificado
- **Comunicações:** `mudancas/M-01-ata-diretoria.md` (ata de 20/01/2027) e `mudancas/M-02-email-ti.md` (e-mail sem data)
- **Baseline:** nenhuma. Os dois arquivos dizem "após a 1ª baseline", mas não houve validação humana para criá-la. Por isso as mudanças foram aplicadas direto, com CR e histórico por requisito.
- **Decisão sem revisor:** a ata foi tratada como aprovação da diretoria. Tudo aqui ainda precisa de conferência humana.

## Resumo

Das 9 afirmações, 4 são conflitantes, 1 é existente, 2 são novas, 2 são complementares e nenhuma é fora de escopo. Três pontos precisam de decisão:

1. **App offline na v1 (CR-004).** Foi aplicado por decisão da diretoria, mas prazo e equipe não mudaram, e as regras offline não existem. O plano de 6 meses não está sustentado.
2. **Bônus do representante (CR-002).** A decisão foi registrada, mas o valor é ambíguo: 6% ou 7% sobre o excedente. Nenhum número foi adotado.
3. **Desconto de 15% e triggers do ERP (CR-003).** Se o trigger de 10% valer para a API, descontos de 10% a 15%, agora sem aprovação, serão recusados na entrada do ERP.

## Classificação por afirmação

| # | Fonte | Afirmação | Classe | Em relação a | Justificativa | Aplicado? |
|---|---|---|---|---|---|---|
| 1 | M-01 item 1 | Excedente do interno passa de 5% para 6% a partir de março | **conflitante** | RN-002 | Muda o percentual da planilha, confirmado em Q-004 | Sim (CR-001) |
| 2 | M-01 item 2 | Representante passa a ter bônus de meta igual ao do interno | **conflitante** | RN-002 | A regra dizia "4% fixo, sem bônus" | Parcial (CR-002) |
| 3 | M-01 item 3 | Desconto sem aprovação sobe para 15% | **conflitante** | RN-001, RF-003, RN-009, política | Substitui os 12% da política, confirmados em Q-001 | Sim (CR-003) |
| 4 | M-01 item 3 | Campanhas da loja web chegam a 15% (motivo citado) | **existente** | DIV-001, EL-020 | Já consta em `[sql: SIS-03/schema.sql:cupons]` | Sem mudança |
| 5 | M-01 item 4 | App offline para representantes entra na v1 | **conflitante** | RF-009, Q-011 | O PO o tinha excluído da v1 | Sim, com conflito aberto (CR-004) |
| 6 | M-02 | VendaMax tem API REST para criar pedido e consultar faturamento | **complementar** | RF-007, RIS-002, Q-023 | Detalha a decisão por API e responde parte de Q-023 | Sim (CR-005) |
| 7 | M-02 | Limite de 60 requisições por minuto | **novo** | RNF-007 (criado) | Nenhuma restrição equivalente | Sim (CR-005) |
| 8 | M-02 | Não há webhook | **novo** | RF-015 (criado) | Nenhum item tratava o retorno por evento | Sim (CR-005) |
| 9 | M-02 | Faturamento só se conhece por consulta periódica | **complementar** | RF-007, RF-015 | Define como funciona o retorno da integração | Sim (CR-005) |

## Impacto por mudança

O grafo (`[método] impacto`) devolve uma lista ampla de candidatos, inflada por itens ligados ao mesmo sistema. Os afetados foram definidos pela leitura dos requisitos e das histórias do tema, sem revisar cada candidato. Portanto, a coluna de candidatos só indica o alcance.

| CR | Status | Complexidade | Candidatos no grafo | Afetados de fato |
|---|---|---|---|---|
| CR-001 | aplicada | moderada | 34 | 5 |
| CR-002 | aprovada, valor pendente | complexa | 58 | 6 |
| CR-003 | aplicada | complexa | 44 | 8 |
| CR-004 | aplicada, com conflito aberto | complexa | 29 | 10 |
| CR-005 | aplicada | complexa | 60 | 14 |

### CR-001: comissão de 6%

- **Requisitos:** RN-002 v3 (antes: 5% sobre o excedente; agora: 5% até fevereiro de 2027 e 6% desde março). RF-010 ganhou data de vigência.
- **Backlog:** US-019 e US-024 em `revisar`, com critérios novos. Exemplo fictício: meta de 100.000 e base de 120.000 pagam 4.000 em fevereiro e 4.200 em março.
- **Documentos:** 02, 03, 04, 05, 06 e 07.
- **Pontos de atenção:** o ano de 2027 é dedução pela data da ata. "A partir de março" pode ser venda ou pagamento (Q-030). Até o sistema entrar, o Financeiro precisa atualizar a planilha (DIV-017).

### CR-002: bônus do representante

- **Requisitos:** RN-002 perdeu "fixo, sem bônus" e agora diz 4% até a meta. RN-015 foi criada, sem percentual.
- **Backlog:** US-030 criada e bloqueada por Q-030. US-019 em `revisar`.
- **Valor em aberto**, em exemplo fictício com meta de 100.000 e base de 120.000:

| Leitura de "igual" | Excedente | Total | Hoje |
|---|---|---|---|
| Mesmo percentual do interno (6%) | 1.200 | 5.200 | 4.800 |
| Mesmo acréscimo do interno (3 pontos, 7%) | 1.400 | 5.400 | 4.800 |

- **Pontos de atenção:** a ata não diz se vale desde março. Os contratos de representantes não foram vistos (RIS-013, Q-028). O custo não foi estimado, por falta de dados.

### CR-003: desconto sem aprovação de 15%

- **Requisitos:** RN-001 v3 (até 15% sem aprovação; acima de 15% até 20% gerente; acima de 20% diretoria) e RF-003 ajustado.
- **Dedução a confirmar (Q-031):** a gerente passa a atuar acima de 15%, e a autorização de cupom (RN-009) também sobe para acima de 15%, pois Q-001 disse que cupons seguem a mesma política. Assim, os cupons atuais de até 15% deixam de precisar de autorização.
- **Backlog:** US-010, US-011 e US-014 em `revisar`. US-012 não muda.
- **Riscos:** RIS-001 piora, como no resumo. Até a API entrar, o CSV continua rejeitando esses pedidos, então GAR-005 segue.
- **Regra que não mudou:** a comissão continua pela metade acima de 8% (RN-011). Mais pedidos podem cair nessa faixa sem aprovação. Confirmar se é a intenção (Q-031).
- **Documentos:** além das entregas, a política comercial precisa ser revisada pela empresa (DIV-017). As fontes não foram alteradas.

### CR-004: app offline na v1

- **Requisitos:** RF-009 passou de Won't para Must. RF-011 (web responsiva) segue até Q-032.
- **Backlog:** novo EP-009, com FT-013 e US-031 a US-033, todas bloqueadas por Q-032. US-006, US-015 e US-016 em `revisar`.
- **Conflitos com regras confirmadas (DIV-015):**

| Regra | Por que colide sem internet |
|---|---|
| RN-006 e RF-006: reserva e saldo único | Dois aparelhos podem vender a mesma unidade; afeta a meta de menos de 5 cancelamentos/mês |
| RN-001 e RF-003: alçada | Desconto acima de 15% não tem como ser aprovado na hora |
| RN-004: crédito | O limite pode estar defasado no aparelho |
| RN-008: tabela única | O preço pode estar defasado no aparelho |
| RNF-005: painel | O pedido offline só aparece depois da sincronização |

- **Plano:** o Must passa de 5 para 6 itens, com 4 devs e 1 PO, enquanto comissão segue fora do Must (DIV-014). RIS-004 sobe para crítica. As histórias não têm estimativa, então o impacto em tempo **não foi calculado**.
- **Recomendação:** antes de iniciar, a diretoria e o PO devem escolher entre tirar algo do escopo, ampliar prazo ou aumentar a equipe. Se isso não acontecer, o item deve voltar à diretoria como risco de prazo.

### CR-005: API do VendaMax

- **Requisitos:** RF-007 v3; novos RF-015 (consulta periódica) e RNF-007 (60 req/min); RNF-006 ganhou critério de limite; RNF-005 ficou em risco.
- **Backlog:** novas US-028 e US-029. US-008, US-017, US-018 e US-027 em `revisar`. US-018 segue bloqueada pelos triggers.
- **Achados:** RIS-002 caiu de crítica para alta. Novos RIS-015 e RIS-016. Q-023 segue aberta, com resposta parcial.
- **Capacidade (estimativa, em `03-tecnico.md`, seção 8):** criar 900 pedidos/dia cabe no limite. O problema é a consulta: um ciclo de 5 minutos cobre cerca de 290 pedidos, e 900 em aberto levariam cerca de 16 minutos. O painel só fica seguro se venda for pedido criado ou se houver consulta em lote (Q-027, Q-033).
- **O que o e-mail não confirma:** apesar do assunto "API de NF-e", ele não cita emissão de nota por API. Também não cita triggers, CPF, cliente, produto, preço, estoque, imposto, frete, devolução, custo e prazo. Portanto, "sem troca de arquivos" (RF-007) ainda não está garantido, e a comissão continua sem origem de dados (RIS-008).

## Novas perguntas

| ID | Para | Assunto |
|---|---|---|
| Q-030 | Diretoria e Coordenadora Financeira | Valor e início do bônus; significado de "a partir de março" |
| Q-031 | Diretoria | Vigência dos 15%, faixa da gerente, cupom, redutor de 8%, revisão da política |
| Q-032 | Diretoria e PO | O que sai ou muda para caber o app; regras offline; futuro da web responsiva |
| Q-033 | Gerente de TI e fornecedor | Alcance do limite, consulta em lote, cobertura da API, erro ao exceder |

## O que mudou nas entregas

| Entrega | Mudança |
|---|---|
| `01-diagnostico.md` | Nova seção 12, com achados e severidades |
| `02-negocio.md` | Bloqueios, escopo, fluxo com 15%, regras, premissas, riscos e pendências |
| `03-tecnico.md` | Requisitos, integrações, triggers, dimensionamento e pendências |
| `04-backlog.md` | 9 épicos, 13 features e 33 histórias: 6 novas e 12 em `revisar` |
| `05-jira.csv`, `06-azure-devops.csv` | Regerados por completo; `[método]entregaveis/backlog/` também tem `*-delta.csv`, só com novos e `revisar`, para conferência (o delta do Azure não repete os pais de cada item) |
| `07-rastreabilidade.md` | Novos requisitos, histórias, achados e CRs |

Requisitos alterados: RN-001, RN-002, RN-009, RF-003, RF-007, RF-009, RF-010, RF-011, RNF-005 e RNF-006. Criados: RN-015, RF-015 e RNF-007. Nada foi marcado como obsoleto. Os requisitos ficaram `confirmado`, não `alterado`, porque não há baseline.

## Limitações

- Ninguém validou as CRs. As fontes em `fontes/` e `mudancas/` não foram alteradas.
- O motor rodou em baseline (`adaptive_rag` indicado, mas não implementado), com índice lexical. A classificação veio da leitura do modelo e das comunicações.
- O e-mail não tem data, e a ata é de data posterior aos demais materiais; a ordem entre os dois não afeta as decisões acima.
- Valores em reais são exemplos fictícios, e o dimensionamento usa premissas não confirmadas.
