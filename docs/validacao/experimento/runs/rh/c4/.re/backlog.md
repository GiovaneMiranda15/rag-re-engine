# Backlog

## EP-001 — Governança, contenção e transição [proposto]

Trata exposição atual, alinha as regras nos legados, migra e prepara usuários.

Prioridade: Must

### FT-001 — Contenção imediata de dados [proposto]

Medidas sem depender do novo sistema.

Prioridade: Must

#### US-001 — Fechar o link aberto da planilha [proposto]

Como Encarregada de Dados, quero restringir o acesso à planilha a pessoas autorizadas, para reduzir a exposição de CPF e dados de saúde.

Prioridade: Must · Requisitos: RNF-001

- Dado o link atual, quando a medida é aplicada, então acesso sem login é negado.
- Dado usuário sem autorização, quando tenta abrir a planilha, então é negado.

#### US-002 — Revisar acessos a dados sensíveis nos legados [proposto]

Como Encarregada de Dados, quero revisar os acessos de gerentes a candidato, backup e exame, para eliminar acesso sem necessidade.

Prioridade: Must · Requisitos: RNF-002, RN-007, RN-014

- Dado o usuário gerente_loja, quando a revisão termina, então não lê candidato_bkp_2022 nem campos sensíveis.
- Dado o perfil rh_loja, quando a revisão termina, então não lê CID nem observação clínica.

#### US-003 — Eliminar cópias vencidas de candidatos [proposto]

Como Encarregada de Dados, quero eliminar a tabela de backup e os registros vencidos conforme a decisão de Q-043, para cumprir os 6 meses.

Prioridade: Must · Requisitos: RN-006

- Dado candidato_bkp_2022, quando a decisão é executada, então não restam dados de não contratados vencidos.
- Dado reprovado há 7 meses, quando a limpeza roda, então seus dados são eliminados.

### FT-002 — Alinhamento das regras nos legados [proposto]

Manual, planilha, FolhaCerta, Recruta+ e EducaFarma.

Prioridade: Must

#### US-004 — Revogar regras divergentes da planilha e do manual [proposto]

Como Coordenadora de Operações, quero publicar as regras confirmadas no manual e na planilha, para as lojas pararem de seguir valores vencidos.

Prioridade: Must · Requisitos: RF-024, RN-001, RN-002, RN-003, RN-004

- Dado o Leia-me, quando revisado, então indica ASO de 30 dias, experiência 30+60 e veda protocolo de CRF.
- Dado o manual 3.2, quando publicado o novo texto, então a versão antiga sai de circulação.

#### US-005 — Ajustar regras da FolhaCerta [proposto]

Como analista do DP, quero ter a janela de ASO, a experiência e o CRF corretos na folha, para evitar ativação fora da regra.

Prioridade: Must · Requisitos: RF-024, RN-001, RN-002, RN-003

- Dada admissão com ASO de 31 dias, quando se tenta ativar, então é recusada.
- Dado cargo FARM_RT sem CRF, quando se tenta ativar, então é recusado.

#### US-006 — Tirar CID da FolhaCerta [proposto]

Como Encarregada de Dados, quero remover ou bloquear o CID na FolhaCerta, para CID só existir no ambiente do SESMT.

Prioridade: Must · Requisitos: RN-007, RF-024

- Dado novo exame, quando registrado na folha, então não há CID.
- Dado CID já gravado, quando a limpeza roda, então ele deixa de existir fora do SESMT.

#### US-007 — Atualizar tabela e campos do Recruta+ [proposto]

Como Business Partner de RH, quero alinhar piso, alçada e campos do Recruta+, para evitar oferta com dado vencido.

Prioridade: Must · Requisitos: RF-024, RN-009, RN-012

- Dado balconista em SP, quando a tabela é consultada, então coincide com a FolhaCerta.
- Dado formulário de candidato, quando exibido, então não pede gravidez nem antecedentes.

#### US-008 — Corrigir prazo da integração no EducaFarma [proposto]

