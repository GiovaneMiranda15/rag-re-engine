# Transcrição de estrutura: fontes/SIS-04-treinamento/export_trilhas_lms.csv e export_matriculas_lms.csv
Somente cabeçalhos e agregados. Nenhuma linha de dado pessoal foi copiada.

## Trilhas (catálogo, sem dado pessoal)
Colunas: trilha_id, cargo, curso, carga_h, prazo_dias_apos_inicio, obrigatorio.
Cargos: BALCONISTA, FARMACEUTICO, CAIXA. Não há trilha de aprendiz nem de farmacêutico responsável técnico.
Curso "Integração e Boas Práticas Farmacêuticas": 8 h, obrigatório, prazo de 30 dias após o início para todos os cargos.
Outros obrigatórios: Atendimento e venda com receita (BALCONISTA, 45 dias), LGPD no balcão (BALCONISTA e FARMACEUTICO, 60 dias),
SNGPC e medicamentos controlados (FARMACEUTICO, 30 dias), Operação de PDV (CAIXA, 15 dias).

## Matrículas
Colunas: email_usuario, nome, unidade_lms, trilha_id, dt_matricula, dt_conclusao, status (CONCLUIDO, EM_ANDAMENTO).
Não há CPF nem matrícula da folha. A unidade usa código próprio (UF-sigla).
Agregados: 7 matrículas, todas no curso de Integração. Matrícula de 1 a 6 dias após o início.
4 concluídas, em 15, 17, 23 e 24 dias após o início. 3 em andamento, com pelo menos 8 dias desde o início na data mais recente do arquivo.
