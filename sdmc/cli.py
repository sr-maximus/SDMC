"""Command-line interface for SDMC."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from .model import DimensionScores, ModelParameters, ProfileAssessment, ValidationError, analyze_profile
from .reporting import render_markdown_report
from .sample_data import sample_assessment


def _assessment_from_json(data: dict[str, Any]) -> ProfileAssessment:
    dimensions_data = data.get("dimensions", data)
    dimensions = DimensionScores.from_mapping(dimensions_data)

    centrality = data.get("centrality_betweenness", data.get("C_b", data.get("centrality")))
    if centrality is None:
        raise ValidationError("Falta centrality_betweenness o C_b.")

    parameters = ModelParameters.from_mapping(data.get("parameters", data))
    return ProfileAssessment(
        profile_id=data.get("profile_id", "perfil"),
        dimensions=dimensions,
        centrality_betweenness=centrality,
        parameters=parameters,
        notes=data.get("notes", ""),
    )


def load_assessment(path: Path) -> ProfileAssessment:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValidationError("El archivo de entrada debe contener un objeto JSON.")
    return _assessment_from_json(data)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Calcula perfiles con el Modelo Sistémico Dimensional de Ciberperfilamiento.")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--input", type=Path, help="Ruta a un archivo JSON con dimensiones y parámetros.")
    source.add_argument("--sample", action="store_true", help="Usa un perfil sintético de ejemplo.")
    parser.add_argument("--format", choices=("json", "markdown"), default="json", help="Formato de salida.")
    parser.add_argument("--output", type=Path, help="Ruta de salida. Si se omite, escribe en stdout.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        assessment = sample_assessment() if args.sample else load_assessment(args.input)
        result = analyze_profile(assessment)
        if args.format == "json":
            payload = json.dumps(result.as_dict(), ensure_ascii=False, indent=2) + "\n"
        else:
            payload = render_markdown_report(assessment, result)
    except (OSError, json.JSONDecodeError, ValidationError) as exc:
        print(f"sdmc: {exc}", file=sys.stderr)
        return 2

    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
