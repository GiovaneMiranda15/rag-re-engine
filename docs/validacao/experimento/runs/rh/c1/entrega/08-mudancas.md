# Avaliação de mudanças — Projeto Admissão Única

Comunicações avaliadas: `M-01` (ata do comitê, 28/10/2026) e `M-02` (e-mail de Marina Quintela, 30/10/2026). Cada comunicação foi dividida em afirmações, pois uma mesma mensagem traz classificações diferentes.

## 1. Resultado

| Afirmação | Autor | Resumo | Classificação | Aplicada? |
|---|---|---|---|---|
| M-01.1 | Beatriz Lobo | Nenhum farmacêutico, inclusive RT, inicia sem certidão com CRF ativo; protocolo não basta | **existente** | Nada a mudar na regra |
| M-01.2 | Sérgio Antunes | Experiência padrão de 45+45 a partir de 01/12/2026, com o sistema já nascendo assim | **conflitante** | **Não.** Vale 30+60 até decisão formal |
| M-01.3 | Sérgio Antunes | Incluir cálculo de rescisão e homologação de desligamentos | **fora_escopo** | **Não** |
| M-02.1 | Marina Quintela | Portaria: comprovante de vacinação para quem vai aplicar injetáveis em SP, a partir de 01/02/2027 | **novo** | Sim, com pendências |
| M-02.2 | Marina Quintela | ASO e prazos atuais continuam valendo | **existente** | Nada a mudar na regra |
| M-02.3 | Marina Quintela | Adesão ao programa Acolher a partir do 1º tri/2027 | **novo** | Sim, com pendências |
| M-02.4 | Marina Quintela | Aceitar CRNM como identificação e controlar sua validade | **complementar** | Sim, com pendências |

**O que pede atenção de Helena:**

1. **Decidir o conflito da experiência antes de 01/12/2026** (PD-25).
2. **Responder a Sérgio** que rescisão e homologação seguem fora, ou alterar formalmente o escopo (PD-26).
3. **Garantir controle provisório para fevereiro de 2027**, pois o novo fluxo não tem data (PD-03, US-062).

## 2. Avaliação por afirmação

### M-01.1 — CRF: existente

- **Relação:** repete RN-08 (RH-012 §7, respostas 7 e 8).
- **Requisitos, backlog e documentos:** sem mudança de regra. As histórias US-009 e US-029 continuam válidas.
- **Ganho paralelo:** a ata informa a área de Beatriz, Assuntos Regulatórios, que era uma lacuna. O dado foi atualizado em `01` e `02`.

### M-01.2 — Experiência 45+45: conflitante

**Conflita com:** RN-09; RH-012 §4.1 (30+60); resposta 4 de Marina ("Vale a RH-012: 30+60"); resposta 1 de Helena ("nas regras já definidas, vale a RH-012").

**Por que não foi aplicada:**

- O registro é um **informe** de Operações, não uma decisão. A ata não traz deliberação, aprovação nem revisão da RH-012.
- Helena decide o texto final da RH-012, e Marina confirmou 30+60. As duas estavam presentes, mas a ata não registra a posição delas. O silêncio não foi interpretado como concordância.
- O pedido envolve "toda a rede", e nenhuma fonte mostra Operações como decisora desta regra.
- Não há árbitro definido para discordâncias entre áreas (PD-01).

**Encaminhamento:** PD-25, com Helena e Marina, antes de 01/12/2026.

| Cenário | Requisitos | Backlog | Documentos |
|---|---|---|---|
| **Mantém 30+60** (situação atual) | RN-09 sem mudança | US-012 e US-046 seguem | Comunicar Operações. R-20 continua até a orientação às lojas |
| **Adota 45+45** | RN-09 muda, com revisão prévia da RH-012 pelos aprovadores | Sem história nova: US-003 já prevê troca de parâmetro. US-012 muda, pois a transição fica desnecessária ou menor; US-046 muda os marcos | `01`, `02`, `03`, CSVs e o novo Manual. O padrão de 45 no FolhaCerta deixaria de ser divergência |

**Observações:**

- Os dois modelos somam 90 dias. O modelo 45+45 é o que a prática já usa, então o conflito é sobre a norma e não sobre uma nova operação.
- Passar a usar 45+45 sem rever a RH-012 oficializaria um desvio (R-20).
- A estrutura parametrizada torna o custo técnico baixo nos dois cenários. O problema é de governança.

**Alterações feitas:** PD-25 criada; dependência adicionada a US-012 e US-046; textos de US-012, US-046 e da história de envio ao FolhaCerta agora dizem "regra vigente, hoje 30"; D-03 passa a "Contestada"; R-20 criado.

### M-01.3 — Rescisão e homologação: fora_escopo

**Motivo:** o escopo diz que o desligamento não faz parte da iniciativa, e Helena reafirmou na resposta 4 que rescisão e desligamento estão fora (RN-21).

- **Requisitos e backlog:** sem mudança. US-047 continua terminando no encaminhamento ao DP.
- **Se Helena decidir incluir:** seria uma mudança de escopo, com novo levantamento (regras, cálculo, relação com a folha), novas áreas e efeito em prazo e orçamento, que já são desconhecidos. Nada foi estimado.
- **Encaminhamento:** PD-26, para Helena dar a resposta formal a Sérgio.

