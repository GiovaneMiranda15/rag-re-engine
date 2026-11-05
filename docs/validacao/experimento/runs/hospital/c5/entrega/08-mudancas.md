# Avaliação de mudanças

**Projeto:** sistema único de compras e contratos de manutenção de equipamentos. **Data:** 04/11/2026. **Baseline:** nenhuma; as mudanças foram aplicadas direto e registradas no histórico.
**Comunicações avaliadas:** `M-01-email-suprimentos.md` (Suprimentos, 21/10/2026) e `M-02-memorando-juridico-engclin.md` (Memorando 2026/14, Jurídico e Engenharia Clínica, 03/11/2026).
**Decisões sem interlocutor:** ninguém pôde aprovar durante a execução. Apliquei o que não contradiz nada e deixei o conflito sem resolver.

## Resumo

| # | Afirmação | Classe | Item | Situação |
|---|---|---|---|---|
| M-01.1 | Hospital Aurora Serra será incorporado em janeiro de 2027, com dois contratos, que entram no sistema único | **novo** | RF-021, CR-001 | Aplicado; dados pendentes |
| M-01.2 | Contratos com valor global acima de R$ 250 mil continuam aprovados pela Diretora Geral | **existente** | RN-002 | Só reforço de fonte |
| M-01.3 | Farmácia pede controle de validade de lotes de medicamentos no estoque | **fora_escopo** | Escopo | Registrado; sem requisito |
| M-02.1 | Parecer jurídico só acima de R$ 200.000,00 de valor global, daqui em diante | **conflitante** | RN-005, RN-028, DIV-019, CR-002 | **Não aplicado**; decisão em Q-019 |
| M-02.2 | Soma das glosas limitada a 10% do valor mensal por competência | **complementar** | RN-017 v3, CR-003 | Aplicado |

## M-01.1: Hospital Aurora Serra (novo)

**Justificativa.** Nenhum item tratava de uma quinta unidade. O escopo e a POL-SUP-004 §1.1 falam em quatro.

**Impacto nos requisitos.** Criado RF-021 (confirmado: a fonte é o e-mail). RNF-005 v2: o volume da unidade fica a definir. Novo risco RIS-017.

**Impacto no backlog.** Nova história US-043, bloqueada por Q-020 e Q-021. Em revisão: US-040 (migração), US-035 (visão da rede) e US-042 (capacidade).

**Impacto nos documentos.** Escopo; negócio (seções 3, 5, 9, 10); técnico (seções 3, 5, 8, 10, 11, 14, 15); diagnóstico; rastreabilidade; CSVs.

**Efeito concreto.** A carga passa de oito para dez contratos, com a incorporação em janeiro de 2027, antes da entrada em operação de 30/06/2027. O prazo não mudou.

**Limites.** [F] A comunicação não traz valores, vigência, SLA, equipamentos nem sistemas; nada disso foi estimado. [I] O e-mail relata a reunião do Comitê de 21/10/2026, cuja ata não está nas fontes. Convém confirmar com a Diretora Geral que a inclusão na fase 1 é uma extensão aceita do escopo.

**Alternativa considerada.** Deixar a unidade para a fase 2. Descartada porque o e-mail diz que os contratos precisarão entrar e não fala em fase; a decisão pode ser revista em Q-020.

**Avisar:** Diretora Geral, Jurídico, Engenharia Clínica, TI.

## M-01.2: Alçada acima de R$ 250 mil (existente)

**Justificativa.** Mesmo conteúdo da POL-SUP-004 §2 e §2.2, de RN-001 e RN-002, confirmado em Q-003. "Continuam" reforça que nada mudou.

**Impacto.** Requisitos: fonte acrescentada em RN-002, sem nova versão. Backlog e documentos: nenhum.

**Efeito concreto.** CT-2025-0064, com R$ 528.000,00 de valor global, continua na alçada da Diretora Geral. O ERP segue errado até ser ajustado, pois usa valor mensal (DIV-002).

## M-01.3: Lotes de medicamentos (fora_escopo)

**Justificativa.** O `escopo.md` exclui medicamentos, e a POL-SUP-004 §1.2 os deixa sob a POL-FAR-002. A semelhança com validade de calibração (RF-007, RN-015) é só de palavras: o controle aqui é de lote em estoque.

**Impacto.** Requisitos e backlog: nenhum. Documentos: registro em "fora do escopo" no `.re/escopo.md` e na seção 3 do documento de negócio; cenário de teste 36.

**Avisar:** Gerente de Suprimentos, para responder à Farmácia. Incluir o tema exigiria uma mudança de escopo aprovada pela patrocinadora.

## M-02.1: Parecer acima de R$ 200 mil (conflitante)

**Justificativa.** Contradiz a POL-SUP-004 §4.5 (R$ 30.000,00), aprovada pela Diretoria, e a resposta do próprio Jurídico em Q-006 ("vale a Política"). O memorando não cita revisão da política, nem aprovação da Diretoria, e é assinado por áreas que não a aprovaram. `respostas.md` não tem data, então não dá para dizer qual manifestação veio por último.

**Impacto nos requisitos.** RN-005 fica com status `conflito`, com o enunciado mantido. RN-028 registra a versão do memorando, também em `conflito`. Novo achado DIV-019. DIV-005 continua tratado quanto ao fluxo, que agora é um terceiro valor (R$ 100.000).

