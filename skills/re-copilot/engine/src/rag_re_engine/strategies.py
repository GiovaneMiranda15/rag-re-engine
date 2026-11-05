"""Mapa atividade de Engenharia de Requisitos → arquiteturas RAG adequadas, em ordem de preferência.

Embutido no motor para que ele (e a skill re-copilot) funcionem sem dependências externas.
"""

from __future__ import annotations

from enum import Enum


class Activity(str, Enum):
    ELICITACAO = "elicitacao"
    ANALISE = "analise"
    ESPECIFICACAO = "especificacao"
    VALIDACAO = "validacao"
    GERENCIAMENTO_MUDANCAS = "gerenciamento_mudancas"
    RASTREABILIDADE = "rastreabilidade"


# Primeira da lista = recomendada; as seguintes são alternativas equivalentes (empate).
STRATEGY_MAP: dict[Activity, tuple[str, ...]] = {
    Activity.ELICITACAO: ("agentic_rag",),
    Activity.ANALISE: ("corrective_rag", "self_rag"),
    Activity.ESPECIFICACAO: ("raptor",),
    Activity.VALIDACAO: ("corrective_rag",),
    Activity.GERENCIAMENTO_MUDANCAS: ("adaptive_rag",),
    Activity.RASTREABILIDADE: ("graph_rag",),
}


def candidates(activity: Activity | str) -> tuple[str, ...]:
    return STRATEGY_MAP[Activity(activity)]
