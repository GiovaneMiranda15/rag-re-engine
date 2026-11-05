# Diagnóstico do cenário atual — Projeto Admissão Única

Drogarias Caliandra S.A. · Patrocinadora: Helena Vasconcelos (Gente & Gestão)
Versão 3 (atualizada com `respostas.md` e `mudancas/`) · 04/11/2026

> As seções 4 a 7 preservam a análise inicial. **O que as respostas e as comunicações mudaram está nas seções 12 e 13**, que prevalecem em caso de diferença.

## 1. Síntese

A admissão não tem um processo único. Ela tem **quatro versões de regra** (Política RH-012, Manual de 2019, Leia-me da planilha e travas da FolhaCerta) e **três definições de "admitido"** (Recruta+, DP e lojas). Por isso os números de setembro não fecham: 214, 188 e 176.

O maior problema não é a digitação repetida, embora ela custe cerca de 79 horas por mês. É que **nenhum sistema impede o início irregular**: o "Liberado" é uma marca manual do gerente numa planilha. A amostra mostra as consequências:

| Achado na amostra | Resultado |
|---|---|
| ASO fora da regra de 30 dias, ou emitido depois do início | 3 de 9 |
| Farmacêutica RT ativa sem número de CRF, só com protocolo | 1 de 2 farmacêuticos |
| Integração concluída até o 5º dia | 0 de 4 concluídas (15 a 24 dias) |
| Oferta com validação registrada do BP de RH | 0 de 11 |

**Atenção imediata, sem esperar o projeto** (detalhes na seção 6):

1. A planilha com CPF e dados de saúde está aberta a edição para qualquer pessoa com o link.
2. Gerentes têm permissão de leitura sobre dados de saúde, gestação, PCD e antecedentes.
3. Há registros de candidatos fora do prazo de retenção, com anotações sensíveis.
4. Uma RT aparece ativa só com protocolo do CRF. O prazo informal de 30 dias da planilha venceria em 04/11/2026.
5. Há registro de candidata cujo início será "reavaliado" depois de ela mencionar a gravidez. **O Jurídico precisa ver isso antes de qualquer decisão.**

## 2. Base da análise e limites

| Fonte | Natureza | Data | Limite |
|---|---|---|---|
| Política RH-012, rev. 4 | Norma vigente, aprovada por G&G, Jurídico e Encarregada | 01/03/2025 | Não lista os documentos exigidos |
| Comunicado DP 07/2024 | Norma pontual | 15/07/2024 | Só trata do prazo de documentos |
| Manual de Lojas v3.2 | Norma antiga, ainda na intranet | 03/2019 | Anterior à Política |
| Ata do Grupo de Trabalho | Relatos | 22/09/2026 | Números declarados, não medidos |
| Fluxo atual | Oficina de RH/DP/Operações | 09/2026 | Não mostra BP de RH nem prazos |
| FolhaCerta (PostgreSQL) | Dump com esquema, travas e dados | 20/10/2026 | Amostra de 4 filiais |
| Recruta+ (MySQL, fornecedor externo) | Dump | 20/10/2026 | Amostra |
| Planilha de controle e Leia-me | Exportação e regras de uso | Leia-me de 08/2026 | 10 linhas; data da exportação não informada |
| EducaFarma (LMS) | 2 exportações | Sem data | Só trilhas `*-01` têm matrícula |

**Convenção:** **[F]** fato observado na fonte; **[I]** inferência nossa; **[C]** a confirmar com a área.

- Percentuais da amostra indicam **tipos de falha**, não a frequência na rede. A amostra é pequena e não foi sorteada.
- Não há fontes sobre a Contábil Alfa, a MedTrab, o sistema de chamados, o PDV, o portal do gestor nem a transmissão real ao eSocial.
- Não houve observação direta do trabalho nem entrevistas. "Como funciona de verdade" aqui significa o que os dados e documentos revelam.
- Dados pessoais não foram reproduzidos. Os casos são citados pelo número da linha da planilha (L) ou do contrato (C). Em casos de saúde, gestação e antecedentes, nem esse número é citado.

