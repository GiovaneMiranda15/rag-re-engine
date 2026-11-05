# Diagnóstico do cenário atual — Projeto Admissão Única

Drogarias Caliandra S.A. | Versão 3, atualizada com `respostas.md` e `08-mudancas.md`

## 0. O que mudou com as respostas

As seções seguintes mantêm os achados originais. Esta tabela indica a situação atual de cada divergência. As pendências (PD-xx) estão em `02-negocio.md`, seção 9.

| Item | Situação | Decisão ou pendência |
|---|---|---|
| D-01, D-02 ASO | **Resolvida** | 30 dias corridos, sem exceção (Fábio, Marina). Casos em PD-08 |
| D-03 Experiência | **Contestada** | Vale 30+60 (Marina), mas Sérgio comunicou 45+45 a partir de 01/12/2026 (PD-25). Contratos em curso em PD-06 |
| D-04 CRF | **Resolvida** | Protocolo não vale, inclusive RT (Beatriz Lobo). Complementos em PD-13 |
| D-05 Oferta | **Resolvida na regra** | BP sempre; regional acima do piso; gerente indica e não aprova sozinho (Marina). Prática atual em PD-15 |
| D-06 Integração | **Resolvida na regra** | 5º dia corrido (Beatriz Lobo). Viabilidade e comprovação em PD-21 |
| D-07 Aprendiz | **Adiada** | Entra depois, prioridade 5 (Helena). Toda a pergunta 10 em PD-16 |
| D-08 Retenção | **Resolvida** | 6 meses, inclusive cópias e backups (Paula) |
| D-09 Saúde | **Parcial** | CID só no ambiente do SESMT (Paula). Demais dados em PD-09 |
| D-10 Salário | **Parcial** | Piso da CCT vigente por UF, conforme o FolhaCerta (Rogério). Dono da tabela do Recruta+ em PD-15 |
| D-11 Acesso | **Aberta** | Pergunta 14 sem resposta: PD-20 |
| D-12 Documentos | **Regra clara** | 5 dias úteis. Efeito do atraso em PD-14 |
| Números de setembro | **Conceito resolvido** | Etapas diferentes; admissão oficial é o conceito do DP (Rogério). Números fechados e decomposição em PD-05 |
| Abrangência | **Quase resolvida** | Próprias dentro; franqueadas fora; CD e escritório fora da 1ª fase. Estágio em PD-22 |
| Identificadores | **Parcial** | CPF só com dígitos; código numérico de loja (Igor). EducaFarma exige equivalência |
| Definição de "pode começar" | **Parcial** | ASO e CRF bloqueiam. Demais condições e liberação final em PD-14 |

**Hipótese desfeita ou ajustada:** a ordem de autoridade só foi confirmada para a RH-012, nas regras já definidas. Não há árbitro definido, embora a hipótese da pergunta 1 indicasse Helena (PD-01). Aprendiz não entra primeiro, ao contrário da hipótese da pergunta 2.

**Hipóteses não confirmadas:** as hipóteses de `perguntas.md` para os itens respondidos com "Não sei" continuam só como premissas pendentes. Nenhuma virou fato.

**Achados novos, surgidos ao cruzar respostas e fontes:**

- **Manual:** segundo Rogério, só a seção 4 foi revogada formalmente, e as lojas ainda o consultam. O Comunicado fala do prazo dessa seção. As seções 2, 6 e 9 contrariam a RH-012 e seguirão publicadas até a chegada do sistema, a menos que se decida um aviso provisório (R-17).
- **ATIVO não prova conformidade:** a admissão oficial depende do status ATIVO, mas L415, L426 e C9233 estão ativos fora das regras agora confirmadas (R-18).
- **`pcd_cid`:** a decisão de CID só no SESMT também alcança esse campo do Recruta+, não apenas o FolhaCerta.
- **Tensão de ASO:** o conceito do DP fala em "ASO apto validado", enquanto a RH-012 §11.2 limita dados de saúde ao SESMT. O que o DP pode ver segue em aberto (PD-09).
- **Integração insuficiente:** Recruta+ → FolhaCerta não elimina a digitação sozinha. RG, nome da mãe, CRF, início e experiência não vêm do Recruta+, e `FARMACEUTICO` não distingue RT (`03-tecnico.md`, seção 5).
- **Contagem de dias:** o FolhaCerta soma dias à admissão. Com o dia da admissão incluído, 90 dias podem virar o 91º (PD-06).
- **Lacunas de resposta:** as perguntas 10, 12 e 14 ficaram totalmente sem resposta, e a anomalia de C9240 continua sem explicação. A contenção dos riscos críticos não tem responsável nem data (PD-11).

