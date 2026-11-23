# 08. Avaliação de mudanças

Comunicações avaliadas:

- **M-01:** e-mail de Suprimentos, 21/10/2026, com pontos da reunião do Comitê de Contratos.
- **M-02:** Memorando 2026/14, do Jurídico e da Engenharia Clínica, 03/11/2026.

## 1. Resumo

| ID | Afirmação | Classificação | Aplicado às entregas? |
|---|---|---|---|
| M-01.1a | A Rede incorpora o Hospital Aurora Serra em janeiro de 2027 | **existente** | Só o registro da fonte |
| M-01.1b | Ele chega com dois contratos de manutenção próprios, que precisam entrar no sistema único | **complementar** | Sim |
| M-01.2 | Contratos com valor global acima de R$ 250 mil continuam aprovados pela Diretora Geral | **existente** | Não há o que mudar |
| M-01.3 | A Farmácia pediu controle de validade de lotes de medicamentos em estoque | **fora_escopo** | Só o registro da exclusão |
| M-02.1 | Parecer jurídico obrigatório apenas acima de R$ 200.000,00 de valor global, daqui em diante | **conflitante** | **Não.** Mantido R$ 30.000,00, com decisão escalada |
| M-02.2 | Glosas limitadas a 10% do valor mensal do contrato em cada competência | **complementar** | Sim |

**Decisão necessária da Diretora Geral:** a Diretoria aprovou o limite de R$ 200.000,00 para parecer? Até haver resposta, as entregas seguem a Política, e há risco de dispensa de parecer sem base normativa.

## 2. Análise por afirmação

### M-01.1a: incorporação do Hospital Aurora Serra — existente

- **Relação com o levantado:** a entrada em janeiro de 2027 já consta em R15 e em `02-negocio.md`, seção 3.1. O e-mail é coerente e esclarece que "entrar" significa incorporação à Rede.
- **Requisitos:** nenhum novo. RF-03 já cobre.
- **Backlog:** nenhum novo. HU-040 já cobre.
- **Documentos:** fonte acrescentada.

### M-01.1b: dois contratos próprios — complementar

- **Relação com o levantado:** acrescenta um fato a R15, que não mencionava contratos, e resolve parte da D-02: os dois contratos estão na primeira fase. Continua ampliando o escopo original e a POL 1.1, de quatro unidades, como já registrado.
- **Requisitos:** RF-03, RF-31 e RN-08 passam a abranger esses contratos.
- **Backlog:** nova HU-044; HU-041 e HU-042 ajustadas.
- **Documentos:** `01`, `02` (seção 3.1, D-02, nova D-15), `03` (migração e riscos), `04` a `07`.
- **Atenção:**
  - A incorporação ocorre **cerca de 5 meses antes do go-live**. De janeiro a junho, os contratos precisam de controle no processo atual e de registro no ERP antes do primeiro pagamento (POL 4.1).
  - Número, fornecedor, valor, vigência, SLA e equipamentos não foram informados.
  - O e-mail não fala de inventário, OS, sistemas ou volume do hospital. Isso segue fora do que foi confirmado, e pode pesar na data de 30/06/2027.
  - Não se sabe se os contratos atendem à Política; a D-15 assume que entram sem aprovação retroativa.

### M-01.2: alçada da Diretora Geral — existente

- **Relação com o levantado:** igual à POL 2 e 2.2 e à RN-01 e RN-02, inclusive na base de valor global. A palavra "continuam" confirma que não há mudança.
- **Requisitos, backlog e documentos:** sem impacto, além de acrescentar a fonte na rastreabilidade.
- **Observação:** o ERP ainda compara esse limite com o valor mensal. Esse achado segue tratado por RF-10 e HU-014.

### M-01.3: validade de lotes de medicamentos — fora_escopo

- **Relação com o levantado:** o escopo exclui medicamentos, e a POL 1.2 os remete à POL-FAR-002.
- **Requisitos e backlog:** nenhum.
- **Documentos:** exclusão explicitada em `02-negocio.md`, seção 3.
- **Encaminhamento:** informar à Farmácia que o pedido não será atendido neste projeto e deve ir à patrocinadora como demanda separada. Só ela pode mudar o escopo.

### M-02.1: parecer acima de R$ 200.000,00 — conflitante

