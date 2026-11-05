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

| Defeito | Causa | Melhoria proposta (não implementada) |
|---|---|---|
| `confirmado` inflado | proposta documentada contada como decisão | distinguir origem: decisão humana × documento vigente × proposta; proposta nunca confirma |
| Confirmado com pergunta aberta | `lint` não cruza pergunta e requisito | apontar confirmado ligado a pergunta aberta |
| Contradição entre requisitos | só o agente detecta | revisar pares do mesmo tema, com `candidatos`, antes de entregar |
| Agrupamento em um só requisito | referência a outra documentação | limitar tamanho e exigir critério por comportamento |
| Hipótese invisível em `backlog.md` | a marca não sai no `render` | incluir label e status na visão gerada |
| Fontes linkadas não lidas | sem varredura de ligações | relatório de fontes citadas e não lidas |
| Motor considerado indisponível em execução delegada | restrições do agente | documentar o uso do motor em subagentes |
| Máscara de segredos falhou ao conferir código | filtro por `chave=valor` | nunca imprimir arquivo com token conhecido; filtrar também cabeçalhos `Bearer` |

## Limites

Uma execução, um auditor de IA, sem execução do sistema e sem opinião humana. A validade para o TCC depende da avaliação do engenheiro e
da reunião de validação, ainda não ocorrida.
