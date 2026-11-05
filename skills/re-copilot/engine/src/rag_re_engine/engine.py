"""Liga a atividade de RE (qual arquitetura, `strategies`) aos pipelines implementados (como executar)."""

from __future__ import annotations

import time
from collections.abc import Callable

from rag_re_engine.embeddings import Embedder
from rag_re_engine.llm import LLM
from rag_re_engine.models import EvidencePackage
from rag_re_engine.pipelines import Pipeline
from rag_re_engine.pipelines.adaptive import AdaptiveRagPipeline
from rag_re_engine.pipelines.agentic import AgenticRagPipeline
from rag_re_engine.pipelines.baseline import BaselinePipeline
from rag_re_engine.pipelines.corrective import CorrectiveRagPipeline, CragConfig
from rag_re_engine.pipelines.external import LocalRequery
from rag_re_engine.pipelines.graph import GraphRagPipeline
from rag_re_engine.pipelines.raptor import RaptorPipeline
from rag_re_engine.pipelines.self_rag import SelfRagConfig, SelfRagPipeline
from rag_re_engine.store import SqliteStore
from rag_re_engine.strategies import Activity, candidates

PipelineFactory = Callable[[SqliteStore, Embedder, LLM | None, int], Pipeline]


def _baseline(store: SqliteStore, embedder: Embedder, llm: LLM | None, k: int) -> Pipeline:
    return BaselinePipeline(store, embedder, k)


def _corrective(store: SqliteStore, embedder: Embedder, llm: LLM | None, k: int) -> Pipeline:
    if llm is None:
        raise ValueError("corrective_rag exige um LLM (retrieval evaluator)")
    return CorrectiveRagPipeline(store, embedder, llm, LocalRequery(store, embedder), CragConfig(k=k))


def _needs_llm(name: str, llm: LLM | None) -> LLM:
    if llm is None:
        raise ValueError(f"{name} exige um LLM")
    return llm


def _adaptive(store: SqliteStore, embedder: Embedder, llm: LLM | None, k: int) -> Pipeline:
    return AdaptiveRagPipeline(store, embedder, _needs_llm("adaptive_rag", llm), _corrective(store, embedder, llm, k), k)


def _self_rag(store: SqliteStore, embedder: Embedder, llm: LLM | None, k: int) -> Pipeline:
    return SelfRagPipeline(store, embedder, _needs_llm("self_rag", llm), SelfRagConfig(k=k))


def _agentic(store: SqliteStore, embedder: Embedder, llm: LLM | None, k: int) -> Pipeline:
    return AgenticRagPipeline(store, embedder, _needs_llm("agentic_rag", llm), k)


def _raptor(store: SqliteStore, embedder: Embedder, llm: LLM | None, k: int) -> Pipeline:
    return RaptorPipeline(store, embedder, k)


def _graph(store: SqliteStore, embedder: Embedder, llm: LLM | None, k: int) -> Pipeline:
    return GraphRagPipeline(store, embedder, k)


PIPELINES: dict[str, PipelineFactory] = {
    "baseline": _baseline,
    "corrective_rag": _corrective,
    "adaptive_rag": _adaptive,
    "self_rag": _self_rag,
    "agentic_rag": _agentic,
    "raptor": _raptor,
    "graph_rag": _graph,
}

# Executam sem LLM na consulta (o LLM é usado antes, no `build`).
NO_LLM_AT_QUERY = {"baseline", "raptor", "graph_rag"}


def select_strategy(activity: Activity | str) -> tuple[str, str, list[str]]:
    """Retorna (recomendada, executada, notas).

    Entre as arquiteturas indicadas para a atividade, usa a primeira já implementada; se
    nenhuma estiver implementada, usa o baseline e registra o motivo.
    """
    tied = candidates(activity)
    recommended = tied[0]
    for name in tied:
        if name in PIPELINES:
            notes = [] if name == recommended else [f"empate com {recommended}; usando {name} (implementada)"]
            return recommended, name, notes
    return recommended, "baseline", [f"{', '.join(tied)} ainda não implementada(s); usando baseline"]


def retrieve(
    query: str,
    activity: Activity | str,
    store: SqliteStore,
    embedder: Embedder,
    llm: LLM | None,
    k: int = 5,
    strategy: str | None = None,
) -> EvidencePackage:
    if strategy:
        recommended, chosen, notes = candidates(activity)[0], strategy, ["estratégia forçada pelo usuário"]
        if chosen not in PIPELINES:
            raise ValueError(f"estratégia não implementada: {chosen} (disponíveis: {sorted(PIPELINES)})")
    else:
        recommended, chosen, notes = select_strategy(activity)

    if chosen not in NO_LLM_AT_QUERY and llm is None:
        notes.append(f"{chosen} exige LLM e nenhum foi configurado; usando baseline")
        chosen = "baseline"

    pipeline = PIPELINES[chosen](store, embedder, llm, k)
    started = time.monotonic()
    output = pipeline.run(query)
    return EvidencePackage(
        query=query,
        activity=Activity(activity).value,
        recommended=recommended,
        strategy=chosen,
        evidence=output.evidence,
        trace=output.trace,
        llm_calls=output.llm_calls,
        latency_s=time.monotonic() - started,
        notes=notes,
    )
