# Backlog ágil e exportação

## Montagem do backlog (`backlog.json`)

1. **Épicos** (EP): um por processo de negócio ou capacidade grande (ex.: "Solicitação
   de reembolso", "Aprovações").
2. **Features** (FT): agrupam requisitos coesos dentro do épico.
3. **Histórias** (US), uma ou mais por requisito (hipóteses inclusive, com o label `hipotese`):
   - "Como <papel>, quero <ação>, para <benefício>" (papel real do glossário);
   - **no mínimo 2 critérios** em Dado/Quando/Então, e 3 em histórias `Must`: caminho normal, erro
     ou exceção, e limite (ex.: dia 30 aceita, dia 31 recusa), com valores concretos. Cada critério
     precisa ser verificável: descreve comportamento, não uma tarefa nem uma decisão;
   - decisão pendente **não é história**: vira pergunta. Escreva a história com a premissa explícita
     e `bloqueada_por: ["Q-NNN"]`, e prefira fatiar o que dá para fazer sem a decisão;
   - `dependencias`: IDs das histórias que precisam vir antes, quando houver;
   - `requisitos`: os IDs de origem (obrigatório); `prioridade`: herdada (maior MoSCoW);
   - INVEST: independente, negociável, valiosa, estimável, pequena, testável. História
     grande → divida.
   - RNF transversais viram critérios de aceite das histórias afetadas ou "enablers"
     (`labels: ["enabler"]`).
4. Trabalho transversal também é backlog: migração, carga inicial, convivência, auditoria,
   permissões, monitoramento e treinamento viram features ou enablers, não notas de rodapé.
5. Proponha uma sequência de entrega (ondas ou sprints) com as dependências.

Depois de montar: `recop.py check` → `recop.py lint` → `recop.py render` (gera `.re/backlog.md`) e copie
para `entregaveis/backlog/backlog.md`.

## Jira — `entregaveis/backlog/jira.csv`

Importação: *Jira Settings › System › External System Import › CSV* (ou
*Issues › Import issues from CSV* em projetos company-managed). Colunas:

| Coluna CSV | Origem | Observação |
|---|---|---|
| `Issue Id` | sequencial 1..n | usado para ligar pai e filho no import |
| `Parent Id` | `Issue Id` do pai | épico → história (em team-managed, mapeie para *Parent*) |
| `Issue Type` | `Epic` / `Story` (features como `Epic` ou `Story` com label `feature`) | ajuste aos tipos do projeto |
| `Summary` | `titulo` | |
| `Description` | `descricao` + critérios de aceite + "Requisitos: RN-004, RF-010" | quebras de linha dentro de aspas |
| `Priority` | Must→`Highest`, Should→`High`, Could→`Medium`, Won't→`Low` | |
| `Labels` | `labels` + IDs de requisito (`req-RN-004`) | um label por coluna `Labels` repetida |

## Azure DevOps — `entregaveis/backlog/azure-devops.csv`

Importação: *Boards › Work items › Import Work Items* (CSV). Hierarquia por colunas
`Title 1`/`Title 2`/`Title 3`, uma linha por item, na ordem pai → filhos:

| Coluna CSV | Origem |
|---|---|
| `Work Item Type` | `Epic` / `Feature` / `User Story` (processo Agile) ou `Product Backlog Item` (Scrum) |
| `Title 1` | título do épico (só na linha do épico) |
| `Title 2` | título da feature |
| `Title 3` | título da história |
| `Description` | `descricao` + "Requisitos: …" |
| `Acceptance Criteria` | critérios de aceite (histórias) |
| `Priority` | Must→1, Should→2, Could→3, Won't→4 |
| `Tags` | labels + IDs de requisito separados por `; ` |

Pergunte o processo do projeto (Agile, Scrum ou Basic) antes de gerar. Basic não tem
Feature: use `Epic` → `Issue`.

## Regras do CSV

- UTF-8, separador vírgula, todos os campos entre aspas duplas; aspas internas duplicadas (`""`).
- **Não escreva à mão.** Gere a partir de `backlog.json`:

  ```bash
  python3 -I <skill>/scripts/recop.py exportar jira --saida .re/entregaveis/backlog/jira.csv
  python3 -I <skill>/scripts/recop.py exportar azure --processo agile --saida .re/entregaveis/backlog/azure-devops.csv
  ```
- O ID do requisito sempre vai em label ou tag: é o que mantém a rastreabilidade depois da
  importação. Após um CR, gere só os itens `revisar` com `--delta` (arquivo `*-delta.csv`). Reimportar
  cria itens novos: o delta serve de lista do que atualizar no Jira ou Azure.
