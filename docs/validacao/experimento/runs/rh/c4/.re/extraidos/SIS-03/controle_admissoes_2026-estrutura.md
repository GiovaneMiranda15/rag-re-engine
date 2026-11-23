# Transcrição de estrutura: fontes/SIS-03-controle-lojas/controle_admissoes_2026.csv
Somente cabeçalhos, tipos e agregados. Nenhuma linha de dado pessoal foi copiada. Amostra: 10 linhas.

## Colunas
id (inteiro), cpf (texto livre; 8 linhas com máscara e 2 sem), nome, cargo (texto livre), tipo_contrato (CLT, APRENDIZ),
loja ("código - nome"), regional, gerente, dt_aprov_oferta, dt_solic_aso, dt_aso (dd/mm/aaaa), resultado_aso (APTO),
dt_inicio, experiencia (45+45 ou -), jornada_sem (44 ou 30), carencia_plano_dias (90 ou 30),
situacao (Em ASO, Liberado, Iniciado), responsavel_dp, obs (texto livre).

## Agregados da amostra
- Intervalo entre aprovação da oferta e solicitação do ASO: 1 a 2 dias.
- Intervalo entre solicitação e emissão do ASO: 5 a 8 dias, mediana 7 (9 linhas com as duas datas).
- Intervalo entre emissão do ASO e início: 11, 12, 12, 12, 13, 13, 45 e 63 dias, e um caso de -3 dias (início antes do exame).
- Intervalo entre aprovação da oferta e início: mediana 21 dias, mínimo 7, máximo 70.
- Toda linha CLT usa experiência 45+45.
- O campo obs tem conteúdo em 6 das 10 linhas; 2 linhas contêm informação de saúde ou gestação; 1 linha informa CRF em protocolo; 1 linha informa idade de menor de 18 anos.
- CPF: 1 linha difere em 2 dígitos do CPF da mesma pessoa na FolhaCerta; a planilha coincide com o Recruta+ nesse caso.
