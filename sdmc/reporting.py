"""Report rendering helpers for SDMC."""

from __future__ import annotations

from .model import DIMENSION_DESCRIPTIONS, ProfileAssessment, ProfileResult, interpret_score


def render_markdown_report(assessment: ProfileAssessment, result: ProfileResult) -> str:
    """Render a compact Markdown report suitable for audit trails."""

    dimensions = assessment.dimensions.as_dict()
    weights = assessment.parameters.weight_map()

    lines = [
        f"# Reporte SDMC - {assessment.profile_id}",
        "",
        "## Alcance",
        "",
        "Este reporte resume un cálculo del Modelo Sistémico Dimensional de Ciberperfilamiento. Debe ser interpretado como apoyo analítico y no como diagnóstico psicológico, decisión automatizada o atribución concluyente.",
        "",
        "## Entradas",
        "",
        "| Dimensión | Valor | Peso alpha | Lectura | Descripción |",
        "| --- | ---: | ---: | --- | --- |",
    ]

    for name, value in dimensions.items():
        lines.append(
            f"| {name} | {value:.4f} | {weights[name]:.4f} | {interpret_score(value)} | {DIMENSION_DESCRIPTIONS[name]} |"
        )

    lines.extend(
        [
            "",
            f"- Centralidad de intermediación (C_b): `{assessment.centrality_betweenness:.4f}`.",
            f"- Beta: `{assessment.parameters.beta:.4f}`.",
            f"- Lambda de decaimiento: `{assessment.parameters.lambda_decay:.4f}`.",
            f"- Grado máximo de propagación: `{assessment.parameters.max_degree}`.",
            "",
            "## Resultados",
            "",
            f"- Perfil base ponderado (P_u): `{result.base_profile:.4f}`.",
            f"- Influencia directa (I_u): `{result.direct_influence:.4f}`.",
            f"- Impacto total (T_u): `{result.total_impact:.4f}`.",
            f"- Dimensión dominante por valor observado: `{result.dominant_dimension}`.",
            "",
            "| Grado | Influencia estimada |",
            "| ---: | ---: |",
        ]
    )

    for degree, value in result.degree_influences.items():
        lines.append(f"| {degree} | {value:.4f} |")

    lines.extend(
        [
            "",
            "## Interpretación prudente",
            "",
            f"El perfil base se ubica en nivel `{interpret_score(result.base_profile)}` según una escala descriptiva simple. La influencia directa aumenta o disminuye en función de la centralidad indicada, y la propagación se atenúa por grado según lambda.",
            "",
            "La salida no identifica intenciones, culpabilidad ni rasgos clínicos. Solo organiza variables observables y puntuaciones declaradas para facilitar revisión humana.",
            "",
            "## Controles recomendados",
            "",
            "- Documentar fuente, fecha y legitimidad de los datos usados.",
            "- Mantener evidencia separada de inferencias.",
            "- Revisar falsos positivos antes de tomar decisiones.",
            "- Evitar datos privados, sensibles o no autorizados.",
            "- Recalibrar pesos con muestras más amplias antes de uso operativo.",
        ]
    )

    if assessment.notes:
        lines.extend(["", "## Notas del analista", "", assessment.notes.strip()])

    return "\n".join(lines) + "\n"