- **Conflita com:** POL 4.5 (R$ 30.000,00, aprovada pela Diretoria), R3 ("proposta ainda não aprovada pela Diretoria; até lá, vale a Política") e RN-07.
- **Por que não foi aplicada:** o memorando vem do Jurídico e da Engenharia Clínica e não cita aprovação da Diretoria nem revisão da Política. O próprio Jurídico, junto com a Diretora Geral, disse que a mudança dependia dessa aprovação. As respostas não têm data, então não dá para saber se a aprovação veio depois delas, mas nada nas fontes a comprova.
- **Requisitos:** RN-07 permanece, com o conflito registrado. RF-16 já permite a mudança por parâmetro.
- **Backlog:** sem nova história. HU-016 e HU-020 foram redigidas para não depender do valor.
- **Documentos:** `01`, `02` (RN-07, nova D-16, seção 10), `03`, `04` a `07`.
- **Efeito sobre os 8 contratos, se aprovado:** pelo valor global, seriam 6 com parecer, contra os 8 de hoje. CT-2025-0102 (R$ 163.200,00) e CT-2026-0021 (R$ 58.800,00) deixam de exigi-lo. Valores calculados com o mensal atual.
- **Efeito sobre o gargalo:** reduziria a fila dos 23 dias, em proporção desconhecida, pois não há volume de pareceres por faixa (R5).
- **Se aprovado, será preciso:** ato formal da Diretoria, revisão da POL 4.5, nova versão do parâmetro com data de início, e atualização de RN-07, HU-020 e `03-tecnico.md`. O fluxo de 2025, com R$ 100.000,00, continua a adequar em qualquer caso.
- **Risco imediato:** o memorando diz "daqui em diante". Se o Jurídico já dispensar pareceres nessa faixa, haverá descumprimento da POL 4.5, e as duas renovações citadas acima estão próximas.

### M-02.2: teto de glosa — complementar

- **Relação com o levantado:** R9 trouxe o teto de 10% por competência, sem base de cálculo. O memorando define a base: **valor mensal do contrato**. Isso confirma a parte correspondente da D-08.
- **Requisitos:** RN-14 passa a ter a base definida.
- **Backlog:** HU-034 ajustada. Exemplo: R$ 11.040,00 por mês têm teto de R$ 1.104,00, atingido em 5 eventos de R$ 220,80.
- **Documentos:** `01`, `02` (RN-14, D-08), `03` (parâmetros), `04` a `07`.
- **Ressalvas:**
  - A POL 5.3 não prevê teto, e o memorando não cita aprovação da Diretoria. Não há proibição expressa, por isso aplico como complemento, com a formalização mantida como pendência antes da primeira glosa no sistema.
  - A definição de "evento", as regras do relógio de SLA e o caráter sugerido da glosa continuam em D-08, sem resposta.
  - Em contrato em dólar, o teto é calculado em dólar.

## 3. O que mudou nas entregas

| Arquivo | Mudança |
|---|---|
| `01-diagnostico.md` | Aurora Serra e teto de glosa atualizados; nova seção 10 |
| `02-negocio.md` | Seção 3 (Farmácia), 3.1 (Aurora Serra), RN-07, RN-14, D-02, D-08; novas D-15 e D-16; pendências, ações imediatas, riscos e histórico |
| `03-tecnico.md` | Parâmetros de parecer e glosa, carga e reconciliação com os 2 contratos, capacidade, risco técnico |
| `04-backlog.md` | Nova HU-044. Ajustes em HU-016, HU-020, HU-034, HU-041 e HU-042. Total: 44 histórias |
| `05-jira.csv`, `06-azure-devops.csv` | Mesmas mudanças de `04-backlog.md` |
| `07-rastreabilidade.md` | Fontes M-01 e M-02, HU-044, nova seção 5 |

## 4. O que não mudou, de propósito

- **RN-07 e limite de R$ 30.000,00:** aguardam a Diretoria.
- **Data de 30/06/2027:** nenhuma comunicação a altera, mas a Aurora Serra aumenta o risco se o inventário e as OS do hospital também forem incluídos.
- **Backlog da Farmácia:** nenhum item criado.

## 5. Pendências abertas por estas comunicações

| Pendência | Quem responde |
|---|---|
| A Diretoria aprovou o limite de R$ 200.000,00? Desde quando vale? | Diretora Geral |
| A Diretoria aprova o teto de glosa? Ele vale para os contratos vigentes ou depende de aditivo? | Diretora Geral, Jurídico |
| Dados e documentos dos 2 contratos da Aurora Serra; como ficam até o go-live | Jurídico, Suprimentos |
| Inventário, OS e sistemas da Aurora Serra entram na primeira fase? | Diretora Geral |
| A POL 1.1 será revista para abranger a Aurora Serra? | Diretora Geral |
| Ata completa da reunião de 21/10/2026 | Suprimentos, Jurídico |
| Resposta à Farmácia sobre o pedido fora do escopo | Diretora Geral |
