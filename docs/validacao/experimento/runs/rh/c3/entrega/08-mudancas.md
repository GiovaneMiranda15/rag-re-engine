# Avaliação de mudanças: Projeto Admissão Única

**Comunicações avaliadas:** M-01, ata do Comitê de 28/10/2026; M-02, e-mail de Marina Quintela de 30/10/2026. **Baseline de referência:** B-001, foto de trabalho sem validação das áreas.

## 1. Resumo

| Classe | Afirmações |
|---|---|
| existente | 2 |
| conflitante | 1 |
| fora_escopo | 1 |
| novo | 4 |
| complementar | 1 |

- **Não aplicado, precisa de decisão:** experiência de 45+45 (CR-001). O valor de 30+60 continua no modelo, em conflito. Há urgência, porque a data anunciada é 01/12/2026.
- **Não aplicado, fora do escopo:** rescisão e homologação de desligamentos.
- **Aplicado:** comprovante de vacinação da Portaria CVS-SP 88/2026 (CR-002) e CRNM do programa Acolher (CR-003). Vieram do Jurídico, mas não foram validados pelas áreas e têm detalhes em aberto.

## 2. Avaliação por afirmação

| # | Afirmação | Fonte | Classe | Em relação a | Justificativa | Decisão |
|---|---|---|---|---|---|---|
| A1 | Nenhum farmacêutico, inclusive RT, inicia sem certidão de regularidade com CRF ativo; protocolo não basta | M-01, item 1 | **existente** | RN-003, Q-006 | Mesmo conteúdo da RH-012 §7 e da resposta de Beatriz Lobo | Fonte acrescentada, sem nova versão |
| A2 | Beatriz Lobo é de Assuntos Regulatórios | M-01, presentes | **complementar** | `02-negocio.md`, seção 3 | Preenche uma lacuna, sem contradizer nada | Aplicado |
| A3 | A partir de 01/12/2026, a experiência padrão de toda a rede será de 45+45, e o sistema deve nascer assim | M-01, item 2 | **conflitante** | RN-001, DIV-003 | Marina Quintela confirmou que vale a RH-012, 30+60 (Q-004), e não há decisão registrada que mude isso | Não sobrescrito; CR-001 aberto |
| A4 | Incluir cálculo de rescisão e homologação de desligamentos | M-01, item 3 | **fora_escopo** | `escopo.md`, Q-004, RF-009 | O escopo exclui desligamento, e o Jurídico confirmou | Registrado em `.re/escopo.md`; Q-036 |
| A5 | A partir de 01/02/2027, quem vai aplicar injetáveis em lojas de SP apresenta, junto com o ASO, comprovante de vacinação contra hepatite B e tétano antes do início | M-02 | **novo** | RN-016 (criado), RF-012 | Nenhum requisito tratava disso | Aplicado; CR-002 |
| A6 | O ASO e os prazos atuais continuam valendo | M-02 | **existente** | RN-002 | A Portaria acrescenta um requisito e não muda os 30 dias | Fonte acrescentada, sem nova versão |
| A7 | A Rede vai aderir ao programa Acolher a partir do 1º trimestre de 2027 | M-02 | **novo** | RF-019, RIS-018 | Fato novo. A abrangência não foi informada | Aplicado como contexto; Q-034 |
| A8 | Essas admissões usam a CRNM como identificação, e o processo precisa aceitá-la | M-02 | **novo** | RF-019 (criado), RF-003, DIV-016 | Lista de documentos e sistemas não preveem a CRNM | Aplicado; CR-003 |
| A9 | O processo precisa controlar a validade da CRNM | M-02 | **novo** | RF-020 (criado) | Sem campo de validade nas fontes | Aplicado; CR-003 |

### Por que A3 não foi aplicada

- A ata registra um **informe e um pedido** de Sérgio Antunes (Operações). Não registra decisão do Comitê.
- A regra tem decisora: Marina Quintela respondeu 30+60 na Q-004, e Helena Vasconcelos decide o texto da RH-012 (Q-002). Ambas estavam presentes, mas a ata não traz a posição delas.
- O e-mail de Marina, dois dias depois, não trata de experiência. "Prazos atuais" está no contexto do ASO, portanto **não foi lido** como confirmação nem como rejeição do 45+45.

## 3. Impacto

| # | Requisitos | Backlog | Documentos |
|---|---|---|---|
| A1 | RN-003: nova fonte | Nenhum | `07-rastreabilidade.md` |
| A2 | Nenhum | Nenhum | `01-diagnostico.md`, `02-negocio.md` |
| A3 | RN-001 passa a `conflito`; RN-017 criado em `conflito`; RF-009 e RF-002 indiretamente | US-015 e US-020 em `revisar`; critérios **não** alterados | `01` (DIV-003 reaberto), `02` (regra saiu do corpo), `03` (regra e folha), `04`, `05`, `06`, `07` |
| A4 | Nenhum; RF-009 já exclui rescisão | Nenhum; US-015 já cobre | `02`, `.re/escopo.md` |
| A5 | RN-016 criado; RF-012 v2 `alterado`; RN-014 v2 (hipótese); RN-009 ganha uma condição conhecida | US-033 criada; US-002 em `revisar`, com novo critério | `01`, `02`, `03`, `04`, `05`, `06`, `07` |
| A6 | RN-002: nova fonte | Nenhum; US-033 traz critério de não regressão | `07` |
| A7 | Contexto de RF-019 | Nenhum diretamente | `01` (RIS-018), `02` |
| A8 | RF-019 criado | US-034 criada; US-021 em `revisar`, por causa do CPF | `01`, `02`, `03` (de-para e dados), `04`, `05`, `06`, `07` |
| A9 | RF-020 criado | US-035 criada | `02`, `03`, `04`, `05`, `06`, `07` |

