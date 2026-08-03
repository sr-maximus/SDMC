# SDMC

**Systemic Dimensional Model of Cyberprofiling**

SDMC es una implementación pública y source-available del Modelo Sistémico Dimensional de Ciberperfilamiento propuesto como apoyo a labores de SOCMINT. El proyecto convierte la base conceptual del TFM *Modelo sistémico dimensional de apoyo a labores de ciberperfilamiento para actividades de SOCMINT* en una herramienta reproducible para calcular, documentar y discutir perfiles dimensionales a partir de datos públicos y evaluaciones controladas.

El repositorio no pretende diagnosticar personalidad ni sustituir criterio profesional. Su objetivo es ofrecer un marco calculable, trazable y responsable para organizar percepciones observables en redes sociales, explicar los supuestos usados y producir reportes que puedan ser revisados por analistas.

## Licencia y uso comercial

SDMC es público para consulta, revisión académica y evaluación no comercial, pero **no es software libre/open source ni permite uso comercial sin pago**. Todo derecho económico queda reservado por Edwin Javier Peñuela Camacho.

Cualquier uso comercial, profesional, institucional, remunerado, de consultoría, SOCMINT/OSINT operativo, capacitación pagada, integración en productos, servicios, reportes para clientes, SaaS, API, dashboard, dataset, modelo, flujo interno de negocio o cualquier beneficio económico directo o indirecto requiere autorización previa por escrito y una licencia comercial pagada.

Consulta la licencia completa en [LICENSE](LICENSE).

## Qué contiene

- Paquete Python `sdmc` con el modelo matemático principal.
- CLI para analizar perfiles desde JSON o desde un ejemplo reproducible.
- Validación de entradas para dimensiones, pesos, centralidad y parámetros.
- Reporte Markdown automatizado para dejar evidencia del análisis.
- Documentación metodológica derivada del TFM.
- Pruebas unitarias para proteger la fórmula y la validación básica.
- Script histórico `Cyberprofile_Tesis_Mejorado.py` conservado como wrapper de compatibilidad.

## Base del modelo

El TFM plantea que el ciberperfilamiento para SOCMINT puede entenderse como un sistema multidimensional donde interactúan:

- SOCMINT: recolección y análisis de información pública de redes sociales.
- Percepción visual humana: evaluación de datos visibles del perfil y publicaciones.
- DISC: marco descriptivo de tendencias conductuales observables.
- Teoría General de Sistemas: integración de sistemas abiertos, relaciones, atributos y entorno.
- Influencia en red: lectura de impacto, centralidad y propagación por grados.

La versión ejecutable modela seis dimensiones:

| Dimensión | Descripción sintética |
| --- | --- |
| D1 | Datos e información visibles del perfil |
| D2 | Emoción percibida al leer contenido público |
| D3 | Rasgos DISC observables como tendencia, no diagnóstico |
| D4 | Relacionamiento o proxémica digital |
| D5 | Percepción de influencia e impacto |
| D6 | Grado de influencia percibida |

La fórmula base calcula el perfil ponderado:

```text
P_u = alpha1*D1 + alpha2*D2 + alpha3*D3 + alpha4*D4 + alpha5*D5 + alpha6*D6
```

Luego ajusta la influencia directa con centralidad de intermediación:

```text
I_u = P_u * (1 + beta*C_b)
```

Y estima la influencia por grados con decaimiento exponencial:

```text
I_u^(n) = I_u * e^(-lambda*n)
```

El impacto total suma la influencia directa y la propagación hasta el grado configurado:

```text
T_u = sum(I_u * e^(-lambda*n)) para n = 0..N
```

## Instalación

Requisitos:

- Python 3.10 o superior.

Uso directo desde el checkout:

```bash
python -m sdmc.cli --sample --format markdown --output report.md
```

Instalación editable para desarrollo:

```bash
python -m pip install -e .
sdmc --sample --format json
```

## Uso con datos propios

Crea un archivo JSON con dimensiones normalizadas entre `0` y `1`:

```json
{
  "profile_id": "perfil_demo",
  "dimensions": {
    "D1": 0.8,
    "D2": 0.6,
    "D3": 0.7,
    "D4": 0.5,
    "D5": 0.9,
    "D6": 0.4
  },
  "centrality_betweenness": 0.7,
  "parameters": {
    "alpha1": 0.25,
    "alpha2": 0.2,
    "alpha3": 0.15,
    "alpha4": 0.15,
    "alpha5": 0.15,
    "alpha6": 0.1,
    "beta": 0.6,
    "lambda_decay": 0.25,
    "max_degree": 3
  }
}
```

Ejecuta:

```bash
python -m sdmc.cli --input examples/sample_profile.json --format markdown --output report.md
```

## Uso responsable

SDMC debe utilizarse sólo sobre información pública, con finalidad legítima, minimización de datos y revisión humana. Los resultados deben tratarse como indicadores de análisis, no como veredictos automáticos sobre una persona. El propio TFM identifica limitaciones de muestra, necesidad de más perfiles, participación interdisciplinaria y validación futura.

Consulta:

- [Base académica del TFM](docs/01-base-academica-tfm.md)
- [Modelo matemático y dimensiones](docs/02-modelo-sistemico-dimensional.md)
- [Metodología operativa](docs/03-metodologia-operativa.md)
- [Ética, privacidad y uso responsable](docs/04-etica-privacidad-y-uso-responsable.md)
- [Validación, limitaciones y trabajos futuros](docs/05-validacion-limitaciones-y-trabajos-futuros.md)
- [Licencia y uso comercial](docs/06-licencia-y-uso-comercial.md)

## Pruebas

```bash
python -m unittest discover -s tests
```

## Estado

Este repositorio es una base técnica y documental para investigación aplicada. No incluye el TFM completo ni datos personales de los perfiles evaluados. La documentación pública resume el fundamento, las fórmulas, los límites y los criterios de uso responsable para facilitar revisión, extensión y auditoría.

La disponibilidad pública del repositorio no autoriza explotación comercial sin licencia pagada del autor.
