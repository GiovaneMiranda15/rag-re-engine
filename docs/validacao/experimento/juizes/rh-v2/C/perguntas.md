# Perguntas aos stakeholders

Projeto Admissão Única. São 15 perguntas para resposta única. Cada uma traz, entre parênteses, os achados do `01-diagnostico.md` que resolve.
Quando não houver resposta, o levantamento seguirá como hipótese o valor da RH-012, a norma mais recente aprovada por Gente & Gestão, Jurídico e Encarregada de Dados.

1. **Para: Helena Vasconcelos** (DIV-016)  
   O sistema cobre quais unidades e modalidades? Confirme para cada uma: 184 lojas próprias, CD, escritório central e 28 franqueadas; CLT, aprendiz e estágio. Hipótese: só as unidades regidas pela RH-012, sem franqueadas.

2. **Para: Helena Vasconcelos** (RIS-014)  
   Quais são as restrições e a governança do projeto: data-limite, teto de orçamento, critérios para decidir entre comprar ou construir, quem aprova requisitos e o que o comitê de 28/10/2026 decidiu? Não há registro dessa reunião nas fontes.

3. **Para: Helena Vasconcelos, com Rogério Tavares, Cláudia Reis e Recrutamento** (DIV-009)  
   Qual evento será o número oficial de admissão: aceite (214), ATIVO (188) ou primeiro dia (176)? Quais parcelas explicam a diferença em setembro (aprendizes, franqueadas, desistências, início em outro mês)? Em 3 meses de uso, quais metas devem mudar (redigitação, devoluções, oferta até início, acesso no primeiro dia)?

4. **Para: Marina Quintela e Fábio Arantes** (DIV-001)  
   A validade do ASO será a da RH-012 (até 30 dias corridos antes do início), em vez dos 60 da planilha e dos 90 da FolhaCerta? O que fazer com ASO vencido por adiamento, resultado inapto ou apto com restrição? A MedTrab pode usar API por contrato, e o que ela retornaria?

5. **Para: Marina Quintela e Rogério Tavares** (DIV-002, RIS-007)  
   A experiência será 30+60 (RH-012) ou 45+45 (manual, planilha, FolhaCerta)? Como tratar contratos em curso e os já firmados com 45 dias? Quem decide prorrogar ou encerrar, com quantos dias de antecedência, e onde a decisão fica registrada?

6. **Para: Marina Quintela** (DIV-003, RIS-005)  
   Confirma que nenhuma função farmacêutica, inclusive RT, pode iniciar só com protocolo, contrariando a regra 4 da planilha? Há exceção para evitar loja sem RT? Quem confere a certidão, com que validade, e o que fazer agora com quem já iniciou com protocolo?

7. **Para: Sérgio Antunes e Cláudia Reis, com Marina Quintela** (DIV-014, DIV-015, RIS-006)  
   Quais critérios formam o Pode começar, por modalidade e cargo: documentos, ASO, CRF, contrato assinado, S-2190, acesso, kit? Quais bloqueiam o início e quais só alertam? Alguém pode autorizar exceção, e qual a alternativa quando a loja fica desfalcada?

8. **Para: Helena Vasconcelos e BP de RH** (DIV-005, DIV-010)  
   O BP de RH valida hoje as ofertas? Em qual canal, já que o Recruta+ não o registra? O que significa acima do piso e quem aprova oferta no piso? A tabela de piso da FolhaCerta será a fonte oficial e quem mantém o Recruta+ atualizado?

9. **Para: Rogério Tavares** (DIV-014, GAR-006, RIS-010, RIS-011)  
   Como funcionam contrato e eSocial: onde o contrato é gerado e assinado; quem transmite e acompanha S-2190 e S-2200; como um S-2190 pode sair antes do ASO se a trigger exige ASO; o que acontece se a data de início muda; a amostra de eventos está completa? O S-2220 está no escopo e quem o envia?

10. **Para: Rogério Tavares** (GAR-001, GAR-002)  
   Qual é a lista oficial de documentos por modalidade e cargo, já que a única lista é a do manual de 2019? Quais são as principais causas dos 30% de devolução, em percentuais, se houver? Quais campos consomem mais os 25 minutos de digitação, e existe pico mensal além da média de 190?

11. **Para: Rogério Tavares e Marina Quintela** (DIV-008, RIS-009, GAR-008)  
   Por que o aprendiz fica com a Contábil Alfa: limite de sistema ou decisão contratual? Quem é responsável pelo eSocial e pelo prazo, dado o lote quinzenal? O novo sistema só acompanha esse fluxo ou o elimina? Há regra específica para menores de 18 anos (autorização do responsável, restrições de função)?

12. **Para: Paula Nogueira e Fábio Arantes** (DIV-007, RIS-013)  
   O que cada papel pode ver do exame? Proposta: DP e gerente veem só apto ou inapto, data e validade; CID, restrição e observação clínica ficam só no SESMT. A FolhaCerta precisa manter CID e observação? Como eliminar saúde de e-mail, planilha e campos livres?

13. **Para: Paula Nogueira e Marina Quintela** (DIV-006, RIS-001, RIS-002, RIS-003)  
   Campos gestante, pcd_cid e antecedentes têm finalidade e base legal na admissão? O que fazer com candidato_bkp_2022 e o expurgo de 24 meses? Os 6 meses valem para todo não contratado, inclusive oferta recusada? Quais medidas de contenção imediata serão tomadas para a planilha aberta e os acessos, sem esperar o novo sistema?

14. **Para: Igor Melo** (DIV-012, DIV-013, RIS-004, RIS-014)  
   Quais integrações são viáveis e com que limites em FolhaCerta (escrita de colaborador e contrato, leitura de eventos), Recruta+ (contrato e API do fornecedor) e EducaFarma? Qual o caminho do acesso ao PDV: qual sistema de chamados, por que leva 3 dias, é possível provisionar antes do primeiro dia, e o que substitui o login do gerente nesse intervalo?

15. **Para: Cláudia Reis e Helena Vasconcelos** (DIV-004, GAR-005, RIS-007)  
   A integração vale até o 5º dia (RH-012), em vez de 15 (manual) ou 30 (EducaFarma)? Quem atesta o atendimento acompanhado até a conclusão? Quais trilhas faltam para aprendiz e RT? O que deve ser acompanhado até o fim da experiência (cursos, conversas de 30 e 60 dias, avaliação), e por quem?
