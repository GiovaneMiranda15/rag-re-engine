# Avaliação — 14 consultas, k=3, embedder=fastembed:sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2, llm=None

| Estratégia | hit | recall | precision | mrr | context_chars | llm_calls | latency_s | degradada |
|---|---|---|---|---|---|---|---|---|
| raptor | 0.9286 | 0.619 | 0.6905 | 0.881 | 3964.43 | 0 | 0.0092 | 0 |
| graph_rag | 0.9286 | 0.475 | 0.5476 | 0.7738 | 1374.21 | 0 | 0.0099 | 0 |
| baseline | 0.8571 | 0.3738 | 0.381 | 0.8571 | 1271.07 | 0 | 0.0069 | 0 |
