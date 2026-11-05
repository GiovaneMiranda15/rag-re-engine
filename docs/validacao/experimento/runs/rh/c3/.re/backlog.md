# Backlog

## EP-001 — Fluxo único de admissão de CLT de loja [proposto]

Prioridade 1 da patrocinadora: fluxo único de balconista, caixa e farmacêutico, com bloqueio de início.

Prioridade: Must

### FT-001 — Visão única da admissão [proposto]

Situação de cada etapa em um só lugar.

Prioridade: Must · Requisitos: RF-001

#### US-001 — Ver a situação da admissão em um só lugar [proposto]

Como gerente de loja, quero ver todas as etapas de uma admissão, para não procurar em vários canais.

Prioridade: Must · Requisitos: RF-001, RNF-002

- Dado admissão de minha loja, quando abro o painel, então vejo oferta, documentos, exame, contrato, eSocial, acessos e treinamentos.
- Dado admissão de outra loja, quando tento abri-la, então o acesso é negado.

#### US-002 — Saber se o colaborador pode começar [revisar]

Como gerente de loja, quero saber se o colaborador pode começar, para planejar a escala com segurança.

Prioridade: Must · Requisitos: RF-001, RF-012, RN-016

- Dado ASO válido e, se exigido, CRF ativo, quando consulto, então essas condições aparecem atendidas.
- Dada condição não atendida, quando consulto, então vejo qual falta e a situação aparece como não liberada.
- Dado admitido sujeito à RN-016 sem comprovante de vacinação, quando consulto, então a condição aparece como não atendida, sem mostrar o conteúdo do comprovante.

#### US-003 — Acompanhar a oferta [proposto]

Como gerente de loja, quero ver a situação da oferta, para saber quando o processo começou.

Prioridade: Must · Requisitos: RF-011

- Dada oferta aceita no Recruta+, quando consulto, então a admissão aparece como oferta aceita.

#### US-004 — Acompanhar o contrato [proposto]

Como analista do DP, quero ver a situação do contrato, para saber o que falta para efetivar a admissão.

Prioridade: Must · Requisitos: RF-013

- Dado contrato PRE ou ATIVO na FolhaCerta, quando consulto, então vejo essa situação.

#### US-005 — Acompanhar S-2190 e S-2200 [proposto]

Como analista do DP, quero ver prazo e situação dos eventos, para agir antes do vencimento.

Prioridade: Must · Requisitos: RF-005

- Dado evento sem envio, quando consulto, então vejo prazo e situação pendente.
- Dado evento enviado, quando consulto, então vejo a data de envio.

#### US-006 — Acompanhar a solicitação de acesso [proposto]

Como gerente de loja, quero ver se o acesso do novo colaborador foi solicitado e concluído, para preparar o primeiro dia.

Prioridade: Must · Requisitos: RF-006

- Dado colaborador com início marcado, quando consulto, então vejo a situação do acesso.

#### US-007 — Contar as etapas sem misturar conceitos [proposto]

Como gestora de Gente & Gestão, quero ver oferta aceita, admissão efetivada e primeiro dia separados, para entender onde as admissões param.

Prioridade: Should · Requisitos: RF-008, RN-015

- Dada oferta aceita sem contrato ATIVO, quando conto admissões, então ela não entra na conta.
- Dado contrato ATIVO sem primeiro dia, quando conto iniciados, então ele não entra na conta.

### FT-002 — Bloqueio de início [proposto]

Sem ASO válido e sem CRF ativo, não há liberação.

Prioridade: Must · Requisitos: RF-012

#### US-008 — Bloquear início sem ASO válido [proposto]

Como Jurídico, quero que ninguém seja liberado sem ASO válido, para cumprir a RH-012 sem exceção.

Prioridade: Must · Requisitos: RF-012, RN-002

- Dado ASO apto emitido 30 dias corridos antes do início, quando se tenta liberar, então a condição é atendida.
- Dado ASO apto emitido 31 dias corridos antes do início, quando se tenta liberar, então a liberação é recusada.
- Dado ASO emitido depois da data de início, quando se tenta liberar, então a liberação é recusada.
- Dada loja desfalcada, quando se pede exceção, então o sistema não oferece forma de liberar.

#### US-009 — Revalidar o ASO quando o início é adiado [proposto]

Como gerente de loja, quero ser avisado quando o adiamento invalida o ASO, para pedir novo exame a tempo.

Prioridade: Must · Requisitos: RN-002

- Dado ASO válido, quando a data de início passa a mais de 30 dias corridos da emissão, então o ASO deixa de valer e a admissão volta a não liberada.

