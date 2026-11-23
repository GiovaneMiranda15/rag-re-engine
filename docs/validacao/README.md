# Validação da skill re-copilot

Como avaliar a skill e comparar versões e alternativas de forma repetível. Resultados de cada
rodada ficam em `resultados/`. Próxima rodada: `rodadas/r04-RUNBOOK.md`. Resultados: `rodada-01.md` (v1 e v2, arquiteturas RAG) e `rodada-02.md` (v3, caso novo) e `rodada-03-caso-real.md` (projeto real, anonimizado).

## Pergunta avaliada

A skill entrega requisitos melhores que as alternativas, a um custo aceitável? Em particular:

1. encontra o que importa nas fontes (cobertura) sem inventar nem cair em falsos positivos;
2. produz documentação e backlog utilizáveis;
3. mantém os requisitos quando chega informação nova;
4. as arquiteturas RAG de cada etapa ajudam mais do que a busca simples?

## Condições comparadas

| Condição | O que é |
|---|---|
| `c1` | IA comum: só o modelo e as ferramentas básicas |
| `c2` | skill timovi, usada até o breakdown (não foi feita para levantamento de requisitos) |
| `c3` | re-copilot v1 |
| `c4` | re-copilot v2, com RAG real e regras de completude |
| `c5` | re-copilot v3, com `verificar`, matrizes geradas e modo direto |

A skill e os casos `exemplos/` estão no repositório [re-copilot](https://github.com/GiovaneMiranda15/re-copilot).
Todas recebem o mesmo `briefing-comum.md`, o mesmo modelo e cópias congeladas da skill, sem casos
de exemplo. Cada execução é um agente novo, em um diretório isolado.

## Casos

| Caso | Autor | Armadilhas | Observação |
|---|---|---|---|
| `exemplos/vendas-unificado` | o autor da skill | não | **fácil**: gera efeito teto |
| `exemplos/rh-admissao` | agente sem acesso à skill | 7 | projeto de RH, DP e Jurídico; o mais informativo |
| `experimento/casos/hospital-compras` | agente sem acesso à skill | 8 | caso novo, usado para evitar sobreajuste da v3 |

## Protocolo

1. **Etapa 1:** diagnóstico e até 15 perguntas. Um **oráculo** (agente com os fatos de `oraculo.md`)
   responde sem saber o método. Isso substitui o stakeholder humano, de forma igual para todos.
2. **Etapa 2:** documentação de negócio e técnica, backlog, CSVs e rastreabilidade.
3. **Etapa 3:** as `mudancas/` são entregues e o método classifica, analisa o impacto e aplica.
4. **Medidas objetivas:** `avaliar_entregas.py`.
5. **Avaliação cega:** `preparar_juizes.py` sorteia letras e remove os nomes dos métodos. Dois juízes
   independentes seguem `instrucao-juiz.md` (o gabarito é a referência).
6. **Agregação:** `agregar_juizes.py` calcula médias e concordância (kappa ponderado). Só aqui o mapa
   letra → condição é aberto.

## Como ler as métricas

| Métrica | Fonte | Leitura |
|---|---|---|
| Cobertura (D, G, R, P, O) | juiz | item encontrado e correto: 2; parcial: 1; ausente: 0. Normalizada de 0 a 1 |
| Armadilhas caídas | juiz | falsos positivos. Quanto menos, melhor |
| Adicionais `sem_suporte`/`falso` | juiz | indício de invenção. Quanto menos, melhor |
| Citações corretas | juiz | amostra de 10 citações conferidas nas fontes |
| Classificação de mudanças e impacto | juiz | acerto da classe e cobertura do impacto |
| Qualidade (1 a 5) | juiz | negócio, técnico, backlog, rastreabilidade, manutenção, honestidade, perguntas |
| Entregas, CSV válido, história na matriz | script | conformidade mecânica |
| Tempo e ferramentas | execução | custo. O número de tokens é o tamanho final do contexto, não o consumo total |
| hit, recall, precision, mrr | `rag-re-engine evaluate` | qualidade da recuperação, por documento |

**Critérios para declarar melhora:** diferença em pelo menos 2 casos, sem piorar em armadilhas ou
invenção, e maior que a variação entre juízes. Com uma execução por condição, tudo é **indício**, não
prova estatística.

## Avaliação das arquiteturas RAG

`rag/*-consultas.jsonl` tem consultas anotadas por atividade (`relevant_doc_ids`). A saída traz a
coluna `degradada`: fração de consultas em que o LLM falhou ou a estrutura não existia. Se ela for
maior que zero, o relatório avisa e **o resultado não vale** (ver `rag/descartados/`).

## Reproduzir

```bash
python3 -I docs/validacao/preparar_juizes.py <exp> <rotulo> <caso_em_runs> <caso_selado> c1,c2,c3
python3 -I docs/validacao/avaliar_entregas.py <exp>/runs/<caso>/c1 ... --json saida.json
python3 -I docs/validacao/agregar_juizes.py juiz-1.json juiz-2.json --mapa mapa.json --saida res.json
uv run --project <re-copilot> --extra embeddings rag-re-engine evaluate --db <db> \
  --dataset docs/validacao/rag/rh-consultas.jsonl --llm claude:claude-haiku-5-5 -k 3 --out <saida>
```

Guarde dados de experimento em `docs/validacao/experimento/`, nunca em `/tmp`: um reinício os apaga.

## Rumo ao formulário com engenheiros

A avaliação com pessoas ainda não foi feita. Dimensões sugeridas, alinhadas às métricas acima, para
comparar a opinião humana com os juízes:

- **Perfil:** papel, anos de experiência, se já fez levantamento de requisitos.
- **Tarefa:** projeto real ou caso sintético, tamanho das fontes, tempo gasto, retrabalho.
- **Utilidade (Likert 1 a 5):** diagnóstico, perguntas, documentação de negócio, documentação técnica,
  backlog e manutenção. Reaproveitaria o entregável sem reescrever?
- **Confiança:** encontrou informação inventada? As citações ajudaram a conferir?
- **Comparação:** preferiu isto ou o processo atual (e a IA comum)? Faria de novo?
- **Modelos de aceitação:** SUS (usabilidade) e TAM (utilidade e facilidade percebidas).
- **Aberta:** o que faltou, o que atrapalhou, o que foi errado.
