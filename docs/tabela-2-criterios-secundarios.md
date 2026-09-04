# Extensão do Framework de Decisão: Critérios Secundários de Refinamento

> Texto de apoio, em prosa acadêmica, pensado para ser incorporado à seção 4 ("Proposta") do TCC, como continuação direta da Tabela 1. Todas as citações abaixo foram verificadas diretamente nas fontes primárias (PDFs já anexados ao projeto e artigos originais consultados online), não apenas em resumos de terceiros.

## Nota preliminar: correções à Tabela 1 e às Referências

Antes de estender o framework, é necessário corrigir duas referências da proposta original, identificadas durante a verificação das fontes primárias:

- A citação de **Adaptive RAG** como "SARAVANAN et al., 2024, arXiv:2403.14481" está incorreta: esse identificador do arXiv corresponde a um artigo de neurociência computacional sem relação com Retrieval-Augmented Generation, e não existe trabalho de Adaptive RAG com autoria "Saravanan". A citação correta é:

  > JEONG, Soyeong; BAEK, Jinheon; CHO, Sukmin; HWANG, Sung Ju; PARK, Jong C. Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity. In: **Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)**, 2024. arXiv preprint arXiv:2403.14403.

- A citação de **RAPTOR** como "SAHA et al., 2024" está incorreta: a autoria real, confirmada via ICLR/DBLP, não inclui nenhum "Saha". A citação correta é:

  > SARTHI, Parth; ABDULLAH, Salman; TULI, Aditi; KHANNA, Shubh; GOLDIE, Anna; MANNING, Christopher D. RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval. In: **International Conference on Learning Representations (ICLR)**, 2024.

As demais referências de arquiteturas RAG usadas na Tabela 1 (GraphRAG — Edge et al., 2024; Self-RAG — Asai et al., 2024; Corrective RAG — Yan et al., 2024) foram confirmadas como corretas.

## Introdução

A Tabela 1 estabelece uma afinidade primária entre cada atividade da Engenharia de Requisitos e a arquitetura RAG cujo mecanismo central melhor endereça a natureza daquela atividade. Contudo, dentro de uma mesma atividade, a tarefa concreta enfrentada pelo analista pode variar em volume documental, estrutura dos dados, necessidade de rastreabilidade explícita, criticidade de auditoria e orçamento de latência disponível — dimensões já mencionadas na proposta original como fatores relevantes para a escolha arquitetural ("a natureza das bases de dados, a complexidade da tarefa e os limites de cada etapa de engenharia"). Esta seção formaliza essas dimensões como **critérios secundários de refinamento**, cada um ancorado no mecanismo técnico documentado no artigo original da respectiva arquitetura, e não em uma leitura genérica de suas características.

## Critérios secundários por arquitetura

### GraphRAG (atividade primária: Rastreabilidade)

**Critério:** a presença de dados com estrutura relacional explícita (por exemplo, vínculos entre requisitos, regras de negócio, casos de teste e trechos de código) reforça a adequação do GraphRAG frente às demais arquiteturas.

O RAG tradicional, ao segmentar documentos em blocos independentes, tende a negligenciar relações estruturais entre entidades — limitação que a arquitetura GraphRAG endereça diretamente ao construir um grafo de conhecimento sobre o corpus, permitindo recuperação que preserva interdependências entre conceitos (PENG et al., 2024). O artigo original de Edge et al. (2024) descreve o mecanismo de extração de entidades e geração de resumos hierárquicos de comunidades do grafo como o que viabiliza análises holísticas sobre relações estruturais nos dados.

Vale uma ressalva importante para a redação do TCC: os próprios autores de GraphRAG reconhecem, como limitação corrente da arquitetura, uma capacidade ainda fraca de preservar citações e exemplos específicos na resposta final gerada (EDGE et al., 2024). Ou seja, o GraphRAG é comprovadamente forte em **representar** interdependências estruturais entre entidades — o que sustenta seu uso quando a tarefa exige mapear relações —, mas isso não deve ser confundido com uma capacidade nativa de **rastrear a proveniência exata** de cada citação. Por isso, recomenda-se que este critério seja descrito como "estrutura relacional / interdependências explícitas entre artefatos", e não como "rastreabilidade de citação" em sentido estrito.