**Nova participante:** Beatriz Lobo, de Assuntos Regulatórios (área confirmada na ata de 28/10), respondeu sobre CRF e integração. Helena indicou também Vera Castro (CFO) para orçamento.

**Atualização pelas comunicações de 28 e 30/10 (`08-mudancas.md`):** a ata do comitê de 28/10 só traz informes, sem decisão registrada. Ela expõe um conflito sobre a experiência e torna concreta a falta de árbitro (PD-01). O e-mail do Jurídico traz duas frentes novas, com datas próprias (R-21).

## 1. Síntese

A admissão não tem uma regra única nem um registro único. Quatro sistemas, uma planilha e o e-mail usam regras, códigos e conceitos diferentes, e a norma vigente (Política RH-012) não está implementada em quase nenhum deles.

**Principais achados (situação atual de cada decisão na seção 0):**

1. **Regras em conflito com efeito legal.** A validade do ASO tem três valores (30, 60 e 90 dias) e a experiência tem dois (30+60 e 45+45). O CRF tem duas regras opostas e uma falha de sistema. O prazo de integração tem três valores (5, 15 e 30 dias). A amostra já contém contratos e inícios fora da Política.
2. **Início sem as condições exigidas.** Há na amostra um início antes do ASO e uma farmacêutica responsável técnica ativa sem número de CRF. Não existe uma definição compartilhada de "pode começar".
3. **Exposição de dados sensíveis.** Há informação de saúde e de gestação em planilha editável por qualquer pessoa com o link. Gerentes têm leitura de dados clínicos e de antecedentes. Dados de candidatos reprovados ficam guardados muito além do prazo da Política, inclusive em uma tabela de backup de 2021–2022.
4. **Risco de discriminação.** Uma linha da planilha registra que a regional vai "reavaliar início" de uma candidata após menção a gravidez. O Recruta+ tem campos de gestação e de antecedentes, incluindo anotação sobre ação trabalhista.
5. **Login compartilhado.** O colaborador novo fica cerca de 3 dias usando o login do gerente no PDV, inclusive em venda com receita.
6. **Etapa da Política inexistente.** A validação do BP de RH, obrigatória em toda oferta, não aparece no Recruta+ nem no fluxo atual.

**Os três números de setembro (214, 188 e 176) não provam erro.** Eles medem eventos diferentes (seção 3.3). O alinhamento necessário é de definição, mas a diferença ainda não foi explicada por inteiro.

**Três pontos pedem contenção agora, sem esperar o projeto:** o link aberto da planilha, o login compartilhado no PDV e a avaliação do caso de gestação pelo Jurídico. A decisão é das áreas responsáveis e nenhuma ação foi executada neste levantamento.

## 2. Base da análise e limites

**Fontes:** escopo; ata de 22/09/2026; fluxo atual (oficina de 09/2026); Política RH-012 rev. 4; Comunicado DP 07/2024; Manual v3.2 (2019); leia-me e planilha de controle; dumps do FolhaCerta e do Recruta+; exportações do EducaFarma.

**Limites:**

- Os dumps e exportações são **amostras** (4 lojas). Os percentuais e contagens desses dados indicam a existência do problema, não a sua frequência na rede.
- Os números da ata (25 min, 30% de devolução, 3 dias sem login, cerca de 1 semana de exame) são relatos. Só o prazo do exame pôde ser conferido com dados.
- Os dumps mostram a estrutura e as permissões. Não mostram como os sistemas são usados na prática nem se as permissões são as de produção.
- A exportação do EducaFarma não tem data. A data mais recente nela é 14/10/2026.
- Não houve acesso a: e-mails, chamados de TI, documentos das pastas, contratos assinados, ASOs, contratos com MedTrab e Contábil Alfa, Acordo Coletivo de 2024, CCTs e qualquer documentação de API.
- Referências a lei vêm de conhecimento geral, não das fontes, e dependem de confirmação do Jurídico.

**Dados pessoais:** este documento não reproduz nomes, CPFs, CIDs ou dados de registros das fontes. Casos comuns são citados pelo identificador técnico. Casos com dado sensível são descritos sem identificador, e podem ser localizados nos campos indicados.

**Convenção:** `L###` é a linha da planilha, `C####` é o contrato no FolhaCerta e `O####` é a oferta no Recruta+.

## 3. Divergências

### 3.1 Regras de negócio

