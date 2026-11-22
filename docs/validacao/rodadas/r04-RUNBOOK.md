# Rodada 04 — runbook

**Pergunta:** a v4 mantém a qualidade e recupera a cobertura, em um caso que ela nunca viu?

| Condição | O que é |
|---|---|
| `c1` | IA comum |
| `c2` | skill timovi |
| `c6` | re-copilot v4 |

Para iniciar, abra o Claude Code na raiz do repositório e diga: **"execute docs/validacao/rodadas/r04-RUNBOOK.md"**.
Para retomar depois de uma interrupção, diga a mesma coisa: o passo 0 mostra onde parou.

## Instruções para o agente que conduz

- Todos os dados ficam em `docs/validacao/experimento/r04/` (`$E`). Nunca em `/tmp`.
- Rode os passos em ordem. A autorização vale só para esta rodada. Não faça commit nem push.
- Não leia `$E/sealed/` nem o mapa cego antes do passo 8. Não ajude nem corrija nenhum participante.
- Registre em `$E/custos.csv` (`etapa,condicao,tokens,ferramentas,duracao_ms`) o uso informado ao fim de cada agente.
- Limite de uso atingido: pare, informe o usuário e não refaça nada. Agente interrompido: retome com SendMessage. Se não
  puder, crie outro com o mesmo prompt mais "continue do que está em disco".
- Caminhos absolutos nos prompts: substitua `<REPO>` pela raiz do repositório.

## Passos

**0. Situação.** `python3 -I docs/validacao/rodada.py status` e siga do primeiro passo pendente.

**1. Preparar.** `python3 -I docs/validacao/rodada.py preparar` (copia a skill de `../re-copilot`, ou de `$RE_COPILOT`). Se acusar problema, pare e informe.

**2. Criar o caso.** Um agente, com o prompt A. Depois: `python3 -I docs/validacao/rodada.py selar`.

**3. Etapa 1.** Três agentes em segundo plano, com os prompts B1, B2 e B6.

**4. Oráculo.** Quando todos terminarem: `rodada.py oraculo`; um agente com o prompt C; `rodada.py respostas`. Envie a cada
participante: "As respostas estão em entrega/respostas.md. Execute a Etapa 2 do BRIEFING.md, mantendo as mesmas regras de método."

**5. Etapa 2 e 3.** Quando um participante concluir a etapa 2: `rodada.py mudancas`, e envie a ele: "Chegaram comunicações
novas em mudancas/. Execute a Etapa 3 do BRIEFING.md, mantendo as mesmas regras de método."

**6. Avaliação cega.** Quando os três concluírem: `rodada.py juizes` e dois agentes com o prompt D (arquivos `juiz-1.json` e `juiz-2.json`).

**7. Checagem da skill.** Em `$E/runs/c6`, rode `recop.py verificar --docs entrega` e `lint`, com o `recop.py` de `$E/skills/re-copilot/scripts/`.
Copie a contagem para o relatório.

**8. Resultado.** `rodada.py resultado`. Escreva `docs/validacao/resultados/rodada-04.md`, como a `rodada-02.md`: conclusão,
tabela, o que ainda é fraco e limitações. Diga claramente se a cobertura melhorou. Não favoreça a skill; se ela perder, escreva.

## Se o limite for curto

Pule `c2` (use `--condicoes c1,c6` em todos os comandos) e use um juiz só. O resultado fica mais fraco: registre isso.

## Prompts

