# Briefing da tarefa (idêntico para todos os participantes)

Você é o apoio de um engenheiro de software / PMO num projeto. O escopo está em
`escopo.md` e os materiais existentes da empresa estão em `fontes/` (somente leitura).

Faça o levantamento e a documentação dos requisitos do projeto, nesta sequência:

## Etapa 1 — Análise inicial e perguntas

1. Analise as fontes e documente o cenário atual em `entrega/01-diagnostico.md`:
   divergências entre sistemas e documentos, gargalos, riscos, pontos de apoio e
   oportunidades.
2. Escreva em `entrega/perguntas.md` as perguntas que precisa fazer aos stakeholders.
   **Máximo de 15 perguntas**, numeradas, cada uma indicando a quem se destina. Elas
   serão respondidas uma única vez.
3. Pare aí e responda apenas "ETAPA 1 CONCLUÍDA". As respostas chegarão numa próxima mensagem.

## Etapa 2 — Documentação (depois das respostas)

As respostas estarão em `entrega/respostas.md`. Produza:

- `entrega/02-negocio.md`: documentação de negócio.
- `entrega/03-tecnico.md`: documentação técnica.
- `entrega/04-backlog.md`: backlog ágil (épicos, features, histórias com critérios de aceite).
- `entrega/05-jira.csv` e `entrega/06-azure-devops.csv`: o mesmo backlog para importação
  no Jira e no Azure DevOps.
- `entrega/07-rastreabilidade.md`: ligação entre requisitos, fontes e backlog.

Atualize o `01-diagnostico.md` se as respostas mudarem algo. Responda apenas "ETAPA 2 CONCLUÍDA".

## Etapa 3 — Manutenção (depois da etapa 2)

Chegarão comunicações novas em `mudancas/`. Avalie-as em `entrega/08-mudancas.md`: para
cada afirmação, diga se ela é **novo**, **existente**, **conflitante**, **complementar** ou
**fora_escopo** em relação ao que já foi levantado, e qual o impacto nos requisitos, no
backlog e nos documentos. Aplique às entregas o que for coerente e registre o que mudou.
Responda apenas "ETAPA 3 CONCLUÍDA".

## Regras do experimento

- Trabalhe **somente** neste diretório. Não leia nada fora dele, a não ser o material
  indicado nas instruções de método abaixo.
- **Não há ninguém disponível para responder durante a execução.** Se o seu método pede
  perguntas interativas, junte-as em `entrega/perguntas.md`. Não peça confirmações: tome
  a decisão razoável e registre-a.
- Não invente fatos. Não copie para as entregas dados pessoais de registros das fontes.
- Escreva em português do Brasil.
- Não use git, não faça deploy, não escreva código de aplicação.
