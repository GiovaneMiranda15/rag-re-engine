# Avaliação — 14 consultas, k=3, embedder=fastembed:sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2, llm=claude-cli:claude-haiku-5-5

| Estratégia | hit | recall | precision | mrr | context_chars | llm_calls | latency_s |
|---|---|---|---|---|---|---|---|
| baseline | 0.8571 | 0.3738 | 0.381 | 0.8571 | 1271.07 | 0 | 0.0146 |
| corrective_rag | 0.8571 | 0.3595 | 0.5238 | 0.8571 | 831 | 1.5 | 9.2779 |
| adaptive_rag | 0.8571 | 0.3738 | 0.4405 | 0.8571 | 1092.93 | 1.9286 | 11.6817 |
| self_rag | 0.8571 | 0.3833 | 0.5357 | 0.8571 | 1089.21 | 2.3571 | 19.9893 |
| agentic_rag | 0.8571 | 0.4393 | 0.4167 | 0.8571 | 1729.79 | 2.2857 | 15.4606 |
| raptor | 0.8571 | 0.3179 | 0.3095 | 0.7381 | 3625.5 | 0 | 0.0188 |
| graph_rag | 0.8571 | 0.4369 | 0.4524 | 0.8214 | 1351.57 | 0 | 0.0242 |
