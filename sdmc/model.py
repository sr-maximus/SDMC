"""Core calculation engine for SDMC.

The model keeps the mathematics intentionally small and auditable. It does not
collect data from social networks; callers must provide already-scored,
legitimate, reviewable inputs.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from math import exp, isfinite
from typing import Any, Mapping

DIMENSION_NAMES = ("D1", "D2", "D3", "D4", "D5", "D6")

DIMENSION_DESCRIPTIONS = {
    "D1": "Percepción visual de datos e información pública expuesta por el perfil.",
    "D2": "Emoción percibida al leer contenido público.",
    "D3": "Tendencias DISC observables como lectura descriptiva, no diagnóstica.",
    "D4": "Relacionamiento o proxémica digital percibida.",
    "D5": "Percepción de influencia e impacto.",
    "D6": "Grado de influencia percibida.",
}

DIMENSION_VARIABLES = {
    "D1": [
        "fotografía",
        "nombre de usuario",
        "género percibido",
        "seguidores",
        "seguidos",
        "biografía",
        "localización",
        "tweets",
        "retweets",
    ],
    "D2": ["positivo", "negativo", "activo", "pasivo"],
    "D3": ["dominante", "influyente", "analítico", "estable"],
    "D4": ["íntima", "personal", "social", "pública"],
    "D5": ["influencia", "impacto"],
    "D6": ["primer grado", "segundo grado", "tercer grado"],
}

DEFAULT_WEIGHTS = (0.25, 0.20, 0.15, 0.15, 0.15, 0.10)


class ValidationError(ValueError):
    """Raised when an SDMC input is outside the accepted model contract."""


def _require_number(name: str, value: Any) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValidationError(f"{name} debe ser numérico.")
    numeric = float(value)
    if not isfinite(numeric):
        raise ValidationError(f"{name} debe ser finito.")
    return numeric


def _require_unit_interval(name: str, value: Any) -> float:
    numeric = _require_number(name, value)
    if numeric < 0 or numeric > 1:
        raise ValidationError(f"{name} debe estar entre 0 y 1.")
    return numeric


@dataclass(frozen=True)
class DimensionScores:
    """Normalized scores for the six SDMC dimensions."""

    d1: float
    d2: float
    d3: float
    d4: float
    d5: float
    d6: float

    def __post_init__(self) -> None:
        for name, value in self.as_dict().items():
            _require_unit_interval(name, value)

    @classmethod
    def from_mapping(cls, data: Mapping[str, Any]) -> "DimensionScores":
        values = []
        for name in DIMENSION_NAMES:
            value = data.get(name, data.get(name.lower()))
            if value is None:
                raise ValidationError(f"Falta la dimensión {name}.")
            values.append(value)
        return cls(*values)

    def as_dict(self) -> dict[str, float]:
        return {
            "D1": float(self.d1),
            "D2": float(self.d2),
            "D3": float(self.d3),
            "D4": float(self.d4),
            "D5": float(self.d5),
            "D6": float(self.d6),
        }


@dataclass(frozen=True)
class ModelParameters:
    """Weights and propagation controls used by the model."""

    weights: tuple[float, float, float, float, float, float] = DEFAULT_WEIGHTS
    beta: float = 0.6
    lambda_decay: float = 0.25
    max_degree: int = 3

    def __post_init__(self) -> None:
        if len(self.weights) != len(DIMENSION_NAMES):
            raise ValidationError("weights debe contener seis valores.")

        normalized_weights = tuple(_require_number(f"alpha{i + 1}", value) for i, value in enumerate(self.weights))
        if any(value < 0 for value in normalized_weights):
            raise ValidationError("Los pesos alpha no pueden ser negativos.")
        if sum(normalized_weights) <= 0:
            raise ValidationError("La suma de pesos alpha debe ser mayor que cero.")

        beta = _require_number("beta", self.beta)
        if beta < 0:
            raise ValidationError("beta no puede ser negativo.")

        lambda_decay = _require_number("lambda_decay", self.lambda_decay)
        if lambda_decay < 0:
            raise ValidationError("lambda_decay no puede ser negativo.")

        if isinstance(self.max_degree, bool) or not isinstance(self.max_degree, int):
            raise ValidationError("max_degree debe ser entero.")
        if self.max_degree < 1:
            raise ValidationError("max_degree debe ser mayor o igual a 1.")

        object.__setattr__(self, "weights", normalized_weights)
        object.__setattr__(self, "beta", beta)
        object.__setattr__(self, "lambda_decay", lambda_decay)

    @classmethod
    def from_mapping(cls, data: Mapping[str, Any] | None) -> "ModelParameters":
        if not data:
            return cls()

        if "weights" in data:
            weights_value = data["weights"]
            if isinstance(weights_value, Mapping):
                weights = tuple(weights_value[name] for name in DIMENSION_NAMES)
            else:
                weights = tuple(weights_value)
        else:
            weights = tuple(data.get(f"alpha{i}", DEFAULT_WEIGHTS[i - 1]) for i in range(1, 7))

        lambda_decay = data.get("lambda_decay", data.get("lambda_param", cls.lambda_decay))
        return cls(
            weights=weights,  # type: ignore[arg-type]
            beta=data.get("beta", cls.beta),
            lambda_decay=lambda_decay,
            max_degree=data.get("max_degree", cls.max_degree),
        )

    def weight_map(self) -> dict[str, float]:
        return dict(zip(DIMENSION_NAMES, self.weights))


@dataclass(frozen=True)
class ProfileAssessment:
    """A single profile assessment ready for SDMC calculation."""

    profile_id: str
    dimensions: DimensionScores
    centrality_betweenness: float
    parameters: ModelParameters = field(default_factory=ModelParameters)
    notes: str = ""

    def __post_init__(self) -> None:
        if not self.profile_id.strip():
            raise ValidationError("profile_id no puede estar vacío.")
        _require_unit_interval("centrality_betweenness", self.centrality_betweenness)


@dataclass(frozen=True)
class ProfileResult:
    """Calculated SDMC values for a profile."""

    profile_id: str
    base_profile: float
    direct_influence: float
    degree_influences: dict[int, float]
    total_impact: float
    dominant_dimension: str
    parameters: ModelParameters

    def as_dict(self) -> dict[str, Any]:
        return {
            "profile_id": self.profile_id,
            "base_profile": self.base_profile,
            "direct_influence": self.direct_influence,
            "degree_influences": {str(key): value for key, value in self.degree_influences.items()},
            "total_impact": self.total_impact,
            "dominant_dimension": self.dominant_dimension,
            "parameters": {
                "weights": self.parameters.weight_map(),
                "beta": self.parameters.beta,
                "lambda_decay": self.parameters.lambda_decay,
                "max_degree": self.parameters.max_degree,
            },
        }


class CyberProfilingModel:
    """Auditable implementation of the Systemic Dimensional Model."""

    def __init__(self, parameters: ModelParameters | None = None) -> None:
        self.parameters = parameters or ModelParameters()

    def calculate(self, assessment: ProfileAssessment) -> ProfileResult:
        params = assessment.parameters
        dimensions = assessment.dimensions.as_dict()
        weights = params.weight_map()

        base_profile = sum(dimensions[name] * weights[name] for name in DIMENSION_NAMES)
        direct_influence = base_profile * (1 + params.beta * assessment.centrality_betweenness)
        degree_influences = {
            degree: direct_influence * exp(-params.lambda_decay * degree)
            for degree in range(1, params.max_degree + 1)
        }
        total_impact = direct_influence + sum(degree_influences.values())
        dominant_dimension = max(DIMENSION_NAMES, key=lambda name: dimensions[name])

        return ProfileResult(
            profile_id=assessment.profile_id,
            base_profile=base_profile,
            direct_influence=direct_influence,
            degree_influences=degree_influences,
            total_impact=total_impact,
            dominant_dimension=dominant_dimension,
            parameters=params,
        )


def analyze_profile(assessment: ProfileAssessment) -> ProfileResult:
    """Calculate a profile result with the parameters embedded in the assessment."""

    return CyberProfilingModel(assessment.parameters).calculate(assessment)


def interpret_score(value: float) -> str:
    """Return a conservative qualitative label for a normalized score."""

    numeric = _require_number("value", value)
    if numeric < 0.34:
        return "bajo"
    if numeric < 0.67:
        return "medio"
    return "alto"
