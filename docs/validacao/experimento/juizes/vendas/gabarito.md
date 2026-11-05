# Gabarito — o que a skill deveria encontrar

> Não indexar. Use para avaliar o diagnóstico (cobertura) e a classificação das mudanças.

## Divergências (regra × sistema)

| ID | Tema | SIS-01 ERP | SIS-02 Comissões | SIS-03 Loja | Política / ata |
|---|---|---|---|---|---|
| D1 | Desconto máximo sem aprovação | 10% (trigger) | — | 15% (cupom) | 12%; 12–20% gerente; >20% diretoria |
| D2 | Comissão do vendedor interno | 3% do total bruto | 3% até a meta + 5% acima, sobre o líquido | — | definida pelo financeiro |
| D3 | Comissão do representante | 3% | 4% fixo | — | — |
| D4 | Desconto alto × comissão | não considera | >8% paga metade | — | — |
| D5 | Comissão de pedido web | sem vendedor, sem comissão | 1% ao dono da carteira | — | — |
| D6 | Tipo de cliente | só CNPJ | — | CPF ou CNPJ | PF profissional permitida desde 2025 |
| D7 | Prazo de análise de crédito | ~2 dias úteis (prática) | — | cartão não passa | 1 dia útil |
| D8 | Devolução | lançada como cancelamento | estorna no mês seguinte | — | — |

## Gargalos
- G1 Fila manual de crédito (consulta ao Serasa fora do sistema; sexta-feira só na terça).
- G2 Recadastro manual diário de clientes PF (~1h/dia).
- G3 Planilha de comissão: exportação, correção manual, aprovação por e-mail.
- G4 Integração por CSV noturno, com preço e estoque defasados no dia.
- G5 Ajuste manual de desconto de cupom recusado.

## Riscos
- R1 Venda sem estoque (baixa só no faturamento, loja com estoque de D-1): ~20 cancelamentos/mês.
- R2 Falha silenciosa da integração (sem alerta).
- R3 Servidor da loja sem backup testado.
- R4 LGPD: `aceita_marketing` vem marcado por padrão (DEFAULT 1), o que contraria o consentimento explícito.
- R5 Dependência do VendaMax para a NF-e: não pode ser desligado no ano.
- R6 Conflito de comissão gera reclamações (~15/mês) e desgaste com representantes.
- R7 Integração com 1 desenvolvedor terceirizado (dependência de pessoa).

## Pontos de apoio
- P1 Regras de crédito e de desconto já automatizadas por trigger no ERP (lógica reaproveitável).
- P2 Tabela de preço única já é política oficial.
- P3 ERD e status de pedido bem definidos no ERP.
- P4 Loja já atende PF e aceita pix e cartão.

## Oportunidades
- O1 Cadastro único de clientes PF/PJ.
- O2 Estoque reservado na digitação do pedido, em tempo real para todos os canais.
- O3 Motor de comissão configurável pelo financeiro (pedido da ata).
- O4 Alçada de desconto por faixa com fluxo de aprovação (e substituto em férias).
- O5 Crédito automático para bom pagador (prioridade 1 do diretor).
- O6 Integração com o ERP via API e observabilidade.

## Perguntas abertas esperadas
- Quem aprova desconto de 12–20% quando o gerente está de férias? (ata, pendente)
- App offline entra na v1? (ata, avaliar)
- Qual regra de comissão prevalece: a do ERP ou a da planilha? (resposta esperada: planilha/financeiro)

## Mudanças (modo manutenção)

| Mudança | Item | Classe esperada | Impacto esperado |
|---|---|---|---|
| M-01 | 1. comissão 5% → 6% | conflitante (altera RN de comissão) | RN de comissão, motor configurável, histórias de comissão, critérios de aceite |
| M-01 | 2. bônus para representantes | conflitante (a regra vigente é 4% fixo, sem bônus) | RN de comissão do representante (D3) |
| M-01 | 3. desconto sem aprovação 12% → 15% | conflitante | RN de alçada (D1/O4), cupons, critérios de aceite, validação |
| M-01 | 4. app offline na v1 | conflitante (reverte a decisão de deixá-lo fora da v1; 'novo' vale meio ponto) | escopo, RNF offline/sincronização, épico mobile, prazo (gestao-pmo) |
| M-02 | API com limite e sem webhook | complementar/restrição | integração ERP (O6), RNF de atualização de status, "tempo real" da ata |
