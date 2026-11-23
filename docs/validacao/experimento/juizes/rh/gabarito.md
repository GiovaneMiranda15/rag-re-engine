# Gabarito — Caso rh-admissao (Drogarias Caliandra S.A., fictício)

Caminhos relativos a `fontes/`. Abreviações: `folha` = `SIS-01-folha-dp/folhacerta_dump.sql`; `recruta` = `SIS-02-recrutamento/recrutamais_dump.sql`; `planilha` = `SIS-03-controle-lojas/controle_admissoes_2026.csv`; `leiame` = `SIS-03-controle-lojas/LEIA-ME.md`; `trilhas` = `SIS-04-treinamento/export_trilhas_lms.csv`; `matriculas` = `SIS-04-treinamento/export_matriculas_lms.csv`; `manual` = `geral/manual-admissao-lojas-v3.2-2019.md`; `comunicado` = `geral/comunicado-dp-07-2024.md`; `politica` = `geral/politica-RH-012-admissao-integracao.md`; `ata` = `geral/ata-2026-09-22-grupo-trabalho-admissao.md`; `fluxo` = `geral/fluxo-admissao-atual.md`. "Linha N" da `planilha` é o valor N da coluna `id`. "Linha N" da `planilha` é o valor N da coluna `id`.

## Divergências

| ID | Conceito | Valores e onde aparecem | Cruzamento DDL/trigger × documento? |
|---|---|---|---|
| D1 | Validade do ASO no início | 30 dias (`politica` 6.2); 60 dias (`leiame` regra 2); 90 dias (`folha`, `fn_valida_contrato`: `data_admissao - 90`); na prática, ASO com 63 dias na `planilha` linha 415 e com 45 dias na linha 426 | Sim |
| D2 | Admissão de aprendiz | 14 a 24 anos (`politica` 4.2); mínimo de 18 anos (`folha`, `fn_valida_contrato`) e sem o tipo APRENDIZ (`folha`, `chk_tipo_contrato`) | Sim |
| D3 | Contrato de experiência | 30+60 (`politica` 4.1); 45+45 (`manual` seção 6, `leiame` regra 3, coluna `experiencia` da `planilha`); padrão de 45 dias (`folha`, `dias_experiencia`) | Sim |
| D4 | Identificador da pessoa | `CHAR(11)` só dígitos (`folha`, `colaborador.cpf`); `varchar(14)` com máscara (`recruta`, `candidato.cpf`); formato livre (`leiame` e linhas 419/433 da `planilha`); e-mail, sem CPF (`matriculas`) | Só entre sistemas |
| D5 | Código da loja | `147` (`folha`); `LJ-0147` (`recruta`); `147 - Savassi` (`planilha`); `MG-SAV` (`matriculas`) | Só entre sistemas |
| D6 | "Admissão concluída" | Oferta aceita = CONTRATADO (`recruta`, `trg_oferta_aceita`); contrato ATIVO (`folha`, comentário de `contrato.status`); primeiro dia + kit = Iniciado (`leiame`); números de 214/188/176 (`ata`) | Sim |
| D7 | Exigência de CRF do farmacêutico | CRF ativo inclusive RT, sem protocolo (`politica` 7); protocolo por 30 dias (`leiame` regra 4); trigger cobre só `FARM`, embora `FARM_RT` tenha `exige_crf` verdadeiro (`folha`); pedir cópia da carteira (`manual` seção 7) | Sim |
| D8 | Retenção de candidatos não contratados | 6 meses (`politica` 11.3); 24 meses (`recruta`, `sp_expurgo_candidatos`); candidato 877, reprovado em 10/02/2025, segue na base (`recruta`) | Sim |
| D9 | Alçada de aprovação da oferta | BP de RH sempre + regional acima do piso (`politica` 3); gerente de loja (`manual` seção 2); `aprovador_perfil` só aceita gerente de loja ou regional, sem RH (`recruta`); "Gerente aprova" (`fluxo`, etapa B) | Sim |
| D10 | Piso de balconista em SP | R$ 1.820,00 desde 01/03/2026 (`folha`, `cargo_piso`); R$ 1.750,00 de 2025 (`recruta`, `tabela_salarial`, vagas 502/505/507) | Só entre sistemas |
| D11 | Prazo do treinamento de integração | 5º dia corrido (`politica` 9); 15 dias (`manual` seção 9); 30 dias (`trilhas`, T-BALC-01, T-FARM-01, T-CAIXA-01) | Só documento × export |

