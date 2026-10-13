# Artefatos em `.re/`

```
.re/
├── state.json              estado e checkpoint
├── escopo.md               escopo reformulado + glossário
├── contexto.md             achados do RAG e do código, com citações
├── requisitos.md           fonte da verdade dos requisitos
├── perguntas-abertas.md    lacunas com responsável
├── entrevistas/<perfil>.md transcrição resumida Q/R por perfil
├── especificacao.md        documento consolidado (fase especificacao)
├── rastreabilidade.md      matriz (fase rastreabilidade)
├── log-rag.jsonl           log de consultas ao RAG
└── index.db                índice vetorial (não versionar: sugerir no .gitignore)
```

Sugira ao usuário adicionar `.re/index.db` ao `.gitignore`; os `.md` devem ser versionados.

## state.json

```json
{
  "version": "1.0",
  "projeto": "reembolso-app",
  "fase": "entrevistas",
  "perfil_atual": "ux-designer",
  "perfis": {
    "negocio": {"status": "concluido", "perguntas": 9},
    "ux-designer": {"status": "em_andamento", "perguntas": 4},
    "backend-engineer": {"status": "pendente", "perguntas": 0}
  },
  "proximo_id": {"RF": 15, "RNF": 7, "RN": 4, "Q": 22},
  "indice": {"db": ".re/index.db", "fontes": ["docs/"], "embedder": "fastembed:...", "indexado_em": "2026-10-06T14:00:00Z"},
  "atualizado_em": "2026-10-06T15:10:00Z"
}
```

`fase` ∈ `escopo | contexto | entrevistas | analise | especificacao | validacao | rastreabilidade | concluido`.
`perfis.*.status` ∈ `pendente | em_andamento | concluido`. Nunca remova campos; só adicione/atualize.

## escopo.md

```markdown
# Escopo — <projeto>
## Objetivo
## Problema
## Atores / usuários
## Dentro do escopo
## Fora do escopo
## Premissas
## Restrições conhecidas
## Glossário
| Termo | Definição | Fonte |
```

## requisitos.md

Agrupe por tipo: Funcionais (RF), Não funcionais (RNF), Regras de negócio (RN). IDs nunca
são reutilizados; descartados permanecem com status `descartado`.

```markdown
### RF-014 — Anexar comprovante
- **Enunciado:** O sistema deve permitir que o colaborador anexe comprovante em PDF, JPG ou PNG de até 10 MB por despesa.
- **Tipo:** funcional            <!-- RNF: indicar categoria ISO/IEC 25010 (desempenho, segurança, usabilidade…) -->
- **Prioridade:** Must           <!-- MoSCoW: Must | Should | Could | Won't -->
- **Critérios de aceite:**
  - Dado um arquivo PDF de 2 MB, quando o colaborador anexa, então o arquivo aparece na despesa.
  - Dado um arquivo de 12 MB, quando o colaborador anexa, então o sistema recusa e informa o limite.
- **Fontes:** [entrevista: frontend-engineer Q-018]; [doc: politica-reembolso.pdf#3]
- **Perfis:** frontend-engineer, backend-engineer
- **Depende de:** RF-002
- **Status:** confirmado         <!-- hipótese | confirmado | conflito | validado | descartado -->
- **Histórico:** 2026-10-06 criado (frontend-engineer Q-018)
```

Enunciado: "O sistema deve <ação> <objeto> <condição/restrição mensurável>." Um requisito
por enunciado.

## perguntas-abertas.md

```markdown
| ID | Pergunta | Responsável | Origem | Relacionado | Status |
|---|---|---|---|---|---|
| Q-021 | Quem define a identidade visual? | negocio | frontend-engineer | RNF-006 | aberta |
```

## entrevistas/<perfil>.md

```markdown
# Entrevista — ux-designer
## Rodada 1 — 2026-10-06
**Q-015** Quais dispositivos os colaboradores usam para lançar despesas?
**R:** Majoritariamente celular, na rua, logo após a compra.
→ RNF-005 criado (mobile-first); RF-014 refinado.
```

## especificacao.md

1. Introdução (propósito, escopo, definições → glossário)
2. Visão geral (atores, contexto, premissas e restrições)
3. Requisitos funcionais (por módulo/fluxo)
4. Requisitos não funcionais (por categoria ISO/IEC 25010)
5. Regras de negócio
6. Pendências (hipóteses, conflitos, perguntas abertas)
7. Fontes consultadas
