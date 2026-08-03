import math
import unittest

from sdmc.model import (
    DimensionScores,
    ModelParameters,
    ProfileAssessment,
    ValidationError,
    analyze_profile,
)
from sdmc.reporting import render_markdown_report
from sdmc.sample_data import sample_assessment


class ModelTest(unittest.TestCase):
    def test_sample_calculation_matches_formula(self):
        assessment = sample_assessment()
        result = analyze_profile(assessment)

        expected_base = 0.25 * 0.8 + 0.20 * 0.6 + 0.15 * 0.7 + 0.15 * 0.5 + 0.15 * 0.9 + 0.10 * 0.4
        expected_direct = expected_base * (1 + 0.60 * 0.70)
        expected_total = expected_direct + sum(expected_direct * math.exp(-0.25 * degree) for degree in range(1, 4))

        self.assertAlmostEqual(result.base_profile, expected_base)
        self.assertAlmostEqual(result.direct_influence, expected_direct)
        self.assertAlmostEqual(result.degree_influences[2], expected_direct * math.exp(-0.50))
        self.assertAlmostEqual(result.total_impact, expected_total)

    def test_dimensions_must_be_normalized(self):
        with self.assertRaises(ValidationError):
            DimensionScores(1.1, 0.2, 0.3, 0.4, 0.5, 0.6)

    def test_parameters_reject_negative_lambda(self):
        with self.assertRaises(ValidationError):
            ModelParameters(lambda_decay=-0.1)

    def test_report_contains_audit_sections(self):
        assessment = sample_assessment()
        report = render_markdown_report(assessment, analyze_profile(assessment))

        self.assertIn("## Entradas", report)
        self.assertIn("## Resultados", report)
        self.assertIn("## Controles recomendados", report)


if __name__ == "__main__":
    unittest.main()
