"""Servidor MCP que expõe o motor de recomendação como uma tool via stdio."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from rag_re_advisor.engine import recommend
from rag_re_advisor.models import Activity, Criticality, DataStructure, DataVolume, TaskContext

mcp = FastMCP("rag-re-advisor")


@mcp.tool()
def recommend_rag_architecture(
    activity: str,
    data_volume: str | None = None,
    data_structure: str | None = None,
    needs_traceability: bool | None = None,
    needs_external_lookup: bool | None = None,
    audit_criticality: str | None = None,
    latency_budget: str | None = None,
) -> dict:
    """Recomenda a arquitetura RAG mais adequada para uma atividade de Engenharia de
    Requisitos, com base no framework do TCC "Aplicação de Arquiteturas RAG na
    Engenharia de Requisitos" (Giovane Luna Miranda).

    Args:
        activity: uma de elicitacao, analise, especificacao, validacao,
            gerenciamento_mudancas, rastreabilidade.
        data_volume: baixo, medio ou alto (opcional).
        data_structure: nao_estruturado, semi_estruturado ou relacional_grafo (opcional).
        needs_traceability: se a tarefa exige rastrear interdependências entre
            artefatos (opcional).
        needs_external_lookup: se a base interna pode estar incompleta/desatualizada e
            exigir busca externa complementar (opcional).
        audit_criticality: baixo, medio ou alto — tolerância a alucinação (opcional).
        latency_budget: baixo, medio ou alto — tempo/recursos disponíveis (opcional).
    """

    context = TaskContext(
        activity=Activity(activity),
        data_volume=DataVolume(data_volume) if data_volume else None,
        data_structure=DataStructure(data_structure) if data_structure else None,
        needs_traceability=needs_traceability,
        needs_external_lookup=needs_external_lookup,
        audit_criticality=Criticality(audit_criticality) if audit_criticality else None,
        latency_budget=Criticality(latency_budget) if latency_budget else None,
    )
    return recommend(context).to_dict()


def run() -> None:
    mcp.run()


if __name__ == "__main__":
    run()