Como responsável por treinamentos sanitários, quero ver o 5º dia na trilha, para o LMS refletir a RH-012.

Prioridade: Must · Requisitos: RF-024, RN-004

- Dada a trilha de integração, quando consultada, então o prazo é de 5 dias.
- Dado matriculado após a mudança, quando chega o 6º dia sem conclusão, então aparece vencido.

### FT-003 — Migração, convivência e capacitação [proposto]

Carga inicial, operação paralela e treinamento.

Prioridade: Must

#### US-009 — Carregar admissões em andamento [proposto]

Como analista do DP, quero trazer os casos em aberto, para não recomeçar processos.

Prioridade: Must · Requisitos: RF-018

- Dada linha em andamento, quando a carga roda, então o processo surge com datas e situação.
- Dada linha com campo livre, quando a carga roda, então o campo obs não é levado.

#### US-010 — Operar em convivência por onda de lojas [proposto]

Como Coordenadora de Operações, quero saber qual canal cada loja usa, para evitar registro duplo.

Prioridade: Must · Requisitos: RF-018

- Dada loja na onda ativa, quando abre admissão, então usa só o novo sistema.
- Dada loja fora da onda, quando consulta o sistema, então vê a orientação de usar o processo atual.

#### US-011 — Capacitar usuários [proposto]

Como Coordenadora de Operações, quero capacitar gerentes, DP, SESMT e BPs, para a adoção não gerar erro.

Prioridade: Should · Requisitos: RF-023

- Dada onda planejada, quando entra em operação, então os usuários previstos estão capacitados.
- Dado gerente sem capacitação, quando a loja entra, então a pendência aparece.

## EP-002 — Oferta [proposto]

Da aprovação do candidato ao aceite.

Prioridade: Must

### FT-004 — Abertura do processo [proposto]

Um processo por admissão.

Prioridade: Must

#### US-012 — Abrir admissão a partir da oferta [proposto]

Como Business Partner de RH, quero abrir o processo com a oferta, para ter histórico único.

Prioridade: Must · Requisitos: RF-011, RN-016

- Dado candidato aprovado em loja própria, quando a oferta é criada, então há um processo vinculado ao CPF.
- Dada loja franqueada, quando se tenta abrir, então é recusado.

### FT-005 — Aprovação e piso [proposto]

Alçada da RH-012 e piso da FolhaCerta.

Prioridade: Must

#### US-013 — Aprovar oferta conforme alçada [proposto]

Como Business Partner de RH, quero aprovar ou recusar a oferta, para cumprir a RH-012.

Prioridade: Must · Requisitos: RF-012, RN-005

- Dada oferta no piso, quando o BP aprova, então pode ser apresentada.
- Dado gerente de loja, quando tenta aprovar, então só consegue indicar o candidato.

#### US-014 — Exigir regional acima do piso [proposto]

Como gerente regional, quero aprovar ofertas acima do piso, para controlar o custo.

Prioridade: Must · Requisitos: RF-012, RN-005, RN-009

- Dada oferta de R$ 1.820,01 para balconista em SP, quando o BP aprova, então vai ao regional.
- Dada oferta de R$ 1.820,00, quando o BP aprova, então não vai ao regional.

#### US-015 — Conferir piso da FolhaCerta [proposto]

Como Business Partner de RH, quero ver o piso vigente na oferta, para evitar retrabalho.

Prioridade: Must · Requisitos: RF-013, RN-009

- Dada oferta de R$ 1.750,00 para balconista em SP, quando registrada, então é recusada.
- Dado piso indisponível, quando registrada, então fica retida para análise.

## EP-003 — Documentos [proposto]

Coleta, conferência e prazo.

Prioridade: Must

### FT-006 — Checklist e conferência [proposto]

Documentos por modalidade e cargo.

Prioridade: Must

#### US-016 — Enviar documentos por checklist [revisar]

Como gerente de loja, quero enviar os documentos pelo sistema, para reduzir devolução.

