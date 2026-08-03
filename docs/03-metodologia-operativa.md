# Metodología operativa

Esta metodología adapta el enfoque del TFM a un flujo práctico para analistas. El objetivo es que cada resultado sea explicable, revisable y proporcional.

## 1. Definir el caso

Antes de puntuar un perfil, documentar:

- Finalidad legítima del análisis.
- Alcance autorizado.
- Plataforma o fuente consultada.
- Fecha y hora de observación.
- Identificador interno del caso.
- Restricciones legales o contractuales aplicables.

SDMC no debe usarse para exploración indiscriminada de personas. Debe existir una razón clara y proporcionada.

## 2. Recolectar sólo datos permitidos

El TFM trabaja con datos e información visible en perfiles públicos. En un flujo operativo, esto se traduce en:

- No usar credenciales ajenas.
- No evadir controles de privacidad.
- No recolectar mensajes privados.
- No publicar capturas con datos personales en el repositorio.
- Separar evidencia cruda de resultados derivados.

## 3. Codificar variables

Cada dimensión debe puntuar entre `0` y `1`. Si el origen usa escala `1..5`, puede normalizarse así:

```text
valor_normalizado = (valor_original - 1) / 4
```

Ejemplo:

| Escala original | Normalizado |
| ---: | ---: |
| 1 | 0.00 |
| 2 | 0.25 |
| 3 | 0.50 |
| 4 | 0.75 |
| 5 | 1.00 |

## 4. Calcular con pesos documentados

Los pesos por defecto del proyecto son:

| Peso | Dimensión | Valor |
| --- | --- | ---: |
| alpha1 | D1 | 0.25 |
| alpha2 | D2 | 0.20 |
| alpha3 | D3 | 0.15 |
| alpha4 | D4 | 0.15 |
| alpha5 | D5 | 0.15 |
| alpha6 | D6 | 0.10 |

Estos pesos son una configuración inicial de trabajo. No deben presentarse como calibración universal.

## 5. Generar reporte

Ejemplo:

```bash
python -m sdmc.cli --input examples/sample_profile.json --format markdown --output report.md
```

El reporte debe conservar:

- Entradas.
- Pesos.
- Parámetros.
- Resultados.
- Notas del analista.
- Controles y limitaciones.

## 6. Revisar interpretaciones

Una lectura responsable distingue:

- Evidencia: dato observado o puntuación declarada.
- Cálculo: salida derivada por fórmula.
- Inferencia: interpretación del analista.
- Decisión: acción posterior tomada por una persona autorizada.

No mezclar estos niveles evita exagerar el alcance del modelo.

## 7. Contrastar falsos positivos

Antes de usar el resultado en un contexto sensible:

- Revisar si el perfil es parodia, fan, automatizado o suplantado.
- Confirmar que las variables no dependan de una sola publicación.
- Considerar contexto cultural, ironía, idioma y actualidad.
- Pedir revisión de otro analista cuando el caso tenga impacto real.
- Registrar dudas y supuestos.

## 8. Mejorar el modelo con evidencia

Las mejoras futuras deben priorizar:

- Muestras más amplias.
- Perfiles más diversos.
- Validación estadística de pesos.
- Comparación entre evaluadores.
- Integración con herramientas de análisis de red.
- Participación interdisciplinaria.
