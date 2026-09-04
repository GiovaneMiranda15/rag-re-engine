"""Tipos de dados do motor de recomendação: entrada (TaskContext) e saída (Recommendation)."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Activity(str, Enum):
    """As 6 atividades clássicas da Engenharia de Requisitos (Tabela 1 da proposta de TCC)."""

    ELICITACAO = "elicitacao"
    ANALISE = "analise"
    ESPECIFICACAO = "especificacao"
    VALIDACAO = "validacao"
    GERENCIAMENTO_MUDANCAS = "gerenciamento_mudancas"
    RASTREABILIDADE = "rastreabilidade"


class DataVolume(str, Enum):
    BAIXO = "baixo"
    MEDIO = "medio"
    ALTO = "alto"


class DataStructure(str, Enum):
    NAO_ESTRUTURADO = "nao_estruturado"
    SEMI_ESTRUTURADO = "semi_estruturado"
    RELACIONAL_GRAFO = "relacional_grafo"


class Criticality(str, Enum):
    """Usado tanto para audit_criticality quanto para latency_budget."""

    BAIXO = "baixo"
    MEDIO = "medio"
    ALTO = "alto"


class RagArchitecture(str, Enum):
    GRAPH_RAG = "graph_rag"
    SELF_RAG = "self_rag"
    CORRECTIVE_RAG = "corrective_rag"
    ADAPTIVE_RAG = "adaptive_rag"
    RAPTOR = "raptor"
    AGENTIC_RAG = "agentic_rag"


@dataclass(frozen=True, slots=True)
class TaskContext:
    """Descreve a tarefa de Engenharia de Requisitos para a qual se busca uma arquitetura RAG."""

    activity: Activity
    data_volume: DataVolume | None = None
    data_structure: DataStructure | None = None
    needs_traceability: bool | None = None
    needs_external_lookup: bool | None = None
    audit_criticality: Criticality | None = None
    latency_budget: Criticality | None = None


@dataclass(frozen=True, slots=True)
class ScoredArchitecture:
    """Uma arquitetura RAG com sua pontuação e as razões que a levaram a essa pontuação."""

    architecture: RagArchitecture
    score: float
    reasons: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True, slots=True)
class Recommendation:
    """Resultado do motor de recomendação para um TaskContext."""

    context: TaskContext
    top: ScoredArchitecture
    alternatives: tuple[ScoredArchitecture, ...]

    def to_dict(self) -> dict:
        def scored_to_dict(scored: ScoredArchitecture) -> dict:
            return {
                "architecture": scored.architecture.value,
                "score": scored.score,
                "reasons": list(scored.reasons),
            }

        return {
            "context": {
                "activity": self.context.activity.value,
                "data_volume": self.context.data_volume.value if self.context.data_volume else None,
                "data_structure": self.context.data_structure.value if self.context.data_structure else None,
                "needs_traceability": self.context.needs_traceability,
                "needs_external_lookup": self.context.needs_external_lookup,
                "audit_criticality": self.context.audit_criticality.value if self.context.audit_criticality else None,
                "latency_budget": self.context.latency_budget.value if self.context.latency_budget else None,
            },
            "top": scored_to_dict(self.top),
            "alternatives": [scored_to_dict(alt) for alt in self.alternatives],
        }
