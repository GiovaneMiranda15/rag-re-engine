# Perguntas aos stakeholders

As perguntas foram priorizadas e terão resposta única. Cada uma traz a evidência do diagnóstico (`01-diagnostico.md`) e a suposição que será adotada se ficar sem resposta. As áreas são citadas por função.

## Direção do projeto

**1. Para: Diretora Geral e TI (a indicar).** O que significa "sistema único" na prática? Na categoria de manutenção de equipamentos, o novo sistema substitui o ERP SupriMax e a planilha? O ManutClin continua como dono de OS e inventário, com integração? Há decisão ou restrição entre comprar e desenvolver, e quem responde tecnicamente pelo projeto, já que a TI não aparece em nenhuma fonte?
*Suposição:* substitui a planilha e o ERP só em `MANUT_EQUIP`; o ManutClin permanece e é integrado; nada é decidido sobre comprar ou desenvolver.

**2. Para: Diretora Geral.** Se nem tudo couber até 30/06/2027, o que é inegociável na primeira fase e o que pode ficar para depois? Entram as quatro unidades de uma vez? Como medir o sucesso? Contratos de usina de oxigênio e gases ficam dentro do escopo, ou contam como predial?
*Suposição:* contrato, alçada, medição e pagamento têm prioridade sobre o TCO completo; quatro unidades; gases dentro do escopo; metas em cima dos indicadores atuais.

## Regras e alçadas

**3. Para: Diretor Financeiro e Gerente de Suprimentos.** A POL-SUP-004 rev. 3 vale integralmente, ou existe exceção formal para os limites que o ERP aplica (alçada de R$ 80 mil em vez de R$ 50 mil, três cotações a partir de R$ 25 mil em vez de R$ 15 mil, alçada de contrato sobre valor mensal em vez de global)? Os contratos anteriores à rev. 3 precisam ser reavaliados ou ficam como estão até o aditivo ou renovação?
*Suposição:* a política prevalece, sem exceções; os limites do ERP são defasagem; os contratos anteriores só são reavaliados em aditivo ou renovação.

**4. Para: Jurídico.** O parecer é exigido na prática acima de R$ 30 mil (POL 4.5) ou R$ 100 mil (fluxo de jun/2025)? Ele também se aplica a aditivo e renovação? Dos 23 dias em média na fila do parecer, o que os causa, e que tipos de contrato poderiam usar minuta padrão? Quantos pareceres o Jurídico conseguiria absorver a mais com o limite menor?
*Suposição:* R$ 30 mil, inclusive aditivos e renovações, com possibilidade de minuta padrão.

**5. Para: Jurídico, Engenharia Clínica e Suprimentos.** A renovação começa em 120, 90 ou 60 dias, e quem é o dono de cada etapa? Na transição, como tratar os contratos que vencem antes de 30/06/2027 (só o CT-2025-0031 não vence), e qual é a periodicidade do reajuste?
*Suposição:* 120 dias, com a área gestora e o Jurídico como donos (POL 4.2); renovações em andamento continuam no processo atual e são cadastradas na carga; reajuste anual, a confirmar contrato a contrato.

**6. Para: Jurídico.** Os contratos e aditivos originais podem ser disponibilizados? Eles decidem as divergências: CT-2024-0117 (SLA de 4 h ou 8 h; R$ 126.000,00 ou R$ 132.480,00/ano), CT-2025-0064 (IPCA ou IGP-M) e CT-2023-0088 (aditivo de 20/05/2026: valor, nova data de fim, houve parecer?). Quem será o dono do cadastro de contratos no novo sistema?
*Suposição:* o documento assinado prevalece; até vê-lo, usa-se o ERP para datas e valores, o ManutClin para SLA e a política para índice; Jurídico é dono do cadastro.

**7. Para: Jurídico e Diretor Financeiro.** Quando um contrato passa da data de fim sem aditivo (caso do CT-2022-0055, vencido desde 31/08/2025 e ainda pago), o sistema deve bloquear OS, medição e pagamento? Que exceção vale para serviço crítico, quem a autoriza e como ela é formalizada?
*Suposição:* bloqueia o pagamento, com liberação excepcional justificada do Diretor Financeiro e Jurídico, sem interromper o atendimento.