#### US-010 — Bloquear farmacêutico sem CRF ativo [proposto]

Como responsável pela regra de CRF, quero impedir o início sem CRF ativo, para que nenhuma função farmacêutica comece irregular.

Prioridade: Must · Requisitos: RF-012, RN-003

- Dado farmacêutico ou RT com certidão e CRF ativo, quando se verifica, então a condição é atendida.
- Dado farmacêutico ou RT só com protocolo, quando se tenta liberar, então a liberação é recusada.
- Dado balconista ou caixa, quando se verifica, então a condição de CRF não se aplica.

#### US-011 — Apontar contrato ativo sem condição atendida [proposto]

Como Jurídico, quero ver contratos ATIVO sem ASO válido ou CRF ativo, para agir se a folha for usada fora do fluxo.

Prioridade: Must · Requisitos: RF-012, RF-013

- Dado contrato ATIVO na FolhaCerta com condição não atendida, quando o sistema o identifica, então ele aparece como inconsistência para o DP e o Jurídico.

#### US-033 — Exigir vacinação de quem aplica injetáveis em SP [proposto]

Como Jurídico, quero exigir o comprovante de vacinação de quem vai aplicar injetáveis em SP, para cumprir a Portaria CVS-SP 88/2026.

Prioridade: Must · Requisitos: RN-016, RF-012, RN-002

- Dado admitido que vai aplicar injetáveis em loja de SP, com início em 01/02/2027 ou depois, sem comprovante de hepatite B e tétano, quando se tenta liberar, então a liberação é recusada.
- Dado o mesmo admitido com início em 31/01/2027, quando se tenta liberar, então a condição não se aplica.
- Dado admitido em loja de MG, ou em SP sem aplicar injetáveis, quando se tenta liberar, então a condição não se aplica.
- Dado o comprovante apresentado, quando consultado fora do SESMT, então só a situação aparece.
- Dado comprovante apresentado, quando se avalia o ASO, então a regra de 30 dias continua igual.

### FT-003 — Exame admissional [proposto]

Etapas do exame sem dado clínico.

Prioridade: Must · Requisitos: RF-004

#### US-012 — Registrar as etapas do exame [proposto]

Como analista do SESMT, quero registrar pedido, agendamento e emissão, para que todos vejam o andamento sem receber dado clínico.

Prioridade: Must · Requisitos: RF-004, RN-008

- Dado exame pedido, quando atualizo a etapa, então a data fica registrada.
- Dado perfil fora do SESMT, quando consulta o exame, então nenhum CID aparece.

### FT-004 — Treinamentos e experiência [proposto]

Prazos depois do início.

Prioridade: Must · Requisitos: RF-007, RF-009

#### US-013 — Controlar a integração até o 5º dia [proposto]

Como gerente de loja, quero ver o prazo da integração, para não deixar o colaborador sozinho no balcão antes da conclusão.

Prioridade: Must · Requisitos: RN-005, RF-007

- Dado início em D, quando consulto, então o prazo aparece como D+5, mesmo com outro prazo no EducaFarma.
- Dada integração não concluída, quando consulto, então o colaborador aparece como não apto a atender sozinho no balcão.

#### US-014 — Acompanhar os cursos obrigatórios do cargo [proposto]

Como gerente de loja, quero ver todos os cursos obrigatórios, para não perder prazo.

Prioridade: Must · Requisitos: RF-007

- Dado cargo com cursos obrigatórios, quando consulto, então cada curso aparece com prazo e situação.

#### US-015 — Acompanhar o fim da experiência [revisar]

Como analista do DP, quero ver as datas de 30 e 90 dias, para acompanhar até o fim do período.

Prioridade: Should · Requisitos: RN-001, RF-009, RN-017

- Dado contrato de experiência com início em D, quando consulto, então vejo as datas de fim do 1º período e do total.
- Dada não continuidade, quando consulto, então o sistema não oferece rescisão nem desligamento.

## EP-002 — Fim da redigitação [proposto]

Prioridade 2 da patrocinadora: entrega digital de documentos e integração Recruta+ para FolhaCerta.

Prioridade: Must

### FT-005 — Entrega digital de documentos [proposto]

Documentos em formato digital, com pendências e datas.

Prioridade: Must · Requisitos: RF-003

#### US-016 — Entregar documentos em formato digital [proposto]

Como candidato aprovado, quero entregar meus documentos em formato digital, para não depender de envio por e-mail.

Prioridade: Must · Requisitos: RF-003, RNF-002

