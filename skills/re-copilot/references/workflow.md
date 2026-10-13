# Workflow — fases do re-copilot

As fases seguem as atividades de RE da Tabela 1 do TCC. A ordem é a sugerida, mas o
usuário pode pular ou voltar a qualquer fase; atualize `state.json.fase` ao trocar.

| Fase | Atividade de RE | Arquitetura (Tabela 1) | Execução no MVP |
|---|---|---|---|
| `escopo` | — | — | conversa |
| `contexto` | Elicitação | Agentic RAG | você (o agente) decompõe e chama `retrieve --activity elicitacao` |
| `entrevistas` | Elicitação | Agentic RAG | perfis + `retrieve` antes de cada pergunta |
| `analise` | Análise | Self-RAG / CRAG | `retrieve --activity analise` (CRAG) |
| `especificacao` | Especificação | RAPTOR | `retrieve --activity especificacao` (baseline; RAPTOR pendente) |
| `validacao` | Validação | CRAG | `retrieve --activity validacao` (CRAG) |
| `rastreabilidade` | Rastreabilidade | GraphRAG | matriz em Markdown (GraphRAG pendente) |

Ao usar uma estratégia que caiu no baseline, não esconda isso: o campo `notes` do
Evidence Package diz o motivo.

---

## 1. `escopo`

**Entrada:** texto livre ou arquivo indicado pelo usuário.

1. Leia o escopo. Reformule em `.re/escopo.md` (formato em `artefatos.md`): objetivo,
   problema, usuários/atores, dentro do escopo, fora do escopo, premissas, restrições
   conhecidas, glossário inicial.
2. Liste o que está ambíguo ou ausente (no máximo 5 pontos mais importantes) e pergunte
   ao usuário — **uma pergunta por vez**.
3. Peça confirmação explícita da reformulação. Só então crie `state.json` e avance.

## 2. `contexto` (Elicitação via RAG + código)

1. Pergunte quais fontes existem: pastas de documentos (atas, briefings, contratos,
   normas, docs de sistemas legados) e repositórios de código relacionados.
2. Documentos: indexe conforme `rag.md` (confirme as pastas antes).
3. Decomponha o escopo em 6–10 subperguntas cobrindo: atores, processos/fluxos, dados,
   integrações/sistemas, regras de negócio, restrições legais, requisitos de qualidade.
4. Para cada subpergunta: `retrieve --activity elicitacao`; para código, use Grep/Read
   direcionados (rotas, entidades, schemas, integrações). Registre em `.re/contexto.md`
   o que foi encontrado, **com citação**.
5. Gere requisitos iniciais em `requisitos.md` com status `hipótese` (fonte = doc/código).
6. Lacunas viram perguntas em `perguntas-abertas.md`, cada uma com o perfil responsável.
7. Proponha os perfis a entrevistar (com base no escopo e nas lacunas) e peça ao usuário
   para confirmar/ajustar a lista. Grave em `state.json.perfis`.

Sem documentos? Pule o RAG, registre "sem fontes documentais" em `contexto.md` e siga —
as entrevistas passam a ser a fonte principal.

## 3. `entrevistas`

Siga `entrevista.md`. Ordem sugerida: `negocio` → `ux-designer` → `software-architect`
→ `backend-engineer` → `frontend-engineer` → `dba` → `security` → `qa` → `devops`.
Pule perfis não selecionados. O usuário pode trocar de perfil a qualquer momento.

## 4. `analise`

Para cada requisito (ou grupo por tema), verifique:

- **Qualidade (ISO/IEC/IEEE 29148):** necessário, singular, não ambíguo, verificável,
  viável, consistente, rastreável. Termos vagos a caçar: "rápido", "fácil", "intuitivo",
  "adequado", "eficiente", "etc.", "e/ou", "suportar", "flexível", "na maioria dos casos".
- **Conflitos** entre requisitos e entre requisito e documento: `retrieve --activity
  analise --query "<enunciado do requisito>"` e compare com as evidências.
- **Duplicidades** e requisitos sem critério de aceite.
- **Lacunas de cobertura:** atores sem requisito, dados sem dono, integrações sem
  tratamento de falha, NFR ausentes (desempenho, segurança, disponibilidade, LGPD).

Resultado: `status: conflito` nos afetados + perguntas novas para o perfil adequado. Mostre
um resumo e pergunte se o usuário quer resolver agora (voltando à entrevista do perfil).

## 5. `especificacao`

Consolide em `.re/especificacao.md` (estrutura em `artefatos.md`) apenas requisitos
`confirmado` ou `validado`; hipóteses e conflitos vão para a seção "Pendências". Use
`retrieve --activity especificacao` para completar definições a partir dos documentos.

## 6. `validacao`

1. Confronte cada requisito com normas/documentos de referência: `retrieve --activity
   validacao` (CRAG).
2. Revise com o usuário em lotes por tema: "Este conjunto representa o que você precisa?"
   Use AskUserQuestion com opções Aprovar / Ajustar / Descartar quando couber.
3. Aprovados → `validado`. Ajustes → voltam para entrevista/análise.

## 7. `rastreabilidade`

Gere `.re/rastreabilidade.md`: matriz requisito × fontes (doc/código/entrevista) × perfis
× dependências entre requisitos × (quando existirem) testes e módulos de código. Aponte
requisitos órfãos (sem fonte) e fontes sem requisito.

---

## Painel de status

```
📋 <projeto> — fase: <fase>
Requisitos: <n> (✅ validado <a> · ✔️ confirmado <b> · 💭 hipótese <c> · ⚠️ conflito <d>)
Perguntas abertas: <n>  ·  Índice RAG: <db> (<n> docs) | sem índice

| Perfil | Status | Perguntas | Requisitos gerados |
|---|---|---|---|
| 💼 negocio | concluído | 9 | 6 |
| 🎨 ux-designer | em andamento | 4 | 2 |
| ⚙️ backend-engineer | pendente | — | — |

Próximo passo sugerido: <ação>
```