**8. Para: Gerente de Suprimentos e Jurídico.** Por que o CT-2026-0021 não está no ERP e é pago por OC avulsa de R$ 4.900,00/mês? Existem outros contratos nessa situação? O que é, afinal, uma OC "AVULSA", e ela continua existindo?
*Suposição:* é falha de registro; os R$ 4.900,00 são o pagamento do contrato; OC avulsa continua só para serviço sem contrato e sem recorrência.

**9. Para: Gerente de Suprimentos e Diretor Financeiro.** Quando o aprovador da alçada é também o solicitante (OC-2026-00420), ou está ausente, quem aprova? Quem deve constar como solicitante: a área que precisa ou o analista que digita? Como o sistema deve reconhecer "mesma necessidade" para detectar fracionamento (fornecedor, requisição, período?) e bloquear ou só alertar?
*Suposição:* sobe ao nível acima; solicitante é a área demandante; fracionamento = mesmo fornecedor e objeto em 30 dias ou mesma requisição, com alerta e reavaliação pela alçada da soma.

## Financeiro e custo

**10. Para: Diretor Financeiro.** Em qual sistema o título é pago e baixado, e como a nota entra hoje? Qual o motivo das cerca de 140 alterações manuais de vencimento por mês: o limite de 30 dias do ERP ante os 45 da política, ou outra causa? O pagamento fica no novo sistema ou ele apenas libera para o sistema financeiro?
*Suposição:* o sistema financeiro é separado e continua; o novo sistema entrega o título liberado, com vencimento calculado pela política.

**11. Para: Engenharia Clínica, Financeiro e Jurídico.** Como funcionam medição e glosa? O que as analistas conferem hoje, item a item? O relógio do SLA para em AGUARDANDO_COMPRA ou quando a peça não é coberta? O prazo é em horas corridas? O que é um "evento" (2% por OS ou por mês)? Quem decide a glosa, e por que ela foi zero em 2025?
*Suposição:* horas corridas; relógio suspenso só com peça comprovadamente não coberta; 2% por OS em violação; sistema sugere, Engenharia Clínica decide no ateste.

**12. Para: Diretora Geral e Diretor Financeiro.** Como compor o "custo por equipamento": como ratear o valor do contrato entre os equipamentos cobertos (inclusive calibração, sem lista de itens), a equipe própria entra, e quantos anos de histórico são necessários? Em contrato em dólar, a visão consolidada usa o câmbio de referência ou o valor efetivamente pago em reais?
*Suposição:* rateio igual entre itens cobertos; soma de contrato, chamados e peças, sem equipe própria (como pediu a Diretora Geral); dados a partir da entrada em operação; as duas visões em dólar, com a paga como oficial.

## Engenharia Clínica e segurança

**13. Para: Engenharia Clínica.** Qual a classificação oficial de criticidade e como A/B/C e Crítico/Não crítico correspondem aos quatro níveis da POL 6.2? Ela é por equipamento, e o contrato a herda? Por que o tomógrafo é B/Não crítico? Qual é a periodicidade correta para ventiladores (contrato semestral ou plano de 365 dias), e faltam planos para desfibriladores na Central e na Litoral?
*Suposição:* adotam-se os quatro níveis da política por equipamento, com mapeamento feito pela Engenharia Clínica; prevalece o intervalo mais curto.

**14. Para: Diretor Técnico e Engenharia Clínica.** Na primeira fase, o sistema deve impedir o fechamento de OS e a volta ao uso sem teste aprovado, liberação e calibração válida, ou só alertar? Há exceção para situação assistencial extrema, e quem autoriza? Quem cuida do evento adverso (Qualidade, Risco) e o que aconteceu com o caso da OS 88213 e sua calibração?
*Suposição:* bloqueio com exceção registrada do Diretor Técnico; o tratamento do evento adverso fica fora do sistema, que só registra o indicador e aciona o responsável, a identificar.

**15. Para: TI e responsável por privacidade/DPO (a indicar).** Por que nome e prontuário de paciente estão na OS, com leitura pela conta `prestador_portal`? Os prestadores usam esse portal, um a um ou com conta compartilhada? O acesso já foi auditado, e o novo sistema deve oferecer portal ao fornecedor? Quais exigências de retenção, auditoria e acesso devem ser seguidas?
*Suposição:* nada de dado de paciente no novo sistema; acesso externo individual e restrito aos próprios contratos, sem editar evidência de SLA; trilha de auditoria completa.