**Regra de leitura:** a Política RH-012 rev. 4 foi usada como referência por ser a mais recente e a de maior alçada. As respostas a confirmaram **tema a tema** (experiência, ASO, CRF, oferta, dados), mas a prevalência geral segue sem resposta (PD-06). Rogério informou que só a seção 4 do Manual foi revogada formalmente.

## 3. O processo real

| # | Etapa | Responsável | Ferramenta | Tempo observado |
|---|---|---|---|---|
| 1 | Aprovação e aceite da oferta | Recrutamento e gerente | Recruta+ | Sem medição |
| 2 | Abertura da linha de controle | Gerente | Planilha | Manual |
| 3 | Pedido de ASO | Gerente → SESMT | E-mail | Cerca de 2 dias após a oferta |
| 4 | Agendamento e emissão do ASO | 1 analista do SESMT → MedTrab | E-mail, PDF | 5 a 8 dias, média de 6,8 |
| 5 | Coleta de documentos | Candidato → loja → DP | Papel, e-mail | Não medido; a planilha não tem a data |
| 6 | Conferência | 4 analistas do DP | E-mail | Cerca de 30% das pastas voltam |
| 7 | Cadastro na folha | DP | FolhaCerta | Cerca de 25 min por admissão |
| 8 | Ativação do contrato e eSocial | DP | FolhaCerta | Corrida na véspera do início |
| 9 | "Liberado" | Gerente | Planilha | Manual, sem vínculo com a FolhaCerta |
| 10 | Chamado de acesso ao PDV | Gerente → TI | Chamado | Cerca de 3 dias sem login |
| 11 | Primeiro dia e "Iniciado" | Gerente | Checklist, planilha | — |
| 12 | Matrícula nos treinamentos | Loja | EducaFarma | 1 a 6 dias após o início |
| 13 | Acompanhamento até o fim da experiência | Sem responsável definido | **Nenhuma** | Não medido |

Da oferta ao início, a mediana da amostra é de **21 dias**, variando de 7 a 70. O caso de 7 dias começou sem ASO, e os de 54 e 70 dias estouraram a validade do exame.

Aprendizes seguem outro caminho: a partir da conferência, o DP envia os dados à Contábil Alfa, que devolve o cadastro em lotes quinzenais.

## 4. Divergências

### 4.1 Em aberto

