# Planilha de Controle de Contratos de Manutenção: como usar

Rede Hospitalar Aurora do Vale (organização fictícia). Jurídico. Última atualização da planilha: 25/09/2026.

## Quem mexe

- Só a Marta Quintela (Jurídico) altera a planilha, normalmente às sextas-feiras.
- O arquivo fica na pasta de rede do Jurídico. As demais áreas pedem alteração por e-mail à Marta e recebem cópia em PDF.
- Não há histórico de versões. Quando a Marta está de férias, a planilha não é atualizada.

## Colunas

- `valor_anual_brl`: valor anual do contrato, em reais. Em contrato em moeda estrangeira, valor mensal × 12 × `cambio_ref`.
- `cambio_ref`: câmbio de referência definido pelo Financeiro na assinatura. Vazio para contrato em reais.
- `qtd_equip`: equipamentos cobertos. Contrato de calibração cobre instrumentos e fica com 0.
- `sla_atend_h`: horas até o início do atendimento, conforme contrato.
- `preventiva`: periodicidade prevista em contrato.
- `criticidade`: Crítico ou Não crítico, conforme informado pela Engenharia Clínica no pedido de contratação.
- `indice`: índice de reajuste previsto em contrato.

## Status

| Status | Quando usar |
|---|---|
| Vigente | Faltam mais de 60 dias para o fim |
| A renovar | Faltam 60 dias ou menos: a Marta envia e-mail de aviso à Engenharia Clínica e a Suprimentos |
| Em renovação | Minuta em discussão com o fornecedor |
| Vencido | Data de fim já passou e não houve aditivo informado ao Jurídico |
