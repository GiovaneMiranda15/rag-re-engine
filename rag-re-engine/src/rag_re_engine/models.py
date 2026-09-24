"""Tipos de dados do motor: chunks indexados, evidências e o Evidence Package de saída."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class Chunk:
    """Trecho de um documento do corpus, unidade de indexação e recuperação."""

    chunk_id: str
    doc_id: str
    position: int
    text: str


@dataclass(frozen=True, slots=True)
class ScoredChunk:
    """Chunk retornado pela busca vetorial com sua similaridade (cosseno) com a consulta."""

    chunk: Chunk
    similarity: float


@dataclass(frozen=True, slots=True)
class Evidence:
    """Trecho entregue ao agente, com a origem e as pontuações que justificam sua inclusão."""

    doc_id: str
    chunk_id: str
    text: str
    similarity: float
    relevance: float | None = None
    origin: str = "internal"  # internal | external

    def to_dict(self) -> dict:
        return {
            "doc_id": self.doc_id,
            "chunk_id": self.chunk_id,
            "text": self.text,
            "similarity": round(self.similarity, 4),
            "relevance": None if self.relevance is None else round(self.relevance, 4),
            "origin": self.origin,
        }


@dataclass(slots=True)
class PipelineOutput:
    """Resultado bruto de um pipeline, antes de ser embalado no Evidence Package."""

    evidence: list[Evidence]
    trace: list[str] = field(default_factory=list)
    llm_calls: int = 0


@dataclass(slots=True)
class EvidencePackage:
    """Contrato de saída do motor: o que foi recuperado, por qual estratégia e por quê."""

    query: str
    activity: str
    recommended: str
    strategy: str
    evidence: list[Evidence]
    trace: list[str]
    llm_calls: int
    latency_s: float
    notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "query": self.query,
            "activity": self.activity,
            "recommended": self.recommended,
            "strategy": self.strategy,
            "evidence": [e.to_dict() for e in self.evidence],
            "trace": list(self.trace),
            "llm_calls": self.llm_calls,
            "latency_s": round(self.latency_s, 3),
            "notes": list(self.notes),
        }