Helena confirmou que, nas regras já definidas, vale a RH-012. A ordem completa segue pendente (PD-23); nesta análise, usa-se como hipótese: Política RH-012 rev. 4 (2025), depois Comunicado 07/2024, depois Manual v3.2 (2019). A planilha e as configurações de sistema mostram a prática e não são norma. A planilha foi revisada em agosto/2026, depois da Política, mas ser mais recente não lhe dá autoridade.

| ID | Tema | Política RH-012 | Manual 2019 / Comunicado | Planilha (leia-me) | Sistemas | O que os dados mostram | Sev. |
|---|---|---|---|---|---|---|---|
| D-01 | Validade do ASO no início | §6.2: até 30 dias corridos | Manual §5: só "exame feito" | Até 60 dias | FolhaCerta: até 90 dias, sem limite para ASO posterior ao início | L426 com 45 dias e L415 com 63 dias, ambos ativos. O sistema aceitou os dois. | Alta |
| D-02 | ASO antes do início | §6.1: ninguém inicia sem ASO apto | §5: igual | "Liberado" pede ASO conferido | Comentário de `contrato.status`: ATIVO exige ASO validado | L438 / C9240: início 3 dias antes do ASO, por pressão de falta de pessoal | Crítica |
| D-03 | Experiência | §4.1: 30+60 | Manual §6: 45+45 | 45+45 | FolhaCerta: padrão 45 | Todos os 8 contratos CLT de 2026 têm 45 dias. Nenhum segue a Política vigente desde 01/03/2025. | Alta |
| D-04 | CRF | §7: certidão com CRF ativo antes do início, inclusive RT; protocolo não substitui | Manual §7: "carteira do CRF" | Pode começar com protocolo; 30 dias para o número | FolhaCerta exige número só para `FARM`, e `FARM_RT` escapa apesar de `exige_crf = true`. Nenhum sistema controla a certidão. | L431 / C9233: RT ativa desde 05/10 em protocolo e sem número. Os 30 dias da própria planilha terminam em 04/11/2026. | Crítica |
| D-05 | Aprovação da oferta | §3: BP de RH valida toda oferta; acima do piso, também o gerente regional | Manual §2: gerente aprova e assina | Linha aberta "quando a oferta é aprovada" | Recruta+: só `GERENTE_LOJA` e `GERENTE_REGIONAL` | 0 de 11 ofertas com BP registrado. Ofertas no piso foram aprovadas ora pela loja, ora pela regional (seção 4). | Alta |
| D-06 | Integração | §9: até o 5º dia corrido e antes de atender sozinho no balcão | Manual §9: até 15 dias | "Mostrar a trilha" no 1º dia | EducaFarma: 30 dias | Das 4 conclusões: 15 a 24 dias, nenhuma no prazo da Política. Matrícula 1 a 6 dias após o início. | Alta |
| D-07 | Idade e aprendiz | §4.2: aprendiz de 14 a 24 anos | Sem menção | Aprendiz vai à Contábil Alfa | FolhaCerta: mínimo de 18 anos e sem tipo de contrato para aprendiz | É provável que essa restrição técnica explique o desvio pela Contábil Alfa (a confirmar). Aprendiz menor de idade em L440. | Média |
| D-08 | Retenção de candidatos | §11.3: eliminar em até 6 meses | Sem menção | Sem regra | Recruta+: expurgo mensal após 24 meses, só de `REPROVADO`; o backup não é expurgado | Candidato reprovado em 02/2025 ainda na base; 3 registros de 2021–2022 no backup | Alta |
| D-09 | Acesso a dado de saúde | §11.2: exclusivo do SESMT | Sem menção | `resultado_aso` e `obs` abertos a quem tem o link | FolhaCerta: `exame_admissional`, inclusive CID e observação clínica, legível por `dp_analista` e `rh_loja`. Não existe papel para o SESMT no dump. | 1 registro clínico detalhado no FolhaCerta; 1 linha da planilha com dado de saúde | Crítica |
| D-10 | Tabela salarial | Referência ao piso da função | Sem menção | Sem campo | FolhaCerta: Balconista SP R$ 1.820 (CCT 2026), com histórico. Recruta+: R$ 1.750 (vigência 2025), sem histórico, sem caixa, RT ou aprendiz | O7005 abaixo do piso (detalhe abaixo) | Alta |
| D-11 | Momento do chamado de acesso | Sem menção | Manual §8: no 1º dia | Checklist: "conferir se foi aberto" no 1º dia | Fluxo: ao marcar "Liberado" | Três versões do mesmo passo, e relato de cerca de 3 dias sem login | Alta |
| D-12 | Prazo dos documentos | §2: 5 dias úteis | Manual §4: 3; Comunicado: 5, revoga o Manual nesse ponto | 5 dias úteis | Sem campo em nenhum sistema | Divergência só no Manual, que segue publicado. O cumprimento não é mensurável, pois não há data de entrega de documentos. | Baixa |