Prioridade: Must · Requisitos: RF-003, RNF-001, RF-027

- Dado item faltante, quando tenta enviar, então o sistema aponta o item.
- Dado envio completo, quando concluído, então o documento não circula por e-mail.
- Dada admissão do programa Acolher, quando o checklist é exibido, então a CRNM aparece como documento de identificação.

#### US-017 — Conferir ou devolver pasta [revisar]

Como analista do DP, quero conferir e devolver com motivo, para medir as causas.

Prioridade: Must · Requisitos: RF-003, RF-025

- Dado documento ilegível, quando devolvido, então o motivo é obrigatório.
- Dada pasta conferida, quando aprovada, então o critério muda com data e autor.

#### US-018 — Controlar os 5 dias úteis [proposto]

Como analista do DP, quero ver quem está fora do prazo, para agir antes do início.

Prioridade: Must · Requisitos: RN-010

- Dado início em 15/03/2027, quando há pendência em 09/03/2027, então a admissão aparece atrasada.
- Dado documentos completos em 08/03/2027, quando calculado, então fica no prazo.

### FT-024 — Programa Acolher e CRNM [revisar]

Pessoas refugiadas e migrantes, a partir do 1º trimestre de 2027.

Prioridade: Must

#### US-054 — Aceitar CRNM no checklist [revisar]

Como analista do DP, quero conferir CRNM como documento de identificação, para admitir pelo programa Acolher.

Prioridade: Must · Requisitos: RN-021, RF-027

- Dada admissão do programa Acolher, quando o checklist é gerado, então a CRNM aparece.
- Dada CRNM sem validade, quando o DP tenta concluir, então a data é exigida.

#### US-055 — Controlar validade da CRNM [revisar]

Como analista do DP, quero ver a validade da CRNM e receber alerta, para agir antes do vencimento.

Prioridade: Must · Requisitos: RF-028

- Dada CRNM vigente, quando consultada, então mostra a validade.
- Dada CRNM vencida antes do início, quando consultada, então aparece como pendência, conforme Q-053.

#### US-056 — Enviar pessoa com CRNM aos legados [revisar]

Como analista do DP, quero tratar a CRNM na integração, para evitar recusa por falta de campo.

Prioridade: Must · Requisitos: RF-029

- Dada pessoa com CRNM e CPF, quando enviada, então o CPF é a chave.
- Dada pessoa sem CPF, quando enviada, então fica retida.

#### US-057 — Restringir a condição de refugiado ou migrante [revisar]

Como Encarregada de Dados, quero limitar quem vê essa condição, para evitar uso indevido.

Prioridade: Should · Requisitos: RN-022

- Dada a matriz de Q-054, quando um papel consulta, então vê só o permitido.
- Dado acesso negado, quando ocorre, então fica na trilha.

## EP-004 — Exame admissional [proposto]

Pedido, agendamento e validade do ASO.

Prioridade: Must

### FT-007 — Acompanhamento e validade do ASO [proposto]

Regra de 30 dias e sigilo.

Prioridade: Must

#### US-019 — Solicitar e acompanhar exame [proposto]

Como gerente de loja, quero solicitar e ver a situação do exame, para parar de usar e-mail.

Prioridade: Must · Requisitos: RF-005

- Dado pedido, quando registrado, então aparece na fila do SESMT.
- Dado exame agendado, quando consultado, então mostra data sem dado clínico.

#### US-020 — Validar janela de 30 dias do ASO [proposto]

Como analista do SESMT, quero ter a validade calculada, para evitar início irregular.

Prioridade: Must · Requisitos: RN-001, RN-011

- Dado início em 20/03/2027 e ASO de 18/02/2027, quando calculado, então é válido.
- Dado ASO de 17/02/2027 ou posterior ao início, quando calculado, então é inválido.

#### US-021 — Reavaliar ASO ao adiar início [proposto]

