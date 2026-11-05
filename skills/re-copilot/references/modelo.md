# Modelo de dados — `.re/`

```
.re/
├── state.json              fase, perfis, baseline vigente, índice RAG
├── fontes.json             sistemas e fontes (hash para detectar mudança)
├── escopo.md               escopo reformulado + glossário (escrito por você)
├── modelo/                 FONTE DA VERDADE (JSON, editado por você)
│   ├── requisitos.json     RF, RNF, RN
│   ├── elementos.json      processos, entidades, atores, integrações, regras existentes
│   ├── achados.json        divergências, gargalos, riscos, apoio, oportunidades
│   ├── perguntas.json      lacunas com responsável
│   ├── backlog.json        épicos, features, histórias
│   └── mudancas.json       CRs (pedidos de mudança)
├── entrevistas/<perfil>.md log Q/R por perfil (escrito por você)
├── mudancas/CR-NNN.md      análise de impacto de cada CR (escrito por você)
├── baselines/B-NNN.json    fotos congeladas do modelo
├── extraidos/              transcrições de ERD/BPMN/planilhas para indexar
├── entregaveis/            documentos finais (entregaveis.md)
├── requisitos.md · perguntas-abertas.md · achados.md · backlog.md · rastreabilidade.md · cenarios.md
│                           GERADOS por `recop.py render`, não editar
├── log-rag.jsonl           log de consultas e decisões (métricas)
└── index.db                índice RAG (não versionar)
```

Sugira ao usuário pôr `.re/index.db` no `.gitignore`. Os `.md` e `.json` podem conter
trechos de documentos internos: avise antes de versionar em repositório público.

## Comandos do utilitário

```bash
python3 -I <skill>/scripts/recop.py check     # integridade (IDs, status, referências)
python3 -I <skill>/scripts/recop.py render    # gera os .md a partir do modelo
python3 -I <skill>/scripts/recop.py lint      # lacunas de completude (história sem 2 critérios, achado sem tratamento…)
python3 -I <skill>/scripts/recop.py verificar --docs <pasta>  # números sem fonte, citações e IDs inválidos, DIV sem checagem
python3 -I <skill>/scripts/recop.py status    # números do painel
python3 -I <skill>/scripts/recop.py fontes [--update]
python3 -I <skill>/scripts/recop.py impacto <ID> [<ID>...] [--depth 3]
python3 -I <skill>/scripts/recop.py candidatos "<afirmação>"
python3 -I <skill>/scripts/recop.py baseline --nota "…"
python3 -I <skill>/scripts/recop.py diff [B-NNN]
python3 -I <skill>/scripts/recop.py exportar jira|azure [--processo agile|scrum|basic] [--delta] [--saida arq.csv]
```

Depois de cada lote de alterações no modelo, rode `check` e, se der ok, `render`.

## Convenções

- Cada arquivo do modelo é `{"itens": [ ... ]}`.
- IDs são sequenciais por prefixo, **nunca reutilizados**. O próximo número fica em
  `state.json.proximo_id`. Itens descartados permanecem com status `descartado`.
- `fontes`: lista de citações textuais (`"doc:SIS-01/schema.sql#2"`, `"entrevista:negocio Q-004"`).
- `fontes_id`: lista de IDs de `fontes.json` (`"F-003"`), quando a fonte inteira sustenta o item.
- `rel`: arestas do grafo, `{"<tipo>": ["ID", ...]}`. Tipos: `deriva_de`, `depende_de`,
  `conflita_com`, `complementa`, `substitui`, `detalha`, `afeta`, `implementado_em`.
- Campos que também viram arestas: `pai` e `requisitos` (detalha), `sistemas`
  (implementado_em), `relacionados` e `afetados` (afeta).
- Datas em ISO 8601.

## requisitos.json

```json
{"id": "RN-004", "titulo": "Alçada de aprovação de reembolso", "versao": 2,
 "enunciado": "O sistema deve exigir aprovação do gerente financeiro para reembolsos acima de R$ 1.000.",
 "tipo": "regra", "categoria": null, "prioridade": "Must",
 "criterios_aceite": ["Dado um reembolso de R$ 1.200, quando o colaborador envia, então a solicitação vai para o gerente financeiro."],
 "status": "confirmado",
 "fontes": ["doc:geral/politica-viagens.md#0", "entrevista:financeiro Q-012"],
 "sistemas": ["SIS-01", "SIS-03"], "perfis": ["financeiro", "negocio"],
 "rel": {"deriva_de": ["DIV-001"], "depende_de": ["RF-002"]},
 "historico": [{"versao": 1, "data": "2026-11-03", "nota": "criado (diagnóstico)", "antes": null},
               {"versao": 2, "data": "2026-11-05", "mudanca": "CR-001", "antes": "…acima de R$ 800…"}]}
```

- `tipo`: `funcional` (RF), `nao_funcional` (RNF, com `categoria` ISO/IEC 25010:
  desempenho, confiabilidade, segurança, usabilidade, compatibilidade, manutenibilidade,
  portabilidade, adequação funcional) ou `regra` (RN).
- `prioridade`: MoSCoW (`Must | Should | Could | Won't`).
- `status`: `hipótese | confirmado | conflito | validado | alterado | obsoleto | descartado`.
  `alterado` = mudou depois da baseline e aguarda revalidação.
