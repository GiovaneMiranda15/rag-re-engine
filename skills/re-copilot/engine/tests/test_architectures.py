"""Pipelines Adaptive, Self-RAG, Agentic, RAPTOR e GraphRAG com LLM falso roteirizado (sem rede)."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from rag_re_engine import cli
from rag_re_engine.embeddings import HashEmbedder
from rag_re_engine.engine import retrieve
from rag_re_engine.ingest import chunk_text
from rag_re_engine.pipelines.adaptive import AdaptiveRagPipeline, heuristic_route
from rag_re_engine.pipelines.agentic import AgenticRagPipeline
from rag_re_engine.pipelines.baseline import BaselinePipeline
from rag_re_engine.pipelines.common import rrf
from rag_re_engine.pipelines.graph import GraphRagPipeline, build_graph, label_propagation
from rag_re_engine.pipelines.raptor import RaptorPipeline, build_raptor, kmeans
from rag_re_engine.pipelines.self_rag import SelfRagPipeline
from rag_re_engine.store import SqliteStore

DOCS = {
    "SIS-01/credito.md": "A análise de crédito do cliente é feita pelo financeiro em até um dia útil.",
    "SIS-01/pedido.md": "O vendedor digita o pedido e o sistema ERP valida o desconto máximo do pedido.",
    "SIS-02/comissao.md": "A comissão do vendedor é calculada pelo financeiro em uma planilha mensal.",
    "geral/lgpd.md": "Dados pessoais de clientes exigem consentimento explícito para uso em marketing.",
    "geral/estoque.md": "O estoque é baixado no faturamento e a loja recebe o estoque uma vez por dia.",
}


class Scripted:
    """Responde conforme o início do prompt; `fail` simula indisponibilidade em todas as chamadas."""

    name = "scripted"

    def __init__(self, route: str = "simples", fail: bool = False, rel: float = 0.9, sufficient: bool = True,
                 faltando: str = "", graph: dict | None = None) -> None:
        self.route, self.fail, self.rel, self.sufficient, self.faltando = route, fail, rel, sufficient, faltando
        self.graph = graph or {}
        self.calls: list[str] = []

    def complete(self, prompt: str) -> str:
        self.calls.append(prompt[:40])
        if self.fail:
            raise RuntimeError("LLM indisponível")
        if prompt.startswith("Classifique"):
            return json.dumps({"complexidade": self.route, "motivo": "teste"})
        if prompt.startswith("Decomponha"):
            return json.dumps({"subqueries": ["comissão vendedor", "crédito cliente"]})
        if prompt.startswith("Você é um avaliador"):
            n = prompt.count("\n[")
            return json.dumps({"scores": [self.rel] * n})
        if prompt.startswith("Reescreva"):
            return json.dumps({"query": "estoque"})
        if prompt.startswith("A partir SOMENTE"):
            return json.dumps({"afirmacoes": [{"texto": "x", "trechos": [0], "suporte": "total"}], "faltando": self.faltando})
        if prompt.startswith("Você está levantando"):
            return json.dumps({"suficiente": self.sufficient, "buscas": ["estoque loja"]})
        if prompt.startswith("Resuma os trechos"):
            return "Resumo: comissão, crédito e estoque."
        if prompt.startswith("Extraia"):
            return json.dumps(self.graph)
        if prompt.startswith("Resuma em 2"):
            return "Comunidade de comissão e financeiro."
        raise AssertionError(prompt[:60])


@pytest.fixture
def embedder() -> HashEmbedder:
    return HashEmbedder()


@pytest.fixture
def idx(tmp_path: Path, embedder: HashEmbedder) -> SqliteStore:
    store = SqliteStore(tmp_path / "a.db")
    chunks = [c for d, t in DOCS.items() for c in chunk_text(d, t, sistema=d.split("/")[0])]
    store.add(chunks, embedder.embed([c.text for c in chunks]), embedder.name)
    yield store
    store.close()


def adaptive(idx, embedder, llm, k=2):
    return AdaptiveRagPipeline(idx, embedder, llm, BaselinePipeline(idx, embedder, k), k)


@pytest.mark.parametrize("route, expect", [("simples", "retrieve: top-2"), ("moderada", "retrieve: top-2"), ("complexa", "decompose")])
def test_adaptive_routes(idx, embedder, route, expect) -> None:
    llm = Scripted(route=route)
    out = adaptive(idx, embedder, llm).run("comissão do vendedor")
    assert out.trace[0].startswith(f"route: {route}")
    assert any(expect in t for t in out.trace) and out.evidence


def test_adaptive_complex_filters_with_evaluator(idx, embedder) -> None:
    out = adaptive(idx, embedder, Scripted(route="complexa", rel=0.1)).run("comissão e crédito")
    assert out.evidence == [] and any("filter: 0/" in t for t in out.trace)


def test_adaptive_degrades_to_heuristic_when_llm_fails(idx, embedder) -> None:
    out = adaptive(idx, embedder, Scripted(fail=True)).run("comissão")
    assert "heurística" in out.trace[0] and out.evidence


def test_heuristic_route_levels() -> None:
    assert heuristic_route("limite de crédito") == "simples"
    assert heuristic_route("impacto da comissão e do desconto entre os sistemas e todos os relatórios") == "complexa"


def test_self_rag_keeps_supported_and_stops(idx, embedder) -> None:
    llm = Scripted()
    out = SelfRagPipeline(idx, embedder, llm).run("comissão do vendedor")
    assert len(out.evidence) == 1 and out.evidence[0].relevance == 0.9
    assert any("ISSUP" in t for t in out.trace) and not any(t.startswith("iter 2") for t in out.trace)


def test_self_rag_iterates_on_missing(idx, embedder) -> None:
    out = SelfRagPipeline(idx, embedder, Scripted(faltando="estoque")).run("comissão do vendedor")
    assert any(t.startswith("iter 2: retrieve 'estoque'") for t in out.trace)


def test_self_rag_degrades(idx, embedder) -> None:
    out = SelfRagPipeline(idx, embedder, Scripted(fail=True)).run("comissão")
    assert out.evidence and any("degradando" in t for t in out.trace)


def test_agentic_loops_until_sufficient(idx, embedder) -> None:
    done = AgenticRagPipeline(idx, embedder, Scripted(sufficient=True), k=2).run("vendas")
    more = AgenticRagPipeline(idx, embedder, Scripted(sufficient=False), k=2).run("vendas")
    assert any("suficiente" in t for t in done.trace)
    assert any("rodada 2" in t and "estoque loja" in t for t in more.trace) and more.evidence


def test_agentic_survives_llm_failure(idx, embedder) -> None:
    out = AgenticRagPipeline(idx, embedder, Scripted(fail=True), k=2).run("comissão")
    assert out.evidence


def test_rrf_favors_items_in_both_rankings(idx, embedder) -> None:
    a = idx.search(embedder.embed_query("comissão"), 3)
    b = idx.search(embedder.embed_query("crédito"), 3)
    common = {h.chunk.chunk_id for h in a} & {h.chunk.chunk_id for h in b}
    merged = rrf([a, b], 5)
    assert len({h.chunk.chunk_id for h in merged}) == len(merged)
    if common:
        assert merged[0].chunk.chunk_id in common


def test_kmeans_is_deterministic(embedder) -> None:
    m = embedder.embed(list(DOCS.values()))
    assert kmeans(m, 2).tolist() == kmeans(m, 2).tolist()


def test_raptor_builds_tree_and_cites_leaves(idx, embedder) -> None:
    report = build_raptor(idx, embedder, Scripted(), cluster_size=2)
    assert report["niveis"] and report["falhas"] == 0
    assert idx.count() == len(DOCS)  # resumos não contam como trechos
    assert all(h.chunk.nivel == 0 for h in idx.search(embedder.embed_query("resumo comissão"), 20))
    out = RaptorPipeline(idx, embedder, k=20).run("resumo comissão crédito estoque")
    summaries = [e for e in out.evidence if e.origin == "summary"]
    assert summaries and all(e.derived_from and all(not d.startswith("raptor/") for d in e.derived_from) for e in summaries)
    # refazer não duplica
    build_raptor(idx, embedder, Scripted(), cluster_size=2)
    assert idx.conn.execute("SELECT COUNT(*) FROM chunks WHERE chunk_id LIKE 'raptor/L1/%'").fetchone()[0] == report["niveis"][1]


def test_raptor_without_build_warns(idx, embedder) -> None:
    out = RaptorPipeline(idx, embedder).run("comissão")
    assert "árvore não construída" in out.trace[0] and out.evidence


def test_raptor_skips_failed_clusters(idx, embedder) -> None:
    report = build_raptor(idx, embedder, Scripted(fail=True), cluster_size=2)
    assert report["falhas"] > 0 and not idx.has_summaries()


GRAPH = {
    "entidades": [
        {"nome": "Comissão", "tipo": "regra", "descricao": "cálculo mensal", "trechos": [0, 1, 2, 3]},
        {"nome": "Financeiro", "tipo": "ator", "descricao": "área", "trechos": [0]},
    ],
    "relacoes": [{"de": "financeiro", "para": "comissão", "rotulo": "calcula", "trecho": 0},
                 {"de": "financeiro", "para": "crédito", "rotulo": "analisa", "trecho": 1}],
}


def test_graph_build_query_and_incremental(idx, embedder) -> None:
    llm = Scripted(graph=GRAPH)
    report = build_graph(idx, embedder, llm, batch=10)
    assert report["entidades"] == 3 and report["relacoes"] == 2 and report["chunks_processados"] == len(DOCS)
    assert report["comunidades"] == 1
    calls = len(llm.calls)
    assert build_graph(idx, embedder, llm, batch=10, communities=False)["chunks_processados"] == 0
    assert len(llm.calls) == calls  # incremental: nada novo a extrair
    out = GraphRagPipeline(idx, embedder, k=3).run("comissão")
    assert len(out.evidence) == 3 and any("expansão" in t for t in out.trace)
    assert any("comunidade" in t for t in out.trace)


def test_graph_without_build_falls_back(idx, embedder) -> None:
    out = GraphRagPipeline(idx, embedder, k=2).run("comissão")
    assert any("grafo não construído" in t for t in out.trace) and len(out.evidence) == 2


def test_graph_counts_failed_batches(idx, embedder) -> None:
    report = build_graph(idx, embedder, Scripted(fail=True), batch=2)
    assert report["lotes_com_falha"] == 3 and report["entidades"] == 0


def test_label_propagation_groups_components() -> None:
    labels = label_propagation([1, 2, 3, 4], [(1, 2), (3, 4)])
    assert labels[1] == labels[2] and labels[3] == labels[4] and labels[1] != labels[3]


def test_reindex_marks_derived_stale(idx, embedder) -> None:
    build_graph(idx, embedder, Scripted(graph=GRAPH), batch=10)
    assert idx.get_meta("derivados_desatualizados") == "0"
    idx.delete_docs(["SIS-02/comissao.md"])
    assert idx.get_meta("derivados_desatualizados") == "1"
    assert idx.conn.execute("SELECT COUNT(*) FROM mentions WHERE chunk_id LIKE 'SIS-02/%'").fetchone()[0] == 0
    out = GraphRagPipeline(idx, embedder, k=2).run("comissão")
    assert any("desatualizado" in t for t in out.trace)


@pytest.mark.parametrize("strategy", ["raptor", "graph_rag"])
def test_structural_strategies_run_without_llm_at_query(idx, embedder, strategy) -> None:
    package = retrieve("comissão", "rastreabilidade", idx, embedder, llm=None, k=2, strategy=strategy)
    assert package.strategy == strategy and package.evidence


@pytest.mark.parametrize("activity, strategy", [("gerenciamento_mudancas", "adaptive_rag"), ("elicitacao", "agentic_rag")])
def test_activity_runs_its_strategy_with_llm(idx, embedder, activity, strategy) -> None:
    package = retrieve("comissão", activity, idx, embedder, Scripted(), k=2)
    assert package.strategy == package.recommended == strategy


def test_llm_strategy_without_llm_falls_back(idx, embedder) -> None:
    package = retrieve("comissão", "gerenciamento_mudancas", idx, embedder, llm=None, k=2)
    assert package.strategy == "baseline" and any("exige LLM" in n for n in package.notes)


def test_cli_build_requires_llm_spec(tmp_path, capsys, monkeypatch) -> None:
    folder = tmp_path / "docs"
    folder.mkdir()
    (folder / "a.md").write_text("A comissão é calculada pelo financeiro.")
    (folder / "b.md").write_text("O crédito é analisado pelo financeiro.")
    db = tmp_path / "c.db"
    assert cli.main(["index", str(folder), "--db", str(db), "--embedder", "hash"]) == 0
    monkeypatch.setattr(cli, "get_llm", lambda spec: Scripted(graph=GRAPH))
    capsys.readouterr()
    assert cli.main(["build", "--db", str(db)]) == 0
    report = json.loads(capsys.readouterr().out)
    assert report["raptor"]["niveis"] and report["graph"]["entidades"] >= 2