Como gerente de loja, quero ver o efeito de mudar a data, para não começar com ASO vencido.

Prioridade: Must · Requisitos: RF-015, RN-001

- Dado adiamento que vence o ASO, quando salvo, então o início fica bloqueado.
- Dado adiamento que não vence, quando salvo, então o critério segue atendido.

#### US-022 — Definir o que cada papel vê do ASO [proposto]

Como Encarregada de Dados, quero registrar e aplicar a decisão sobre visibilidade, para resolver o conflito com a RH-012.

Prioridade: Must · Requisitos: RN-013, RN-007

- Dada decisão de Q-040, quando aplicada, então DP e gerente veem só o definido.
- Dada ausência de decisão, quando se tenta homologar o módulo, então a história fica impedida.

### FT-008 — Agendamento com a clínica [proposto]

Integração com a MedTrab.

Prioridade: Should

#### US-023 — Agendar pela API da MedTrab [proposto]

Como analista do SESMT, quero agendar pelo sistema, para reduzir espera e dependência.

Prioridade: Should · Requisitos: RF-019

- Dada vaga na agenda, quando agendado, então retorna data e local.
- Dada falha da API, quando esgotada, então vai para fila manual.

## EP-005 — Contrato e eSocial [proposto]

Cadastro na folha, contrato e eventos.

Prioridade: Must

### FT-009 — Cadastro sem redigitação [proposto]

Envio à FolhaCerta.

Prioridade: Must

#### US-024 — Enviar cadastro à FolhaCerta [revisar]

Como analista do DP, quero enviar sem digitar, para eliminar os 25 minutos de redigitação.

Prioridade: Must · Requisitos: RF-002, RF-029

- Dada oferta aceita e pasta conferida, quando envia, então a folha recebe os dados sem nova digitação.
- Dada folha indisponível, quando envia, então o cadastro fica na fila.
- Dada pessoa com CRNM, quando enviada à folha, então o tratamento segue a decisão de Q-053.

#### US-025 — Validar CPF e chave única [revisar]

Como analista do DP, quero detectar CPF inválido ou divergente, para evitar erro na folha.

Prioridade: Must · Requisitos: RF-002, RF-029

- Dado CPF com máscara, quando recebido, então é normalizado para 11 dígitos.
- Dado CPF com dígito inválido, quando recebido, então é retido.
- Dada pessoa com CRNM sem CPF, quando recebida, então fica retida conforme Q-053.

### FT-010 — Contrato e eventos [proposto]

Situação do contrato, S-2190 e S-2200.

Prioridade: Must

#### US-026 — Acompanhar contrato [proposto]

Como analista do DP, quero registrar a situação do contrato, para saber o que falta.

Prioridade: Must · Requisitos: RF-004

- Dado contrato assinado, quando registrado, então há data e autor.
- Dado contrato não assinado, quando há consulta, então a admissão não conta como concluída.

#### US-027 — Acompanhar S-2190 e S-2200 [proposto]

Como analista do DP, quero ver prazo, envio e recibo, para não correr na véspera.

Prioridade: Must · Requisitos: RF-006, RN-017

- Dado início em 15/03/2027, quando calculado, então os prazos são 14/03 e 15/04/2027.
- Dado S-2190 sem envio na véspera, quando chega a data, então há alerta.

## EP-006 — Prontidão e início [proposto]

Em um só lugar, quando o colaborador pode começar.

Prioridade: Must

### FT-011 — Painel Pode começar [proposto]

Critérios e bloqueios.

Prioridade: Must

#### US-028 — Ver se pode começar [revisar]

Como gerente de loja, quero ver em um só lugar a situação, para saber quando conto com o colaborador.

Prioridade: Must · Requisitos: RF-001, RN-011, RNF-008, RF-026

- Dados ASO válido e CRF não aplicável, quando abre o painel, então vê Pode começar.
- Dado ASO vencido, quando abre o painel, então vê Não pode começar e a pendência.
- Dado critério condicional aplicável, quando o gerente abre o painel, então vê a situação sem dado de saúde.

