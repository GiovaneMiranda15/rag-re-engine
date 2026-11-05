# Avaliação de mudanças

Comunicações analisadas em `mudancas/`: M-01 (e-mail de Suprimentos, 21/10/2026, com recados do Comitê de Contratos) e M-02 (Memorando 2026/14 do Jurídico e da Engenharia Clínica, 03/11/2026). Pessoas citadas por função.

## Resumo

| ID | Afirmação | Classificação | Decisão | Alterou as entregas? |
|---|---|---|---|---|
| M-01.1 | Incorporação do Hospital Aurora Serra em janeiro de 2027, com dois contratos de manutenção próprios a entrar no sistema | **novo** | Aplicada, com dados pendentes | Sim: RF-37, US-37, DP-20, RIS-15 |
| M-01.2 | Contratos com valor global acima de R$ 250 mil continuam aprovados pela Diretora Geral | **existente** | Nada a fazer | Não |
| M-01.3 | Farmácia pede controle de validade de lotes de medicamentos no estoque | **fora_escopo** | Não aplicada; devolver à Farmácia | Só o registro |
| M-02.1 | Parecer jurídico obrigatório só acima de R$ 200.000,00 de valor global | **conflitante** | **Não aplicada.** RN-07 segue em R$ 30 mil até decisão da Diretoria | Só a sinalização: DP-19 |
| M-02.2 | Soma das glosas limitada a 10% do valor mensal por competência | **complementar** | Aplicada, como provisória | Sim: RN-14, US-14, US-30, testes |

## M-01.1: Hospital Aurora Serra (novo)

**Por que é novo:** nenhuma fonte cita essa unidade. O escopo e a POL-SUP-004, item 1.1, falam em quatro unidades.

**Impacto nos requisitos**

- Novo RF-37: cadastrar a nova unidade e carregar seus dois contratos.
- RF-10 e RF-31 passam a incluir a unidade. O sistema já trata unidade como cadastro, então o modelo não precisa mudar.
- DP-02 ganha nova pergunta: em que momento a nova unidade entra.
- Nova DP-20, porque não se sabe:
  - os dados dos dois contratos (números, fornecedores, vigência, valor, índice, SLA) nem onde estão registrados;
  - quantos equipamentos a unidade tem, se têm patrimônio, e quais sistemas usa;
  - se a Política passa a valer para ela, e a partir de quando.

**Impacto no backlog:** nova US-37 (prioridade 1, depende de US-01, US-02 e US-03). No `feature.json` ela é a ISSUE-40, porque as ISSUE-37 a 39 já foram usadas pelas candidatas canceladas.

**Impacto nos documentos:** `01` (RIS-15), `02` (escopo, perfis, DP, RF, ação 13, riscos), `03` (unidades, carga, capacidade), `04` a `07`.

**Atenção**

- A incorporação ocorre **antes** da entrada em operação (30/06/2027). Entre janeiro e a entrada, os dois contratos ficam nos controles atuais, e a planilha precisa recebê-los.
- Os volumes de `RNF-05` e a linha de base dos indicadores eram de quatro unidades, e o prazo não foi reavaliado. Ainda não dá para medir o efeito sobre 30/06/2027.
- A informação veio por e-mail, em nome do Comitê. Falta confirmação da Diretora Geral sobre a inclusão na primeira fase. Apliquei porque o texto é claro ("precisarão entrar"); o item é fácil de reverter.

## M-01.2: alçada acima de R$ 250 mil (existente)

Coincide com RN-01 e RN-02 (POL, itens 2 e 2.2; resposta 3). A palavra "continuam" também indica que não há mudança.

**Impacto:** nenhum em requisitos, backlog ou documentos. O achado de `01-diagnostico.md`, seção 4.2, permanece: o CT-2025-0064, de R$ 528.000,00, tem a Gerente como aprovadora no ERP.

## M-01.3: lotes de medicamentos (fora do escopo)

O escopo exclui medicamentos, e a POL-SUP-004, item 1.2, os remete à POL-FAR-002.

**Impacto:** nenhum requisito ou história criados. **Encaminhamento:** informar a Farmácia e, se houver interesse, tratar como demanda separada junto à Diretora Geral.

## M-02.1: parecer acima de R$ 200 mil (conflitante)

**Conflitos**

| Fonte | Limite |
|---|---|
| POL-SUP-004 rev. 3, item 4.5, aprovada pela Diretoria | R$ 30.000,00 |
| Resposta 4, do próprio Jurídico: "Vale a Política" | R$ 30.000,00 |
| Fluxo de junho de 2025, que já deveria se adequar | R$ 100.000,00 |
| Memorando 2026/14 | R$ 200.000,00 |

