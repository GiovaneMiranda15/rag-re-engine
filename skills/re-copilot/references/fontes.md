# Fontes — sistemas, extração e detecção de mudança

Acesso **somente leitura**. Nada fora de `.re/` é alterado.

## 1. Registrar sistemas

Pergunte ao usuário quais sistemas e "não sistemas" participam do processo: ERPs,
sistemas web, planilhas, e-mails padronizados, processos em papel. Para cada um, grave em
`fontes.json.sistemas`: `id` (`SIS-NN`), `nome`, `papel`, `descricao`, `pastas` (onde estão
as fontes dele, relativas à raiz do projeto). Documentação transversal (políticas, atas,
contratos) vai no sistema `geral`.

## 2. Registrar e extrair fontes

```bash
python3 -I <skill>/scripts/recop.py fontes --update   # registra os arquivos das pastas com hash
```

Por formato:

| Formato | Ação |
|---|---|
| txt, md, pdf | indexa direto |
| `.sql` (dump/backup) | indexa direto: o motor mantém só a estrutura (DDL, constraints, procedures, triggers, comments) e descarta `INSERT`/`COPY`. Sem motor: leia o arquivo **filtrando** com `grep -v -iE '^(INSERT\|COPY)'` ou equivalente; nunca carregue blocos de dados |
| ERD (png, jpg, pdf de imagem) | leia a imagem e transcreva para `.re/extraidos/<sistema>-<nome>.md`: entidades, atributos-chave, relações e cardinalidades (Mermaid `erDiagram`) e observações |
| BPMN, drawio (XML) | extraia raias, tarefas, gateways e fluxos para `.re/extraidos/…md` (processo em lista numerada) |
| csv, xlsx | só cabeçalhos, tipos e regras visíveis (fórmulas, validações). Sem linhas de dados pessoais. Transcreva para `.re/extraidos/` |
| docx | `pandoc -t plain` se existir; senão peça exportação para PDF |
| código-fonte | não indexe; use Grep/Read direcionados (rotas, entidades, regras) e cite `[código: path:linha]` |

Transcrições em `.re/extraidos/` são indexadas com o mesmo `--sistema` da fonte original.
Registre a transcrição como fonte, citando a original na primeira linha.

## 3. Indexar (com motor)

Uma chamada por pasta de sistema, sempre no mesmo `--db` e com o mesmo embedder:

```bash
$ENGINE index <pasta> --db .re/index.db --sistema SIS-01 --embedder fastembed:sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
$ENGINE index .re/extraidos --db .re/index.db --sistema SIS-01   # se houver transcrições daquele sistema
```

O `doc_id` fica prefixado pelo sistema (`SIS-01/schema.sql#2`), o que torna a citação
autoexplicativa. Reindexar a mesma pasta substitui os chunks antigos. Atualize
`fontes[].indexado_em` e `state.json.indice`.

## 4. Detectar mudança

```bash
python3 -I <skill>/scripts/recop.py fontes            # só mostra
python3 -I <skill>/scripts/recop.py fontes --update   # registra hashes novos
```

- **novas / alteradas:** extraia e indexe de novo; leia o conteúdo novo (para alteradas,
  compare com o que o modelo já cita daquela fonte) e passe cada informação relevante pelo
  classificador (`manutencao.md`, gatilho `fonte`).
- **removidas:** liste os itens do modelo que citam a fonte e pergunte ao usuário se
  continuam válidos.

Rode `fontes` sempre que a skill for ativada num projeto existente.
