# Rodada 02 — re-copilot v3 em caso novo

Executada em 2026-11-04 e 2026-11-05. Protocolo em `../README.md`. Resultado completo em `hospital-v3.json`.

A v3 foi ajustada com o feedback dos juízes no caso de RH. Para evitar sobreajuste, foi testada em um **terceiro
caso, novo** (`hospital-compras`: compras e contratos de manutenção de uma rede de hospitais), criado por um
agente sem acesso à skill, com 8 armadilhas de tipos variados. Dois juízes cegos, sem CSV descartado e com
amostra de citações por sorteio.

## Conclusão

**A v3 passou a ter a melhor documentação, mas a menor cobertura.** Média de qualidade 4,86, contra 4,00 da
timovi e 4,00 da IA comum, ao custo próximo da timovi. Em compensação, encontrou um pouco menos do gabarito
(92%, contra 99% da timovi e 96% da IA comum).

| Métrica | c1 IA comum | c2 timovi | c5 re-copilot v3 |
|---|---|---|---|
| Cobertura total | 0,959 | **0,986** | 0,919 |
| Divergências | 1,00 | 1,00 | 0,96 |
| Riscos | 0,95 | 0,95 | 0,90 |
| Oportunidades | 0,80 | **1,00** | 0,80 |
| Apoio | 1,00 | 1,00 | 0,90 |
| Armadilhas caídas (de 8) | 0 | 0 | 0 |
| Adicionais sem suporte (de 10) | 1,5 | 2,5 | 2,5 |
| Afirmações falsas | 0 | 0 | 0 |
| Citações corretas (de 10) | 9,5 | 9,5 | 9,5 |
| Classificação de mudanças | 0,90 | **1,00** | **1,00** |
| Impacto de mudanças | 1,00 | 1,00 | 1,00 |
| Negócio | 4,0 | 4,0 | **5,0** |
| Técnico | 3,5 | 4,0 | **5,0** |
| Backlog | 3,5 | **4,0** | **4,0** |
| Rastreabilidade | 4,0 | 3,0 | **5,0** |
| Manutenção | 4,0 | 4,0 | **5,0** |
| Honestidade | 4,0 | **5,0** | **5,0** |
| Perguntas | 4,0 | 4,0 | **5,0** |
| **Média de qualidade** | 4,00 | 4,00 | **4,86** |
| Duração somada | 26,8 min | 36,4 min | 35,8 min |
| Ferramentas | 25 | 53 | 52 |
| Contexto final | 182 mil | 245 mil | 292 mil |

Medidas objetivas em `hospital-objetivas.json`: 9 de 9 entregas e CSVs válidos nas três condições.

## O que explica a melhora

- `recop.py verificar` e `lint` saíram limpos na v3: nenhum número sem fonte em item confirmado, nenhuma citação
  inválida, toda divergência com checagem de falso positivo. As ferramentas forçam o que a instrução sozinha não garantiu.
- Rastreabilidade gerada por script: nota 5, contra 3 e 4.
- O modo direto trouxe o tempo de 57 min (v2) para 36 min, ao nível da timovi, mas sem o motor RAG.

## O que ainda é fraco

- **Cobertura:** a v3 ficou abaixo das duas alternativas. Hipóteses a investigar, sem confirmação:
  1. a regra de "uma decisão por pergunta" obteve bem menos informação do oráculo (385 palavras de resposta, contra
     929 e 735), o que é coerente com a nota 5 em perguntas, mas custa conteúdo quando há um limite de 15 perguntas;
  2. o esforço de estrutura pode tirar atenção da varredura das fontes.
- **Sem armadilhas para nenhuma condição:** nenhuma caiu aqui; portanto, este caso não mostra se a regra nova
  evitou falsos positivos.

## Limitações

- **Uma execução por condição** e um único caso novo: é um indício forte de direção, não prova.
- **Concordância de 100% entre juízes** (kappa 1,00): são o mesmo modelo, então isso não atesta que as notas
  estão corretas. Falta avaliação humana.
- **O juiz valoriza a estrutura:** a rubrica dá nota alta a formatos que a v3 foi ajustada para produzir. É preciso
  ver se engenheiros reais também preferem.
- **RAG não testado nesta rodada:** a v3 escolheu o modo direto (72 KB de fontes). A avaliação das arquiteturas segue na
  `rodada-01.md`.
- **Não testado:** modo interativo com pessoa, ativação pelo comando `re-copilot` (os agentes leram os arquivos
  da skill), manutenção entre sessões, projetos grandes e importação real no Jira e no Azure DevOps.
