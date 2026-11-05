# Escopo reformulado: Admissão Única

Situação: `hipótese` até as respostas. Confirmação pendente em `entrega/perguntas.md` (modo Delegado).

**Objetivo.** Sistema único de admissão e onboarding, do candidato aprovado ao fim da experiência [doc: escopo.md].

**Problema.** Etapas espalhadas entre Recruta+, planilha, FolhaCerta, EducaFarma e e-mail; gerente sem visão única; DP redigita; Jurídico sem segurança sobre o cumprimento das regras [doc: escopo.md].

**Atores.** Candidato, gerente de loja, gerente regional, BP de RH, Recrutamento, DP, SESMT, Jurídico, Encarregada de Dados, Operações, TI, MedTrab, Contábil Alfa.

**Áreas.** RH, DP, Jurídico e Operações puxam; TI apoia; patrocinadora Helena Vasconcelos.

**Dentro.** Oferta, documentos, exame, contrato, acompanhamento do envio ao eSocial, acessos, treinamentos obrigatórios, visão do gerente.

**Fora.** Folha de pagamento (segue na FolhaCerta), desligamento; a decisão de comprar ou construir vem depois do entendimento.

**Premissas (hipótese).** Política RH-012 como referência provisória; 184 lojas próprias como base (Q-001).

**Restrições.** Fontes somente leitura; prazos e orçamento não informados (Q-002).

## Glossário

| Termo | Definição | Fonte |
|---|---|---|
| ASO | Atestado de Saúde Ocupacional | doc: geral/politica-RH-012-admissao-integracao.md#1 |
| BP de RH | Business Partner de RH da regional | doc: geral/politica-RH-012-admissao-integracao.md#0 |
| CONTRATADO | Status do Recruta+ depois da oferta aceita | sql: SIS-02/recrutamais_dump.sql:trg_oferta_aceita |
| ATIVO | Status da folha: admissão efetivada, contrato assinado e ASO validado | sql: SIS-01/folhacerta_dump.sql:contrato.status |
| Liberado | Documentos e ASO conferidos, com data marcada | doc: SIS-03/LEIA-ME.md#1 |
| Iniciado | Primeiro dia trabalhado e kit recebido | doc: SIS-03/LEIA-ME.md#1 |
| RT | Farmacêutico responsável técnico | doc: geral/politica-RH-012-admissao-integracao.md#1 |
| S-2190 / S-2200 | Registro preliminar / admissão no eSocial | sql: SIS-01/folhacerta_dump.sql:esocial_prazo |
| Loja própria / franqueada | Empregador Caliandra / empregador próprio, fora da Política | doc: geral/politica-RH-012-admissao-integracao.md#0 |

## Registros da Etapa 3

**Fora do escopo (pedido registrado, M-01 item 3).** Cálculo de rescisão e homologação de desligamentos, pedidos por Sérgio Antunes. Contradiz o escopo e a resposta da Q-004; depende de decisão de Helena Vasconcelos (Q-036).

| Termo | Definição | Fonte |
|---|---|---|
| CRNM | Carteira de Registro Nacional Migratório | doc: geral/M-02-email-juridico-2026-10-30.md#0 |
| Programa Acolher | Contratação de pessoas refugiadas e migrantes, a partir do 1º trimestre de 2027 | doc: geral/M-02-email-juridico-2026-10-30.md#0 |
