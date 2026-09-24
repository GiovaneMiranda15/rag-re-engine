# rag-re-engine

Fase 2 do TCC "Aplicação de Arquiteturas RAG na Engenharia de Requisitos" (Giovane Luna
Miranda): **executa** a arquitetura RAG que o [`rag-re-advisor`](../rag-re-advisor) recomenda
para cada atividade de RE e devolve um **Evidence Package** auditável — o que foi
recuperado, por qual estratégia, com quais pontuações e qual o caminho de decisão (trace).

```
atividade de RE ──► rag-re-advisor (qual arquitetura, Tabelas 1 e 2)
                        │
                        ▼
                 rag-re-engine (executa) ──► Evidence Package ──► agente / analista
```

## Estado

| Arquitetura (Tabela 1) | Atividade primária | Status |
|---|---|---|
| Corrective RAG | Análise, Validação | ✅ implementada (adaptada, ver abaixo) |
| baseline (naive RAG) | — | ✅ referência de comparação |
| Self-RAG | Análise | ⏳ |
| RAPTOR | Especificação | ⏳ |
| Adaptive RAG | Gerenciamento de Mudanças | ⏳ |
| Agentic RAG | Elicitação | ⏳ |
| GraphRAG | Rastreabilidade | ⏳ |

Arquitetura recomendada ainda não implementada → o motor usa o baseline e registra o motivo
em `notes`. Em empates do advisor (Análise: Self-RAG = CRAG) usa a primeira já implementada.

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
`pdftotext` (poppler-utils). O LLM padrão é o Claude Code headless (`claude -p`), sem API key.

## Uso

```bash
# 1. indexar o corpus (txt, md, pdf)
uv run rag-re-engine index ../corpus/pure --db pure.db

# 2. recuperar evidências (estratégia escolhida pelo advisor)
uv run rag-re-engine retrieve --db pure.db --activity analise \
  --query "requisitos conflitantes sobre autenticação"

# forçar estratégia / sem LLM
uv run rag-re-engine retrieve --db pure.db --activity analise --query "..." --strategy baseline --llm none

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
