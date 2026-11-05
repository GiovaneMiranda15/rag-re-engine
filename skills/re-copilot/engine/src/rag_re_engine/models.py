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
    sistema: str = ""  # sistema de origem (ex.: SIS-01); vazio = documentação geral
    tipo: str = ""  # documento | ddl | erd | processo | planilha | export | outro | resumo
    nivel: int = 0  # 0 = trecho original; >= 1 = resumo hierárquico (RAPTOR)


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
    sistema: str = ""
    derived_from: tuple[str, ...] = ()  # resumo RAPTOR: chunks originais que ele resume

    def to_dict(self) -> dict:
        extra = {"derived_from": list(self.derived_from)} if self.derived_from else {}
        return {
            **extra,
            "doc_id": self.doc_id,
            "chunk_id": self.chunk_id,
            "text": self.text,
            "similarity": round(self.similarity, 4),
            "relevance": None if self.relevance is None else round(self.relevance, 4),
            "origin": self.origin,
            "sistema": self.sistema,
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
