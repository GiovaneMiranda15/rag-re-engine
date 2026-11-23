# Avaliação de mudanças

Projeto Admissão Única. Data: 04/11/2026. Baseline: sem baseline. Fontes avaliadas: `mudancas/M-01-ata-comite-2026-10-28.md` e `mudancas/M-02-email-juridico-2026-10-30.md`.

## Resumo

- **Decisão urgente:** Helena e Marina precisam decidir sobre a experiência de 45+45 antes de 01/12/2026 (CR-001). O sistema e as entregas seguem com 30+60 até lá.
- **Fora do escopo:** rescisão e homologação não entraram.
- **Aplicadas:** vacinação para injetáveis em SP (CR-002) e programa Acolher com CRNM (CR-003).
- **Sem efeito:** o reforço sobre CRF e a continuidade do ASO só reforçam o que existe.

## Classificação por afirmação

| ID | Afirmação | Classe | Item | Justificativa | Impacto nos requisitos | Impacto no backlog | Impacto nos documentos |
|---|---|---|---|---|---|---|---|
| M-01.1 | Nenhum farmacêutico, inclusive RT, inicia sem certidão com CRF ativo; protocolo não basta | **existente** | RN-003 | Mesmo conteúdo da RH-012 e de Q-006, com a mesma autora | Fonte acrescentada, sem nova versão. Q-029 e Q-030 seguem abertas | Nenhum | 07 |
| M-01.2 | Experiência padrão de 45+45 em toda a rede a partir de 01/12/2026 | **conflitante** | RN-002, DIV-002 | Contradiz a RH-012 e Marina (Q-005), que exige revisão aprovada por Helena e por ela. A ata registra informe de Sérgio, sem decisão ou revisão | RN-002 fica em conflito, com enunciado mantido; novos DIV-019, RIS-018, Q-050 e CR-001 (proposta). Se aprovado: RN-002, RF-009 e RF-024 mudam | US-004, US-005 e US-036 com label `aguarda-cr-001`, sem mudar texto | 01, 02, 03, 04, 07 |
| M-01.3 | Novo sistema deve nascer com 45+45 | **conflitante** | RN-002 | Mesma origem e mesmo conflito de M-01.2. RNF-009 permite trocar o valor por parâmetro, se aprovado | Como M-01.2 | Como M-01.2 | Como M-01.2 |
| M-01.4 | Incluir cálculo de rescisão | **fora_escopo** | Escopo | O escopo exclui desligamento e mantém a folha no sistema atual | Nenhum requisito; registrado em `.re/escopo.md`; Q-056 para Helena, que decide escopo | Nenhum | 02 |
| M-01.5 | Incluir homologação de desligamentos | **fora_escopo** | Escopo | O escopo exclui desligamento | Como M-01.4 | Nenhum | 02 |
| M-02.1 | A partir de 01/02/2027, quem vai aplicar injetáveis em lojas de SP apresenta, com o ASO, comprovante de vacinação contra hepatite B e tétano antes do início | **complementar** | RN-011 | Acrescenta um critério a um grupo, sem contradizer ASO nem prazos | RN-011 v3; RF-001 com novo critério; novos RN-019, RF-026 e RN-020 [hipótese, por analogia com dado de saúde]; Q-051, Q-052 | FT-023, US-050 a US-053; US-028 e US-029 em revisar | 02, 03, 04, 05, 06, 07 |
| M-02.2 | ASO e prazos atuais continuam valendo | **existente** | RN-001, RN-010 | Confirma o que já está nos requisitos | Fonte acrescentada em RN-001, sem nova versão | Nenhum | 07 |
| M-02.3 | Adesão ao programa Acolher no 1º trimestre de 2027 | **novo** | — | Nenhum item trata esse programa | Novo RN-021; Q-055; prioridade e fase dependem de Helena | FT-024 | 02, 03, 04, 05, 06, 07 |
| M-02.4 | Essas admissões usam CRNM como documento de identificação | **novo** | RF-003 (toca) | Não há esse documento; legados exigem CPF e não têm campo | Novos RF-027 e RF-029 [hipótese], RN-022 [hipótese]; RF-003 v3; RIS-019; Q-053, Q-054 | US-054, US-056, US-057; US-016, US-017, US-024 e US-025 em revisar | 02, 03, 04, 05, 06, 07 |
| M-02.5 | O processo controla a validade da CRNM | **novo** | — | Nenhum requisito controla validade de documento de identificação | Novo RF-028; consequência do vencimento em Q-053 | US-055 | 03, 04, 05, 06, 07 |