**Análise pelo grafo** (`recop.py impacto`): os candidatos foram lidos um a um, e o grafo aponta possibilidades, não certezas.

| CR | Partida | Prof. | Candidatos | Afetados de fato | Candidatos descartados |
|---|---|---|---|---|---|
| CR-001 | RN-001 | 3 | 25 | 7 | RF-007, US-013, US-014, US-019, US-021, US-022: ligados só pela mesma feature ou pelo mesmo épico |
| CR-002 | RF-012 | 2 | 23 | 6 | US-008, US-009, US-010: regras de ASO e CRF não mudam. US-011: a folha não tem esse dado |
| CR-003 | RF-003 | 2 | 11 | 7 | US-016: a US-034 cobre a CRNM. US-017, US-018: conferência e prazo funcionam igual |

## 4. Pedidos de mudança

### CR-001, experiência de 45+45: **proposta, não aplicada**

- **Mudança pedida:** RN-001 de 30+60 para 45+45, a partir de 01/12/2026.
- **Se for aceita:** é preciso alterar a RH-012. O padrão atual da FolhaCerta passa a coincidir. Precisa haver regra por data de início, já que contratos anteriores podem seguir outro prazo. US-015 e US-020 mudam.
- **Se for recusada:** Sérgio Antunes precisa avisar a rede. Permanece a alteração necessária na folha.
- **Risco imediato:** lojas podem aplicar 45+45 em 01/12/2026 sem decisão.
- **Recomendação:** Marina Quintela e Helena Vasconcelos decidem antes de 01/12/2026 (Q-035). Até lá, 30+60 segue como regra do modelo e nenhuma história implementa valor fixo.

### CR-002, Portaria de vacinação: **aplicada, sem validação das áreas**

- **Pontos em aberto (Q-033):**
  - o texto da Portaria não foi recebido;
  - nenhuma fonte identifica quem aplica injetáveis;
  - não se sabe se vale para quem já trabalha ou muda de função;
  - não se sabe quem confere o comprovante, como cada vacina é comprovada e por quanto tempo guardar.
- **Decisões de trabalho:**
  - O marco é a data de início, a partir de 01/02/2027.
  - O comprovante é dado de saúde, com conteúdo só no SESMT (RH-012 §11.2). Paula Nogueira não estava entre os destinatários e precisa validar.
- **Dependência:** com a data do projeto desconhecida (Q-018), pode ser necessário controle transitório a partir de 01/02/2027 (RIS-018).

### CR-003, CRNM no programa Acolher: **aplicada, sem validação das áreas**

- **Pontos em aberto (Q-034):**
  - cargos, lojas e data exata;
  - prioridade, que está como Should de forma provisória, porque Helena Vasconcelos ainda não priorizou;
  - o que acontece com CRNM vencida antes do início, o que hoje apenas gera sinalização, sem bloqueio;
  - quem controla a validade depois da experiência, quando o sistema deixa de acompanhar.
- **Riscos (RIS-019):** CPF é obrigatório em Recruta+ e FolhaCerta, mas não se sabe se toda pessoa do programa terá CPF. A FolhaCerta só tem o campo `rg`, sem validade. A condição migratória precisa de proteção, e Paula Nogueira não estava entre os destinatários.

## 5. O que mudou nas entregas

| Entrega | Alteração |
|---|---|
| `01-diagnostico.md` | Versão 3: seção 13; DIV-003 reaberto; RIS-018 e RIS-019; função de Beatriz Lobo; lista de fontes |
| `02-negocio.md` | RN-016 incluída; RN-001 movida para Pendências; escopo, glossário, riscos e perguntas |
| `03-tecnico.md` | RF-012 v2, RF-019, RF-020; cálculo de RN-016; experiência em conflito; de-para e dados pessoais; matriz de acesso |
| `04-backlog.md` | US-033 a US-035; quatro histórias em `revisar`; pendências |
| `05-jira.csv`, `06-azure-devops.csv` | Regerados com 49 itens e a etiqueta `revisar` |
| `07-rastreabilidade.md` | Novos requisitos, versões, situação das histórias e seção de mudanças |

Para quem já importou o backlog, os itens alterados e novos também estão em `.re/entregaveis/backlog/jira-delta.csv` e `azure-devops-delta.csv`.

**Modelo:**

| Item | Antes | Depois |
|---|---|---|
| RN-001 | confirmado | conflito (v1, texto mantido) |
| RF-012 | confirmado, v1 | alterado, v2 |
| RN-014 | hipótese, v1 | hipótese, v2 |
| DIV-003 | tratado | aberto |
| RN-016, RN-017, RF-019, RF-020 | não existiam | confirmado, conflito, confirmado, confirmado |
| Histórias | 32 | 35, 4 em `revisar` |
| Perguntas abertas | 18 | 22 (Q-033 a Q-036) |

A baseline B-001 foi mantida. Não foi criada nova baseline, porque nenhuma mudança foi validada pelas áreas.

## 6. Decisões necessárias

| Pergunta | Quem | Prazo |
|---|---|---|
| Q-035: 30+60 ou 45+45 | Marina Quintela e Helena Vasconcelos, com Sérgio Antunes | Antes de 01/12/2026 |
| Q-033: detalhes da Portaria | Marina Quintela, com Fábio Arantes, Beatriz Lobo e Paula Nogueira | Antes de 01/02/2027 |
| Q-034: abrangência do Acolher e CRNM | Helena Vasconcelos, com Marina Quintela, Rogério Tavares e Paula Nogueira | Antes do 1º trimestre de 2027 |
| Q-036: rescisão e homologação seguem fora | Helena Vasconcelos | Na próxima reunião |
