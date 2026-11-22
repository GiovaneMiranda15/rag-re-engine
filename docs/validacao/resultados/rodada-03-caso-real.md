# Rodada 03 — primeiro uso em projeto real

Registro de 2026-11-05. Cliente anonimizado: três sistemas em substituição a versões antigas (site e dois apps),
com ERP legado distribuído em filiais. Detalhes, achados e dados ficam com o cliente, fora deste repositório.

Modo direto, sem RAG, por decisão do agente diante das restrições da execução (cerca de 430 KB de texto). Sem gabarito e sem
outras condições: a auditoria por amostragem, feita por um agente, mede fidelidade às fontes, não comparação.

| Verificação | Resultado |
|---|---|
| Citações (amostra de 25) | 18 corretas, 7 parciais, 0 incorretas |
| Afirmações das notas do engenheiro (40) | 36 cobertas, 4 parciais, 0 ausentes |
| Respostas do engenheiro aplicadas (7) | 5 corretas, 2 parciais, 0 incorretas |
| `confirmado` com fonte real (amostra de 15) | 11; 4 deveriam ser hipótese |
| Afirmações críticas (11) | 9 sustentadas, 2 parciais, 0 sem suporte |
| Divergências registradas (7) | 5 reais, 2 parcialmente falso positivo |
| Histórias testáveis (amostra de 12) | 8 testáveis, 4 em parte |

Notas de 1 a 5: pauta 4, BRD 4, rastreabilidade 4, perguntas 4, SRS 3, honestidade 3.
Custo: 32 min somados nas etapas medidas, 116 ferramentas.

## O que aprender

O desempenho aqui foi **abaixo do caso sintético** (média de 3,67 contra 4,86), com a ressalva de que são
rubricas, juízes e condições diferentes. As notas mais baixas surgiram onde o sintético é fraco: fontes de qualidade desigual.

Só o que está marcado como testado foi verificado, com o modelo do caso real em cópia temporária e sem LLM. As mudanças
nas instruções ainda não passaram por uma execução completa.

| Defeito | Melhoria (v4) | Resultado no caso real |
|---|---|---|
| `confirmado` inflado | natureza da fonte; proposta e legado não confirmam; citação humana precisa tratar do assunto | **4 de 4** da amostra do auditor detectados; 6 outros ainda sem conferência |
| Requisito agrupado | `lint` conta referências e intervalos externos | 5 detectados (RF-024 a 027, RF-029) |
| Hipótese invisível em `backlog.md` | marca e bloqueio na visão gerada | testado com caso de teste |
| Fonte citada e não lida | `recop.py ligacoes` | achou a nota não registrada; 48 itens, com ruído de navegação |
| Vazamento de segredo | `recop.py ver`; `verificar` conta dados sensíveis sem mostrar valores | ocultou o token real; recusa arquivos de credenciais |
| Motor considerado indisponível | exige teste real antes de dispensar | não testado |
| Cobertura menor (rodada 02) | fazer as contas, varredura final e `fontes_sem_nenhum_item` | 12 fontes listadas; efeito na cobertura não testado |

**Não resolvidos:**

- **Contradição específica:** `pares` não acha o par do auditor. Só aparece com `candidatos "<verbo>" -n 40`, na posição 21, o que depende de o agente ler a lista. Não insisti para evitar sobreajuste a um único exemplo.
- **Pergunta aberta só em documento externo:** invisível para as checagens, porque não está no modelo. Virou instrução: importar as perguntas pendentes.
- **Repositório legado não lido:** quando a nota sobre ele está registrada, nada acusa que o código não foi lido.
- **Julgamento de conteúdo:** requisito que mantém regra legada com outra citação válida não é detectado.

## Limites

Uma execução, um auditor de IA, sem execução do sistema e sem opinião humana. A validade para o TCC depende da avaliação do engenheiro e
da reunião de validação, ainda não ocorrida.