#### US-029 — Bloquear início com critério bloqueante [revisar]

Como gerente de loja, quero ser impedido de confirmar início irregular, para evitar risco legal.

Prioridade: Must · Requisitos: RN-011, RNF-004, RN-019

- Dado ASO vencido e loja desfalcada, quando confirma início, então é bloqueado sem exceção.
- Dado farmacêutico só com protocolo, quando confirma início, então é bloqueado.
- Dado aplicador de injetáveis em SP com início em 01/02/2027, sem comprovante de vacinação, quando confirma o início, então é bloqueado.

#### US-030 — Configurar critérios como bloqueio ou alerta [proposto]

Como Coordenadora de Operações, quero parametrizar os critérios restantes, para aplicar a decisão de Q-031.

Prioridade: Should · Requisitos: RN-018

- Dado critério como alerta, quando pendente, então não bloqueia.
- Dado critério como bloqueante, quando pendente, então bloqueia.

### FT-012 — CRF de farmacêuticos [proposto]

Certidão e conferência.

Prioridade: Must

#### US-031 — Registrar e conferir certidão de CRF [proposto]

Como responsável de Assuntos Regulatórios, quero conferir a certidão, para garantir CRF ativo.

Prioridade: Must · Requisitos: RF-016, RN-003

- Dado RT com certidão conferida, quando registrado, então o critério fica atendido.
- Dado protocolo de inscrição, quando anexado, então o critério segue pendente.

### FT-013 — Acesso ao PDV [proposto]

Acesso individual no início.

Prioridade: Must

#### US-032 — Acompanhar pedido de acesso ao PDV [proposto]

Como gerente de loja, quero ver o pedido a partir da liberação, para não precisar emprestar login.

Prioridade: Must · Requisitos: RF-007, RNF-003

- Dada liberação, quando confirmada, então o pedido é aberto.
- Dado acesso não ativo na véspera, quando consulta, então vê alerta.

### FT-023 — Vacinação para aplicar injetáveis em SP [revisar]

Portaria CVS-SP 88/2026, a partir de 01/02/2027.

Prioridade: Must

#### US-050 — Definir processo provisório da Portaria [revisar]

Como analista do SESMT, quero um processo manual para 01/02/2027, para cumprir a norma mesmo sem o sistema.

Prioridade: Must · Requisitos: RN-019

- Dada admissão de aplicador em SP com início em 01/02/2027, quando o sistema ainda não opera, então o SESMT confere o comprovante antes do início.
- Dado comprovante faltante, quando chega a véspera, então o início não é confirmado.

#### US-051 — Marcar vaga que aplica injetáveis [revisar]

Como Business Partner de RH, quero marcar a vaga, para o critério surgir só quando aplicável.

Prioridade: Must · Requisitos: RF-026

- Dada vaga marcada em SP, quando o processo abre, então o critério aparece.
- Dada vaga não marcada, quando o processo abre, então não aparece.

#### US-052 — Receber comprovante de vacinação no SESMT [revisar]

Como analista do SESMT, quero receber os comprovantes de hepatite B e tétano com o ASO, para manter o sigilo.

Prioridade: Must · Requisitos: RN-019, RN-020

- Dados os dois comprovantes conferidos, quando registrados, então o critério fica atendido.
- Dado usuário fora do SESMT, quando tenta abrir o comprovante, então é negado.

#### US-053 — Aplicar vigência e UF ao critério de vacinação [revisar]

Como gerente de loja, quero ver o critério só quando valer, para não pedir comprovante sem necessidade.

Prioridade: Must · Requisitos: RN-019, RF-026

- Dado início em 01/02/2027 em SP, quando calculado, então o critério vale.
- Dado início em 31/01/2027 ou loja em MG, quando calculado, então não se aplica.

## EP-007 — Treinamentos e experiência [proposto]

Do início ao fim da experiência.

Prioridade: Must