| ID | Tema | O que cada fonte diz | Evidência e leitura | P. |
|---|---|---|---|---|
| D1 | O que é "admitido" | Recruta+: `CONTRATADO`, no aceite da oferta. DP: `ATIVO`, com contrato assinado e ASO validado. Lojas: `Iniciado`, após o primeiro dia | [F] 214, 188 e 176 na projeção de setembro. [I] Medem momentos diferentes. Causas possíveis: desistências (nenhum sistema tem esse estado), defasagem de datas, aprendizes fora da FolhaCerta, franqueadas e CD/escritório contados de formas distintas. **Os dados não permitem conciliar** | 3 |
| D2 | Abrangência | Escopo: 212 lojas. RH-012: 184 próprias, CD e escritório; as 28 franqueadas têm empregador próprio e ficam fora. Ata: 184 lojas | [I] Os 212 somam próprias e franqueadas. Levar as franqueadas muda a base legal, os CNPJs e o controlador dos dados | 1 |
| D3 | Contrato de experiência | RH-012: **30+60**. Manual, Leia-me e FolhaCerta (`DEFAULT 45`): **45+45** | [F] Todos os 8 contratos de experiência da amostra têm 45 dias, mesmo após a vigência da Política. [F] O checklist usa conversas aos 30 e 60 dias, coerentes com 30+60. [C] A prorrogação não tem campo na FolhaCerta: C9140 e C9177 já tinham passado de `fim_experiencia` em 20/10, sem registro. [C] O sistema soma 45 à data de admissão; se o primeiro dia contar, são 46 dias | 4, 10 |
| D4 | Validade do ASO | RH-012: **30 dias**. Leia-me: **60**. FolhaCerta: **90**, sem limite superior. Manual: só "exame feito" | [F] L415 (63 dias) e L426 (45 dias) passaram na trava da folha. [F] L438 começou 3 dias **antes** da emissão do ASO, e a trava aceita ASO emitido depois da admissão | 5 |
| D5 | CRF do farmacêutico | RH-012: certidão com CRF ativo antes do início; **protocolo não vale**. Leia-me: **pode começar com protocolo**, com 30 dias para regularizar. Manual: cópia da carteira | [F] A trava testa só `cargo_cod = 'FARM'`; ignora `FARM_RT` e o campo `exige_crf`. [F] C9233/L431 (RT) está `ATIVO` sem CRF, com protocolo na observação. [I] A FolhaCerta guarda o número, não a certidão nem sua validade | 6 |
| D6 | Aprendiz | RH-012: de **14 a 24 anos**, 30h semanais. FolhaCerta: exige **18 anos**, não tem tipo de contrato nem cargo de aprendiz, e a jornada padrão é 220h | [F] A folha não comporta o menor aprendiz, daí a Contábil Alfa (cerca de 40 por ano). [I] O lote quinzenal parece incompatível com o S-2190 na véspera do início. [C] Sem evidência de quem transmite os eventos. A vaga de aprendiz não tem referência salarial nem validação de piso | 8 |
| D7 | Aprovação da oferta | RH-012: **BP de RH valida toda oferta**; acima do piso, também o gerente regional. Manual e fluxo: o **gerente aprova**. Recruta+: só `GERENTE_LOJA` e `GERENTE_REGIONAL` | [F] 0 de 11 ofertas com BP. [I] A validação não ocorre ou ocorre por fora. [F] Nenhuma oferta da amostra supera o piso, logo a regra da alçada regional não pôde ser testada; o regional aprovou ofertas no piso, inclusive as de farmacêutico. [F] Só a planilha traz a regional | 7 |
| D8 | Tabela salarial | FolhaCerta (CCT SP 2026): balconista **R$ 1.820**. Recruta+ (vigência 2025): **R$ 1.750** | [F] A oferta 7005 saiu a R$ 1.750, voltou da folha e foi refeita (L433). [F] Três vagas de SP ainda têm referência de R$ 1.750. [F] O Recruta+ não guarda histórico nem tem caixa, RT e aprendiz. [I] O piso só é checado depois do aceite do candidato | 12 |
| D9 | Prazo da integração | RH-012: **5º dia corrido**, e antes de atender sem acompanhamento. Manual: **15 dias**. EducaFarma: **30 dias** | [F] Concluídas em 15, 17, 23 e 24 dias. [F] Três em andamento já tinham passado do 5º dia. L438 foi matriculada no 6º dia, após o fim do prazo | 13 |
| D10 | Retenção de candidatos | RH-012: eliminar em **6 meses**. Recruta+: rotina apaga `REPROVADO` após **24 meses**, e nenhum outro status | [F] Há reprovado de 02/2025 ainda na base. [F] `candidato_bkp_2022` guarda 3 registros de 2021–2022 fora de qualquer rotina, ainda legíveis por gerentes | 14 |
| D11 | Acesso a dados de saúde | RH-012: **só o SESMT**. FolhaCerta: `exame_admissional` com CID e observação clínica, legível por `rh_loja` e gravável pelo DP; não há perfil do SESMT. Planilha: resultado do ASO aberto | [F] Um registro da folha traz CID e observação clínica. [F] Um campo `obs` da planilha traz condição de saúde. [C] O portal pode filtrar mais do que o `GRANT` mostra | 11, 14 |
| D12 | Quando se pode começar | Leia-me: `Liberado` = documentos e ASO conferidos. Fluxo: depois do contrato `ATIVO`. Ata: "ninguém pode começar" sem S-2190. RH-012: também ASO apto e CRF | [I] **Não existe lista única de impedimentos.** `Liberado` ignora S-2190, contrato e CRF | 5 |
| D13 | Identificadores | Loja: `147`, `LJ-0147`, `147 - Savassi`, `MG-SAV`. Cargo: `BALC`, `BALCONISTA`, `Balconista`. Pessoa: CPF com e sem máscara, e-mail no LMS | [F] Não há chave comum, e o LMS não tem CPF nem matrícula. [F] Há homônimos com CPFs diferentes na folha, portanto cruzar por nome erra. [F] O LMS não tem trilha de aprendiz nem de RT; o Recruta+ não distingue RT | 12 |
| D14 | Momento do chamado de PDV | Manual e checklist: no primeiro dia. Fluxo: ao marcar `Liberado` | [I] Abrir no primeiro dia explica os cerca de 3 dias sem login | 12 |
| D15 | Início do controle | Leia-me: linha aberta com a oferta **aprovada**. Fluxo: depois do **aceite** | [I] Efeito menor, mas muda a contagem por etapa | 3 |

