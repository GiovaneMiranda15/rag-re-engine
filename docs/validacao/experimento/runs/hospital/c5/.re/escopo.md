# Escopo reformulado

Reformulação de `escopo.md`, ainda não confirmada (execução sem interlocutor; ver Q-001 e Q-002).

## Objetivo
Criar sistema único para comprar, contratar, acompanhar e pagar serviços de manutenção de equipamentos nas quatro unidades da Rede e, a partir de janeiro de 2027, no Hospital Aurora Serra (M-01, item 1), com visão consolidada por contrato, fornecedor, equipamento e unidade.

## Problema
A contratação passa por ERP de compras, sistema de OS e planilha de contratos, sem integração e com regras diferentes da política.

## Atores e áreas
Patrocinadora: Diretora Geral. Áreas que puxam o projeto: Suprimentos, Engenharia Clínica, Jurídico e Financeiro. Outros atores nas fontes: Diretor Técnico, Controladoria, Comitê de Contratos e prestadores.

## Dentro do escopo
Requisição, cotação, aprovação, contrato, aditivo, renovação, medição e pagamento; relação com OS e inventário da Engenharia Clínica; visão consolidada.

## Fora do escopo
Medicamentos, OPME, obras prediais e prontuário eletrônico.

Pedido recebido e não aceito: controle de validade de lotes de medicamentos no estoque, da Farmácia (M-01, item 3).

## Premissas (hipóteses)
- Planilha substituída; ManutClin mantido e integrado; ERP mantido nas demais categorias (Q-001).
- Pontos de apoio reaproveitados: APO-001, APO-002, APO-005, APO-006.
- Fonte das regras: POL-SUP-004 rev. 3 e Portaria DG-017/2025 (Q-003).

## Restrições
Fase 1 em operação até 30/06/2027. Orçamento e equipe: a definir.

## Glossário

| Termo | Definição | Fonte |
|---|---|---|
| OS | Ordem de serviço do ManutClin | `manutclin_dump.sql`, `ordem_servico` |
| OC | Ordem de compra: REGULAR, EMERGENCIAL ou AVULSA | `erp_suprimax_dump.sql`, `ordem_compra` |
| Medição | Valor mensal de contrato sujeito a ateste, glosa e pagamento | `erp_suprimax_dump.sql`, `medicao` |
| Ateste | Confirmação da Engenharia Clínica para pagar a medição | POL-SUP-004 §5.2 |
| Glosa | Desconto de 2% do valor mensal por evento de descumprimento de SLA | POL-SUP-004 §5.3 |
| SLA de atendimento | Horas até o início do atendimento | `regras_da_planilha.md`, Colunas |
| SLA de solução | Horas para resolver (`sla_solucao_h`) | `manutclin_dump.sql`, `contrato_ref` |
| Valor global | Valor durante toda a vigência do contrato | POL-SUP-004 §2.2 |
| Compra emergencial | Compra para evitar interrupção imediata da assistência por parada de equipamento | Portaria DG-017/2025, art. 1º |
| Patrimônio / tag | Etiqueta do equipamento, como chave entre ERP e ManutClin | `contrato_item`, `equipamento` |