### FT-014 — Treinamentos obrigatórios [proposto]

Prazos, restrição e matrícula.

Prioridade: Must

#### US-033 — Ver treinamentos do colaborador [proposto]

Como gerente de loja, quero ver prazos e situação, para cumprir as trilhas.

Prioridade: Must · Requisitos: RF-008, RN-004

- Dado início em 15/03/2027, quando consulta, então integração vence em 20/03/2027.
- Dado curso vencido, quando consulta, então aparece destacado.

#### US-034 — Indicar restrição de atendimento sozinho [proposto]

Como gerente de loja, quero saber quem não pode atender sozinho, para cumprir a RH-012.

Prioridade: Must · Requisitos: RF-022, RN-004

- Dada integração não concluída, quando consulta, então vê a restrição.
- Dada integração concluída, quando atualiza, então a restrição sai.

#### US-035 — Matricular automaticamente [proposto]

Como gerente de loja, quero ter o colaborador matriculado até o início, para não matricular à mão.

Prioridade: Should · Requisitos: RF-014

- Dado início confirmado de balconista, quando liberado, então as três trilhas ficam matriculadas.
- Dada falha da API, quando esgotada, então há alerta e opção manual.

### FT-015 — Fim da experiência [proposto]

Marcos, alertas e decisões.

Prioridade: Must

#### US-036 — Controlar marcos de 30 e 90 dias [proposto]

Como analista do DP, quero registrar prorrogação ou encerramento, para não perder o prazo.

Prioridade: Must · Requisitos: RF-009, RN-002

- Dado colaborador iniciado, quando calculado, então há marcos de 30 e 90 dias.
- Dado marco sem decisão, quando chega a data, então fica vencido.

## EP-008 — Aprendiz [proposto]

Entrada do aprendiz no fluxo único.

Prioridade: Should

### FT-016 — Fluxo de aprendiz [proposto]

Faixa de 14 a 24 anos e critérios próprios.

Prioridade: Should

#### US-037 — Acompanhar aprendiz no fluxo único [proposto]

Como gerente de loja, quero ver o aprendiz no mesmo painel, para não ter processo paralelo.

Prioridade: Should · Requisitos: RF-021, RN-008

- Dado aprendiz de 16 anos, quando aberto, então não há recusa por idade.
- Dado candidato de 25 anos a aprendiz, quando aberto, então aponta fora da faixa.

#### US-038 — Definir saída do cadastro de aprendiz [proposto]

Como analista do DP, quero aplicar a decisão sobre a Contábil Alfa, para fechar o ciclo.

Prioridade: Should · Requisitos: RF-021

- Dada decisão de Q-038, quando aplicada, então o destino do cadastro fica automatizado ou orientado.
- Dada ausência de decisão, quando o aprendiz chega à etapa, então fica pendente com responsável.

## EP-009 — Plataforma e conformidade [proposto]

Permissões, auditoria, LGPD, monitoramento, indicadores e qualidade.

Prioridade: Must

### FT-017 — Permissões e proteção de dados [proposto]

Papéis, unidade e sigilo.

Prioridade: Must

#### US-039 — Aplicar permissões por papel e unidade [proposto]

Como Encarregada de Dados, quero aplicar a matriz de acesso, para limitar dados por necessidade.

Prioridade: Must · Requisitos: RNF-002, RN-014, RNF-001

- Dado gerente de uma loja, quando busca outra, então é negado.
- Dado usuário fora do SESMT, quando busca CID, então é negado e registrado.

#### US-040 — Proteger dados em trânsito e repouso [proposto]

Como Encarregada de Dados, quero ter dados criptografados, para reduzir vazamento.

Prioridade: Must · Requisitos: RNF-011

- Dada conexão sem TLS, quando tentada, então é recusada.
- Dado documento armazenado, quando inspecionado, então está criptografado.

#### US-041 — Evitar campo livre de saúde e dado vedado [proposto]