*Referências:* EDGE, Darren et al. From Local to Global: A Graph RAG Approach to Query-Focused Summarization. Microsoft Research, 2024. arXiv:2404.16130. PENG, Boci et al. Graph Retrieval-Augmented Generation: A Survey. **ACM Computing Surveys**, 2024. *(este survey já compõe o acervo do projeto, mas ainda não consta na lista de referências da proposta — recomenda-se incluí-lo, por ser a fonte mais direta para este critério).*

### Self-RAG (atividade primária: Análise)

**Critério:** alta criticidade de auditoria (baixa tolerância à geração de informação não sustentada pelos documentos-fonte) reforça a adequação do Self-RAG.

O mecanismo central do Self-RAG é o uso de *tokens* de reflexão que avaliam a própria geração durante a inferência — em particular o token `IsSup`, que determina "se todas as afirmações passíveis de verificação na saída são sustentadas pela passagem recuperada" (ASAI et al., 2024, tradução nossa). Os autores demonstram ainda que essa verificação é controlável em tempo de inferência: para tarefas que exigem forte aderência factual às evidências, o modelo pode ser ajustado para recuperar passagens com maior frequência e priorizar mais fortemente o critério de sustentação (`IsSup`), sem necessidade de retreinamento. Esse mecanismo mapeia diretamente para a necessidade de revisão crítica da atividade de Análise, especialmente quando a tolerância a erro é baixa.

*Referência:* ASAI, Akari; WU, Zeqiu; WANG, Yizhong; SIL, Avirup; HAJISHIRZI, Hannaneh. Self-RAG: Learning to Retrieve, Generate and Critique through Self-Reflection. In: **International Conference on Learning Representations (ICLR)**, 2024. arXiv:2310.11511.

### Corrective RAG — CRAG (atividades primárias: Análise e Validação)

**Critérios:** (a) alta criticidade de auditoria e (b) necessidade de busca externa complementar quando a base documental interna está incompleta ou desatualizada reforçam a adequação do CRAG.

O CRAG introduz um avaliador de confiança que classifica cada recuperação em três categorias — *Correct*, *Incorrect* e *Ambiguous* — e aciona uma busca web complementar precisamente quando "os escores de confiança de todos os documentos recuperados estão abaixo do limiar inferior" (YAN et al., 2024, tradução nossa), combinando as duas estratégias no caso ambíguo. Os próprios autores motivam esse desenho apontando que recuperadores de baixa qualidade "impedem o gerador de adquirir conhecimento preciso... resultando em problemas como alucinações" — exatamente o risco que a atividade de Validação busca mitigar ao confrontar requisitos com documentos de referência e regulamentos, e que a Análise busca mitigar ao revisar inconsistências conceituais.

*Referência:* YAN, Shi-Qi; GU, Jia-Chen; ZHU, Yun; LING, Zhen-Hua. Corrective Retrieval Augmented Generation. arXiv:2401.15884, 2024.

### RAPTOR (atividade primária: Especificação)

**Critério:** alto volume documental reforça a adequação do RAPTOR frente às demais arquiteturas.

Os autores motivam o RAPTOR observando que "a maioria dos métodos existentes recupera apenas blocos curtos e contíguos, limitando a compreensão holística do contexto geral do documento" (SARTHI et al., 2024, tradução nossa), propondo em vez disso a construção de uma árvore com múltiplos níveis de sumarização recursiva sobre o corpus. Os resultados reportados mostram ganho de até 20% de acurácia no benchmark QuALITY, que exige raciocínio multi-etapa sobre documentos longos — cenário diretamente análogo à especificação de sistemas a partir de bases documentais extensas e dispersas.

*Referência (corrigida — ver nota preliminar):* SARTHI, Parth et al. RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval. In: **International Conference on Learning Representations (ICLR)**, 2024.

### Adaptive RAG (atividade primária: Gerenciamento de Mudanças)

**Critério:** baixo orçamento de latência/recursos computacionais reforça a adequação do Adaptive RAG.

O Adaptive-RAG (nome correto da arquitetura — ver nota preliminar) emprega um classificador dedicado que estima a complexidade da consulta recebida e escolhe dinamicamente entre não recuperar, recuperar em uma única etapa ou recuperar em múltiplas etapas, buscando um custo computacional proporcional à real necessidade de cada consulta (JEONG et al., 2024). Esse mecanismo corresponde exatamente à necessidade de a atividade de Gerenciamento de Mudanças processar solicitações de alteração de complexidade variável sem incorrer no custo máximo de busca para toda e qualquer mudança.