## Pedidos de mudança

| CR | Classe | Complexidade | Status | Decisão registrada |
|---|---|---|---|---|
| CR-001 | conflitante | complexa | proposta | Não aplicado. Conflito não se resolve em silêncio: decidem Helena e Marina (Q-050) |
| CR-002 | complementar | moderada | aplicada | Aplicado por vir do Jurídico, sem contradizer item, antes de baseline |
| CR-003 | novo | complexa | aplicada | Aplicado com prioridade proposta; fase aguarda Helena (Q-055) |

Detalhes em `.re/mudancas/CR-00N.md`. Nenhum dos CRs teve aprovação humana: CR-002 e CR-003 foram aplicados como decisão razoável prevista no briefing, e a reversão é possível pelo histórico.

## Pontos de atenção

- **Autoridade em M-01.2.** Helena e Marina estavam presentes, mas a ata não registra aprovação. A resposta de Marina a Q-005, dada depois da ata, mantém 30+60. Se houve decisão não registrada, CR-001 pode ser aprovado com a revisão da RH-012.
- **Efeito na operação.** A FolhaCerta, o manual e a planilha já usam 45+45. Sem aviso, nada impede que a data de 01/12/2026 seja seguida na prática (RIS-018).
- **Texto da Portaria.** Só há o resumo do e-mail; a norma não foi lida. Cargos, doses, validade e aplicação a quem já trabalha são desconhecidos (Q-052).
- **Destinatários.** Beatriz Lobo e Paula Nogueira não estão no e-mail, embora os temas toquem o Regulatório e a LGPD. Recomenda-se encaminhar.
- **Datas.** Portaria e Acolher podem chegar antes do sistema, que não tem data (Q-017). US-050 cobre o processo provisório da Portaria; para o Acolher, depende de Q-055.
- **Q-020.** A ata de 28/10 responde em parte: só traz informes. Quem aprova requisitos segue em aberto.

## O que mudou nas entregas

| Entrega | Mudança |
|---|---|
| `01-diagnostico.md` | Nova seção de atualização; DIV-019; RIS-018 a RIS-020 |
| `02-negocio.md` | Escopo, processos, RN, datas externas, riscos, glossário e pendências |
| `03-tecnico.md` | RF-026 a RF-029; regras com exemplo; ADR; dicionário; de-para; LGPD; integrações e ajustes nos legados |
| `04-backlog.md` | FT-023, FT-024, US-050 a US-057; US-016, US-017, US-024, US-025, US-028 e US-029 em revisar; US-004, US-005 e US-036 aguardando CR-001 |
| `05-jira.csv`, `06-azure-devops.csv` | Regenerados. A lista só com o que mudou está em `.re/entregaveis/backlog/*-delta.csv`; reimportar o arquivo completo cria itens duplicados |
| `07-rastreabilidade.md` | Novos itens, M-01, M-02 e tabela de CRs |
| `perguntas.md`, `respostas.md` | Sem mudança; 7 novas perguntas abertas (Q-050 a Q-056) em `02-negocio.md` §11 |

## Método e limitações

O classificador usou `recop.py candidatos` e `retrieve --activity gerenciamento_mudancas` (Adaptive RAG, `claude-haiku-5-5`), mais Corrective RAG para conferência. A consulta sobre rescisão não retornou evidência, o que é coerente com fora do escopo. O `recop.py impacto` retornou muitos candidatos porque o nó de sistema `geral` liga quase tudo; os afetados foram decididos pela leitura dos itens. Registro em `.re/log-rag.jsonl`. Requisitos seguem sem validação formal e sem baseline.
