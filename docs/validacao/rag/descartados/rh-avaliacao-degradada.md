# Avaliação — 14 consultas, k=3, embedder=fastembed:sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2, llm=claude-cli:claude-haiku-5-5

| Estratégia | hit | recall | precision | mrr | context_chars | llm_calls | latency_s | degradada |
|---|---|---|---|---|---|---|---|---|
| baseline | 0.7857 | 0.494 | 0.6429 | 0.75 | 1132 | 0 | 0.0082 | 0 |
| corrective_rag | 0.7857 | 0.4464 | 0.631 | 0.75 | 730.143 | 1.4286 | 7.1263 | 0.5714 |
| adaptive_rag | 0.7857 | 0.4345 | 0.6429 | 0.75 | 910.714 | 1.6429 | 7.4993 | 0.5714 |
| self_rag | 0.7857 | 0.4702 | 0.6381 | 0.75 | 1051.14 | 2.0714 | 14.1367 | 0.6429 |
| agentic_rag | 0.7857 | 0.5774 | 0.5714 | 0.75 | 1595.5 | 2.3571 | 12.7731 | 0.6429 |
| raptor | 0.7857 | 0.4583 | 0.5 | 0.7143 | 2534 | 0 | 0.0143 | 0 |
| graph_rag | 0.8571 | 0.3988 | 0.4762 | 0.6786 | 1401.93 | 0 | 0.0157 | 0 |

**ATENÇÃO: resultado não confiável.** Fração de consultas degradadas: {'corrective_rag': 0.5714, 'adaptive_rag': 0.5714, 'self_rag': 0.6429, 'agentic_rag': 0.6429}.