### M-02.1 — Vacinação para injetáveis em SP: novo

**Motivo:** nenhuma fonte ou resposta tratava de injetáveis ou vacinação. É uma condição adicional, com vigência própria, que não altera as demais.

| Área | Impacto |
|---|---|
| **Requisitos** | Novos RN-22 e RF-23. Linha nova na tabela "pode começar" (`02`, seção 6) |
| **Backlog** | Nova feature F-20 (E-05), com US-061 a US-064 |
| **Documentos** | `01` (R-21, R-22), `02`, `03` (entidade, cálculo, matriz de acesso), `04` a `07` |

**Decisões registradas:**

- O comprovante é tratado como **dado de saúde**, sujeito a RN-15: fica no ambiente do SESMT e o fluxo guarda só a condição. É uma leitura deste levantamento, a ser confirmada por Paula.
- A regra usa **vigência**: inícios anteriores a 01/02/2027 não são alcançados.
- Foi criado um **controle provisório** (US-062), pois a data do novo fluxo é desconhecida e a portaria tem data certa.

**Lacunas (PD-27):**

- O texto da portaria não está nas fontes. O conteúdo vem do e-mail de Marina e não foi conferido.
- Nenhum sistema identifica quem aplica injetáveis, e não se sabe se isso é cargo ou função.
- Não se sabe se a exigência alcança quem já trabalha e passará a aplicar, nem se a pessoa pode iniciar sem aplicar.
- Paula e Beatriz não constam como destinatárias do e-mail e precisam ser envolvidas (R-22).

### M-02.2 — ASO e prazos atuais: existente

- **Relação:** confirma RN-06, RN-07 e demais prazos. O comprovante é somado ao ASO, sem substituí-lo.
- **Impacto:** sem mudança de regra. Foi incluído um critério de aceite em US-064 para deixar isso claro.

### M-02.3 — Programa Acolher: novo

**Motivo:** nenhuma fonte citava esse programa. É um novo público, com data própria.

- **Requisitos e backlog:** RN-23 e US-065 (definição das regras e do procedimento provisório).
- **Atenção:** a informação veio do Jurídico, com cópia a Helena, que decide escopo e prioridades. A prioridade 1 de US-065 é uma proposta para garantir a decisão a tempo. A entrada no fluxo depende de Helena.
- **Abrangência:** não se sabe se o programa alcança só CLT de loja, primeira fase do projeto, ou também CD e escritório (PD-28).

### M-02.4 — CRNM: complementar

**Motivo:** completa algo já levantado: a coleta de documentos (RF-04) e o acompanhamento de prazos. Acrescenta um tipo de documento e o controle de validade.

| Área | Impacto |
|---|---|
| **Requisitos** | RN-23, RF-24; complementa RF-04 |
| **Backlog** | Nova feature F-21 (E-04), com US-066 e US-067 |
| **Documentos** | `01` (R-23), `02`, `03` (entidade, cálculo, cadastro, matriz), `04` a `07` |

**Pontos a verificar (PD-28):**

- **Identificador:** RN-20 adotou CPF como chave, e o CPF é obrigatório nos dumps. O e-mail não diz se todas as pessoas do programa terão CPF ao chegar à admissão.
- **Cadastro:** o FolhaCerta tem só `rg` no dump. Registrar a CRNM depende de PD-19.
- **Vencimento:** o e-mail manda controlar, mas não diz o efeito. O fluxo só avisa, sem assumir bloqueio.
- **Duração:** a validade pode vencer depois da experiência, quando o projeto termina.
- **Privacidade:** a condição migratória fica com acesso restrito e não serve de critério de decisão (Paula).

## 3. O que mudou nas entregas

| Arquivo | Mudança |
|---|---|
| `01-diagnostico.md` | Versão 3. D-03 "Contestada"; área de Beatriz; riscos R-20 a R-23; nota sobre as comunicações |
| `02-negocio.md` | RN-22, RN-23, RF-23, RF-24; PD-25 a PD-28; PD-04 encerrada; condições de início; abrangência; validação por área |
| `03-tecnico.md` | Entidades, cálculos, identificadores, cadastro e matriz de acesso para vacinação e CRNM; nota de conflito na experiência |
| `04-backlog.md` | 67 histórias e 21 features; US-061 a US-067; F-20 e F-21; dependências e textos de US-001, US-012, US-046 e da história de envio ao FolhaCerta |
| `05-jira.csv`, `06-azure-devops.csv` | Mesmas alterações do backlog, com contagem e títulos conferidos entre os três arquivos |
| `07-rastreabilidade.md` | Novos requisitos, riscos e pendências; seção 5, de comunicações para requisitos |

**PD-04 encerrada:** a ata de 28/10 registra só informes, sem decisões. Ela não traz, porém, nenhuma resposta às demais pendências.

**Não alterado:** RN-09 (segue 30+60), RN-21 (rescisão e desligamento fora), RN-08, RN-06 e RN-07. `perguntas.md` e `respostas.md` ficam como registro histórico.

**Limite:** não houve importação real dos CSVs no Jira nem no Azure DevOps.
