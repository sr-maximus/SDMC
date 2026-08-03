# Ética, privacidad y uso responsable

SDMC trabaja en un área sensible: análisis de personas o perfiles en redes sociales. Por eso el repositorio debe ser técnicamente útil y, al mismo tiempo, prudente en sus límites.

## Principio de autorización

Usar SDMC sólo cuando exista base legítima:

- Investigación autorizada.
- Diligencia reputacional proporcional.
- Análisis defensivo o preventivo.
- Docencia o investigación con datos sintéticos.
- Reproducción académica sin datos personales reales.

No usarlo para acoso, vigilancia invasiva, discriminación, doxxing o toma de decisiones automatizadas sobre personas.

## Principio de minimización

Recolectar lo mínimo necesario:

- Preferir IDs internos antes que nombres reales.
- Evitar publicar capturas de perfiles.
- Evitar almacenar datos sensibles.
- Eliminar información que no sea necesaria para el objetivo.
- Mantener evidencia privada fuera del repositorio público.

## Principio de explicabilidad

Todo resultado debería responder:

- Qué datos se evaluaron.
- Quién los puntuó.
- Qué escala se usó.
- Qué pesos se aplicaron.
- Qué parámetros influyeron en el cálculo.
- Qué limitaciones afectan la lectura.

Si una conclusión no puede explicarse, no debe presentarse como resultado robusto.

## Principio de no diagnóstico

El uso de DISC en SDMC es descriptivo. No acredita rasgos clínicos, intenciones, peligrosidad ni personalidad real. La documentación debe evitar frases que conviertan una percepción en una conclusión absoluta.

Formulación preferida:

```text
El perfil presenta una puntuación alta en D3 bajo los criterios observados.
```

Formulación a evitar:

```text
La persona es dominante o peligrosa.
```

## Principio de revisión humana

El modelo no debe ejecutar sanciones, rechazos, bloqueos o decisiones de alto impacto. Sirve para orientar revisión humana, abrir preguntas y organizar evidencia.

## Riesgos principales

| Riesgo | Mitigación |
| --- | --- |
| Falso positivo | Revisión cruzada, contexto, evidencia adicional |
| Sesgo del evaluador | Escalas claras, múltiples evaluadores, trazabilidad |
| Sobreinterpretación | Separar dato, cálculo e inferencia |
| Datos privados | Usar sólo fuentes públicas y autorizadas |
| Discriminación | No usar atributos protegidos para decisiones adversas |
| Desactualización | Registrar fecha y versión de datos |

## Recomendación para publicaciones

El repositorio público debe contener metodología, fórmulas, ejemplos sintéticos y límites. No debe contener:

- El TFM completo si no se decide publicarlo expresamente.
- Datos personales de perfiles estudiados.
- Capturas de publicaciones reales.
- Credenciales o llaves API.
- Afirmaciones de certificación, aval externo o capacidad predictiva no validada.

## Lenguaje responsable

Usar términos como:

- "apoyo analítico"
- "indicador"
- "percepción declarada"
- "señal observable"
- "resultado sujeto a revisión"

Evitar términos como:

- "detección definitiva"
- "diagnóstico automático"
- "perfil psicológico real"
- "predicción garantizada"
- "clasificación final"