**Detalhe de D-10:** a oferta O7005 foi aprovada abaixo do piso de SP, cancelada e refeita em O7006 uma semana depois. A planilha registra "voltou da folha" (L433). As vagas de balconista em SP na amostra trazem referência abaixo do piso. A barreira do FolhaCerta funcionou, mas só no fim do processo.

### 3.2 Regras que parecem divergir, mas não divergem

Estes pontos foram conferidos e **não** precisam de decisão:

- **Jornada:** 44 h semanais (Política e planilha) e 220 h mensais (FolhaCerta) são a mesma jornada na conversão usual.
- **Carência do plano:** 90 dias, e 30 para farmacêutico, está igual na Política, na planilha e no FolhaCerta, incluindo RT. Resta confirmar se o Acordo Coletivo de 2024, que não está nas fontes, continua vigente.
- **S-2200:** dia 15 do mês seguinte na Política, no FolhaCerta e nos dados.
- **S-2190:** véspera do início no FolhaCerta e nos dados, compatível com o "registro preliminar antes do início" da Política. É necessário verificar se o cálculo em dia não útil traz problema (início na segunda gera limite no domingo).
- **Dados entre sistemas na amostra:** CPF (após retirar a máscara), datas de início, datas de ASO e salários batem nos 8 casos presentes nos três sistemas. O problema é o retrabalho e a falta de chave comum, não uma corrupção visível.

### 3.3 Números de setembro

| Área | Valor (projeção) | O que provavelmente mede | Fonte da definição |
|---|---|---|---|
| Recrutamento | 214 | Oferta aceita: `CONTRATADO` | Gatilho `trg_oferta_aceita` |
| DP | 188 | Contrato efetivado: `ATIVO` | Comentário de `contrato.status` |
| Lojas | 176 | Trabalhou o 1º dia e recebeu o kit: `Iniciado` | Leia-me da planilha |

São três marcos de um mesmo funil, não três medidas de uma mesma coisa. **Na amostra:** 10 `CONTRATADO`, 8 `ATIVO` e 8 `Iniciado`. As 2 diferenças são 1 aprendiz (fora do FolhaCerta) e 1 candidata ainda em ASO.

Hipóteses para as diferenças de 26 e de 12, **não verificadas**:

- oferta aceita que não evolui: o Recruta+ não tem como voltar de `CONTRATADO` nem registra desistência;
- aprendizes, que entram no Recruta+ mas não no FolhaCerta (cerca de 3 por mês);
- defasagem entre os marcos, somada ao fato de os dados serem projeção;
- centro de distribuição e escritório, que estão na Política mas podem não estar na planilha "das lojas";
- franqueadas, caso usem o Recruta+;
- atraso no preenchimento da planilha.

A média de "190 admissões por mês nas 184 lojas" também não deixa claro se inclui CD e escritório.

**Depois das respostas:** Rogério confirmou que as diferenças vêm, antes de tudo, de serem etapas diferentes, e que a admissão oficial é contrato assinado, ASO apto validado e ATIVO no FolhaCerta. A separação numérica das hipóteses acima não foi informada e os números seguem como projeção (PD-05).

### 3.4 Abrangência

- O escopo fala em **212 lojas**. A Política separa **184 próprias** e **28 franqueadas**, com empregador próprio e fora da Política. A soma fecha, mas o projeto não diz se as franqueadas entram.
- A Política também cobre CD e escritório, onde "gerente de loja" e "planilha das lojas" não se aplicam.
- A Política prevê estágio. O FolhaCerta tem `ESTAGIO`, mas estágio não aparece na planilha, no fluxo nem nos dados.
- **Depois das respostas:** franqueadas fora; CD e escritório fora da primeira fase; CLT de loja primeiro; aprendiz depois; estágio não decidido (Helena).

### 3.5 Dados mestres

| Conceito | FolhaCerta | Recruta+ | Planilha | EducaFarma |
|---|---|---|---|---|
| Pessoa | CPF de 11 dígitos, matrícula | CPF com máscara, id | CPF livre (com e sem máscara na amostra) | E-mail pessoal, sem CPF |
| Loja | `147` | `LJ-0147` | `147 - Savassi` | `MG-SAV` |
| Cargo | `BALC`, `FARM_RT` | `BALCONISTA`, `FARMACEUTICO` (sem RT) | Texto livre (com variação de gênero) | `BALCONISTA`, `FARMACEUTICO` (sem RT e sem aprendiz) |
| Contrato | `CLT_EXP`, `CLT_IND`, `ESTAGIO` | Não há | `CLT`, `APRENDIZ` | Não há |
| Regional | Não há | Não há | `MG-01` | Prefixo de UF na unidade |

