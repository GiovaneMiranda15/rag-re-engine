# Entrevista por perfil

Você assume a persona do perfil e entrevista o usuário pela ótica dele. O usuário responde
como stakeholder (ou repassa a pergunta para quem souber). Você **pergunta**; nunca
responde por ele.

## Preparação (ao entrar em um perfil)

1. Leia `roles/<perfil>.md`. Perfil inexistente → crie a partir de `roles/_template.md`,
   salve em `.re/perfis/<perfil>.md` e mostre ao usuário em 3 linhas antes de começar.
2. Leia `escopo.md` e, no modelo, os itens ligados ao perfil: requisitos (`perfis`),
   perguntas `aberta` com `responsavel` = perfil e achados `aberto` do tema do perfil.
3. Rode as consultas de "Consultar antes de perguntar" (RAG por sistema e código) e anote
   o que já se sabe. Pergunte só o que falta.
4. Apresente-se em uma linha com o número de perguntas previsto (meta: 6–12 por rodada) e os temas.

   > 💰 **[Financeiro]** Vou olhar aprovação e pagamento de reembolsos. Encontrei 2
   > divergências de limite entre o portal e a política. Umas 8 perguntas.

## Ciclo de cada pergunta

1. **Escolha:** primeiro o que resolve achados críticos e perguntas abertas do perfil;
   depois o que bloqueia outros requisitos; depois as perguntas-semente não cobertas.
2. **Consulte** se a resposta já existe. Se existir, transforme a pergunta em confirmação
   citando a fonte:
   > Encontrei no portal `[sql: SIS-01/schema.sql:ck_limite_diaria]` limite de diária de R$ 300,
   > e na política `[doc: geral/politica-viagens.md#2]` limite de R$ 400.
   > Qual dos dois vale para o novo sistema?
3. **Pergunte:** uma por vez, prefixada pelo perfil. Use **AskUserQuestion** quando houver
   2–4 alternativas plausíveis (o usuário sempre pode responder livremente); senão,
   pergunte em texto e espere.
4. **Classifique** a resposta com o classificador (`manutencao.md` §2): novo, existente,
   conflitante, complementar ou fora do escopo. "Não sei" vira pergunta `aberta` com
   responsável sugerido. Resposta que resolve um achado → achado `tratado`, com a
   pergunta registrada em `gera`.
5. **Aprofunde se vago:** uma pergunta para tornar a resposta verificável (número,
   condição, exemplo, exceção).
6. **Persista:** anexe Q/R em `.re/entrevistas/<perfil>.md`, atualize o modelo JSON
   (requisitos, perguntas, achados) e `state.json` (`proximo_id`, contagem do perfil).
7. **Feedback curto** (1–2 linhas):
   > ✔️ RN-006 confirmado: "Limite de diária de R$ 400 por dia de viagem, em todos os canais."

Ao fim de cada 3–4 perguntas, ou ao encerrar o perfil, rode `recop.py check` e `render`.

### Formato do log `entrevistas/<perfil>.md`

```markdown
# Entrevista — financeiro
## Rodada 1 — 2026-11-03
**Q-015** Qual limite de diária vale para o novo sistema? (DIV-002)
**R:** O da política; o portal está desatualizado.
→ RN-006 confirmado · DIV-002 tratado · classe: conflitante (portal) resolvido
```

## Hipóteses do perfil

O perfil pode levantar preocupações típicas da área ("normalmente pagamento precisa de
trilha de auditoria"). Isso **não** vira requisito: pergunte se se aplica. Registre como
`hipótese` (`fontes: ["hipótese:<perfil>"]`) só se o usuário pedir para anotar.

## Encerramento do perfil

Quando os temas estiverem cobertos, o usuário disser "próximo" ou a meta for atingida:

```
💰 [Financeiro] — resumo
Criados: RN-006, RF-012 · Atualizados: RN-002 (v2) · Achados tratados: DIV-002, GAR-003
Pendências: Q-021 (quem aprova reembolso na ausência do gestor?) → gestao-pmo
```

Marque o perfil `concluido` (ou `em_andamento` se ficou pendência) e sugira o próximo.

## Modos

- **Padrão:** uma pergunta por vez.
- **Rápido** (a pedido): até 4 perguntas numeradas por mensagem; o usuário responde em bloco.
- **Painel** ("rodada com todos"): uma pergunta curta de cada perfil sobre o mesmo tema, para cruzar visões.
- **Delegado** ("vou repassar para o financeiro"): gere a lista de perguntas do perfil em
  `.re/entrevistas/<perfil>-questionario.md` para o usuário enviar; quando as respostas
  voltarem (colar ou arquivo), processe cada uma pelo ciclo acima. Cada pergunta traz: o que as
  fontes já dizem, com citação, **uma** decisão pedida (não acumule temas), e a premissa que será
  usada se ninguém responder. Ordene pelo que destrava mais requisitos.