**Por que não apliquei:** o memorando parte de duas áreas, e não mostra revisão da Política nem aprovação da Diretoria. Mudar um controle desse tipo por memorando repetiria o problema que o projeto quer resolver: regra em uso diferente da regra aprovada. Também não sei se o Diretor Financeiro e a Diretora Geral conhecem a mudança. O texto "daqui em diante" pode indicar intenção real; por isso é uma decisão a tomar, não um erro a descartar.

**Decisão necessária (DP-19, Diretora Geral e Diretor Financeiro, ouvido o Jurídico):** o limite muda? Se mudar, com qual revisão da Política, em que data, e como ficam aditivo e renovação (DP-06)?

**Efeito se a mudança for aprovada**

| Contrato | Global (R$) | Parecer a R$ 30 mil | Parecer a R$ 200 mil |
|---|---|---|---|
| CT-2026-0021 | 58.800,00 | Sim | **Não** |
| CT-2025-0102 | 163.200,00 | Sim | **Não** |
| Outros seis | 269.280,00 ou mais | Sim | Sim |

- Reduz a fila do Jurídico, hoje 23 dos 38 dias do ciclo (a redução não é mensurável sem a capacidade, DP-06). Em troca, contratos de até R$ 200 mil ficam sem revisão jurídica.
- **Sistema:** só muda um parâmetro com vigência (US-14), sem desenvolvimento. Mudariam RN-07, critérios de US-07, US-08, US-17 e US-36, e os testes de limite.
- **Enquanto isso, para os contratos que chegarem agora:** recomendo seguir a Política. Quem dispensar o parecer antes da decisão assume um desvio formal.

**Impacto aplicado:** RN-07 sinalizada; DP-19 ligada a US-07, US-08, US-14, US-17 e US-36; RIS-11 atualizado.

## M-02.2: teto de 10% para glosas (complementar)

**Por que é complementar:** a POL 5.3 define 2% por evento e não fala em limite. O teto acrescenta uma regra sem alterar o percentual. Ele só tem efeito a partir de seis eventos na competência, pois cinco eventos dão exatamente 10%.

**Regra aplicada (provisória):** por contrato e competência, glosa aplicável = menor valor entre a soma das glosas e 10% do valor mensal.

| Exemplo | Valor mensal | Eventos | Soma a 2% | Glosa aplicável |
|---|---|---|---|---|
| CT-2024-0117 | R$ 11.040,00 | 1 | R$ 220,80 | R$ 220,80 |
| CT-2024-0117 | R$ 11.040,00 | 5 | R$ 1.104,00 | R$ 1.104,00 |
| CT-2024-0117 | R$ 11.040,00 | 6 | R$ 1.324,80 | **R$ 1.104,00** |
| CT-2025-0031 | USD 9.800,00 | 6 | USD 1.176,00 | **USD 980,00** |

**Ressalvas**

- O memorando não diz se os contratos assinados preveem glosa diferente, e o Diretor Financeiro não o assina. Isso entra em DP-13, junto da definição de evento, ainda sem resposta.
- O teto reduz a pressão sobre fornecedor com falhas repetidas. Por isso o sistema mostra a soma calculada e o valor limitado, para que o excesso continue visível.
- A vigência "a partir de quando" não foi informada, e a Política não foi revista. Convém formalizar.

**Impacto aplicado:** RN-14, parâmetro de 10%, entidade Glosa, US-14, US-30, casos de teste em `03-tecnico.md`.

## O que mudou nas entregas

| Documento | Alteração |
|---|---|
| `01-diagnostico.md` | Seção de mudanças; RIS-15; RIS-11 e DIV-04 atualizados |
| `02-negocio.md` | Unidade nova; RN-07 e RN-14; RF-37; DP-02, DP-19, DP-20; ação 13; risco; histórico |
| `03-tecnico.md` | Unidades, parâmetros, glosa, carga, capacidade e testes |
| `04-backlog.md` | US-37 nova; US-14, US-17 e US-30 alteradas; DP-19 em US-07, US-08, US-14, US-17 e US-36 |
| `05-jira.csv`, `06-azure-devops.csv` | Mesmas alterações; agora com 37 histórias |
| `07-rastreabilidade.md` | RF-37, US-37, RIS-15 e seção de mudanças |
| `[método]/` | PRD, `feature.json` (ISSUE-40), `state.json`, CONTEXT e ARCHITECTURE |

## Próximos passos

| # | Ação | Responsável |
|---|---|---|
| 1 | Decidir o limite do parecer (DP-19) e, se mudar, revisar a Política | Diretora Geral, Diretor Financeiro |
| 2 | Confirmar a inclusão do Hospital Aurora Serra na primeira fase e fornecer os dados dos contratos (DP-02, DP-20) | Diretora Geral, Suprimentos |
| 3 | Confirmar o teto de glosa com o Financeiro e com os contratos assinados (DP-13) | Diretor Financeiro, Jurídico |
| 4 | Informar a Farmácia de que o pedido está fora do escopo | Suprimentos |