**Armadilha de reconciliação:** há dois colaboradores homônimos no FolhaCerta (matrículas 50211 e 58801), em lojas e datas diferentes. Cruzar por nome atribuiria o registro à pessoa errada. Como o EducaFarma não tem CPF, hoje o cruzamento confiável depende do e-mail, que é pessoal e mutável.

### 3.6 Conceitos de situação

- **`Liberado` não significa "pode começar".** O leia-me exige só documentos, ASO e data marcada. O fluxo coloca a marcação depois do contrato ATIVO. Rogério afirma que ninguém começa sem o S-2190. A Política acrescenta o CRF. L440 está `Liberado` sem contrato no FolhaCerta, por ser aprendiz.
- **A planilha é linear e o processo é paralelo.** "Em documentos" seguido de "Em ASO" não representa documentos e exame correndo ao mesmo tempo, como no fluxo.
- **Contrato assinado:** é condição do status ATIVO, mas nenhuma fonte mostra onde ou quando a assinatura é registrada.

## 4. Achados por caso

Lista só com casos sem dado sensível, todos da amostra.

| Caso | Achado | Regra |
|---|---|---|
| L438 / C9240 | Início em 06/10 com ASO em 09/10. S-2190 enviado em 05/10, antes do ASO. Como o evento nasce do status ATIVO e este exige ASO apto, **a sequência não se explica pelo gatilho do dump**. | §6.1 |
| L431 / C9233 | RT ativa em protocolo, sem número de CRF | §7 |
| L415 / C9208 | ASO com 63 dias, após adiamento pela loja. Fora da Política e da planilha. | §6.2 |
| L426 / C9251 | ASO com 45 dias: fora da Política, aceito pela planilha | §6.2 |
| L433 / O7005–O7006 | Oferta abaixo do piso, detectada na folha; 7 dias de retrabalho | §3, D-10 |
| C9140, C9177 | Em 20/10 já tinham passado de `fim_experiencia` (17/09 e 16/10), seguem `CLT_EXP` com 45 dias. Não há registro de prorrogação ou de conversão, e o modelo de dados não tem lugar para isso. | §4.1 |
| 6 de 8 contratos ativos de 2026 | Sem evento S-2190 nem S-2200 no dump, embora o gatilho gere os eventos ao ativar. Pode ser só recorte da amostra: **precisa de verificação**. | §10 |
| L440 | Aprendiz em lote da Contábil Alfa de 15/10 com início em 19/10. Sem registro no FolhaCerta e no EducaFarma, e sem trilha para o cargo. | §4.2, §9 |
| O7003, O7004, O7006 x O7002, O7009, O7010 | Salários iguais ao piso: os três primeiros aprovados pela regional e os demais pela loja. Sem critério aparente. | §3 |
| Vagas 501 e 507 | Duas ofertas aceitas na mesma vaga. A vaga não tem quantidade nem situação, o que pode distorcer contagens. | — |
| Matrículas no EducaFarma | Só trilhas `*-01` aparecem. Nenhuma das outras obrigatórias está na exportação, mesmo com prazo vencido em casos como L412 (T-BALC-02) e L419 (T-FARM-02). A exportação pode estar filtrada. | Trilhas |

**Tempo da oferta ao início:** 20 a 22 dias em 6 dos 9 casos com início. Os outros 3 são os dois adiamentos (54 e 70 dias) e o caso de 7 dias que violou o ASO.

## 5. Gargalos

| ID | Gargalo | Evidência | Efeito |
|---|---|---|---|
| G-01 | **Digitação no DP** | 25 min por admissão (relato). Com 190 por mês, são cerca de 79 h mensais em 4 analistas (cálculo próprio). | Retrabalho, sem ganho de controle |
| G-02 | **Devolução de pastas** | Cerca de 30% (relato), ou cerca de 57 por mês. Não há registro do motivo. | Pressão na véspera do S-2190 |
| G-03 | **Agendamento de exame** | Uma analista para cerca de 190 exames mensais, por e-mail. 5 a 8 dias do pedido ao exame nos 9 casos da amostra, confirmando o relato. | Ponto único de falha e principal fator de espera |
| G-04 | **Acesso ao PDV** | Cerca de 3 dias (relato), com chamado aberto tarde | Leva ao risco R-05 |
| G-05 | **Corrida pelo S-2190** | Relato do DP. Na amostra, um dos dois envios ocorreu no último dia. | Risco de início irregular |
| G-06 | **Lote quinzenal de aprendiz** | Ata e leia-me. L440: lote a 4 dias do início. | Até 15 dias de espera e pouca visibilidade |
| G-07 | **Matrícula manual tardia** | Feita pela loja após o início, em até 6 dias | Torna o prazo de 5 dias quase inalcançável |
| G-08 | **Conciliação manual** | Planilha, e-mail, 4 códigos de loja | Ninguém vê o estado completo da admissão |

