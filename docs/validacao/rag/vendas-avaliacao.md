# Avaliação — 14 consultas, k=3, embedder=fastembed:sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2, llm=claude-cli:claude-haiku-5-5

| Estratégia | hit | recall | precision | mrr | context_chars | llm_calls | latency_s | degradada |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.8571 | 0.3738 | 0.381 | 0.8571 | 1271.07 | 0 | 0.0105 | 0 |
| corrective_rag | 0.7857 | 0.3238 | 0.7143 | 0.7857 | 268.786 | 2.0714 | 13.2769 | 0 |
| adaptive_rag | 0.8571 | 0.3976 | 0.6786 | 0.8571 | 763.143 | 2.9286 | 20.492 | 0 |
| self_rag | 1 | 0.5262 | 0.8333 | 1 | 841.786 | 3.5 | 34.5458 | 0 |
| agentic_rag | 0.8571 | 0.5821 | 0.4405 | 0.7738 | 2300.64 | 2.7143 | 22.5724 | 0 |
| raptor | 0.8571 | 0.3179 | 0.3095 | 0.7738 | 3964.43 | 0 | 0.0125 | 0 |
| graph_rag | 0.9286 | 0.475 | 0.5476 | 0.7738 | 1374.21 | 0 | 0.0122 | 0 |
