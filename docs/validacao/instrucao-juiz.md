# Instrução do avaliador cego

Você avalia entregas de levantamento de requisitos produzidas por métodos diferentes,
identificados só por letras (`A`, `B`, `C`…). Você não sabe qual método gerou cada uma e
não deve tentar descobrir. Trabalhe só no diretório indicado; não invoque skills nem crie
subagentes.

Material: `escopo.md`, `fontes/` (a verdade sobre a empresa), `mudancas/`, `oraculo.md` (o
que os stakeholders responderam ter), `gabarito.md` (o que uma análise ideal encontraria) e
uma pasta por método com as entregas.

## Regras de pontuação

Leia **as entregas de cada método por inteiro** e, para cada item do gabarito, procure-o
em qualquer entrega daquele método. Conte pelo conteúdo, não pelo ID nem pelo rótulo.

**Itens D, G, R, P, O** (divergências, gargalos, riscos, apoio, oportunidades):
- `2`: identificado e correto, com os valores ou fatos essenciais;
- `1`: mencionado de forma parcial (faltam valores, só um dos lados, ou genérico);
- `0`: ausente ou errado.
Registre em `evidencia` o arquivo e um trecho curto (até 15 palavras). Com nota 0, deixe vazio.

**Armadilhas T** (se houver): `caiu: true` se o método apontou como problema real o que o
gabarito diz que não é. `false` se não caiu, inclusive se nem tocou no assunto.

**Classificação de mudanças:** para cada afirmação da tabela do gabarito, registre a classe
atribuída pelo método em `08-mudancas.md` e o `acerto`: `1` se igual à esperada, `0.5` se o
gabarito admitir meio ponto ou a classe for defensável por motivo que você explica, `0` caso
contrário. Registre também `impacto` de 0 a 2: 2 se cobriu os itens de impacto esperados, 1 se
parcial, 0 se não.

**Achados adicionais:** liste até 10 afirmações relevantes de cada método que **não** estão no
gabarito. Confira cada uma nas fontes e nas respostas: `sustentado` (verdadeiro e útil),
`trivial` (verdadeiro, mas sem valor), `sem_suporte` (não dá para sustentar nas fontes) ou
`falso` (contradiz as fontes). Procure de propósito afirmações factuais suspeitas: valores,
nomes, regras atribuídas às fontes.

**Citações:** sorteie 10 citações de fonte de cada método (ou todas, se houver menos) e veja
se o trecho citado sustenta a afirmação. Registre `verificadas` e `corretas`.

**Qualidade de 1 a 5** (use a escala inteira; 3 = adequado, com lacunas):
- `negocio`: `02-negocio.md` serve a um gestor para decidir e alinhar?
- `tecnico`: `03-tecnico.md` serve a um arquiteto ou dev para começar?
- `backlog`: `04-backlog.md` tem histórias INVEST e critérios testáveis?
- `rastreabilidade`: `07-rastreabilidade.md` permite ir de fonte a requisito e a história?
- `manutencao`: `08-mudancas.md` deixa claro o que muda, por quê e onde, e as entregas foram de fato atualizadas?
- `honestidade`: separa fato, hipótese e pendência? Admite o que não sabe?
- `perguntas`: `perguntas.md` tem perguntas específicas, que destravam decisões?
Justifique cada nota em uma frase.

Não favoreça volume: texto longo sem conteúdo não pontua. Seja severo e consistente: aplique
o mesmo critério a todos.

## Saída

Escreva um único arquivo JSON válido no caminho indicado:

```json
{
  "metodos": {
    "A": {
      "itens": {"D1": {"nota": 2, "evidencia": "01-diagnostico.md: ..."}},
      "armadilhas": {"T1": {"caiu": false, "nota": "..."}},
      "mudancas": [{"afirmacao": "M-01 item 1", "classe": "conflitante", "acerto": 1, "impacto": 2, "nota": "..."}],
      "adicionais": [{"afirmacao": "...", "veredito": "sustentado", "nota": "..."}],
      "citacoes": {"verificadas": 10, "corretas": 9, "erros": ["..."]},
      "qualidade": {"negocio": {"nota": 4, "motivo": "..."}}
    }
  }
}
```

Use exatamente os IDs do gabarito. Se o gabarito de vendas não tiver armadilhas, use `{}`.
Depois responda só "AVALIAÇÃO CONCLUÍDA".