**Tensão de fundo:** o tempo mínimo (cerca de 1 semana de exame, 5 dias úteis de documentos) conflita com a necessidade da loja de não ficar desfalcada. L438 mostra o resultado quando a pressão vence a regra. Adiamentos longos causam o problema inverso: o ASO vence antes do início (L415, L426).

## 6. Riscos

| ID | Risco | Evidência | Sev. | Dono sugerido |
|---|---|---|---|---|
| R-01 | Início sem ASO apto, com exposição trabalhista e de saúde | L438; trigger sem limite para ASO posterior | Crítica | SESMT, Jurídico |
| R-02 | Farmacêutico ou RT sem regularidade no CRF, com possível exposição sanitária e regulatória | L431; regra da planilha; falha do `FARM_RT` | Crítica | Jurídico, Operações |
| R-03 | **Discriminação na admissão.** Gestação associada à reavaliação de início; campo `gestante` no cadastro; `antecedentes_ok/obs` com anotações de histórico judicial, de saúde e criminal, presentes em registros de reprovados. Possível conflito com a Lei 9.029/95. | Planilha; Recruta+ | Crítica | Jurídico |
| R-04 | **Vazamento e adulteração de dados pessoais e sensíveis.** Link aberto e editável com CPF, resultado de ASO e texto livre. | Leia-me; campo `obs` | Crítica | Encarregada, Operações |
| R-05 | Uso de credencial alheia no PDV, inclusive venda com receita: perda de rastreabilidade e de responsabilização, antes de o colaborador concluir o treinamento | Ata | Crítica | Operações, TI, Jurídico |
| R-06 | Acesso indevido a dado clínico por DP e gerentes, sem restrição por loja | Permissões do FolhaCerta e Recruta+ | Alta | Encarregada, TI |
| R-07 | Retenção excessiva: 24 meses contra 6; backup de 2021–2022 legível por gerentes e pela conta de relatórios; candidato sem status `REPROVADO` nunca é expurgado | Recruta+ | Alta | Encarregada, TI |
| R-08 | Contratos fora da Política (45+45) e prazos de experiência sem controle. Continuar após o termo sem prorrogação registrada pode mudar a natureza do contrato (a confirmar). | D-03; C9140, C9177 | Alta | Jurídico, DP |
| R-09 | Oferta sem o BP e salário abaixo do piso na origem | D-05, D-10 | Alta | RH |
| R-10 | Aprendiz, incluindo menor de idade, em processo paralelo com terceiro. Dados de adolescente com a Contábil Alfa; responsabilidade e prazo do eSocial não documentados. | Ata; L440 | Alta | DP, Jurídico, Encarregada |
| R-11 | Atendimento no balcão antes da integração, sem qualquer barreira ou registro | D-06 | Alta | Operações |
| R-12 | Manual de 2019 publicado na intranet com regras superadas, reforçando a prática errada | Manual | Média | DP |
| R-13 | Automatizar a regra errada. As regras principais já foram decididas, mas os sistemas ainda não as seguem, e o novo fluxo pode divergir do FolhaCerta. | Seção 3 | Alta | Comitê |
| R-14 | Decisões sem árbitro. Há decisor por assunto, mas ninguém soube dizer quem arbitra discordâncias entre áreas. | Escopo; resposta 1 | Média | Helena |
| R-15 | Medidas sem base. Os ganhos não poderão ser comprovados, pois 25 min, 30% e 3 dias são relatos sem medição. | Ata | Média | PMO |
| R-16 | Dependências não confirmadas: as APIs são relatos, e a integração com o FolhaCerta e o Recruta+, parte do resultado mínimo, é desconhecida. Igor não soube responder. | Ata; resposta 13 | **Alta** | TI |
| R-17 | Manual segue consultado com regras contrárias à RH-012 até a chegada do sistema | Respostas 1, 4, 9 e 15 | Média | DP, Helena |
| R-18 | Status ATIVO tratado como conformidade, embora o FolhaCerta aceite ASO de até 90 dias e RT sem CRF | Resposta 3; dump | Alta | DP, TI |
| R-19 | Contenção sem responsável nem data, apesar de os riscos serem críticos | Resposta 11 | Crítica | Helena, Encarregada |
| R-20 | Operações adota 45+45 em 01/12/2026 sem revisão da RH-012, oficializando o desvio de D-03 | M-01 | Alta | Helena, Jurídico |
| R-21 | Portaria em vigor em 01/02/2027 e programa Acolher no 1º tri/2027 antes do novo fluxo, cujo prazo é desconhecido | M-02; PD-03 | Alta | Jurídico, SESMT, DP |
| R-22 | Comprovante de vacinação circular como dado de saúde fora do SESMT. A Encarregada e Assuntos Regulatórios não constam como destinatárias do e-mail. | M-02 | Alta | Encarregada |
| R-23 | CRNM conflitar com cadastros que exigem CPF e têm só `rg` como identificação | M-02; dumps | Média | DP, TI |

