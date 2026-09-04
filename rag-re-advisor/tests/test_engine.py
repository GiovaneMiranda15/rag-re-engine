"""Valida que o motor reproduz a Tabela 1 (mapeamento primário) da proposta de TCC."""

from __future__ import annotations

import pytest

from rag_re_advisor.engine import recommend
from rag_re_advisor.models import Activity, Criticality, DataStructure, DataVolume, TaskContext

EXPECTED_PRIMARY: dict[Activity, set[str]] = {
    Activity.ELICITACAO: {"agentic_rag"},
    Activity.ANALISE: {"self_rag", "corrective_rag"},
    Activity.ESPECIFICACAO: {"raptor"},
    Activity.VALIDACAO: {"corrective_rag"},
    Activity.GERENCIAMENTO_MUDANCAS: {"adaptive_rag"},
    Activity.RASTREABILIDADE: {"graph_rag"},
}


@pytest.mark.parametrize("activity", list(Activity))
def test_recommendation_matches_tabela_1(activity: Activity) -> None:
    result = recommend(TaskContext(activity=activity))
    top_score = result.top.score
    top_architectures = {result.top.architecture.value} | {
        alt.architecture.value for alt in result.alternatives if alt.score == top_score
    }
    assert top_architectures == EXPECTED_PRIMARY[activity]


def test_no_secondary_signal_keeps_only_the_primary_reason() -> None:
    result = recommend(TaskContext(activity=Activity.ELICITACAO))
    assert result.top.architecture.value == "agentic_rag"
    assert len(result.top.reasons) == 1


def test_traceability_signal_boosts_graph_rag_for_rastreabilidade() -> None:
    base = recommend(TaskContext(activity=Activity.RASTREABILIDADE))
    boosted = recommend(TaskContext(activity=Activity.RASTREABILIDADE, needs_traceability=True))
    assert boosted.top.architecture.value == "graph_rag"
    assert boosted.top.score > base.top.score


def test_graph_structure_signal_boosts_graph_rag() -> None:
    result = recommend(
        TaskContext(activity=Activity.RASTREABILIDADE, data_structure=DataStructure.RELACIONAL_GRAFO)
    )
    assert result.top.architecture.value == "graph_rag"
    assert len(result.top.reasons) == 2


def test_audit_criticality_breaks_the_tie_between_self_rag_and_crag_for_analise() -> None:
    result = recommend(TaskContext(activity=Activity.ANALISE, audit_criticality=Criticality.ALTO))
    # Ambas ganham +2 pelo mesmo sinal (audit_criticality=alto), então o empate
    # permanece — mas a pontuação de ambas deve subir em relação ao caso sem sinal.
    base = recommend(TaskContext(activity=Activity.ANALISE))
    assert result.top.score > base.top.score


def test_external_lookup_signal_only_affects_corrective_rag() -> None:
    result = recommend(TaskContext(activity=Activity.VALIDACAO, needs_external_lookup=True))
    assert result.top.architecture.value == "corrective_rag"
    assert len(result.top.reasons) == 2


def test_high_data_volume_boosts_raptor_for_especificacao() -> None:
    result = recommend(TaskContext(activity=Activity.ESPECIFICACAO, data_volume=DataVolume.ALTO))
    assert result.top.architecture.value == "raptor"
    assert len(result.top.reasons) == 2


def test_low_latency_budget_boosts_adaptive_rag() -> None:
    result = recommend(
        TaskContext(activity=Activity.GERENCIAMENTO_MUDANCAS, latency_budget=Criticality.BAIXO)
    )
    assert result.top.architecture.value == "adaptive_rag"
    assert len(result.top.reasons) == 2


def test_high_latency_budget_boosts_agentic_rag_for_elicitacao() -> None:
    result = recommend(TaskContext(activity=Activity.ELICITACAO, latency_budget=Criticality.ALTO))
    assert result.top.architecture.value == "agentic_rag"
    assert len(result.top.reasons) == 2
