# Resumen ejecutivo

SDMC, *Systemic Dimensional Model of Cyberprofiling*, es una propuesta técnica para apoyar análisis SOCMINT a partir de información pública, percepción visual y variables dimensionales inspiradas en DISC, comunicación humana, influencia en redes y Teoría General de Sistemas.

El proyecto nace del TFM *Modelo sistémico dimensional de apoyo a labores de ciberperfilamiento para actividades de SOCMINT*, desarrollado por Edwin Javier Peñuela Camacho. La tesis propone integrar varios sistemas de lectura: la persona como sistema abierto, la red social como canal de comunicación, SOCMINT como proceso de inteligencia, DISC como marco de tendencias conductuales y la percepción visual como mecanismo humano de evaluación de datos visibles.

## Problema que atiende

Las redes sociales públicas exponen señales que pueden ser relevantes para estudios reputacionales, diligencias de seguridad, prevención de riesgos y ciberpatrullaje. Sin embargo, muchas herramientas se limitan a sentimiento positivo/negativo, monitoreo de menciones o métricas aisladas de interacción. El TFM plantea la necesidad de un modelo que organice esas señales en dimensiones comparables, con base teórica y con un proceso explicable.

SDMC convierte esa necesidad en una base computable:

- Define seis dimensiones normalizadas.
- Permite ponderar cada dimensión.
- Integra una centralidad de intermediación como aproximación a posición en red.
- Modela influencia por grados con decaimiento exponencial.
- Produce salidas auditables en JSON o Markdown.

## Resultado esperado

El resultado no es un diagnóstico de personalidad ni una sentencia automática. Es una lectura estructurada que permite decir: con estos datos, estos pesos y estos supuestos, el perfil obtiene determinado valor base, determinada influencia directa y determinada propagación estimada.

## Principios públicos del repositorio

- Reproducibilidad: todo cálculo debe poder reconstruirse desde sus entradas.
- Explicabilidad: fórmulas, pesos y dimensiones deben estar documentados.
- Minimización: no se publican datos personales ni el TFM completo.
- Prudencia: el modelo genera indicadores, no conclusiones definitivas.
- Revisión humana: ningún resultado debe usarse sin contraste analítico.

## Mapa documental

- [Base académica del TFM](01-base-academica-tfm.md)
- [Modelo sistémico dimensional](02-modelo-sistemico-dimensional.md)
- [Metodología operativa](03-metodologia-operativa.md)
- [Ética, privacidad y uso responsable](04-etica-privacidad-y-uso-responsable.md)
- [Validación, limitaciones y trabajos futuros](05-validacion-limitaciones-y-trabajos-futuros.md)
- [Licencia y uso comercial](06-licencia-y-uso-comercial.md)