### A. Autor do caso
```
Você vai criar um CASO DE TESTE FICTÍCIO para avaliar ferramentas de levantamento de requisitos. Trabalhe SOMENTE em
<REPO>/docs/validacao/experimento/r04/caso (é o único caminho do repositório que pode abrir). Não leia ~/.claude/skills,
~/.agents, ~/workspace/.agents nem outras pastas de ~/workspace/labs. Não invoque skills nem crie subagentes: você precisa ser
independente das ferramentas avaliadas.

Domínio: uma rede fictícia de escolas particulares (invente o nome; dados claramente falsos) quer um sistema único de
MATRÍCULAS, BOLSAS E INADIMPLÊNCIA. Projeto puxado por Secretaria Escolar, Financeiro, Coordenação Pedagógica e Jurídico. Tudo em
português do Brasil.

Produza:
- escopo.md: o que o patrocinador escreveria (10-15 linhas, sem entregar achados).
- fontes/<SIS-NN-nome>/ e fontes/geral/, com 3 sistemas e documentação geral: 1 dump SQL do sistema acadêmico com DDL, constraints,
  triggers e algumas linhas de dados (INSERT/COPY); 1 dump ou export do financeiro; 1 planilha de controle de bolsas (.csv com
  cabeçalho e linhas, mais um .md com as regras); 1 manual possivelmente desatualizado; 1 regimento ou política; 1 ata; 1 fluxo em
  Mermaid ou texto. De 10 a 14 arquivos curtos e realistas, escritos como documentos reais: NUNCA rotule problemas como "divergência",
  "risco" etc.
- mudancas/M-01-*.md e mudancas/M-02-*.md: comunicações posteriores ao levantamento, com 5 afirmações, ao menos uma de cada classe: novo,
  existente, conflitante, complementar, fora do escopo.
- oraculo.md: fatos para um stakeholder simulado responder: quem decide, qual regra prevalece em cada divergência, volumes, prioridades, e 3
  assuntos com resposta "não sei, pergunte a X". Sem listar achados como tais e sem contradizer as fontes.
- gabarito.md, com IDs estáveis e, por item, onde está a evidência:
  - D1..Dn (mínimo 8): mesmo conceito diferente entre sistemas ou documentos, com valores e arquivos. Ao menos 2 visíveis só cruzando DDL ou trigger com documento.
  - G1..Gn (mínimo 4) gargalos; R1..Rn (mínimo 6) riscos, com ao menos 1 legal ou de dados de menores escondido na estrutura de dados;
    P1..Pn (mínimo 3) pontos de apoio; O1..On (mínimo 4) oportunidades. Ao menos 2 itens só aparecem fazendo contas ou cruzando linhas da planilha.
  - T1..Tn (mínimo 5) armadilhas: coisas que PARECEM divergência ou erro mas NÃO são. Use tipos variados.
  - Tabela de classificação das mudanças: afirmação, classe esperada e temas impactados.

Não coloque dica de gabarito em fontes/, escopo.md ou mudancas/. Confira que cada item é sustentado pelos arquivos e que os fatos são coerentes.
Responda só com a contagem de arquivos e de itens por categoria.
```

### B1. IA comum
```
Seu diretório de trabalho é <REPO>/docs/validacao/experimento/r04/runs/c1 (use caminhos absolutos ou cd nele em cada comando). Leia BRIEFING.md e
execute a Etapa 1.

Método: use somente seu conhecimento e as ferramentas básicas (ler, buscar e escrever arquivos, shell). Não invoque skills, não crie subagentes e não leia
nada fora do seu diretório de trabalho.
```

### B2. timovi
```
Seu diretório de trabalho é <REPO>/docs/validacao/experimento/r04/runs/c2 (use caminhos absolutos ou cd nele em cada comando). Leia BRIEFING.md e
execute a Etapa 1.

Método: siga a skill "timovi", em <REPO>/docs/validacao/experimento/r04/skills/timovi. Comece por SKILL.md e leia as referências e os papéis que ela indicar; mantenha o
estado dela (.product-team/) neste diretório. Como ninguém pode responder durante a execução, nas perguntas interativas do bootstrap infira do escopo e das fontes o que
for possível, registre a suposição e leve o que faltar para entrega/perguntas.md. Use a skill até planejamento, especificação e breakdown; não execute código, git ou deploy.
As entregas do BRIEFING mantêm os nomes em entrega/. Leia a skill direto dos arquivos, sem a ferramenta Skill, não crie subagentes e não leia nada fora do seu diretório e da
pasta da skill.
```

### B6. re-copilot v4
```
Seu diretório de trabalho é <REPO>/docs/validacao/experimento/r04/runs/c6 (use caminhos absolutos ou cd nele em cada comando). Leia BRIEFING.md e
execute a Etapa 1.

Método: siga a skill "re-copilot", em <REPO>/docs/validacao/experimento/r04/skills/re-copilot (esse é o `<skill>`). Comece por SKILL.md e leia as referências e os papéis que ela
indicar; mantenha o estado dela (.re/) neste diretório. Como ninguém pode responder durante a execução, use o modo "Delegado" e leve as perguntas para entrega/perguntas.md.
Escolha o modo de leitura como a skill indica. As entregas do BRIEFING mantêm os nomes em entrega/, além dos artefatos em .re/. Leia a skill direto dos arquivos, sem a ferramenta
Skill, não crie subagentes e não leia nada fora do seu diretório e da pasta da skill.
```

### C. Oráculo
```
Leia e siga <REPO>/docs/validacao/instrucao-oraculo.md (só esse arquivo fora do seu diretório). Diretório: <REPO>/docs/validacao/experimento/r04/oraculo. Não leia nada fora dele.
```

### D. Juiz (N = 1 e 2)
```
Leia e siga <REPO>/docs/validacao/instrucao-juiz.md (só esse arquivo fora do seu diretório). Diretório: <REPO>/docs/validacao/experimento/r04/juizes. Não leia nada fora dele.
Métodos: as pastas com letras. Escreva o resultado em juiz-N.json, sem abrir o de outro juiz: sua avaliação deve ser independente.
```