## 7. Inventário preliminar de dados pessoais

Pedido por Paula Nogueira na ata. Baseado na estrutura das fontes. **Base legal, finalidade e retenção por dado não constam nas fontes** e dependem da Encarregada. "Sensível" segue a noção da LGPD, a confirmar com ela.

| Sistema | Dados comuns | Dados sensíveis ou de atenção | Quem acessa (conforme as fontes) | Retenção conhecida | Lacuna |
|---|---|---|---|---|---|
| **Recruta+** (`candidato`, `oferta`) — fornecedor externo | CPF, nome, e-mail, telefone, nascimento, salário | `gestante`, `pcd`, `pcd_cid`, `antecedentes_ok`, `antecedentes_obs` | `gerente_loja`: leitura de candidatos de todas as lojas, leitura e alteração de ofertas | 24 meses, só `REPROVADO` | Contra §11.1 e §11.3; escopo por loja ausente |
| **Recruta+** (`candidato_bkp_2022`) | CPF, nome, e-mail, nascimento | `gestante`, `pcd_cid`, `antecedentes_obs` | `gerente_loja`, `app_relatorios` | Nenhuma | Sem finalidade aparente; eliminação a avaliar |
| **FolhaCerta** (`colaborador`, `contrato`) | CPF, nome, nascimento, RG, nome da mãe, e-mail pessoal, salário, número do CRF | Dados de menor (se aprendiz migrar) | `dp_analista`; `rh_loja` (gerentes e assistentes), leitura sem filtro por loja | Não informada | Salário e identificação visíveis além da loja |
| **FolhaCerta** (`exame_admissional`) | Data, CRM do médico | `resultado`, `cid_restricao`, `observacao_clinica` | `dp_analista`, `rh_loja` | Não informada | Contra §11.2 |
| **Planilha de controle** | CPF, nome, cargo, loja, datas, gerente, analista | `resultado_aso`, `dt_aso`, `carencia_plano_dias`, `obs` livre (já com saúde e gestação) | Qualquer pessoa com o link: leitura e edição | Não informada | Contra §11; sem trilha confiável |
| **EducaFarma** | E-mail pessoal, nome, unidade, trilha, datas, status | — | Não informado | Não informada | Uso de e-mail pessoal como chave |
| **E-mail** (loja, DP) | Identidade, CPF, residência, carteira de trabalho, título, comprovante bancário | Certidão de nascimento dos filhos (dados de crianças) | Não informado | Não informada | Lista vem do Manual de 2019; necessidade a validar (§11.1) |
| **E-mail / SESMT / MedTrab** | Identificação para agendamento | ASO em PDF, dados de exame | SESMT, clínica. Caminho até o DP não documentado. | Não informada | Fonte não recebida; operador externo |
| **Contábil Alfa** | Dados de cadastro do aprendiz | Dados de adolescente | DP, terceiro | Não informada | Fonte não recebida; contrato de operador não verificado |
| **Chamados de TI** | Possivelmente identificação do colaborador | — | TI, gerente | Não informada | Fonte não recebida |

**Nuance:** nem todo dado sensível deve simplesmente sumir. A informação de deficiência pode ter finalidade legítima (como cota e eSocial), mas deveria ser restrita. Já a gestação não tem finalidade aparente na seleção. A definição é de Paula e Marina.

## 8. Pontos de apoio

