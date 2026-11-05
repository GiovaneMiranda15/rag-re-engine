# Diagnóstico do cenário atual

Objetivo: entender **como funciona hoje**, cruzando os sistemas, antes de definir o que
será construído. Saída: `elementos.json`, `achados.json`, hipóteses de requisito,
perguntas e o relatório `.re/entregaveis/negocio/diagnostico.md`.

## 1. Decompor (Agentic)

Quebre o escopo em processos de ponta a ponta (ex.: solicitação de reembolso →
conferência → aprovação → pagamento → contabilização). Para cada processo, monte subconsultas:

- atores e responsáveis; etapas e sistemas por etapa;
- entidades de dados e quem é a fonte da verdade;
- regras (limites, cálculos, alçadas, validações, status e transições);
- integrações (direção, meio, frequência, tratamento de falha);
- indicadores, volumes e tempos citados; restrições legais.

## 2. Coletar por sistema

Para cada subconsulta, rode o retrieve **por sistema** (`--sistema SIS-01`, depois
`SIS-02`…) e também sem filtro. Dumps SQL: leia constraints, triggers e procedures; são
regras de negócio escondidas. Registre o que existe em `elementos.json` (com fonte).

## 3. Cruzar e classificar achados

| Achado | Como reconhecer | Exemplo |
|---|---|---|
| `DIV` divergência | o mesmo conceito com valor, regra ou definição diferente entre sistemas, ou entre sistema e documento | limite de diária R$ 300 no portal × R$ 400 na política |
| `GAR` gargalo | passo manual, redigitação, fila, espera, planilha intermediária, retrabalho | conferência manual de cada comprovante |
| `RIS` risco | falha possível com impacto (operacional, financeiro, legal, segurança, dependência de pessoa ou fornecedor) | pagamento em lote sem confirmação de retorno |
| `APO` ponto de apoio | o que funciona e deve ser preservado ou reaproveitado (regra automatizada, cadastro confiável, processo maduro) | validação automática de centro de custo |
| `OPO` oportunidade | ganho que o projeto habilita (eliminar gargalo, unificar, automatizar, novo canal) | aprovação pelo celular |

Para confirmar uma divergência, rode `retrieve --activity analise` com o enunciado da
regra; aceite só se as evidências realmente sustentarem os dois lados. Similaridade alta
não é prova.

**Antes de registrar `DIV`, descarte falsos positivos.** Dois valores diferentes só são
divergência se valem para a mesma coisa, ao mesmo tempo:

1. **Vigência:** um dos documentos foi revogado, substituído ou é antigo? Procure comunicados
   e versões posteriores que citem o trecho. Trecho revogado não é divergência; o que pode
   ser achado é o documento antigo ainda circular.
2. **Abrangência:** um valor é total e o outro é subconjunto? Valem para públicos, categorias,
   locais ou períodos diferentes? Confira se a soma ou a segmentação explica a diferença.
3. **Definição:** os termos medem o mesmo conceito?

Se a diferença se explica, registre em `elementos.json` como fato, com a explicação e as
fontes, e não como `DIV`. Se não der para decidir, registre pergunta, não divergência. Todo `DIV`
guarda a checagem no campo `checagem`, e o `recop.py verificar` recusa os que não a têm:
`{"vigencia": "ambos vigentes: …", "abrangencia": "mesmo público: …", "definicao": "mesmo conceito: …"}`.

**Preserve os números.** Volume, percentual, tempo e quantidade de pessoas citados na fonte entram no
achado com o valor exato; "gargalo em X" sem o tamanho vale pouco. Olhe o efeito de cada regra errada em
datas e valores calculados, não só a divergência em si, e reúna o que se pode reaproveitar como
trilhas de auditoria e controles já existentes (`APO`). Não especule sobre obrigações que nenhuma fonte
cita: isso vira pergunta ao perfil responsável, sem afirmar lacuna.

Cada achado deve ter: fontes citadas de **cada** lado, sistemas, severidade (para riscos:
probabilidade × impacto) e o que gera (`gera`):

- divergência → pergunta para o perfil dono da regra ("qual vale?") e RN `hipótese`;
- gargalo / oportunidade → RF ou RNF `hipótese`;
- risco → RNF ou restrição `hipótese` e, se for de projeto, pergunta para `gestao-pmo`;
- ponto de apoio → `elementos.json` marcado para reaproveitamento + premissa no escopo.

## 4. Relatório

`.re/entregaveis/negocio/diagnostico.md`:

1. Resumo executivo: 5 a 8 linhas, com os 3 achados mais críticos.
2. Mapa dos sistemas: tabela sistema × papel × processos × entidades.
3. Por processo: fluxo atual (Mermaid `flowchart`), regras por sistema e achados.
4. Matriz de divergências: regra × sistema (célula = valor + fonte).
5. Riscos: tabela com probabilidade, impacto, severidade e mitigação sugerida.
6. Pontos de apoio e oportunidades.
7. Perguntas para validar o diagnóstico (por perfil).

Mostre o resumo ao usuário, peça validação dos achados críticos e proponha os perfis a
entrevistar com base nos responsáveis das perguntas.
