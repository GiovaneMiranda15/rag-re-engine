# Avaliação — 14 consultas, k=3, embedder=fastembed:sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2, llm=None

| Estratégia | hit | recall | precision | mrr | context_chars | llm_calls | latency_s | degradada |
|---|---|---|---|---|---|---|---|---|
| raptor | 1 | 0.6726 | 0.7619 | 0.8333 | 2534 | 0 | 0.0076 | 0 |
| graph_rag | 0.8571 | 0.3988 | 0.4762 | 0.6786 | 1401.93 | 0 | 0.0104 | 0 |
| baseline | 0.7857 | 0.494 | 0.6429 | 0.75 | 1132 | 0 | 0.007 | 0 |