*Referência (corrigida — ver nota preliminar):* JEONG, Soyeong et al. Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity. In: **NAACL**, 2024. arXiv:2403.14403.

### Agentic RAG (atividade primária: Elicitação)

**Critério:** disponibilidade de orçamento de latência/recursos alto é **pré-condição de viabilidade** para o uso do Agentic RAG — não um benefício em si.

A proposta original do TCC não cita um artigo específico sobre Agentic RAG; a referência mais adequada, identificada durante esta pesquisa, é o survey de Singh et al. (2025). É importante registrar com precisão o que a literatura de fato afirma: o survey não trata a alta tolerância a latência como uma vantagem do Agentic RAG, mas sim como um custo a ser gerenciado — "o uso de múltiplos agentes aumenta os requisitos de recursos para fluxos de trabalho complexos" e "a natureza dinâmica do sistema pode sobrecarregar os recursos computacionais em cenários de alto volume de consultas" (SINGH et al., 2025, tradução nossa). Por outro lado, o mesmo survey sustenta a afinidade primária já estabelecida na Tabela 1: o planejamento multiagente "permite que os agentes decomponham autonomamente tarefas complexas em subtarefas gerenciáveis", o que favorece diretamente a natureza iterativa e exploratória da Elicitação.

Recomenda-se, portanto, formular este critério secundário não como "latência alta beneficia o Agentic RAG", mas como "o Agentic RAG demanda, por natureza, maior orçamento de latência e recursos — custo documentado na literatura —, de modo que só deve ser recomendado quando esse orçamento está disponível". A regra prática de pontuação permanece a mesma (favorecer Agentic RAG quando `latency_budget = alto`), mas a justificativa textual no TCC deve refletir essa relação de pré-condição, não de benefício direto.

*Referência (nova — não constava na bibliografia original):* SINGH, Aditi; EHTESHAM, Abul; KUMAR, Saket; KHOEI, Tala Talaei. Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG. arXiv:2501.09136, 2025.

## Tabela 2. Critérios secundários de refinamento por arquitetura

| Arquitetura | Atividade primária (Tabela 1) | Critério secundário | Natureza da evidência | Fonte |
|---|---|---|---|---|
| GraphRAG | Rastreabilidade | Estrutura relacional/interdependências explícitas entre artefatos | Diretamente suportada | Edge et al., 2024; Peng et al., 2024 |
| Self-RAG | Análise | Alta criticidade de auditoria | Diretamente suportada | Asai et al., 2024 |
| Corrective RAG | Análise / Validação | Alta criticidade de auditoria; necessidade de busca externa complementar | Diretamente suportada | Yan et al., 2024 |
| RAPTOR | Especificação | Alto volume documental | Diretamente suportada | Sarthi et al., 2024 |
| Adaptive RAG | Gerenciamento de Mudanças | Baixo orçamento de latência/recursos | Diretamente suportada | Jeong et al., 2024 |
| Agentic RAG | Elicitação | Alto orçamento de latência/recursos disponível (pré-condição de custo, não benefício) | Inferência razoável, reformulada a partir de evidência direta sobre custo | Singh et al., 2025 |

## Adendo às Referências do TCC

Além das duas correções indicadas na nota preliminar, recomenda-se adicionar as seguintes entradas à lista de referências, na mesma formatação já usada na proposta:

```
JEONG, Soyeong; BAEK, Jinheon; CHO, Sukmin; HWANG, Sung Ju; PARK, Jong C. Adaptive-RAG: Learning
to Adapt Retrieval-Augmented Large Language Models through Question Complexity. In: Proceedings
of the 2024 Conference of the North American Chapter of the Association for Computational
Linguistics (NAACL), 2024.

SARTHI, Parth; ABDULLAH, Salman; TULI, Aditi; KHANNA, Shubh; GOLDIE, Anna; MANNING, Christopher D.
RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval. In: International Conference
on Learning Representations (ICLR), 2024.

PENG, Boci et al. Graph Retrieval-Augmented Generation: A Survey. ACM Computing Surveys, 2024.

SINGH, Aditi; EHTESHAM, Abul; KUMAR, Saket; KHOEI, Tala Talaei. Agentic Retrieval-Augmented
Generation: A Survey on Agentic RAG. arXiv:2501.09136, 2025.
```

E remover (ou substituir pelas corretas acima) as entradas atuais "SARAVANAN et al., 2024" e "SAHA et al., 2024. RAPTOR..." da lista de referências da proposta.