### 4.2 Resolvida, mas ainda visível

**Prazo de documentos.** O Manual diz 3 dias úteis; o Comunicado 07/2024 revogou esse trecho e fixou 5; a RH-012 e o Leia-me também dizem 5. **Vale 5 dias úteis.** O risco é o Manual seguir publicado na intranet. Além disso, o cumprimento não é mensurável, pois nenhuma fonte registra a data de entrega. A L438, com 7 dias entre oferta e início, deixava margem quase nula.

### 4.3 Conferidas: não são divergência

Estes pontos parecem conflitos, mas foram verificados e não devem virar requisito de correção:

- **Carência de 30 dias para farmacêuticos:** é exceção do Acordo Coletivo de 2024, coerente na RH-012, no Leia-me e na `beneficio_regra`.
- **44h semanais e 220h mensais:** são a mesma jornada em unidades diferentes.
- **Prazo do S-2200 (dia 15 do mês seguinte):** a RH-012 e o cálculo da FolhaCerta coincidem nos casos da amostra.
- **Datas de oferta e início, e salários:** batem entre Recruta+, planilha e FolhaCerta nos registros comuns.
- **Formatos de CPF:** batem após normalização. O problema é o formato, não a identidade.

## 5. Conformidade na amostra

"Integração" é o número de dias entre o início e a conclusão da trilha `*-01`.

| Linha | Contrato | Cargo | ASO antes do início | S-2190 na base | Integração | Achado |
|---|---|---|---|---|---|---|
| L412 | C9140 | Balconista | 12 dias | Sem registro | 24 | Integração fora; sem matrícula em T-BALC-02 e 03, já vencidas |
| L415 | C9208 | Balconista | **63 dias** | Sem registro | 23 | ASO acima até da regra da planilha; início adiado pela loja |
| L419 | C9177 | Farmacêutico | 13 dias | Sem registro | 17 | Integração fora; sem matrícula em T-FARM-02 (SNGPC), vencida |
| L423 | C9201 | Balconista | 13 dias | Enviado 3 dias antes | 15 | Integração fora |
| L426 | C9251 | Balconista | **45 dias** | Sem registro | Sem matrícula | ASO fora; início adiado pela loja |
| L431 | C9233 | Farmacêutica RT | 12 dias | Sem registro | Em andamento | **Sem CRF**; integração fora |
| L433 | C9234 | Balconista | 11 dias | Sem registro | Em andamento | Oferta refeita; integração fora |
| L438 | C9240 | Balconista | **3 dias depois** | Enviado na véspera | Em andamento | **Início sem ASO**; integração fora |
| L440 | Fora da folha | Aprendiz | 12 dias | Sem evidência | Sem matrícula | Sem trilha de aprendiz no LMS |
| L447 | Fora da folha | Balconista | Em andamento | — | — | Ver risco R5 |

Três pontos pedem confirmação:

- **Eventos:** 6 de 8 contratos recentes não têm eventos na base. Como a trigger os gera na ativação, pode ser só corte da amostra. **[C]** (pergunta 10)
- **Sequência da L438:** o S-2190 foi enviado em 05/10, mas o ASO é de 09/10. Pela trava, o contrato não ativaria sem ASO, e o evento só nasce na ativação. Os dados não explicam essa ordem. **[C]** (pergunta 10)
- **Vagas com dois aceites:** as vagas 501 e 507 têm duas ofertas aceitas cada. A vaga não tem campo de quantidade, então não se sabe se é normal. **[C]** (pergunta 7)

## 6. Riscos

