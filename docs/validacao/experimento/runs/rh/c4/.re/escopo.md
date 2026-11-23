# Escopo reformulado — Admissão Única

Status: atualizado com `entrega/respostas.md` em 04/11/2026; sem validação formal.

## Objetivo
Oferecer um sistema único de admissão e onboarding, do candidato aprovado até o fim do período de experiência [doc: escopo.md].

## Problema
A admissão passa por recrutamento, planilha das lojas, folha, treinamento e e-mail. O DP redigita dados, o gerente não tem um lugar único para saber quando o colaborador pode começar e o Jurídico não tem segurança sobre o cumprimento das regras [doc: escopo.md].

## Atores e áreas
Patrocinadora: Helena Vasconcelos. Áreas donas: RH, DP, Jurídico e Operações de Loja. TI apoia. Demais: gerente de loja, gerente regional, BP de RH, Recrutamento, SESMT, Encarregada de Dados, clínica MedTrab, Contábil Alfa [doc: geral/ata-2026-09-22-grupo-trabalho-admissao.md#0].

## Dentro do escopo
Acompanhamento de oferta, documentos, exame admissional, contrato, envio ao eSocial, acessos e treinamentos obrigatórios; visão do gerente sobre a data de início; redução da redigitação do DP; conformidade.

## Abrangência da primeira fase
184 lojas próprias; CLT de balconista, caixa e farmacêutico, inclusive RT [entrevista: negocio Q-001]. Aprendizes entram depois, no fluxo único (prioridade 5).

## Fora do escopo
Folha de pagamento, que continua na FolhaCerta; desligamento [doc: escopo.md]. As 28 franqueadas; escritório central e CD na primeira fase [entrevista: negocio Q-001]. Estágio fica fora da primeira fase até resposta [hipótese, Q-016]. Cálculo de rescisão e homologação de desligamentos, pedidos em M-01, ficam fora, pois são desligamento e folha; Helena confirma (Q-056).

## Premissas [hipótese]
A escolha entre comprar e construir só ocorre depois do levantamento, com critérios em aberto (Q-019). A integração com FolhaCerta e Recruta+ é viável, a confirmar (Q-014).

## Restrições
FolhaCerta permanece como sistema da folha. Prazo e orçamento desconhecidos (Q-017, Q-018).

## Glossário
| Termo | Definição | Fonte |
|---|---|---|
| ASO | Atestado de Saúde Ocupacional | doc:geral/politica-RH-012-admissao-integracao.md#1 |
| BP de RH | Business Partner de RH da regional | doc:geral/politica-RH-012-admissao-integracao.md#0 |
| CONTRATADO | Status do candidato no Recruta+ após aceite da oferta | sql:SIS-02/recrutamais_dump.sql:trg_oferta_aceita |
| ATIVO | Contrato efetivado pelo DP, com contrato assinado e ASO validado | sql:SIS-01/folhacerta_dump.sql:contrato.status |
| Liberado | Na planilha: documentos e ASO conferidos, com início marcado | doc:SIS-03/LEIA-ME.md#0 |
| Iniciado | Na planilha: trabalhou o primeiro dia e recebeu o kit | doc:SIS-03/LEIA-ME.md#0 |
| RT | Farmacêutico responsável técnico | doc:geral/politica-RH-012-admissao-integracao.md#1 |
| S-2190 / S-2200 | Registro preliminar / admissão no eSocial | sql:SIS-01/folhacerta_dump.sql:esocial_prazo |
