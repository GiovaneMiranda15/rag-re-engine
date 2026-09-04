"""Motor de recomendação: pontua as arquiteturas RAG para um TaskContext e ranqueia."""

from __future__ import annotations

from rag_re_advisor.knowledge_base import PRIMARY_ACTIVITY_WEIGHT, PROFILES, ArchitectureProfile
from rag_re_advisor.models import Recommendation, ScoredArchitecture, TaskContext


def recommend(context: TaskContext) -> Recommendation:
    scored = [_score(profile, context) for profile in PROFILES]
    scored.sort(key=lambda item: (-item.score, item.architecture.value))
    return Recommendation(context=context, top=scored[0], alternatives=tuple(scored[1:]))


def _score(profile: ArchitectureProfile, context: TaskContext) -> ScoredArchitecture:
    score = 0.0
    reasons: list[str] = []

    if context.activity in profile.primary_activities:
        score += PRIMARY_ACTIVITY_WEIGHT
        reasons.append(f"{profile.primary_reason} ({profile.primary_citation})")

    for rule in profile.signal_rules:
        if rule.predicate(context):
            score += rule.weight
            reasons.append(f"{rule.reason} ({rule.citation})")

    return ScoredArchitecture(architecture=profile.architecture, score=score, reasons=tuple(reasons))