| Ponto | Por que ajuda | Confirmação |
|---|---|---|
| **FolhaCerta** | Sistema estável, valida piso, gera eventos do eSocial, mantém histórico de pisos. Continua como sistema da folha. | Ata e dump |
| **Política RH-012 rev. 4** | Aprovada por RH, Jurídico e Encarregada: boa base para regras | Fonte |
| **Barreira de piso** | Barrou a oferta abaixo do piso (L433) | Dados |
| **Trilhas por cargo no EducaFarma** | Permitem matrícula automática a partir do cargo | Exportação; API é relato |
| **Portal do gestor** | Gerentes já têm um canal no FolhaCerta (`rh_loja`) | Dump; uso real desconhecido |
| **Leia-me e fluxo de 09/2026** | Registro honesto da prática pelas próprias áreas | Fontes |
| **Conversas de 30 e 60 dias** | Já previstas no checklist da loja e coerentes com os marcos 30+60 da Política, ainda que sem registro | Leia-me |
| **Engajamento das áreas** | RH, DP, Jurídico, Encarregada, Operações, SESMT e TI estiveram no grupo de trabalho | Ata |

## 9. Oportunidades

Indicam direção e não são decisões de solução. O escopo pede entendimento antes de escolher.

1. **Regra única versionada:** resolver D-01 a D-12 em uma só decisão do comitê, revisar o Manual e corrigir sistemas e planilha.
2. **Definição única de "pode começar":** painel com condições claras por cargo e modalidade, atendendo ao pedido central do gerente.
3. **Reaproveitar dados:** evitar a redigitação levando ao FolhaCerta o que já veio do Recruta+ e do candidato. Depende de o FolhaCerta aceitar a integração.
4. **Coleta de documentos pelo próprio candidato,** com checagem de completude e motivo de devolução, para reduzir os 30% e criar a medida que hoje falta.
5. **Agendamento pelo portal da MedTrab,** se a API se confirmar, reduzindo o ponto único no SESMT.
6. **Alertas por data:** validade do ASO em caso de adiamento, S-2190, S-2200, fim e prorrogação da experiência, prazos de trilha.
7. **Matrícula automática no EducaFarma** antes do início, com cargo vindo do contrato.
8. **Solicitação de acesso antecipada,** vinculada à data de início, eliminando a causa do login compartilhado.
9. **Separar apto/inapto do dado clínico:** o DP e o gerente só precisam saber se a condição foi cumprida.
10. **Funil único:** usar os marcos de oferta aceita, contrato ativo e início, com um só cadastro, no lugar de três números disputados.
11. **Limpeza de dados:** eliminar o backup e ajustar o expurgo, conforme decisão da Encarregada.
12. **Medir antes de mudar:** uma amostra de linha de base de tempo de digitação, devoluções e dias sem login permitiria comprovar ganhos.

## 10. Implicações para o escopo

- **"Sistema único":** Helena definiu como fluxo único, saída da planilha e integração Recruta+ → FolhaCerta. Se Recruta+ e EducaFarma serão substituídos segue em aberto (PD-02), e nenhuma solução foi escolhida.
- **"Envio ao eSocial"** foi lido como acompanhar o envio, não transmitir, já que o FolhaCerta gera os eventos.
- **Limites:** folha, rescisão e desligamento estão fora. A fronteira exata no fim da experiência segue em aberto (PD-07).
- **Aprovação da oferta:** o escopo começa no "candidato aprovado", mas pede acompanhar a oferta, e a validação do BP ocorre antes de apresentá-la. A etapa precisa ser localizada.

## 11. Stakeholders e fontes faltantes

**Não estiveram na reunião de 22/09:** Recrutamento (enviou números), BPs de RH, gerentes de loja e regionais, analista do SESMT, analistas do DP, responsável pelo EducaFarma. **Externos sem contato:** Contábil Alfa, MedTrab, fornecedor do Recruta+.

**Fontes a obter:** Acordo Coletivo de 2024 e CCTs; contratos com terceiros; modelo de contrato e forma de assinatura; registro de chamados; exportação completa do EducaFarma, com data; dados da rede inteira; ata do comitê de 28/10/2026, caso tenha ocorrido.

## 12. Decisões tomadas neste levantamento

| Decisão | Motivo |
|---|---|
| Política RH-012 rev. 4 como referência provisória nos conflitos | Mais recente entre as normas formais e aprovada por RH, Jurídico e Encarregada |
| Tratar os 3 números como marcos diferentes, não como erro | As definições estão nas fontes |
| Citar casos sensíveis sem identificador | Regra de não copiar dados pessoais |
| Não concluir falha de eSocial pela ausência de eventos | Dump declarado como amostra |
| Não propor solução nem fornecedor | Pedido da patrocinadora |
| Tratar "Não sei" como pendência, não como confirmação das hipóteses | Regra de não inventar fatos |
| Não adotar premissa para os casos legais em aberto (L438, L415, L426, L431, gestação, contratos em curso) | A decisão cabe aos responsáveis |
