# Acompanhamento e manutenção de requisitos

O modo manutenção mantém o modelo coerente quando surge informação nova. O
**classificador** roda em todas as fases; a **análise de impacto**, o **CR** e o
**versionamento** valem a partir da primeira baseline (antes dela, aplique direto e
registre no histórico).

## 1. Gatilhos

| Gatilho | Origem | Exemplo |
|---|---|---|
| `manual` | o usuário descreve ou cola uma mudança (`mudança: …`, `avaliar ata.pdf`) | ata de diretoria |
| `fonte` | `recop.py fontes` acusa fonte nova ou alterada | dump novo de um sistema legado |
| `fluxo` | uma resposta de entrevista, um trecho recuperado ou uma análise traz algo que toca requisitos existentes | perfil financeiro cita regra nova |

## 2. Classificador

Para cada afirmação nova (uma por vez; quebre textos longos em afirmações atômicas):

1. **Candidatos:** rode `recop.py candidatos "<afirmação>"` para ver os itens do modelo com
   termos em comum (só ordena; leia os itens antes de decidir; sinônimos escapam, então
   repita com outros termos se vier vazio) e busque evidências relacionadas
   (`retrieve --activity gerenciamento_mudancas`).
2. **Decida a classe**, com justificativa de 1 linha:

| Classe | Critério | Ação |
|---|---|---|
| `novo` | nenhum item equivalente | cria requisito (`hipótese` ou `confirmado`, conforme a fonte) |
| `existente` | mesmo conteúdo de um item | acrescenta a fonte ao item (reforço); sem nova versão |
| `conflitante` | contradiz um item ou outra fonte | **não sobrescreve**; marca `conflito` + `rel.conflita_com`; abre CR ou pergunta |
| `complementar` | detalha, estende ou restringe sem contradizer | nova versão do item ou requisito filho com `rel.complementa` |
| `fora_escopo` | não pertence ao escopo | registra em `escopo.md` › fora do escopo e avisa |

3. Mostre ao usuário: `🔎 [classe] "<afirmação>" → <item> — <justificativa> [fonte]`.
   Classes `conflitante` e `complementar` sobre itens `validado` exigem confirmação.

## 3. Análise de impacto (Adaptive + grafo)

**Complexidade** (decide a profundidade):

| Complexidade | Critério | Profundidade |
|---|---|---|
| `simples` | 1 item afetado, sem dependentes | `impacto <ID> --depth 1`; sem retrieve extra |
| `moderada` | 2–5 itens ou 1 sistema | `--depth 2` + `retrieve --activity validacao` para checar as fontes |
| `complexa` | cruza sistemas, regras validadas ou backlog pronto; ou mudança de escopo | `--depth 3` + retrieve por sistema afetado + perfis responsáveis |

Execute `python3 -I <skill>/scripts/recop.py impacto <ID> --depth N` a partir de cada item
diretamente afetado. O resultado lista requisitos dependentes, achados, sistemas,
histórias e épicos, com o caminho (`via`). Leia os itens alcançados e decida se cada um é
**afetado de fato**; o grafo indica candidatos, não certezas.

## 4. Pedido de mudança (CR)

Crie `CR-NNN` em `mudancas.json` e `.re/mudancas/CR-NNN.md`:

```markdown
# CR-001 — <título>
- Gatilho / origem: manual · [doc: …]
- Classe: conflitante · Complexidade: complexa · Baseline: B-001
## Mudança proposta
<antes → depois, por item>
## Impacto
| Item | Tipo | Como é afetado | Ação proposta |
## Riscos e esforço relativo
## Perfis a consultar
## Recomendação
```

Pergunte: **Aprovar / Ajustar / Rejeitar** (AskUserQuestion).

- **Aprovar:** aplique. Requisitos: `versao+1`, `historico` com `antes` e `mudanca`,
  status `alterado` (se havia baseline) ou `confirmado`. Histórias e features afetadas:
  `revisar`. Achados resolvidos: `tratado`. CR: `aplicada`. **Reveja as perguntas abertas
  ligadas aos itens afetados:** a resposta pode ter mudado, ou a pergunta pode ter ficado sem
  sentido (cancele ou reescreva). Depois `check` + `lint` + `render` e regenere os
  entregáveis afetados.
- **Rejeitar:** CR `rejeitada` com o motivo; o item conflitante volta ao status anterior.
- **Ajustar:** reescreva o CR e pergunte de novo.

## 5. Baseline

Comando `baseline`: confirme com o usuário, passe `alterado` para `validado` (somente se o
usuário revalidou) e rode `recop.py baseline --nota "<motivo>"`, que congela requisitos e
backlog em `.re/baselines/B-NNN.json` e grava `state.json.baseline`. Ela é recusada se o
modelo estiver inconsistente ou houver requisito em `conflito`.

`recop.py diff [B-NNN]` lista o que foi criado, removido e alterado desde a baseline. Use-o
para atualizar `entregaveis/mudancas.md` (junto com os CRs aplicados e rejeitados).

## 6. Métricas — `.re/log-rag.jsonl`

Além das linhas de retrieve (`rag.md`), registre uma linha por decisão:

```json
{"ts": "…", "evento": "classificacao", "gatilho": "manual", "afirmacao": "…", "classe_proposta": "conflitante", "classe_final": "conflitante", "itens": ["RN-004"], "estrategia": "corrective_rag"}
{"ts": "…", "evento": "impacto", "cr": "CR-001", "complexidade": "complexa", "depth": 3, "n_candidatos": 9, "n_afetados": 6, "decisao": "aprovada"}
```

`classe_final` é a decisão depois da revisão do usuário. Com isso dá para medir a
precisão do classificador e quantos candidatos do grafo eram afetados de fato.
