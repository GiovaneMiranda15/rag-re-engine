# Avaliação — 14 consultas, k=3, embedder=fastembed:sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2, llm=claude-cli:claude-haiku-5-5

| Estratégia | hit | recall | precision | mrr | context_chars | llm_calls | latency_s | degradada |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.7857 | 0.494 | 0.6429 | 0.75 | 1132 | 0 | 0.012 | 0 |
| corrective_rag | 0.9286 | 0.4821 | 0.8333 | 0.881 | 396 | 2.2143 | 15.6468 | 0 |
| adaptive_rag | 0.9286 | 0.5417 | 0.8048 | 0.8929 | 822.5 | 2.7857 | 20.228 | 0 |
| self_rag | 0.9286 | 0.5 | 0.8155 | 0.8929 | 880.357 | 3.7857 | 35.0234 | 0 |
| agentic_rag | 0.9286 | 0.6131 | 0.5179 | 0.7345 | 2232.5 | 2.7143 | 23.8108 | 0 |
| raptor | 0.7857 | 0.4583 | 0.5 | 0.7143 | 2534 | 0 | 0.0138 | 0 |
| graph_rag | 0.8571 | 0.3988 | 0.4762 | 0.6786 | 1401.93 | 0 | 0.0228 | 0 |
