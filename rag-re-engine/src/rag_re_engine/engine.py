"""Liga o rag-re-advisor (qual arquitetura) aos pipelines implementados (como executar)."""

from __future__ import annotations

import time
from collections.abc import Callable

from rag_re_advisor.engine import recommend
from rag_re_advisor.models import TaskContext

from rag_re_engine.embeddings import Embedder
from rag_re_engine.llm import LLM
from rag_re_engine.models import EvidencePackage
from rag_re_engine.pipelines import Pipeline
from rag_re_engine.pipelines.baseline import BaselinePipeline
from rag_re_engine.pipelines.corrective import CorrectiveRagPipeline, CragConfig
from rag_re_engine.pipelines.external import LocalRequery
from rag_re_engine.store import SqliteStore

PipelineFactory = Callable[[SqliteStore, Embedder, LLM | None, int], Pipeline]


def _baseline(store: SqliteStore, embedder: Embedder, llm: LLM | None, k: int) -> Pipeline:
    return BaselinePipeline(store, embedder, k)


def _corrective(store: SqliteStore, embedder: Embedder, llm: LLM | None, k: int) -> Pipeline:
    if llm is None:
        raise ValueError("corrective_rag exige um LLM (retrieval evaluator)")
    return CorrectiveRagPipeline(store, embedder, llm, LocalRequery(store, embedder), CragConfig(k=k))


# Arquiteturas da Tabela 1 que já têm pipeline executável. As demais caem no baseline com aviso.
PIPELINES: dict[str, PipelineFactory] = {
    "baseline": _baseline,
    "corrective_rag": _corrective,
}


def select_strategy(context: TaskContext) -> tuple[str, str, list[str]]:
    """Retorna (recomendada, executada, notas).

    Entre as arquiteturas empatadas com a maior pontuação do advisor, usa a primeira já
    implementada; se nenhuma estiver implementada, usa o baseline e registra o motivo.
    """
    rec = recommend(context)
    tied = [rec.top] + [alt for alt in rec.alternatives if alt.score == rec.top.score]
    recommended = rec.top.architecture.value
    for scored in tied:
        name = scored.architecture.value
        if name in PIPELINES:
            notes = [] if name == recommended else [f"empate com {recommended}; usando {name} (implementada)"]
            return recommended, name, notes
    names = ", ".join(s.architecture.value for s in tied)
    return recommended, "baseline", [f"{names} ainda não implementada(s); usando baseline"]


def retrieve(
    query: str,
    context: TaskContext,
    store: SqliteStore,
    embedder: Embedder,
    llm: LLM | None,
    k: int = 5,
    strategy: str | None = None,
) -> EvidencePackage:
    if strategy:
        recommended, chosen, notes = recommend(context).top.architecture.value, strategy, ["estratégia forçada pelo usuário"]
        if chosen not in PIPELINES:
            raise ValueError(f"estratégia não implementada: {chosen} (disponíveis: {sorted(PIPELINES)})")
    else:
        recommended, chosen, notes = select_strategy(context)

    if chosen != "baseline" and llm is None:
        notes.append(f"{chosen} exige LLM e nenhum foi configurado; usando baseline")
        chosen = "baseline"

    pipeline = PIPELINES[chosen](store, embedder, llm, k)
    started = time.monotonic()
    output = pipeline.run(query)
    return EvidencePackage(
        query=query,
        activity=context.activity.value,
        recommended=recommended,
        strategy=chosen,
        evidence=output.evidence,
        trace=output.trace,
        llm_calls=output.llm_calls,
        latency_s=time.monotonic() - started,
        notes=notes,
    )
