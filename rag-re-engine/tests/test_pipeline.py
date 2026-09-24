"""Testes de ingestão, índice, pipelines, seleção de estratégia, avaliação e CLI."""

from __future__ import annotations

import io
import json

import pytest

from rag_re_advisor.models import Activity, TaskContext

from rag_re_engine import cli
from rag_re_engine.engine import retrieve, select_strategy
from rag_re_engine.evaluation import evaluate, load_dataset, score
from rag_re_engine.ingest import chunk_text, split_strips
from rag_re_engine.pipelines.corrective import Action, CorrectiveRagPipeline, CragConfig, decide_action
from rag_re_engine.pipelines.external import LocalRequery

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
    recommended, chosen, _ = select_strategy(TaskContext(activity=Activity.ANALISE))
    assert recommended in {"corrective_rag", "self_rag"}
    assert chosen == "corrective_rag"


def test_select_strategy_falls_back_to_baseline_with_note() -> None:
    recommended, chosen, notes = select_strategy(TaskContext(activity=Activity.RASTREABILIDADE))
    assert (recommended, chosen) == ("graph_rag", "baseline")
    assert "graph_rag" in notes[0]


def test_retrieve_without_llm_uses_baseline(store, embedder) -> None:
    package = retrieve("password", TaskContext(activity=Activity.ANALISE), store, embedder, llm=None, k=2)
    assert package.strategy == "baseline"
    assert any("exige LLM" in n for n in package.notes)


def test_evaluation_metrics(store, embedder) -> None:
    queries = load_dataset(FIXTURES / "dataset.jsonl")
    report = evaluate(queries, ["baseline"], store, embedder, llm=None, k=2)
    assert report["summary"]["baseline"]["hit"] == 1.0
    assert report["summary"]["baseline"]["mrr"] == 1.0


def test_score_handles_empty_evidence(store, embedder) -> None:
    package = retrieve("x", TaskContext(activity=Activity.ANALISE), store, embedder, llm=None, k=0)
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
