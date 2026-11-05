"""Testes de ingestão, índice, pipelines, seleção de estratégia, avaliação e CLI."""

from __future__ import annotations

import io
import json

import pytest

from rag_re_engine import cli
from rag_re_engine.engine import retrieve, select_strategy
from rag_re_engine.evaluation import evaluate, load_dataset, score
from rag_re_engine.ingest import chunk_text, split_strips
from rag_re_engine.pipelines.corrective import Action, CorrectiveRagPipeline, CragConfig, decide_action
from rag_re_engine.pipelines.external import LocalRequery
from rag_re_engine.strategies import Activity

from conftest import FIXTURES, FakeLLM


def test_chunk_text_respects_max_and_is_deterministic() -> None:
    text = "\n\n".join(["palavra " * 40] * 5)
    first = chunk_text("d", text, max_chars=300, overlap=50)
    assert first == chunk_text("d", text, max_chars=300, overlap=50)
    assert all(len(c.text) <= 300 for c in first)
    assert [c.chunk_id for c in first] == [f"d#{i}" for i in range(len(first))]


def test_split_strips_groups_sentences() -> None:
    assert split_strips("A. B. C.", sentences_per_strip=2) == ["A. B.", "C."]


def test_store_search_ranks_relevant_document_first(store, embedder) -> None:
    hits = store.search(embedder.embed_query("password login attempts locked"), k=3)
    assert hits[0].chunk.doc_id == "auth.txt"


def test_store_rejects_mixing_embedders(store) -> None:
    from rag_re_engine.embeddings import HashEmbedder

    other = HashEmbedder(dim=64)
    with pytest.raises(ValueError):
        store.add([], other.embed([]), other.name)


@pytest.mark.parametrize(
    ("scores", "expected"),
    [([0.9, 0.1], Action.CORRECT), ([0.1, 0.2], Action.INCORRECT), ([0.4, 0.1], Action.AMBIGUOUS)],
)
def test_decide_action(scores, expected) -> None:
    assert decide_action(scores, upper=0.6, lower=0.3) is expected


def _crag(store, embedder, llm) -> CorrectiveRagPipeline:
    return CorrectiveRagPipeline(store, embedder, llm, LocalRequery(store, embedder), CragConfig(k=2))


def test_crag_correct_keeps_only_relevant_internal_strips(store, embedder) -> None:
    llm = FakeLLM(keywords={"password", "locked"})
    out = _crag(store, embedder, llm).run("password lockout rules")
    assert out.evidence and all(e.origin == "internal" for e in out.evidence)
    assert all(e.doc_id == "auth.txt" for e in out.evidence)
    assert out.llm_calls == 2  # grade + refine
    assert any("-> correct" in t for t in out.trace)


def test_crag_incorrect_goes_to_external_source(store, embedder) -> None:
    llm = FakeLLM(keywords={"invoice"}, rewrite_to="monthly invoice late payment")
    out = _crag(store, embedder, llm).run("password lockout rules")
    assert any("-> incorrect" in t for t in out.trace)
    assert out.evidence and all(e.origin == "external" for e in out.evidence)
    assert {e.doc_id for e in out.evidence} == {"billing.txt"}
    assert out.llm_calls == 3  # grade + rewrite + refine


def test_crag_degrades_to_similarity_when_llm_fails(store, embedder) -> None:
    out = _crag(store, embedder, FakeLLM(keywords=set(), fail=True)).run("password")
    assert len(out.evidence) == 2
    assert any("degradando" in t for t in out.trace)


def test_select_strategy_uses_implemented_architecture_for_analise() -> None:
    recommended, chosen, _ = select_strategy(Activity.ANALISE)
    assert recommended in {"corrective_rag", "self_rag"}
    assert chosen == "corrective_rag"


def test_select_strategy_uses_architecture_of_each_activity() -> None:
    expected = {
        Activity.ELICITACAO: "agentic_rag", Activity.ESPECIFICACAO: "raptor", Activity.VALIDACAO: "corrective_rag",
        Activity.GERENCIAMENTO_MUDANCAS: "adaptive_rag", Activity.RASTREABILIDADE: "graph_rag",
    }
    for activity, name in expected.items():
        assert select_strategy(activity)[:2] == (name, name)


