# Workflow — fases

A ordem é sugerida; o usuário pode pular ou voltar. Atualize `state.json.fase` ao trocar.
O classificador de informação nova (`manutencao.md`) roda **em todas as fases**.

| Fase | O que faz | Atividade de RE | Estratégia RAG (`rag.md`) |
|---|---|---|---|
| `escopo` | reformula o escopo e o glossário | — | — |
| `fontes` | registra sistemas e fontes, extrai e indexa | — | — |
| `diagnostico` | cenário atual: divergências, gargalos, riscos, apoio, oportunidades | Elicitação + Análise | você decompõe (Agentic) + `analise` para checar divergências |
| `elicitacao` | entrevistas por perfil | Elicitação | `elicitacao` |
| `analise` | qualidade, conflitos, duplicidades, lacunas | Análise | `analise` |
| `especificacao` | gera os entregáveis | Especificação | `especificacao` |
| `validacao` | revisão com o usuário e contra normas | Validação | `validacao` |
| `manutencao` | modo contínuo a partir da 1ª baseline | Gerenciamento de mudanças + Rastreabilidade | `gerenciamento_mudancas`, `recop.py impacto` |

---

## 1. `escopo`

1. Crie `.re/`, `state.json` (fase `escopo`) e `modelo/` com os arquivos vazios
   (`{"itens": []}`) **logo no início**, para não perder progresso.
2. Leia o escopo (texto ou arquivo). Reformule em `.re/escopo.md`: objetivo, problema,
   atores, áreas da empresa envolvidas, dentro do escopo, fora do escopo, premissas,
   restrições, glossário (`| Termo | Definição | Fonte |`).
3. Pergunte o que for ambíguo ou ausente (no máximo 5 pontos, **uma pergunta por vez**).
4. Peça confirmação explícita da reformulação e avance.

## 2. `fontes`

Escolha o modo (`rag.md`: direto até 300 KB). Siga `fontes.md`: pergunte quais sistemas existem hoje (inclusive planilhas e processos
manuais), quais pastas, dumps, ERDs e documentos o usuário tem de cada um, e registre,
extraia e indexe. Sem fontes, registre "sem fontes documentais" e vá para `elicitacao`.

## 3. `diagnostico`

Siga `diagnostico.md`. Saída: `elementos.json`, `achados.json`, hipóteses de requisito,
perguntas com responsável e a proposta de perfis a entrevistar (confirme a lista com o
usuário e grave em `state.json.perfis`).

## 4. `elicitacao`

Siga `entrevista.md`. Ordem sugerida: `negocio` → perfis de área envolvidos no escopo
(`comercial`, `financeiro`, `operacoes`, `marketing`, `juridico-compliance`, `suporte`,
`dados-bi`) → `gestao-pmo` → `ux-designer` → `software-architect` → `backend-engineer` →
`frontend-engineer` → `dba` → `security` → `qa` → `devops`. Pule os não selecionados.
Priorize perguntas que resolvem achados `aberto` e perguntas `aberta`.

## 5. `analise`

Para cada requisito (ou grupo por tema):

- **Qualidade (ISO/IEC/IEEE 29148):** necessário, singular, não ambíguo, verificável,
  viável, consistente, rastreável. Termos vagos a caçar: "rápido", "fácil", "intuitivo",
  "adequado", "eficiente", "etc.", "e/ou", "suportar", "flexível", "tempo real" (sem número).
- **Conflitos** entre requisitos e entre requisito e fontes: `retrieve --activity analise`.
- **Duplicidades**, requisitos sem critério de aceite, sem fonte ou sem prioridade.
- **Cobertura:** achados abertos sem requisito, atores sem requisito, dados sem dono,
  integrações sem tratamento de falha, RNF ausentes (desempenho, segurança,
  disponibilidade, LGPD).

Resultado: `status: conflito` com `rel.conflita_com`, novas perguntas para o perfil certo
e um resumo. Pergunte se o usuário quer resolver agora.

## 6. `especificacao`

Gere os entregáveis (`entregaveis.md`) e o backlog (`backlog-export.md`). Hipóteses entram
no corpo com a marca `[hipótese]`, para o documento ficar completo; conflitos e perguntas
vão para "Pendências". Rode `recop.py lint` e `recop.py verificar --docs <pasta>` e trate o que eles
apontarem. Revise como leitor: o gestor sabe o que decidir? O dev sabe por onde começar?

## 7. `validacao`

1. Confronte os requisitos com normas e documentos de referência: `retrieve --activity validacao`.
2. Revise com o usuário em lotes por tema, usando AskUserQuestion com Aprovar / Ajustar /
   Descartar. Aprovados → `validado`; ajustes voltam para entrevista ou análise.
3. Proponha a `baseline` (`manutencao.md`) quando o conjunto principal estiver validado.

## 8. `manutencao`

Ativa a partir da primeira baseline. Siga `manutencao.md`.

---

## Painel de status

Monte com `recop.py status`:

```
📋 <projeto> — fase: <fase> — baseline: <B-NNN | nenhuma>
Sistemas: <n> · Fontes: <n> · Índice RAG: <ok | sem índice>
Requisitos: <n> (✅ validado · ✔️ confirmado · 💭 hipótese · ⚠️ conflito · 🔄 alterado)
Achados abertos: <n> (DIV · GAR · RIS · OPO) · Perguntas abertas: <n> · CRs pendentes: <n>
Backlog: <épicos>/<features>/<histórias> (<n> revisar)

| Perfil | Status | Perguntas |
|---|---|---|
| 💼 negocio | concluído | 9 |

Próximo passo sugerido: <ação>
```
