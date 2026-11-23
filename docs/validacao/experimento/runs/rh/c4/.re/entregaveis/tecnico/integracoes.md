# Integrações

Todas as linhas abaixo são **proposta [hipótese]**, porque Igor Melo não soube informar (Q-014). Os únicos fatos das fontes são: EducaFarma tem API REST; MedTrab oferece API de agendamento; e a FolhaCerta valida piso e gera eventos.

| Integração | Direção | Meio | Frequência e volume | Contrato ou dados | Falha | Monitoramento | Responsável |
|---|---|---|---|---|---|---|---|
| Recruta+ → sistema | Entrada | API ou arquivo, a confirmar | Por oferta; até 320 admissões por mês | Candidato sem campos vedados, oferta, vaga | Fila; alerta ao BP | RNF-007 | A definir, Q-035 |
| FolhaCerta → sistema | Entrada | A confirmar | Diário para piso; por mudança para status | Piso, contrato, evento, recibo | Reprocessar; usar último piso com aviso | RNF-007 | Igor, Rogério |
| Sistema → FolhaCerta | Saída | A confirmar | Por admissão | Colaborador e contrato | Fila; sem perda; retido se inválido | RNF-007 | Igor, Rogério |
| Comprovante de vacinação | Entrada no SESMT | Upload no ambiente do SESMT | Só SP, por admissão | Tipo e conferência | Critério pendente | RNF-007 | Fábio |
| MedTrab ↔ SESMT | Ambos | API, se o contrato permitir (Q-026) | Por exame; pico equivalente a 320 por mês | Agendamento; retorno a definir | Fila manual no SESMT | RNF-007 | Fábio |
| SESMT → sistema | Entrada | Interna | Por mudança | Situação, conforme Q-040 | Critério pendente | RNF-007 | Fábio, Paula |
| Sistema ↔ EducaFarma | Ambos | API REST | Por início e diário | Matrícula, conclusão, prazo | Alerta e matrícula manual | RNF-007 | Beatriz, TI |
| Sistema → chamados e PDV | Saída | A confirmar | Por início | Pedido de acesso | Alerta ao gerente e à TI | RNF-007 | Igor |
| Contábil Alfa | A decidir | Hoje, lote quinzenal | Cerca de 40 por ano | A definir, Q-038 | A definir | A definir | Rogério |
| eSocial | Via FolhaCerta | Não integra diretamente | Por evento | Evento e recibo | Conforme Q-009 | Painel do DP | Rogério |

## Ajustes nos legados (RF-024)

| Sistema | Hoje | Necessário |
|---|---|---|
| FolhaCerta | ASO 90 dias, sem limite superior | 30 dias e não posterior ao início |
| FolhaCerta | Default 45 dias | 30, com prorrogação até 90, salvo decisão de CR-001 |
| FolhaCerta e Recruta+ | CPF obrigatório, sem CRNM | Tratamento em Q-053 |
| Recruta+ | Vaga sem marca de injetáveis | Marca no novo sistema ou no Recruta+ |
| FolhaCerta | CRF só FARM, número | Toda função farmacêutica; certidão no novo sistema |
| FolhaCerta | CID e acesso de rh_loja | Sem CID; revisar acesso |
| FolhaCerta | Mínimo de 18 e sem tipo aprendiz | Decisão em Q-038 |
| FolhaCerta | Evento não recalcula quando a data muda | Verificar em Q-009 |
| Recruta+ | Tabela sem CCT 2026 em SP; sem BP; 24 meses; campos vedados; backup | Alinhar ou deixar de usar; eliminar |
| EducaFarma | Integração em 30 dias; sem trilha de aprendiz e RT | 5 dias; trilhas em Q-046 |
| Planilha | Link aberto; regras 2, 3 e 4 | Restringir; revisar; aposentar |
| Manual 3.2 | Valores vencidos | Nova versão ou retirada |

Para FolhaCerta e Recruta+, a viabilidade de alteração não é conhecida (Q-014).
