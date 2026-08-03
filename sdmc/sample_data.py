"""Sample SDMC input inspired by the public TFM methodology."""

from __future__ import annotations

from .model import DimensionScores, ModelParameters, ProfileAssessment


def sample_assessment() -> ProfileAssessment:
    """Return a deterministic demo profile for CLI and tests."""

    return ProfileAssessment(
        profile_id="perfil_demo_tfm",
        dimensions=DimensionScores(
            d1=0.80,
            d2=0.60,
            d3=0.70,
            d4=0.50,
            d5=0.90,
            d6=0.40,
        ),
        centrality_betweenness=0.70,
        parameters=ModelParameters(
            weights=(0.25, 0.20, 0.15, 0.15, 0.15, 0.10),
            beta=0.60,
            lambda_decay=0.25,
            max_degree=3,
        ),
        notes="Datos sintéticos para demostrar el cálculo; no corresponden a una persona real.",
    )