- Dado candidato com oferta aceita, quando envia um documento, então a data de entrega fica registrada.
- Dado documento enviado, quando outro candidato tenta acessá-lo, então o acesso é negado.

#### US-017 — Conferir e devolver com motivo [proposto]

Como analista do DP, quero conferir cada documento e devolver com motivo, para reduzir idas e vindas.

Prioridade: Must · Requisitos: RF-003

- Dado documento ilegível, quando devolvo, então o motivo e a data ficam registrados e a pendência aparece ao gerente.

#### US-018 — Sinalizar o prazo de 5 dias úteis [proposto]

Como analista do DP, quero ver pastas incompletas perto do prazo, para agir antes do início.

Prioridade: Must · Requisitos: RN-010

- Dado início em D, quando a pasta está incompleta no 5º dia útil antes de D, então a pendência aparece ao gerente e ao DP.

#### US-034 — Aceitar a CRNM como identificação [proposto]

Como candidato do programa Acolher, quero usar a CRNM como documento de identificação, para seguir a admissão sem barreira de documento.

Prioridade: Should · Requisitos: RF-019, RF-003

- Dada admissão do programa Acolher, quando envio a CRNM, então ela é aceita como identificação.
- Dada a CRNM aceita, quando o DP confere, então a conferência segue como a de qualquer documento.

#### US-035 — Controlar a validade da CRNM [proposto]

Como analista do DP, quero registrar a validade da CRNM, para agir quando ela vencer.

Prioridade: Should · Requisitos: RF-020

- Dada CRNM com validade futura, quando registrada, então a data fica visível na admissão.
- Dada CRNM vencida, quando a admissão é consultada, então o vencimento aparece ao DP.

### FT-006 — Integração Recruta+ para FolhaCerta [proposto]

Dados da oferta na folha sem nova digitação; canal a verificar.

Prioridade: Must · Requisitos: RF-002

#### US-019 — Verificar os canais da FolhaCerta e do Recruta+ [proposto]

Como equipe do projeto, queremos conhecer API, importação e limites dos dois sistemas, para decidir como integrar.

Prioridade: Must · Requisitos: RF-002

- Dada a verificação concluída, quando apresentada, então registra canal, fornecedor, limites e possibilidade de alterar as regras da folha.

#### US-020 — Levar os dados da oferta à FolhaCerta [revisar]

Como analista do DP, quero receber os dados da oferta na FolhaCerta, para não digitar de novo.

Prioridade: Must · Requisitos: RF-002, RN-001, RN-017

- Dada oferta aceita, quando os dados chegam à FolhaCerta, então nenhum campo já existente na oferta é redigitado.
- Dado contrato CLT de experiência criado pelo fluxo, quando chega à FolhaCerta, então usa 30 dias, não o padrão de 45.
- Dada falha no envio, quando ela ocorre, então a admissão mostra a falha ao DP.

#### US-021 — Fazer a correspondência de loja, cargo e pessoa [revisar]

Como equipe do projeto, queremos a tabela de correspondência de loja, cargo e chave de pessoa, para integrar sem erro.

Prioridade: Must · Requisitos: RF-002

- Dados dois colaboradores com mesmo nome e CPFs diferentes, quando há conciliação, então são tratados como pessoas distintas.
- Dado CPF com ou sem máscara, quando há conciliação, então ele identifica a mesma pessoa.
- Dado cargo farmacêutico no Recruta+, quando há conciliação, então a distinção entre FARM e FARM_RT não se perde.

#### US-022 — Sinalizar oferta abaixo do piso [proposto]

Como analista do DP, quero identificar oferta abaixo do piso antes de chegar ao candidato, para evitar refazer a oferta.

Prioridade: Must · Requisitos: RN-011

- Dada oferta abaixo do piso vigente da UF na FolhaCerta, quando é analisada, então é sinalizada.
- Dada a tabela do Recruta+ diferente da FolhaCerta, quando há comparação, então vale a FolhaCerta.

## EP-003 — Conformidade de dados pessoais [proposto]

Prioridade 3 da patrocinadora: saída da planilha e tratamento de dados de saúde e de seleção.

Prioridade: Must

### FT-007 — Saída da planilha [proposto]

CLT de loja deixa a planilha.

Prioridade: Must · Requisitos: RF-014

#### US-023 — Controlar admissão nova fora da planilha [proposto]

Como coordenadora de Operações de Loja, quero controlar admissões novas de CLT de loja no sistema, para encerrar o uso da planilha nelas.

Prioridade: Must · Requisitos: RF-014

- Dada admissão nova de CLT de loja, quando aberta, então não há linha na planilha.

#### US-024 — Migrar as admissões em andamento [proposto]

