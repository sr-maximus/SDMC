"""Compatibilidad con el script histórico del proyecto SDMC.

La lógica principal vive ahora en el paquete `sdmc`, que permite validación,
pruebas y uso por CLI. Este archivo se conserva para personas que ya ejecutaban
`python Cyberprofile_Tesis_Mejorado.py`.
"""

from __future__ import annotations

from math import exp

from sdmc.model import DimensionScores, ModelParameters, ProfileAssessment, analyze_profile
from sdmc.reporting import render_markdown_report
from sdmc.sample_data import sample_assessment


class CiberPerfilado:
    """Interfaz compatible con la primera version del modelo."""

    def __init__(
        self,
        D1,
        D2,
        D3,
        D4,
        D5,
        D6,
        alpha1=0.2,
        alpha2=0.2,
        alpha3=0.2,
        alpha4=0.2,
        alpha5=0.1,
        alpha6=0.1,
        beta=0.5,
        lambda_param=0.3,
    ):
        self.dimensions = DimensionScores(D1, D2, D3, D4, D5, D6)
        self.parameters = ModelParameters(
            weights=(alpha1, alpha2, alpha3, alpha4, alpha5, alpha6),
            beta=beta,
            lambda_decay=lambda_param,
            max_degree=3,
        )

    def calcular_perfil_usuario(self):
        values = self.dimensions.as_dict()
        weights = self.parameters.weight_map()
        return sum(values[name] * weights[name] for name in values)

    def calcular_influencia(self, C_b):
        return self.calcular_perfil_usuario() * (1 + self.parameters.beta * C_b)

    def calcular_influencia_multigrado(self, C_b, grado):
        return self.calcular_influencia(C_b) * exp(-self.parameters.lambda_decay * grado)

    def calcular_impacto_total(self, C_b):
        influencia = self.calcular_influencia(C_b)
        return influencia + sum(
            influencia * exp(-self.parameters.lambda_decay * grado)
            for grado in range(1, self.parameters.max_degree + 1)
        )


def obtener_datos_api():
    """Devuelve datos sintéticos locales.

    La version inicial intentaba contactar una API ficticia. Para que la demo
    sea reproducible, el wrapper usa el mismo ejemplo que la CLI.
    """

    sample = sample_assessment()
    data = sample.dimensions.as_dict()
    data["C_b"] = sample.centrality_betweenness
    return data


def exportar_a_markdown(assessment: ProfileAssessment, output_path="Resultados_CiberPerfilado.md"):
    result = analyze_profile(assessment)
    report = render_markdown_report(assessment, result)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(report)
    print(f"Documento '{output_path}' creado exitosamente.")


def main():
    assessment = sample_assessment()
    result = analyze_profile(assessment)
    exportar_a_markdown(assessment)

    print(f"Perfil de usuario (P_u): {result.base_profile:.4f}")
    print(f"Influencia del usuario (I_u): {result.direct_influence:.4f}")
    print(f"Influencia de segundo grado (I_u^(2)): {result.degree_influences[2]:.4f}")
    print(f"Impacto total (T_u): {result.total_impact:.4f}")


if __name__ == "__main__":
    main()
