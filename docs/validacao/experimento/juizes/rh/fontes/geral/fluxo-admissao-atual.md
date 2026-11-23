# Fluxo de admissão como é hoje

Desenhado por Cláudia Reis e Rogério Tavares em oficina de 09/2026.

```mermaid
flowchart TD
    A[Recrutamento aprova candidato no Recruta+] --> B[Gerente aprova oferta no Recruta+]
    B --> C[Candidato aceita: status CONTRATADO]
    C --> D[Gerente abre linha na planilha de controle]
    D --> E[Gerente pede ASO ao SESMT por e-mail]
    E --> F[Analista do SESMT agenda com a clínica MedTrab por e-mail]
    F --> G[Clínica emite ASO em PDF e envia ao SESMT]
    D --> H[Candidato entrega documentos na loja]
    H --> I[Loja envia digitalizados ao DP por e-mail]
    I --> J{DP confere: completo?}
    J -- não --> H
    J -- sim --> K[DP digita o colaborador na FolhaCerta]
    G --> K
    K --> L[Contrato PRE, depois ATIVO]
    L --> M[Eventos eSocial S-2190 e S-2200]
    L --> N[Gerente marca Liberado na planilha]
    N --> O[Gerente abre chamado de acesso ao PDV]
    N --> P[Primeiro dia: kit e checklist]
    P --> Q[Gerente marca Iniciado]
    P --> R[Loja matricula no EducaFarma]
    R --> S[Acompanhamento até o fim da experiência]
```

Aprendizes seguem por fora da FolhaCerta: o DP envia os dados à Contábil Alfa a partir da etapa J.
