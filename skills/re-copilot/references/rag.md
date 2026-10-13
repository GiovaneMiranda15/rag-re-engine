# Uso do RAG (rag-re-engine)

O motor é opcional e é localizado nesta ordem (ver `README.md` da skill para instalar):

1. executável `rag-re-engine` no `PATH` (instalado com `uv tool install`);
2. variável `RAG_RE_HOME` apontando para um clone do repositório do motor.

Resolva uma vez por sessão:

```bash
if command -v rag-re-engine >/dev/null 2>&1; then
  ENGINE="rag-re-engine"
elif [ -n "$RAG_RE_HOME" ] && [ -d "$RAG_RE_HOME/rag-re-engine" ]; then
  ENGINE="uv run --project $RAG_RE_HOME/rag-re-engine rag-re-engine"
else
  ENGINE=""
fi
```

Se `ENGINE` ficar vazio, avise o usuário uma vez (apontando o `README.md` da skill) e
siga sem RAG — entrevistas e leitura de código continuam funcionando; mantenha
`state.json.indice` como `null` e não ofereça os comandos "indexar"/"buscar".

## Indexar

Confirme as pastas com o usuário antes. O índice fica em `.re/index.db`.

```bash
$ENGINE index <pasta> --db .re/index.db --embedder fastembed:sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

- Formatos: `.txt`, `.md`, `.pdf` (PDF via `pdftotext`). Outros formatos: peça ao usuário
  para exportar, ou leia diretamente.
- Use **sempre o mesmo embedder** no mesmo índice (o motor recusa misturar). O modelo
  multilíngue acima é o padrão para documentos em português; na 1ª vez baixa ~220 MB.
- Para várias pastas, rode `index` uma vez por pasta no mesmo `--db`. Reindexar é
  idempotente.
- Registre fontes e data em `state.json.indice`.

## Consultar

```bash
$ENGINE retrieve --db .re/index.db --activity <atividade> --query "<consulta>" --json -k 5
```

- `--activity` conforme a fase (tabela em `workflow.md`). O motor escolhe a estratégia
  pelo `rag-re-advisor`.
- `elicitacao`/`especificacao` rodam baseline (sem LLM, rápido).
- `analise`/`validacao` rodam Corrective RAG e chamam `claude -p` (2–3 chamadas, alguns
  segundos). Para consultas exploratórias rápidas, use `--llm none`.
- Escreva a consulta como afirmação ou termos específicos do domínio, não como pergunta
  genérica. Uma consulta por subtema.

## Citar

Cada evidência traz `chunk_id` (`<arquivo>#<n>`). Cite como `[doc: <chunk_id>]`.
Considere evidência útil só se o texto realmente sustenta a afirmação — similaridade alta
não é prova. Se o CRAG devolver `evidence` vazio ou o trace indicar `incorrect`, trate
como "não encontrado nos documentos".

## Registrar (dados para o TCC)

Após cada `retrieve`, anexe uma linha em `.re/log-rag.jsonl`:

```json
{"ts": "<ISO 8601>", "fase": "<fase>", "perfil": "<perfil|null>", "activity": "...", "query": "...", "strategy": "<executada>", "recommended": "...", "n_evidence": 3, "usadas": ["arquivo.pdf#4"], "llm_calls": 2, "latency_s": 4.1}
```

`usadas` = chunks efetivamente citados em requisitos/respostas. Esse log permite medir no
TCC quanto o RAG contribuiu em cada atividade.

## Código do projeto ("consultar sistemas")

No MVP o código não é indexado: use Grep/Read direcionados (rotas, controllers, entidades,
migrations/schemas, clientes de integração, configs). Cite como `[código: path:linha]`.
Nunca leia `.env`, chaves ou pastas de segredos.
