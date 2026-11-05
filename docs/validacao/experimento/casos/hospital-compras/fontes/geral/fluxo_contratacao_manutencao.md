# Fluxo de contratação e manutenção de equipamentos

Rede Hospitalar Aurora do Vale (organização fictícia). Engenharia Clínica e Suprimentos. Revisão de junho de 2025.

## Contratação e renovação

```mermaid
flowchart TD
  A[Eng. Clínica identifica a necessidade] --> B[Requisição no ERP]
  B --> C[Suprimentos faz as cotações]
  C --> D{Valor global acima de R$ 100.000?}
  D -- Sim --> E[Parecer do Jurídico]
  D -- Não --> F[Aprovação conforme alçada]
  E --> F
  F --> G[Assinatura]
  G --> H[Registro no ERP e na planilha do Jurídico]
  H --> I[Execução e medição mensal]
  I --> J[Ateste da Eng. Clínica]
  J --> K[Pagamento pelo Financeiro]
  H --> L[90 dias antes do fim: Suprimentos inicia a renovação]
  L --> C
```

## Manutenção corretiva

```mermaid
flowchart TD
  A[Abertura da OS no ManutClin] --> B[Atendimento pelo prestador]
  B --> C{Precisa de peça não coberta?}
  C -- Sim --> D[OS em AGUARDANDO_COMPRA; requisição digitada no ERP]
  D --> E[Reparo]
  C -- Não --> E
  E --> F[Teste de segurança elétrica]
  F --> G[Engenheiro clínico assina a liberação]
  G --> H[Fechamento da OS e retorno ao uso]
```

Regra da etapa F e G: nenhum equipamento volta ao uso assistencial sem teste aprovado e liberação assinada.
