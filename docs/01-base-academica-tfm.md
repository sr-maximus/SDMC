# Base académica del TFM

Este documento resume la base académica usada para mejorar el repositorio SDMC. No reemplaza al TFM original ni reproduce su contenido completo; organiza sus aportes principales para que el repositorio pueda ser entendido, auditado y extendido.

## Tesis de partida

El TFM propone un modelo sistémico dimensional que apoye labores de ciberperfilamiento para actividades de SOCMINT mediante la evaluación de datos públicos visibles en perfiles de redes sociales. La investigación se enfoca en Twitter como entorno de observación y trabaja con una encuesta de percepción visual aplicada a 50 participantes, quienes evaluaron variables asociadas a ocho perfiles.

La idea central es que el ciberperfilamiento puede beneficiarse de la unión de varios sistemas:

- SOCMINT, como proceso de recolección y análisis de información en redes sociales.
- Percepción visual humana, como mecanismo de interpretación de señales públicas.
- DISC, como marco descriptivo de tendencias de comportamiento.
- Comunicación humana, porque la red social funciona como canal de interacción.
- Teoría General de Sistemas, como base integradora entre entidades, atributos, relaciones y entorno.
- Influencia en red, para observar alcance, impacto y propagación percibida.

## Justificación

El TFM identifica que muchas herramientas disponibles se concentran en monitoreo de redes, análisis de sentimiento, alertas o métricas de interacción. Esas capacidades son útiles, pero no siempre integran dimensiones humanas, perceptivas y relacionales dentro de un marco único y explicable.

SDMC busca cubrir ese espacio como una herramienta de apoyo:

- Organiza variables observables en dimensiones.
- Permite comparar perfiles de forma consistente.
- Explicita los pesos usados en el cálculo.
- Evita que el analista dependa de impresiones no documentadas.
- Reconoce que la interpretación humana sigue siendo indispensable.

## Sistemas integrados

### SOCMINT

SOCMINT se entiende como inteligencia basada en redes sociales. En el contexto del TFM, su utilidad está en recolectar, analizar y convertir información pública en conocimiento útil para investigación, prevención o respuesta. SDMC no realiza scraping ni recolección automática; parte de datos ya obtenidos de manera legítima.

### Percepción visual

El TFM utiliza la percepción visual porque muchos datos de un perfil público se evalúan a partir de lo que el observador ve: fotografía, nombre, biografía, publicaciones, retweets, localización declarada, cantidad de seguidores y tipo de contenido. SDMC traduce esa evaluación a valores numéricos normalizados para conservar trazabilidad.

### DISC

DISC se usa como marco descriptivo de tendencias conductuales observables: dominante, influyente, estable y analítico. En SDMC esta lectura no debe presentarse como diagnóstico psicológico. Es una categorización de percepción sobre señales públicas y debe revisarse con cautela.

### Teoría General de Sistemas

La Teoría General de Sistemas permite entender el fenómeno como una interacción entre sistemas abiertos: persona, plataforma, audiencia, contenido, reglas de la red social y proceso analítico. Esta mirada evita reducir el análisis a una métrica aislada.

### Influencia por grados

El TFM considera la regla de los tres grados de influencia para discutir cómo una señal puede extenderse más allá de conexiones inmediatas. La implementación usa un parámetro de decaimiento para representar que la influencia disminuye con la distancia en red.

## Aporte del repositorio

La versión inicial del proyecto era un script demostrativo. La mejora lo transforma en:

- Un paquete Python modular.
- Una CLI reproducible.
- Un ejemplo sintético sin datos personales.
- Pruebas unitarias.
- Documentación académica y operativa.
- Un marco de uso responsable.

## Alcance académico

SDMC debe leerse como punto de partida de investigación aplicada. Su utilidad aumenta cuando los pesos, escalas y variables son validados con muestras más amplias, perfiles diversos y equipos interdisciplinarios que incluyan ciberseguridad, análisis de inteligencia, psicología, derecho y ética de datos.