| ID | Risco | Grav. | Evidência | Encaminhamento |
|---|---|---|---|---|
| R1 | Vazamento ou adulteração de dados pessoais na planilha | Crítica | "Qualquer pessoa com o link pode editar"; CPF, ASO e saúde em texto livre | **Imediato:** Encarregada restringe o link, sem esperar o sistema novo |
| R2 | Dados de saúde fora do SESMT | Crítica | D11; ASO em PDF circula até o DP | **Imediato:** Encarregada e TI revisam permissões |
| R3 | Dados sensíveis de candidatos acessíveis a gerentes | Crítica | Leitura de `candidato` e do backup por `gerente_loja`, de qualquer host, incluindo gestação, CID de PCD e antecedentes | **Imediato:** Encarregada e fornecedor |
| R4 | Retenção além da Política | Alta | D10 | Corrigir rotina e eliminar o backup, após avaliação do Jurídico |
| R5 | Discriminação por gestação | Crítica | Campo `gestante` no Recruta+; anotação de que o início seria reavaliado após a candidata mencionar a gravidez | **Imediato:** Jurídico avalia antes de qualquer decisão. Caso não reproduzido aqui |
| R6 | Discriminação por antecedentes e histórico | Crítica | Anotações sobre ação trabalhista, afastamento de saúde e registro policial, em candidatos reprovados | Jurídico avalia a coleta e os casos |
| R7 | Início sem ASO válido | Alta | L438, L415, L426; pressão por início rápido relatada na ata | Trava de liberação; exceção só se o Jurídico admitir |
| R8 | Farmacêutico ou RT sem regularidade | Crítica | L431; regra contrária no Leia-me | **Imediato:** Jurídico e Operações verificam a situação atual e retiram a regra do Leia-me |
| R9 | Login compartilhado no PDV, inclusive em venda com receita | Crítica | Ata: cerca de 3 dias com o login do gerente | **Imediato:** Operações e TI. Perde-se a rastreabilidade de quem vendeu; impacto regulatório a avaliar com Jurídico e farmacêuticos |
| R10 | Atendimento sem treinamento obrigatório | Alta | D9; trilhas sem matrícula | Matrícula automática e alerta ao gerente |
| R11 | Atraso ou inconsistência no eSocial | Alta | Corrida de véspera; aprendizes; adiamentos sem recálculo de `dt_limite`; sem tratamento de dia não útil (13/09 e 15/11/2026 são domingos) | Confirmar a operação real com o DP |
| R12 | Aprendiz menor em trilha paralela | Alta | D6; dados saem para terceiro sem evidência de controle | Definir tratamento antes de especificar |
| R13 | Contrato de experiência fora da norma | Alta | D3; prorrogação sem registro | Decisão do Jurídico; possível revisão dos contratos em curso |
| R14 | Oferta sem a validação exigida, ou abaixo do piso | Média | D7, D8 | Validar antes de apresentar ao candidato |
| R15 | **Reproduzir no sistema novo as regras erradas** | Alta | D3, D4, D5, D9 estão codificadas em sistemas e planilha | Validar regras com os donos antes de especificar; não migrar parâmetros sem revisão |
| R16 | Contorno da trava sob pressão da loja | Alta | Ata; L438 | Exceções formais, com alçada e registro; envolver Operações no desenho |
| R17 | Dono indefinido do produto e das regras | Média | RH, DP, Jurídico e Operações puxam; TI só apoia | Pergunta 2 |
| R18 | Dependência de pessoa única no SESMT | Alta | Uma analista agenda todos os exames | Pergunta 11 |

## 7. Gargalos

Os valores abaixo são estimativas a partir de números declarados na ata.

| Gargalo | Dimensão | Consequência |
|---|---|---|
| Redigitação no DP | 190 admissões × 25 min ≈ **79 h/mês**, sem contar conferência e retrabalho | Reduz a capacidade dos 4 analistas e favorece erros |
| Devolução de pastas | 30% de 190 ≈ **57 pastas/mês** | Idas e vindas por e-mail e pressão na véspera |
| Agendamento de ASO | 1 analista, cerca de 9 admissões por dia útil, cerca de 7 dias de espera | Atrasa o início; a pressão leva a L438 |
| ASO desalinhado da data de início | O exame é pedido logo após a oferta, antes de a data estar firme | Adiamentos invalidam o ASO (L415, L426) |
| Véspera do S-2190 | Depende de documentos e ASO que chegam tarde | Risco de prazo e de início irregular |
| Acesso ao PDV | Cerca de 3 dias | Login compartilhado (R9) |
| Matrícula manual no LMS | 1 a 6 dias após o início, com prazo de 5 | O prazo já nasce quase vencido |
| Lote quinzenal de aprendizes | Espera de até cerca de 15 dias | Prazo de início e de eSocial |
| Piso conferido só na folha | Depois do aceite do candidato | Oferta refeita (L433) |
| Pós-início sem ferramenta | A planilha para em `Iniciado` | Prazos de experiência e conversas de 30/60 dias sem controle |