## Gargalos

| ID | Gargalo | Evidência |
|---|---|---|
| G1 | Redigitação da mesma admissão em Recruta+, planilha e FolhaCerta (cerca de 25 min cada) | `ata` (DP); `fluxo` etapas C, D e K |
| G2 | Agendamento de ASO por e-mail, com uma única analista e cerca de 7 dias de espera | `ata` (Exame admissional); `planilha`, `dt_solic_aso` → `dt_aso`; `fluxo` etapas E e F |
| G3 | Pastas de documentos enviadas por e-mail, com cerca de 30% de devolução e 4 analistas para todas as regionais | `ata` (DP); `fluxo`, laço J → H |
| G4 | Aprendiz depende de lote quinzenal da Contábil Alfa, fora da folha | `leiame` regra 7; `ata` (Aprendizes); `fluxo`, nota final; `planilha` linha 440 |
| G5 | Cerca de 3 dias sem acesso ao PDV, por chamado manual à TI | `ata` (Lojas); `leiame` checklist; `fluxo` etapa O |
| G6 | Oferta com salário defasado volta da folha e precisa ser refeita | `planilha` linha 433; `recruta` ofertas 7005/7006; `folha`, validação de piso |

## Riscos

| ID | Risco | Evidência |
|---|---|---|
| R1 | Legal/LGPD: a seleção registra `gestante`, `pcd_cid`, `antecedentes_ok` e `antecedentes_obs`, e `gerente_loja` pode ler (possível discriminação, Lei 9.029/95, e dado sensível, LGPD art. 11) | `recruta`, DDL de `candidato`, GRANT e candidatos 1009, 1007 e 877 |
| R2 | LGPD: `candidato_bkp_2022` guarda dados sensíveis de reprovados desde 2021, fora do expurgo, com leitura por `gerente_loja` e `app_relatorios` | `recruta`, DDL, `sp_expurgo_candidatos`, GRANT e registros 311, 344 e 402 |
| R3 | LGPD: CID e observação clínica ficam legíveis pelo portal do gestor, contra o acesso exclusivo do SESMT | `folha`, `exame_admissional`, GRANT a `rh_loja`, registro 3380; `politica` 11.2 |
| R4 | LGPD/discriminação: planilha com CPF e saúde em texto livre, com link aberto e editável | `leiame` (compartilhamento e campo `obs`); `planilha` linhas 438 e 447 |
| R5 | Legal/saúde ocupacional: início antes do ASO, e o trigger não impede ASO posterior à admissão | `planilha` linha 438 (início 06/10, ASO 09/10); `folha`, contrato 9240, exame 3380, condição só com limite inferior; `politica` 6.1 |
| R6 | Sanitário: RT em atividade sem CRF ativo comprovado | `planilha` linha 431; `folha`, contrato 9233 com `crf_numero` nulo; `politica` 7 |
| R7 | Rastreabilidade/sanitário: login do gerente compartilhado, inclusive em venda com receita | `ata` (Lojas) |
| R8 | Trabalhista: o fim da experiência é calculado com 45 dias, enquanto a política prevê 30+60; datas de conversão ou término podem sair erradas | `folha`, `fn_valida_contrato` e contratos com `dias_experiencia` 45; `politica` 4.1 |

## Pontos de apoio

| ID | Ponto de apoio | Evidência |
|---|---|---|
| P1 | FolhaCerta estável, com validação de piso e geração de eventos do eSocial | `folha`, triggers e `evento_esocial`; `ata` (Sistemas) |
| P2 | Política RH-012 recente, aprovada por Gente & Gestão, Jurídico e Encarregada | `politica`, cabeçalho |
| P3 | EducaFarma com API REST e trilhas por cargo | `ata` (Sistemas); `trilhas` |
| P4 | Checklist de primeiro dia já usado pelas lojas | `leiame`, checklist |
| P5 | Trilha de auditoria do eSocial, com prazo, envio e recibo por evento | `folha`, `evento_esocial` e `esocial_prazo` |