Como coordenadora de Operações de Loja, quero migrar as admissões abertas, para encerrar a planilha sem perder acompanhamento.

Prioridade: Must · Requisitos: RF-014, RNF-002

- Dada admissão de CLT de loja em andamento, quando migrada, então a situação é mantida.
- Dado o campo livre de observações, quando há migração, então seu conteúdo não é copiado automaticamente.

### FT-008 — Dados de saúde [proposto]

CID só no ambiente do SESMT.

Prioridade: Must · Requisitos: RN-008

#### US-025 — Retirar CID do que está fora do SESMT [proposto]

Como Encarregada de Dados, quero CID apenas no ambiente do SESMT, para cumprir a orientação sobre saúde.

Prioridade: Must · Requisitos: RN-008

- Dado o novo sistema fora do SESMT, quando auditado, então não há CID.
- Dada a FolhaCerta, quando auditada depois da correção, então não há CID.

#### US-026 — Aplicar a matriz de acesso [proposto]

Como Encarregada de Dados, quero que cada perfil veja só o necessário, para limitar a exposição.

Prioridade: Must · Requisitos: RNF-002

- Dado um perfil, quando acessa uma admissão, então vê apenas o que a matriz aprovada prevê.

### FT-009 — Dados de seleção e retenção [proposto]

Coleta e eliminação conforme a Encarregada.

Prioridade: Must · Requisitos: RN-012, RN-007

#### US-027 — Retirar gravidez e antecedentes da seleção [proposto]

Como Encarregada de Dados, quero que gravidez e antecedentes não sejam perguntados nem guardados, para eliminar esse tratamento.

Prioridade: Must · Requisitos: RN-012

- Dado qualquer campo de seleção, quando revisado, então não há gravidez nem antecedentes.
- Dados já existentes nesses campos, quando há ajuste, então seguem o tratamento definido pela Encarregada.

#### US-028 — Restringir dado de pessoa com deficiência [proposto]

Como Encarregada de Dados, quero esse dado só para cota e com acesso restrito, para limitar seu uso à finalidade.

Prioridade: Must · Requisitos: RN-013, RN-008

- Dado gerente sem autorização, quando consulta um candidato, então o dado não aparece.
- Dado de pessoa com deficiência, quando registrado, então não inclui CID fora do SESMT.

#### US-029 — Eliminar candidatos não contratados em 6 meses [proposto]

Como Encarregada de Dados, quero eliminar esses dados em até 6 meses, para cumprir a RH-012.

Prioridade: Must · Requisitos: RN-007

- Dado processo encerrado há mais de 6 meses, quando a rotina roda, então os dados do candidato não contratado são eliminados, qualquer que seja a causa da não contratação.
- Dado processo encerrado há 5 meses, quando a rotina roda, então os dados são mantidos.

#### US-030 — Eliminar dados em cópias e backups [proposto]

Como Encarregada de Dados, quero alcançar cópias e backups, como candidato_bkp_2022, para não restar dado fora do prazo.

Prioridade: Must · Requisitos: RN-007

- Dado candidato_bkp_2022, quando concluída a eliminação, então não há registro com mais de 6 meses de processo encerrado.
- Dada a rotina de expurgo do Recruta+, quando corrigida, então não usa mais 24 meses.

## EP-004 — Aprendizes no fluxo único [proposto]

Prioridade 5 da patrocinadora; vem depois de CLT de loja.

Prioridade: Should

### FT-010 — Admissão de aprendiz [proposto]

Programa de 14 a 24 anos dentro do novo processo.

Prioridade: Should · Requisitos: RN-006, RF-015

#### US-031 — Definir o caminho de registro do aprendiz [proposto]

Como equipe do projeto, queremos definir o registro do aprendiz, já que a FolhaCerta exige 18 anos e não tem esse tipo de contrato.

Prioridade: Should · Requisitos: RF-015

- Dada a definição concluída, quando apresentada, então registra papel da Contábil Alfa, responsável pelo eSocial e alterações necessárias.

#### US-032 — Conduzir o aprendiz pelo fluxo único [proposto]

Como analista do DP, quero acompanhar o aprendiz no mesmo fluxo, para trazer o programa para dentro do novo processo.

Prioridade: Should · Requisitos: RF-015, RN-006, RN-002

- Dado aprendiz de 16 anos, quando entra no fluxo, então a admissão é aceita.
- Dado candidato fora de 14 a 24 anos, quando entra como aprendiz, então a admissão é recusada.
- Dado aprendiz, quando consulto o bloqueio, então vale a mesma regra de ASO.