## 8. Inventário de dados pessoais

Pedido por Paula Nogueira na ata de 22/09. Lista **categorias** observadas, sem valores. A base legal e a retenção ainda precisam de avaliação (pergunta 14).

| Sistema | Dados comuns | Dados sensíveis ou de maior risco | Quem acessa (evidência) | Retenção observada |
|---|---|---|---|---|
| Recruta+ `candidato` | CPF, nome, e-mail, telefone, nascimento | Gestação, PCD e CID, antecedentes (com texto livre) | `gerente_loja` (leitura); fornecedor externo | 24 meses, só reprovados |
| Recruta+ `candidato_bkp_2022` | CPF, nome, e-mail, nascimento | Gestação, CID, antecedentes | `gerente_loja`, `app_relatorios` | **Nenhuma rotina** |
| Recruta+ `oferta` | Salário, nome do aprovador | — | `gerente_loja` (leitura e alteração) | Não definida |
| FolhaCerta `colaborador` | CPF, nome, nascimento, RG, nome da mãe, e-mail pessoal | — | `dp_analista`, `rh_loja` | Não identificada |
| FolhaCerta `contrato` | Salário, CRF, filial, cargo | — | `dp_analista`, `rh_loja` | Não identificada |
| FolhaCerta `exame_admissional` | Data, resultado, CRM do médico | **CID, observação clínica** | `dp_analista`, `rh_loja`; sem perfil do SESMT | Não identificada |
| Planilha | CPF, nome, cargo, loja, datas | **Resultado do ASO; texto livre com saúde, gestação e idade de menor** | Qualquer pessoa com o link | Não definida |
| EducaFarma | E-mail, nome, unidade, progresso | — | Não informado | Não informada |
| E-mail (DP, loja, SESMT, MedTrab) | Cópias de documentos, inclusive de filhos, e dados bancários | **ASO em PDF** | Sem controle evidenciado | Não definida |
| MedTrab, Contábil Alfa | Dados enviados aos terceiros | Saúde; dados de menores | **Sem fonte** | **Sem fonte** |
| PDV e chamados | Login, dados do chamado | — | **Sem fonte** | **Sem fonte** |

Também não há evidência de contrato de tratamento de dados com o fornecedor do Recruta+, a MedTrab ou a Contábil Alfa. **[C]**

## 9. Pontos de apoio

- **FolhaCerta:** estável, já valida piso e gera eventos do eSocial, e continuará como folha. Não há motivo para refazer essa lógica; as travas é que precisam de ajuste (ASO, CRF, experiência).
- **Tabela de pisos da FolhaCerta:** vigência e origem por CCT, boa referência única.
- **EducaFarma:** API REST e trilhas por cargo.
- **MedTrab:** oferece portal com API de agendamento, ainda sem uso.
- **Política RH-012 rev. 4:** recente e assinada por G&G, Jurídico e Encarregada, serve de base para arbitrar conflitos.
- **Patrocínio e grupo de trabalho:** todas as áreas-chave estão na mesa. O fluxo atual já foi desenhado em conjunto, e o checklist do primeiro dia é aproveitável.
- **Campos existentes:** `cargo.exige_crf` e `beneficio_regra` já carregam regras úteis.

## 10. Oportunidades

Estas são direções para avaliar, não decisões. A patrocinadora pediu entendimento antes de escolher ou construir.

