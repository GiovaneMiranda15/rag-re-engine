"""Base de conhecimento estática do motor de recomendação.

Este módulo espelha, regra por regra, o texto revisado em
`docs/tabela-2-criterios-secundarios.md` (na raiz do repositório). Toda citação aqui
foi verificada contra a fonte primária antes de virar código — não são heurísticas
inventadas. Qualquer mudança de critério deve primeiro ser revisada naquele documento
e só depois refletida aqui.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

from rag_re_advisor.models import (
    Activity,
    Criticality,
    DataStructure,
    DataVolume,
    RagArchitecture,
    TaskContext,
)

# Peso da afinidade primária (atividade -> arquitetura, conforme Tabela 1 da proposta)
# e de cada sinal secundário que reforça essa escolha (Tabela 2).
PRIMARY_ACTIVITY_WEIGHT = 5.0
SIGNAL_WEIGHT = 2.0


@dataclass(frozen=True, slots=True)
class SignalRule:
    """Uma regra secundária: se `predicate(ctx)` for verdadeiro, soma `weight` pontos."""

    predicate: Callable[[TaskContext], bool]
    reason: str
    citation: str
    weight: float = SIGNAL_WEIGHT


@dataclass(frozen=True, slots=True)
class Precondition:
    """Pré-condição de viabilidade: se `violated(ctx)` for verdadeiro, a arquitetura não
    pode ser a recomendação principal (veto, não penalidade numérica)."""

    violated: Callable[[TaskContext], bool]
    reason: str
    citation: str


@dataclass(frozen=True, slots=True)
class ArchitectureProfile:
    architecture: RagArchitecture
    display_name: str
    primary_activities: frozenset[Activity]
    primary_reason: str
    primary_citation: str
    signal_rules: tuple[SignalRule, ...] = ()
    preconditions: tuple[Precondition, ...] = ()


PROFILES: tuple[ArchitectureProfile, ...] = (
    ArchitectureProfile(
        architecture=RagArchitecture.AGENTIC_RAG,
        display_name="Agentic RAG",
        primary_activities=frozenset({Activity.ELICITACAO}),
        primary_reason=(
            "O planejamento multiagente permite decompor autonomamente um problema "
            "complexo em subtarefas menores e sustentar interação iterativa, apoiando "
            "a descoberta ativa de requisitos em entrevistas."
        ),
        primary_citation="SINGH et al., 2025 (arXiv:2501.09136)",
        signal_rules=(
            SignalRule(
                predicate=lambda ctx: ctx.latency_budget == Criticality.ALTO,
                reason=(
                    "Fluxos multiagente exigem, por natureza, maior orçamento de "
                    "latência e recursos — um custo documentado na literatura, não um "
                    "benefício em si — por isso só deve ser recomendado quando esse "
                    "orçamento está disponível."
                ),
                citation="SINGH et al., 2025 (arXiv:2501.09136)",
            ),
        ),
        preconditions=(
            Precondition(
                violated=lambda ctx: ctx.latency_budget == Criticality.BAIXO,
                reason=(
                    "Orçamento de latência/recursos baixo: fluxos multiagente aumentam os "
                    "requisitos de recursos e podem sobrecarregá-los, e a Tabela 2 trata o "
                    "orçamento alto como pré-condição de viabilidade do Agentic RAG."
                ),
                citation="SINGH et al., 2025 (arXiv:2501.09136)",
            ),
        ),
    ),
    ArchitectureProfile(
        architecture=RagArchitecture.SELF_RAG,
        display_name="Self-RAG",
        primary_activities=frozenset({Activity.ANALISE}),
        primary_reason=(
            "Favorece a revisão crítica, ajudando a identificar inconsistências "
            "conceituais e a validar as informações extraídas."
        ),
        primary_citation="ASAI et al., 2024 (arXiv:2310.11511)",
        signal_rules=(
            SignalRule(
                predicate=lambda ctx: ctx.audit_criticality == Criticality.ALTO,
                reason=(
                    "O token de reflexão IsSup verifica se toda afirmação passível de "
                    "verificação na saída é sustentada pela passagem recuperada, "
                    "reduzindo o risco de aceitar informação incorreta quando a "
                    "criticidade de auditoria é alta."
                ),
                citation="ASAI et al., 2024 (arXiv:2310.11511)",
            ),
        ),
    ),
    ArchitectureProfile(
        architecture=RagArchitecture.CORRECTIVE_RAG,
        display_name="Corrective RAG (CRAG)",
        primary_activities=frozenset({Activity.ANALISE, Activity.VALIDACAO}),
        primary_reason=(
            "Avalia a confiança dos trechos recuperados e, se insuficientes, aciona "
            "busca externa complementar — útil tanto para revisão crítica (Análise) "
            "quanto para verificação de conformidade (Validação)."
        ),
        primary_citation="YAN et al., 2024 (arXiv:2401.15884)",
        signal_rules=(
            SignalRule(
                predicate=lambda ctx: ctx.audit_criticality == Criticality.ALTO,
                reason=(
                    "O classificador de confiança do CRAG evita que recuperações "
                    "insuficientes cheguem à geração sem correção, mitigando "
                    "alucinações quando a auditoria exige alta confiança."
                ),
                citation="YAN et al., 2024 (arXiv:2401.15884)",
            ),
            SignalRule(
                predicate=lambda ctx: ctx.needs_external_lookup is True,
                reason=(
                    "Quando todos os documentos recuperados internamente têm confiança "
                    "abaixo do limiar, o CRAG aciona busca web complementar."
                ),
                citation="YAN et al., 2024 (arXiv:2401.15884)",
            ),
        ),
    ),
    ArchitectureProfile(
        architecture=RagArchitecture.RAPTOR,
        display_name="RAPTOR (Hierarchical RAG)",
        primary_activities=frozenset({Activity.ESPECIFICACAO}),
        primary_reason=(
            "Facilita a leitura e navegação em bases documentais longas, auxiliando a "
            "resumir dados dispersos ao especificar o comportamento do sistema."
        ),
        primary_citation="SARTHI et al., 2024",
        signal_rules=(
            SignalRule(
                predicate=lambda ctx: ctx.data_volume == DataVolume.ALTO,
                reason=(
                    "RAPTOR constrói uma árvore com múltiplos níveis de sumarização "
                    "recursiva, superando a limitação de recuperar apenas blocos curtos "
                    "e contíguos quando o volume documental é alto."
                ),
                citation="SARTHI et al., 2024",
            ),
        ),
    ),
    ArchitectureProfile(
        architecture=RagArchitecture.ADAPTIVE_RAG,
        display_name="Adaptive RAG",
        primary_activities=frozenset({Activity.GERENCIAMENTO_MUDANCAS}),
        primary_reason=(
            "Ajusta dinamicamente a profundidade da busca de acordo com o contexto e a "
            "complexidade das alterações pedidas."
        ),
        primary_citation="JEONG et al., 2024 (arXiv:2403.14403)",
        signal_rules=(
            SignalRule(
                predicate=lambda ctx: ctx.latency_budget == Criticality.BAIXO,
                reason=(
                    "Um classificador dedicado estima a complexidade da consulta e "
                    "escolhe entre não recuperar, recuperar em uma etapa ou em múltiplas "
                    "etapas, mantendo o custo proporcional à necessidade real — "
                    "favorável quando o orçamento de latência é baixo."
                ),
                citation="JEONG et al., 2024 (arXiv:2403.14403)",
            ),
        ),
    ),
    ArchitectureProfile(
        architecture=RagArchitecture.GRAPH_RAG,
        display_name="GraphRAG",
        primary_activities=frozenset({Activity.RASTREABILIDADE}),
        primary_reason=(
            "Representa as conexões e interdependências entre requisitos, regras de "
            "negócio, testes e blocos de código usando grafos."
        ),
        primary_citation="EDGE et al., 2024 (arXiv:2404.16130)",
        signal_rules=(
            # Um único critério da Tabela 2 ("estrutura relacional/interdependências
            # explícitas entre artefatos"): os dois sinais não se somam.
            SignalRule(
                predicate=lambda ctx: (
                    ctx.data_structure == DataStructure.RELACIONAL_GRAFO or ctx.needs_traceability is True
                ),
                reason=(
                    "A tarefa envolve estrutura relacional ou interdependências explícitas "
                    "entre requisitos, regras de negócio e demais artefatos, que o GraphRAG "
                    "explora para preservar relações entre entidades (não deve ser "
                    "confundido com rastreabilidade de citação, ainda uma limitação "
                    "reconhecida pelos próprios autores da arquitetura)."
                ),
                citation="EDGE et al., 2024; PENG et al., 2024",
            ),
        ),
    ),
)


def profile_for(architecture: RagArchitecture) -> ArchitectureProfile:
    for profile in PROFILES:
        if profile.architecture == architecture:
            return profile
    raise KeyError(f"Nenhum perfil cadastrado para {architecture!r}")