Como Encarregada de Dados, quero não ter campos com gravidez, antecedentes ou saúde, para evitar uso indevido.

Prioridade: Must · Requisitos: RN-012, RN-007

- Dado formulário de admissão, quando revisado, então não há campo para gravidez nem antecedentes.
- Dado campo de observação, quando existe, então há aviso e revisão definidos em Q-041.

### FT-018 — Trilha de auditoria [proposto]

Registro de decisões e acessos.

Prioridade: Must

#### US-042 — Registrar trilha de auditoria [proposto]

Como Advogada do Jurídico Trabalhista, quero consultar quem decidiu o quê, para comprovar conformidade.

Prioridade: Must · Requisitos: RNF-004

- Dada mudança no início, quando salva, então a trilha guarda autor, data, antes e depois.
- Dado usuário comum, quando tenta alterar a trilha, então é negado.

### FT-019 — Retenção e eliminação [proposto]

Regra de 6 meses.

Prioridade: Must

#### US-043 — Eliminar não contratados em 6 meses [proposto]

Como Encarregada de Dados, quero automatizar a eliminação, para cumprir RN-006.

Prioridade: Must · Requisitos: RF-017, RN-006, RNF-010

- Dado encerramento em 10/01/2027, quando chega 10/07/2027, então os dados foram eliminados.
- Dada falha na rotina, quando termina, então há alerta.

### FT-020 — Monitoramento e falha de integração [proposto]

Fila, alertas e reprocessamento.

Prioridade: Must

#### US-044 — Monitorar e reprocessar integrações [proposto]

Como responsável de TI, quero ver falhas e reprocessar, para não perder dado.

Prioridade: Must · Requisitos: RF-020, RNF-007

- Dada falha, quando ocorre, então há alerta em até 15 min.
- Dada integração restabelecida, quando processada a fila, então nenhuma mensagem se perde.

### FT-021 — Indicadores [proposto]

Funil e medição.

Prioridade: Must

#### US-045 — Ver funil de admissão [proposto]

Como Diretora de Gente & Gestão, quero ver aceites, admissões concluídas e inícios, para ter um número oficial.

Prioridade: Must · Requisitos: RF-010, RN-015

- Dado contrato assinado, ASO apto validado e ATIVO, quando calculado, então conta como concluída.
- Dada oferta aceita sem ATIVO, quando calculado, então conta só como aceite.

#### US-046 — Medir retrabalho e tempos [proposto]

Como Diretora de Gente & Gestão, quero medir a linha de base, para definir metas.

Prioridade: Should · Requisitos: RF-025

- Dado um mês fechado, quando gerado, então mostra devoluções, tempo e acesso no primeiro dia.
- Dada a falta de meta aprovada, quando gerado, então não exibe semáforo.

### FT-022 — Qualidade de serviço [proposto]

Capacidade, disponibilidade, usabilidade e parâmetros.

Prioridade: Must

#### US-047 — Suportar o pico de 320 admissões [proposto]

Como responsável de TI, quero validar a capacidade no pico, para evitar parada em novembro e dezembro.

Prioridade: Must · Requisitos: RNF-005

- Dada carga de 320 admissões por mês, quando testada, então o painel responde em até 3 s no p95.
- Dado o teste de pico, quando termina, então não há perda de registro.

#### US-048 — Medir disponibilidade [proposto]

Como responsável de TI, quero medir a disponibilidade, para garantir a operação.

Prioridade: Should · Requisitos: RNF-006

- Dado um mês, quando medido, então a disponibilidade é de ao menos 99,5%.
- Dada queda, quando ocorre, então há alerta em até 5 min.

#### US-049 — Parametrizar regras com vigência [proposto]

Como responsável de TI, quero alterar regra sem nova versão, para acompanhar revisões da RH-012.

Prioridade: Should · Requisitos: RNF-009

- Dada revisão aprovada, quando alterada, então vale desde a vigência.
- Dada admissão anterior, quando consultada, então mantém a regra aplicável.