| Oportunidade | Ataca | Base | Depende de |
|---|---|---|---|
| Lista única de condições para "pode começar", a partir das fontes oficiais, no lugar da marca manual | D12, R7, R8, R16 | Pedido do escopo | P5, P6 |
| Registro único de dados, levado à FolhaCerta sem redigitação | 79 h/mês | FolhaCerta preservada | P12 |
| Candidato envia os documentos, com conferência antes de chegar ao DP | 57 pastas/mês | — | P9, P14 |
| Agendamento pela API da MedTrab, com ASO alinhado à data de início | SESMT, D4 | API existente | P11 |
| Só "apto/inapto e data" fora do SESMT | D11, R2 | RH-012 11.2 | P11, P14 |
| Matrícula automática por cargo na data de início | D9, R10 | API do EducaFarma | P12, P13 |
| Acesso ao PDV pronto para o primeiro dia | R9 | — | P12 |
| Validar piso e alçada na oferta, com a tabela de CCT | D7, D8, R14 | Pisos na folha | P7, P12 |
| Definição única de etapas e funil, incluindo desistência | D1 | — | P3 |
| Alertas de fim de experiência e de conversas 30/60 | D3, R13 | Datas na folha | P4, P10 |

## 11. Premissas vigentes

Valem até haver resposta. As confirmadas pelas respostas saíram desta lista.

1. RH-012 rev. 4 é a referência nos temas ainda não arbitrados, como o prazo da integração (D9).
2. Documentos, contrato assinado e S-2190 impedem o início, sem exceção (PD-08).
3. O DP verifica a certidão do CRF (PD-09).
4. A lista de documentos do Manual §4 vale até a revisão (PD-14).
5. DP e lojas veem só resultado e data do ASO (PD-16, PD-19).
6. O Recruta+ segue na seleção, e a integração com ele e com a FolhaCerta é tratada como risco, sem assumir API (PD-17).
7. Nenhuma tecnologia ou fornecedor foi escolhido.
8. Benefícios ficam fora, por não constarem da lista do escopo.

## 12. O que mudou com as respostas

As respostas foram parciais, e P9, P10, P12 e P13 vieram só com "Não sei". Esse retorno não foi tratado como decisão. Pendências PD-xx em `02-negocio.md`, seção 9.

### Divergências

| ID | Situação | O que ficou definido | O que falta |
|---|---|---|---|
| D1 | Parcial | Admissão oficial é o conceito do DP: contrato assinado, ASO apto validado e `ATIVO`. Contratado e Iniciado são etapas distintas. **Isso substitui a premissa de usar o primeiro dia** | Decompor 214, 188 e 176 por causa |
| D2 | Resolvida | 184 próprias; franqueadas fora; CD e escritório fora na primeira fase | — |
| D3 | **Reaberta (ver seção 13)** | 30+60 (Marina) | Conflito com M-01.2; contratos em curso; contagem do primeiro dia; prorrogação |
| D4 | Resolvida | 30 dias corridos, sem exceção, mesmo com loja desfalcada; adiamento invalida | Correção nos sistemas |
| D5 | Regra fechada | CRF ativo, inclusive RT; protocolo não vale (Beatriz Lobo) | Verificador, validade, casos em curso |
| D6 | Parcial | Programa de 14 a 24 anos legítimo; entra no fluxo como prioridade 5 | Contábil Alfa, eventos, marco final. A trava de 18 anos da folha continua sendo obstáculo, não regra |
| D7 | Regra fechada | BP sempre; regional acima do piso; gerente indica, sem aprovar sozinho | Prática atual, BP por regional, vaga múltipla |
| D8 | Inalterada | — | Correção da tabela |
| D9 | **Em aberto** | Ninguém arbitrou 5, 15 ou 30 dias; só a RH-012 sustenta os 5 dias | PD-18 |
| D10 | Resolvida | 6 meses, inclusive cópias e backups | Execução; contenção do backup de 2022 |
| D11 | Parcial | CID só no ambiente do SESMT | Demais campos por perfil |
| D12 | Parcial | ASO e CRF impedem o início | Documentos, contrato e S-2190 (Sérgio não soube) |
| D13, D14 | Inalteradas | — | PD-17 |
| D15 | Superada | O registro passa a começar no candidato aprovado | — |

### Riscos

