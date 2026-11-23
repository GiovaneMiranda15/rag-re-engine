# Oráculo do stakeholder simulado

Uso: responder às perguntas com estes fatos, na voz da área indicada, sem antecipar o que não foi perguntado.
Se a pergunta não estiver coberta, responda que a área não tem essa informação à mão.

## Quem decide

| Assunto | Decisor |
|---|---|
| Escopo e prioridade do projeto; conflito entre áreas | Renata Gaspar, Diretora Geral e patrocinadora |
| Processo de compras e cotações | Cláudia Freitas, Gerente de Suprimentos |
| Criticidade, liberação de equipamento, ateste e preventiva | Beatriz Tavares, Gerente de Engenharia Clínica |
| Texto de contrato, aditivo e parecer | Marta Quintela, Jurídico |
| Pagamento, câmbio de referência e orçamento | Luís Mota, Diretor Financeiro |
| Compra emergencial | Dr. Hélio Sampaio, Diretor Técnico |

Ordem de precedência: contrato assinado (para o que é daquele contrato) > Política POL-SUP-004 rev. 3 e Portaria DG-017/2025 > fluxo de 2025 > regras da planilha > configuração de sistemas. O Manual v2 tem valor apenas histórico nos capítulos revogados.

## Qual regra vale, por tema

- **Alçada de ordem de compra:** vale a Política (R$ 50 mil e R$ 250 mil). A configuração do ERP é antiga e ninguém a revisou após a rev. 3.
- **Alçada de contrato:** vale o valor global da vigência, como na Política, em qualquer contrato assinado desde 01/01/2025.
- **Cotações:** vale a Política (três acima de R$ 15 mil; duas de R$ 5 mil a R$ 15 mil).
- **Parecer jurídico:** vale a Política (acima de R$ 30 mil de valor global).
- **Início da renovação:** vale a Política (120 dias). O fluxo e a planilha terão de se adequar.
- **Prazo de pagamento:** vale a Política (padrão de 45 dias, mínimo de 30), salvo emergencial.
- **Índice de reajuste do CT-2025-0064:** vale IPCA, como no contrato assinado.
- **Vigência do CT-2023-0088:** vale 31/12/2026. O aditivo 2 foi assinado em 20/05/2026 e Suprimentos o lançou no ERP, mas não avisou o Jurídico.
- **Valor do CT-2024-0117:** vale R$ 11.040,00 por mês, após o reajuste de 01/05/2026 registrado no ERP.
- **SLA de atendimento do CT-2024-0117:** valem 4 horas, como no contrato assinado.
- **Preventiva de ventiladores do CT-2023-0019:** vale semestral, como no contrato assinado.
- **Criticidade:** valem os quatro níveis da Política. Enquanto o sistema novo não chega, a Engenharia Clínica usa no ManutClin: A para nível 1, B para níveis 2 e 3, C para nível 4. Monitor multiparamétrico é nível 2, portanto não é suporte à vida.
- **Liberação após reparo:** vale o fluxo. Teste e assinatura são obrigatórios.
- **CT-2022-0055:** venceu em 31/08/2025 sem aditivo. Os serviços continuam e a minuta segue em discussão.
- **CT-2025-0064 (NorteGás):** a renovação ainda não começou. Na prática, o Jurídico só a inicia quando a planilha muda para "A renovar".
- **CT-2026-0021 (Hemofix):** foi assinado localmente pela unidade Litoral e nunca registrado como contrato no ERP. É pago por ordens avulsas mensais de R$ 4.900,00.

## Esclarecimentos

- O gasto de 2025 foi de R$ 3,03 milhões no total, dos quais R$ 1,55 milhão em contratos continuados.
- Há 4.812 equipamentos no inventário, dos quais 393 sob contrato.
- BioVolt é o nome fantasia da MTS Engenharia Biomédica Ltda.
- Filial 01, CEN e Central são a mesma unidade; 02, NOR e Norte; 03, LIT e Litoral; 04, SUL e CDI Aurora Sul.
- O contrato da Helvion tem 6 horas para início do atendimento e 48 horas para solução. É cobrado em dólar, com câmbio de referência de R$ 5,40.
- A OC-2026-00412 foi uma compra emergencial regular.

## Volumes

- Cerca de 640 OS por mês e 1.460 ordens de compra de manutenção por ano.
- Cerca de 140 títulos de manutenção por mês.
- Oito contratos de manutenção de equipamentos ativos ou em renovação.
- Cerca de 60 usuários previstos: 25 em Suprimentos, 20 na Engenharia Clínica, 5 no Jurídico e 10 no Financeiro.
- Quatro unidades hoje. O Hospital Aurora Serra entra em janeiro de 2027, confirmado pela patrocinadora.

## Prioridades da primeira fase

1. Cadastro único de contratos, com vigência, valor, SLA e alertas de renovação.
2. Aprovações conforme a Política, com trilha de auditoria.
3. Ligação entre OS, requisição e medição, com ateste no sistema.
4. Cálculo de glosa por SLA.
5. Custo por equipamento: desejável, pode ficar para a segunda fase.

Portal do prestador fica fora da primeira fase. Controle de lotes de medicamentos está fora do projeto.

## Mudanças posteriores

- A redução do parecer jurídico para R$ 200 mil foi uma proposta do Jurídico e ainda não foi aprovada pela Diretoria. Até lá, vale a Política.
- O limite de 10% das glosas por competência foi aceito pelo Financeiro e pela Engenharia Clínica.

## Assuntos sem resposta

- **Como e por quem são feitas as notificações de eventos adversos ao Notivisa:** "Não sei, pergunte à Dra. Ana Prado, da Gerência de Qualidade e Segurança do Paciente."
- **Base legal, prazo de retenção e acesso a dados de pacientes em ordens de serviço:** "Não sei, pergunte ao Gustavo Leme, encarregado de dados (DPO)."
- **APIs disponíveis no SupriMax e no ManutClin, e custo de integração:** "Não sei, pergunte ao Rafael Couto, coordenador de TI."