- Enunciado: "O sistema deve <ação> <objeto> <condição/limite mensurável>." Um por requisito.
- Ao mudar um requisito: incremente `versao` e acrescente uma entrada no `historico` com o
  texto anterior em `antes`.

## elementos.json

O que **existe hoje** nas fontes (insumo do diagnóstico e da rastreabilidade):

```json
{"id": "EL-007", "tipo": "regra_existente", "nome": "Limite de diária R$ 300 no portal",
 "descricao": "Constraint ck_limite_diaria recusa diária acima de R$ 300.",
 "sistemas": ["SIS-01"], "fontes": ["sql:SIS-01/schema.sql:ck_limite_diaria"]}
```

`tipo`: `processo | etapa | ator | entidade | atributo | integracao | regra_existente | relatorio | indicador`.

## achados.json

```json
{"id": "DIV-001", "titulo": "Limite de diária diverge entre portal e política",
 "descricao": "Portal R$ 300, política R$ 400.",
 "sistemas": ["SIS-01", "SIS-03"], "severidade": "alta",
 "fontes": ["sql:SIS-01/schema.sql:ck_limite_diaria", "doc:geral/politica-viagens.md#0"],
 "status": "aberto", "gera": ["RN-004", "Q-003"], "rel": {"afeta": ["EL-007"]}}
```

Prefixos: `DIV` divergência, `GAR` gargalo, `RIS` risco, `APO` ponto de apoio, `OPO` oportunidade.
`severidade` (riscos: probabilidade × impacto): `baixa | media | alta | critica`.
`DIV` exige `checagem: {"vigencia", "abrangencia", "definicao"}` (ver `diagnostico.md`).
`status`: `aberto | tratado | descartado`.

## perguntas.json

```json
{"id": "Q-003", "pergunta": "Qual limite de diária vale: R$ 300 ou R$ 400?",
 "responsavel": "financeiro", "origem": "diagnostico", "relacionados": ["DIV-001"],
 "status": "aberta", "resposta": null}
```

`status`: `aberta | respondida | cancelada`.

## backlog.json

```json
{"id": "US-014", "tipo": "historia", "titulo": "Enviar reembolso para aprovação",
 "descricao": "Como colaborador, quero enviar meu reembolso para aprovação, para receber sem trocar e-mails.",
 "criterios_aceite": ["Dado …, quando …, então …"], "prioridade": "Must", "estimativa": null,
 "pai": "FT-003", "requisitos": ["RN-004", "RF-010"], "labels": ["financeiro"], "status": "proposto"}
```

`tipo`: `epico` (EP) → `feature` (FT) → `historia` (US). Os campos `pai` e `requisitos` dão
a rastreabilidade. `dependencias`: histórias anteriores. `bloqueada_por`: perguntas abertas que
travam a história. Histórias de requisito `hipótese` levam o label `hipotese`.
`status`: `proposto | pronto | revisar | descartado`. `revisar` = um CR
aplicado afetou o item.

## mudancas.json

```json
{"id": "CR-001", "titulo": "Alçada de aprovação passa a R$ 1.500", "data": "2027-01-20",
 "gatilho": "manual", "origem": "doc:mudancas/ata-comite.md#0",
 "classe": "conflitante", "complexidade": "complexa",
 "afetados": ["RN-004", "DIV-001", "US-014"], "status": "proposta",
 "decisao": null, "baseline": "B-001"}
```

`gatilho`: `manual | fonte | fluxo`. `classe`: `novo | existente | conflitante | complementar | fora_escopo`.
`complexidade`: `simples | moderada | complexa`. `status`: `proposta | aprovada | rejeitada | aplicada`.

## fontes.json

```json
{"sistemas": [{"id": "SIS-01", "nome": "Portal de despesas", "papel": "legado-principal",
               "pastas": ["fontes/SIS-01-portal"], "descricao": "solicitações e aprovações"}],
 "fontes": [{"id": "F-001", "sistema": "SIS-01", "path": "fontes/SIS-01-portal/schema.sql",
             "tipo": "ddl", "sha256": "…", "registrado_em": "…", "indexado_em": "…"}]}
```

Use `geral` como sistema para documentação transversal (políticas, atas). `papel`:
`legado-principal | satelite | externo | alvo | documentacao`.

## state.json

```json
{"version": "2.0", "projeto": "reembolso-app", "fase": "diagnostico",
 "perfil_atual": null,
 "perfis": {"negocio": {"status": "concluido", "perguntas": 9}},
 "proximo_id": {"RF": 1, "RNF": 1, "RN": 1, "EL": 1, "DIV": 1, "GAR": 1, "RIS": 1,
                "APO": 1, "OPO": 1, "Q": 1, "EP": 1, "FT": 1, "US": 1, "CR": 1, "B": 1},
 "baseline": null,
 "indice": {"db": ".re/index.db", "embedder": "fastembed:…", "indexado_em": "…"},
 "atualizado_em": "…"}
```

`fase` ∈ `escopo | fontes | diagnostico | elicitacao | analise | especificacao | validacao | manutencao`.
Nunca remova campos; só adicione ou atualize.

## Baseline — `baselines/B-NNN.json`

```json
{"id": "B-001", "data": "…", "nota": "v1 validada com diretoria",
 "requisitos": [ ...cópia integral de requisitos.json... ], "backlog": [ ... ]}
```