| ID | Mudança |
|---|---|
| R5, R6 | **Mantidos como críticos.** Paula definiu que gravidez e antecedentes não são perguntados nem guardados, mas a coleta, os casos e o responsável ficaram sem resposta (PD-23) |
| R1, R2, R3 | **Mantidos.** Contenção imediata sem resposta (PD-22). CID no Recruta+ (`pcd_cid`) também fica fora da regra |
| R4 | Agravado: a regra de 6 meses alcança cópias e backups. A eliminação precisa respeitar eventual guarda dos casos de R5 e R6 |
| R7 | Regra fechada; exceção descartada para o ASO |
| R8 | Regra fechada, mas o tratamento de quem já começou só com protocolo segue sem resposta (PD-09) |
| R9 | Mantido, sem resposta sobre a causa (PD-17) |
| R16 | Reforçado: não existe caminho formal de exceção para ASO, o que aumenta a tentação de contorno |
| R17 | Mantido: metas, prazo, orçamento e dono sem resposta; Helena indicou Vera Castro (CFO) para os três primeiros |

### Riscos novos

| ID | Risco | Grav. | Evidência | Encaminhamento |
|---|---|---|---|---|
| R19 | Manual antigo segue formalmente vigente nas seções não revogadas, e as lojas o consultam até o sistema chegar | Alta | P4 (Rogério): 45+45, gerente aprovando e prazo de 15 dias continuam publicados | Comunicar as regras já, sem esperar o sistema (US-09) |
| R20 | Riscos críticos sem responsável nomeado | Crítica | P14, P15 e P6 | Helena nomeia responsáveis (US-12, US-15) |
| R21 | O fim da redigitação depende de integração desconhecida | Alta | P12 sem resposta; só há evidência de dump noturno da FolhaCerta | Levantamento antes de decidir (US-20) |
| R22 | `ATIVO` é a definição oficial, mas a folha não registra desistência antes do início | Média | P3; `contrato.status` | Registrar desistência; manter as três etapas (US-37) |
| R23 | Áreas operacionais não responderam, e gerentes, BPs e analistas não foram ouvidos | Alta | P9, P10, P12, P13 e parte de P5 e P7 | Sessão de validação (`02-negocio.md`, seção 12) |

### Novos nomes

- **Vera Castro (CFO):** indicada por Helena para metas, prazo e orçamento; ainda não consultada.
- **Beatriz Lobo:** Assuntos Regulatórios, conforme a ata de 28/10.

## 13. O que mudou com as comunicações de 28/10 e 30/10

Avaliação completa em `08-mudancas.md`.

### Divergência nova

| ID | Tema | Lados | Situação |
|---|---|---|---|
| D16 | Experiência | RH-012 §4.1 e Marina: 30+60. Sérgio, em informe no comitê: 45+45 a partir de 01/12/2026 | **Em aberto.** Segue 30+60 até decisão de Marina e Helena (PD-26) |

### Riscos novos

| ID | Risco | Grav. | Evidência | Encaminhamento |
|---|---|---|---|---|
| R24 | Duas regras de experiência em circulação a partir de 01/12 | Alta | M-01.2; sem revisão da RH-012 | Decidir antes da data (PD-26); não divulgar como regra até lá |
| R25 | Descumprir a Portaria CVS-SP 88/2026 a partir de 01/02/2027 | Alta | M-02; nenhum sistema indica quem aplica injetáveis; texto ainda não analisado | Procedimento provisório independente do sistema (US-53) |
| R26 | CRNM vence sem controle ou condição migratória fica exposta | Média | M-02; validade de documento não existe no processo; a CRNM pode vencer depois da experiência | US-55, US-56 e avaliação de Paula (PD-29) |

**R17:** a ata do comitê não trata de metas, prazo, orçamento nem dono, então o risco se mantém. **Pedido de rescisão e homologação:** fora do escopo; aguarda resposta de Helena (PD-27).

### Inventário de dados pessoais

Acréscimos à seção 8, ainda sem sistema de origem:

| Dado | Natureza | Acesso previsto | Retenção |
|---|---|---|---|
| Comprovante de vacinação | **Dado de saúde** | Só SESMT; fora dele, atendido ou pendente | A definir (PD-20) |
| CRNM: número e validade | Identificação | DP | A definir (PD-20) |
| Condição de refugiado ou migrante | **Risco de discriminação** | Mínimo, a avaliar por Paula | A definir (PD-20) |
