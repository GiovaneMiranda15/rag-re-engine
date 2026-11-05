# rag-re-engine

Motor RAG da skill re-copilot: **executa** a arquitetura RAG indicada para cada atividade
de Engenharia de Requisitos e devolve um **Evidence Package** auditável — o que foi
recuperado, por qual estratégia, com quais pontuações e qual o caminho de decisão (trace).
É autocontido: o mapa atividade → arquitetura fica em `strategies.py`.

```
atividade de RE ──► strategies.py (qual arquitetura)
                        │
                        ▼
                 rag-re-engine (executa) ──► Evidence Package ──► agente / analista
```

## Estado

| Arquitetura | Atividade primária | Status |
|---|---|---|
| Corrective RAG | Análise, Validação | ✅ adaptada |
| baseline (naive RAG) | — | ✅ referência de comparação |
| Self-RAG | Análise (empate) | ✅ adaptada (reflexão por prompts, sem reflection tokens) |
| RAPTOR | Especificação | ✅ adaptada (k-means no lugar de UMAP + GMM; exige `build`) |
| Adaptive RAG | Gerenciamento de Mudanças | ✅ adaptada (roteador por LLM, com heurística de reserva) |
| Agentic RAG | Elicitação | ✅ adaptada (laço fixo com uma ferramenta) |
| GraphRAG | Rastreabilidade | ✅ adaptada (propagação de rótulos no lugar de Leiden; exige `build`) |

Cada módulo em `pipelines/` declara suas adaptações, que devem constar da metodologia. Testes
usam LLM falso: **provam a mecânica, não a qualidade**. A qualidade comparada vem do `evaluate`.

## Corrective RAG — adaptações (declarar na metodologia)

Implementação baseada em Yan et al. (2024), com duas diferenças em relação ao original:

1. **Retrieval evaluator**: o original é um T5-large ajustado; aqui é um LLM via prompt
   (confiança 0–1 por trecho). Limiares `upper=0.6`, `lower=0.3`, `strip_threshold=0.5`
   são parâmetros (`CragConfig`), não valores do artigo — calibrar na avaliação.
2. **Ação corretiva**: o original faz busca web; aqui a fonte externa é plugável
   (`ExternalSource`). A padrão, `LocalRequery`, busca de novo no corpus com a consulta
   reescrita, excluindo os trechos já avaliados.

Se o LLM falhar, o CRAG degrada para o ranking por similaridade e registra no trace.

## Instalação

```bash
cd rag-re-engine
uv sync --extra embeddings     # fastembed (ONNX, sem torch) para embeddings semânticos
```

Sem o extra, apenas `--embedder hash` (lexical, determinístico) funciona. PDFs são lidos com
`pdftotext` (poppler-utils). Dumps `.sql` são indexados só com a estrutura (DDL, triggers,
procedures): blocos `INSERT`/`COPY` são descartados, então registros de dados não entram no índice. O LLM padrão é o Claude Code headless (`claude -p`), sem API key.

## Uso

```bash
# 1. indexar o corpus (txt, md, pdf, sql)
uv run rag-re-engine index ../corpus/pure --db pure.db

# por sistema: doc_id prefixado (SIS-01/arquivo) e filtro --sistema no retrieve
uv run rag-re-engine index fontes/erp --db proj.db --sistema SIS-01

# 2. recuperar evidências (estratégia escolhida por strategies.py)
uv run rag-re-engine retrieve --db pure.db --activity analise \
  --query "requisitos conflitantes sobre autenticação"

# forçar estratégia / sem LLM
uv run rag-re-engine retrieve --db pure.db --activity analise --query "..." --strategy baseline --llm none
uv run rag-re-engine retrieve --db proj.db --activity analise --query "desconto máximo" --sistema SIS-01,SIS-02

# 3. avaliar baseline x CRAG sobre consultas anotadas
uv run rag-re-engine evaluate --db pure.db --dataset eval/queries.jsonl --out reports/analise-v1
```

## Corpus: PURE

PURE — *A Dataset of Public Requirements Documents* (Ferrari, Spagnolo, Gnesi, RE 2017):
79 documentos de requisitos públicos, DOI [10.5281/zenodo.1414117](https://doi.org/10.5281/zenodo.1414117).
Baixe do Zenodo e extraia os PDFs em `../corpus/pure/` (fora do controle de versão).

## Dataset de avaliação

JSONL, uma consulta por linha, relevância no nível de documento:

```json
{"id": "Q1", "activity": "analise", "query": "...", "relevant_doc_ids": ["arquivo.pdf"]}
```

Métricas (média por estratégia): `hit`, `recall`, `precision`, `mrr`, `context_chars` (custo
de contexto), `llm_calls`, `latency_s`. Exemplo mínimo em `tests/fixtures/dataset.jsonl`.

## Integração com o agent-system

O subcomando `context` é um *context provider*: lê um Task Package no stdin e devolve o
Evidence Package no stdout. O Task Package declara:

```json
"context_request": {"provider": "re-rag", "activity": "analise", "db": "/caminho/pure.db", "query": "opcional", "k": 5}
```

## Testes

```bash
uv run pytest
```

Os testes usam o `HashEmbedder` e um LLM falso determinístico — não precisam de rede nem de modelo.