**Impacto no backlog.** US-011 em revisão e bloqueada por Q-019, com o limite de R$ 30.000,00 até a decisão. US-020 já prevê limite como parâmetro com vigência, então mudar o valor não exige redesenho.

**Impacto nos documentos.** Negócio (seções 1, 5, 6.1, 7, 9, 10, 11); técnico (seções 3, 7, 8, 10); diagnóstico (DIV-019). Os cenários 14 e 15 ficam condicionados.

**Efeito concreto, pelo valor global.**

| Contrato | Valor global | Regra de R$ 30.000,00 | Regra de R$ 200.000,00 |
|---|---|---|---|
| CT-2026-0021 | R$ 58.800,00 | Exige | Não exige |
| CT-2025-0102 | R$ 163.200,00 | Exige | Não exige |
| Outros seis contratos | Acima de R$ 200.000,00 | Exige | Exige |

[I] O limite maior reduziria a fila de GAR-001 (23 dos 38 dias), mas o tamanho da redução não pode ser medido com as fontes.

**Recomendação [H].** Manter R$ 30.000,00 até haver revisão da política ou ato da Diretoria. Se for confirmado, RN-028 substitui RN-005, e o fluxo e os critérios de US-011 são atualizados.

**Alternativa considerada.** Aplicar o memorando por ser o documento mais recente. Descartada porque a data sozinha não dá autoridade sobre uma política da Diretoria, e o conflito não pode ser resolvido em silêncio.

**Avisar:** Diretora Geral (decide), Diretor Financeiro, Jurídico, Suprimentos. Enquanto isso, as áreas não devem dispensar parecer com base no memorando.

## M-02.2: Limite de 10% para glosas (complementar)

**Justificativa.** Restringe a soma sem contradizer os 2% por evento da POL-SUP-004 §5.3, que não tem limite. Não muda a regra de cálculo.

**Impacto nos requisitos.** RN-017 v2 → v3. Antes: "calcular glosa de 2% do valor mensal por evento". Depois: acrescenta "com soma limitada a 10% do valor mensal do contrato em cada competência".

**Impacto no backlog.** US-032 em revisão, com dois critérios novos. US-033 e Q-010 seguem abertas, e essa pergunta agora inclui se o limite incide sobre glosa proposta ou aceita.

**Impacto nos documentos.** Negócio (seções 5, 7); técnico (seções 3, 7, 10); diagnóstico (RIS-006).

**Efeito concreto.** CT-2024-0117, com R$ 11.040,00/mês: 1 evento = R$ 220,80; o limite é R$ 1.104,00; 5 eventos o atingem; o 6º não aumenta o valor. Na regra anterior, 6 eventos dariam R$ 1.324,80. A OS 88170 não muda.

**Ponto de atenção [I].** A partir do 6º evento na competência, não há desconto adicional. O Diretor Financeiro não assina o memorando, e a política não foi alterada formalmente. Como não há contradição, apliquei, e registrei a validação pendente na seção 11 do documento de negócio.

**Alternativa considerada.** Requisito separado. Descartada porque o limite só existe junto com o cálculo.

**Avisar:** Diretor Financeiro, Engenharia Clínica.

## O que mudou nas entregas

| Entrega | Mudança |
|---|---|
| `01-diagnostico.md` | Seção 0, matriz e riscos: DIV-019, RIS-017, RIS-006 |
| `02-negocio.md` | Escopo, decisões, regras, requisitos por área, pendências, riscos, validação, histórico |
| `03-tecnico.md` | Requisitos, regras, mudanças em sistemas, cenários 33 a 36, migração, de-para, integrações, pendências |
| `04-backlog.md` | US-043 nova; US-011, US-032, US-035, US-040, US-042 em revisão |
| `05-jira.csv`, `06-azure-devops.csv` | Regenerados com o backlog atual |
| `05-jira-delta.csv`, `06-azure-devops-delta.csv` | Novos: só os itens em revisão, para atualizar o que já tiver sido importado. Reimportar o CSV completo cria duplicados |
| `07-rastreabilidade.md` | Regenerado, com CR-001, CR-002 e CR-003 |

**Modelo:** RF-021 e RN-028 criados; RN-005 v3 (conflito), RN-017 v3, RNF-005 v2; RN-002 com fonte nova; DIV-019 e RIS-017 criados; Q-019, Q-020 e Q-021 abertas; CR-001 e CR-003 aplicados; CR-002 proposto. Baseline não criada: há requisitos em conflito, e a skill a recusaria.

**Checagens:** `recop.py check` e `verificar --docs` saíram limpos. O `lint` aponta só Q-010, Q-020 e Q-021 como perguntas abertas ligadas a mudanças: foram revistas e continuam válidas, aguardando resposta.

## Decisões pedidas

| Pergunta | Decisão | Para quem |
|---|---|---|
| Q-019 | R$ 30.000,00 ou R$ 200.000,00, e se há ato da Diretoria | Diretora Geral, com o Jurídico |
| Q-020 | Dados de contratos, equipamentos e sistemas do Hospital Aurora Serra | Gerente de Suprimentos |
| Q-021 | Política aplicável ao Hospital Aurora Serra e tratamento de contratos anteriores | Jurídico |
