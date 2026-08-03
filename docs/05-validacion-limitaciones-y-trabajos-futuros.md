# Validación, limitaciones y trabajos futuros

El TFM identifica que el modelo es prometedor como punto de partida, pero necesita más validación antes de presentarse como herramienta operativa madura. Esta página convierte esas conclusiones en una agenda técnica para SDMC.

## Validación actual

La investigación base utilizó:

- Enfoque descriptivo mixto.
- Encuesta de percepción visual.
- Muestra de 50 participantes.
- Ocho perfiles públicos agrupados por tipo.
- Dimensiones asociadas a datos visibles, emociones, DISC, proxémica, impacto e influencia.
- Análisis con medidas de tendencia central: media, moda y mediana.
- Escalamiento multidimensional para observar proximidad entre dimensiones.

La implementación actual valida sólo el contrato computacional: rangos, pesos, parámetros y consistencia de fórmulas.

## Limitaciónes

| Limitación | Impacto |
| --- | --- |
| Muestra reducida | Los resultados no generalizan por sí solos |
| Perfiles limitados | Puede haber sesgos por tipo de cuenta o contexto |
| Evaluación perceptiva | Depende de observadores, cultura, idioma y momento |
| Pesos iniciales | Requieren calibración empírica |
| DISC como marco descriptivo | No debe usarse como diagnóstico psicológico |
| Centralidad simplificada | Debe calcularse con grafo real o declararse como aproximación |
| Plataforma cambiante | Las redes sociales modifican reglas, señales y visibilidad |

## Validaciones recomendadas

### 1. Confiabilidad entre evaluadores

Aplicar el instrumento a varios analistas y medir consistencia entre puntuaciones. Esto ayuda a saber si las dimensiones están redactadas con suficiente claridad.

### 2. Sensibilidad de pesos

Ejecutar escenarios donde cambien `alpha1..alpha6` para identificar si el modelo es demasiado dependiente de una dimensión.

### 3. Comparación de grupos

Evaluar si los resultados distinguen grupos sin depender de atributos sensibles o variables irrelevantes.

### 4. Validación temporal

Repetir evaluaciones en distintos momentos para saber si el resultado cambia por coyunturas temporales.

### 5. Revisión interdisciplinaria

Incorporar profesionales de ciberseguridad, análisis de inteligencia, psicología, derecho y ética de datos.

## Trabajos futuros

El TFM propone incorporar tecnología para procesamiento, análisis y generación de reportes. Para el repositorio, esto se traduce en:

- Importadores para CSV y hojas de cálculo.
- Reportes comparativos entre perfiles.
- Gráficas de radar y mapas de calor.
- Cálculo real de centralidad con librerías de grafos.
- Plantillas de encuesta para codificar dimensiones.
- Validación estadística de pesos.
- Versionado de configuraciones de análisis.
- Integración opcional con notebooks.
- Exportación a DOCX/PDF para informes profesionales.
- Guía de calibración por dominio de uso.

## Roadmap técnico sugerido

| Prioridad | Mejora | Resultado esperado |
| --- | --- | --- |
| Alta | CSV batch | Analizar múltiples perfiles en una ejecución |
| Alta | Gráficas | Visualizar dimensiones y propagación |
| Alta | Config YAML | Reutilizar pesos y parámetros por caso |
| Media | NetworkX opcional | Calcular centralidad desde grafos reales |
| Media | Plantillas DOCX | Generar informes ejecutivos |
| Media | Evaluación interjueces | Medir confiabilidad de puntuaciones |
| Baja | Dashboard | Explorar casos con interfaz visual |

## Criterio de madurez

SDMC puede considerarse más maduro cuando:

- Sus pesos estén justificados con datos.
- Existan pruebas automatizadas y casos de validación.
- El modelo pueda explicar sensibilidad ante cambios.
- Los reportes separen evidencia, cálculo e inferencia.
- La documentación de uso responsable sea parte del flujo, no un anexo decorativo.