## Oportunidades

| ID | Oportunidade | Evidência |
|---|---|---|
| O1 | Integrar Recruta+ e FolhaCerta para acabar com a redigitação (cerca de 190 × 25 min/mês) | `ata` (Números e DP); `fluxo` |
| O2 | Usar a API de agendamento da MedTrab | `ata` (Exame admissional) |
| O3 | Entrega digital de documentos pelo candidato, com validação na origem | `ata` (30% de devolução); `fluxo`, etapas H a J |
| O4 | Disparar acessos e matrícula a partir do evento de admissão | `ata` (Lojas e Sistemas); `matriculas` (matrícula após o início); `fluxo`, etapas O e R |
| O5 | Bloquear o início por regras únicas (ASO e CRF), reaproveitando a validação existente | `folha`, `fn_valida_contrato`; `politica` 6 e 7; `planilha` linhas 431 e 438 |
| O6 | Cadastro mestre de pessoa e de loja, com expurgo automático por política | `folha`, `recruta`, `matriculas`; `politica` 11.3 |

## Armadilhas (apontá-las como problema real é falso positivo)

| ID | Parece | Por que não é | Evidência |
|---|---|---|---|
| T1 | Prazo de documentos: 3 × 5 dias úteis | A seção 4 do manual foi revogada explicitamente; todas as fontes vigentes dizem 5 | `manual` seção 4; `comunicado`; `politica` 2; `leiame` regra 1 |
| T2 | Número de lojas: 212 × 184 | 212 é o total; 184 são as próprias e 28 as franqueadas | `../escopo.md`; `politica` 1; `ata` |
| T3 | Carência do plano: 90 × 30 dias | Valem para públicos diferentes: geral e farmacêuticos (Acordo Coletivo de 2024) | `politica` 8; `folha`, `beneficio_regra`; `leiame` regra 6; `planilha` |
| T4 | Jornada: 44h × 220h | Mesma jornada, semanal e mensal | `politica` 5; `leiame` regra 5; `folha`, `cargo.jornada_mensal` |
| T5 | Prazo do eSocial: véspera × dia 15 | São eventos diferentes: S-2190 na véspera e S-2200 até o dia 15 do mês seguinte | `folha`, `esocial_prazo` e `fn_gera_esocial`; `politica` 10; `ata` (DP) |
| T6 | Piso de balconista: R$ 1.690 × R$ 1.820 | São pisos de UFs diferentes, MG e SP (o problema real de SP é o D10) | `folha`, `cargo_piso` |
| T7 | Carlos Eduardo Lima duplicado na folha | São homônimos, com CPF, nascimento, mãe e filial diferentes | `folha`, matrículas 50211 e 58801 |

## Classificação das mudanças

| ID | Origem | Afirmação | Classe | Temas/itens impactados |
|---|---|---|---|---|
| C1 | `mudancas/M-01`, informe 1 | Farmacêutico, inclusive RT, só inicia com CRF ativo; protocolo não basta | existente | D7, R6, O5 (repete `politica` 7) |
| C2 | `mudancas/M-01`, informe 2 | Experiência padrão 45+45 a partir de 01/12/2026 | conflitante | D3, R8 (contradiz `politica` 4.1; depende de revisão aprovada por Helena e Marina) |
| C3 | `mudancas/M-01`, informe 3 | Incluir cálculo de rescisão e homologação de desligamentos | fora_escopo | Escopo (`../escopo.md` exclui desligamento); sem impacto nos requisitos |
| C4 | `mudancas/M-02`, 1º parágrafo informativo | Portaria CVS-SP 88/2026 (fictícia): comprovante de vacinação para quem aplica injetáveis em SP, somado ao ASO | complementar | Documentos e exame admissional, `politica` 2 e 6, O3, O5, R5; cargo e UF como condição; vigência em 01/02/2027 |
| C5 | `mudancas/M-02`, 2º parágrafo informativo | Programa Acolher: admissão com CRNM e controle de validade | novo | Novo tema de documentação de migrantes; D4 e O6 (cadastro de pessoa), O3 (entrega digital), G3 (conferência) |

## Contagem

D: 11 | G: 6 | R: 8 | P: 5 | O: 6 | T: 7 | C: 5