def test_retrieve_without_llm_uses_baseline(store, embedder) -> None:
    package = retrieve("password", Activity.ANALISE, store, embedder, llm=None, k=2)
    assert package.strategy == "baseline"
    assert any("exige LLM" in n for n in package.notes)


def test_evaluation_metrics(store, embedder) -> None:
    queries = load_dataset(FIXTURES / "dataset.jsonl")
    report = evaluate(queries, ["baseline"], store, embedder, llm=None, k=2)
    assert report["summary"]["baseline"]["hit"] == 1.0
    assert report["summary"]["baseline"]["mrr"] == 1.0


def test_score_handles_empty_evidence(store, embedder) -> None:
    package = retrieve("x", Activity.ANALISE, store, embedder, llm=None, k=0)
    assert score(package, frozenset({"auth.txt"}))["hit"] == 0.0


def test_cli_context_reads_task_package(store, embedder, monkeypatch, capsys) -> None:
    task = {
        "task_id": "T1",
        "objective": "password lockout rules",
        "context_request": {"activity": "analise", "db": store.path, "k": 2},
    }
    monkeypatch.setattr("sys.stdin", io.StringIO(json.dumps(task)))
    assert cli.main(["context", "--llm", "none"]) == 0
    package = json.loads(capsys.readouterr().out)
    assert package["strategy"] == "baseline"
    assert package["evidence"][0]["doc_id"] == "auth.txt"


def test_sql_structure_drops_data_rows() -> None:
    from rag_re_engine.ingest import sql_structure

    dump = (
        "CREATE TABLE cliente (id INT PRIMARY KEY, cpf VARCHAR(11));\n"
        "INSERT INTO cliente VALUES (1, '12345678900');\n"
        "INSERT INTO cliente VALUES\n(2, '98765432100'),\n(3, '11122233344');\n"
        "COPY public.pedido (id, total) FROM stdin;\n1\t10.0\n\\.\n"
        "ALTER TABLE pedido ADD CONSTRAINT ck_total CHECK (total >= 0);\n"
    )
    out = sql_structure(dump)
    assert "CREATE TABLE cliente" in out and "ck_total" in out
    assert "123456" not in out and "987654" not in out and "10.0" not in out


def test_index_with_sistema_prefixes_and_filters(tmp_path) -> None:
    from rag_re_engine.store import SqliteStore

    for sis, text in (("SIS-01", "Desconto máximo de 10% por pedido."), ("SIS-02", "Desconto máximo de 15% por pedido.")):
        folder = tmp_path / sis
        folder.mkdir()
        (folder / "regras.md").write_text(text)
        assert cli.main(["index", str(folder), "--db", str(tmp_path / "i.db"), "--embedder", "hash", "--sistema", sis]) == 0
    store = SqliteStore(tmp_path / "i.db", {"SIS-02"})
    from rag_re_engine.embeddings import HashEmbedder

    hits = store.search(HashEmbedder().embed_query("desconto máximo"), 5)
    assert [h.chunk.doc_id for h in hits] == ["SIS-02/regras.md"]
    assert hits[0].chunk.sistema == "SIS-02" and hits[0].chunk.tipo == "documento"


def test_evaluation_flags_degraded_runs(store, embedder) -> None:
    from rag_re_engine.evaluation import to_markdown

    queries = load_dataset(FIXTURES / "dataset.jsonl")
    report = evaluate(queries, ["corrective_rag"], store, embedder, FakeLLM({"x"}, fail=True), k=2)
    assert report["summary"]["corrective_rag"]["degradada"] == 1.0
    assert "resultado não confiável" in to_markdown(report)
    clean = evaluate(queries, ["baseline"], store, embedder, None, k=2)
    assert "não confiável" not in to_markdown(clean)


def test_score_credits_summary_by_its_source_documents() -> None:
    from rag_re_engine.models import Evidence, EvidencePackage

    summary = Evidence("raptor/L1", "raptor/L1/0", "resumo", 0.9, None, "summary", "", ("auth.txt#0", "billing.txt#1"))
    package = EvidencePackage("q", "especificacao", "raptor", "raptor", [summary], [], 0, 0.0)
    result = score(package, frozenset({"auth.txt", "reports.md"}))
    assert result["hit"] == 1.0 and result["recall"] == 0.5 and result["precision"] == 1.0
