# Modelo sistémico dimensional

Este documento describe la estructura matemática y conceptual implementada en el paquete `sdmc`.

## Entradas

El modelo recibe seis dimensiones normalizadas entre `0` y `1`. Normalizar permite comparar perfiles aunque los datos originales provengan de escalas distintas, encuestas o codificaciones internas.

| Dimensión | Nombre operativo | Variables derivadas del TFM |
| --- | --- | --- |
| D1 | Datos visibles del perfil | Fotografia, nombre de usuario, género percibido, seguidores, seguidos, biografía, localización, tweets, retweets |
| D2 | Emoción percibida | Positivo, negativo, activo, pasivo |
| D3 | Tendencia DISC observable | Dominante, influyente, analítico, estable |
| D4 | Proxémica digital | Íntima, personal, social, pública |
| D5 | Influencia e impacto | Influencia, impacto |
| D6 | Grado de influencia | Primer, segundo o tercer grado percibido |

La implementación también recibe:

- `C_b`: centralidad de intermediación o valor equivalente normalizado entre `0` y `1`.
- `alpha1..alpha6`: pesos de cada dimensión.
- `beta`: sensibilidad de la influencia ante la centralidad.
- `lambda_decay`: decaimiento por distancia en red.
- `max_degree`: grado máximo de propagación incluido en el impacto total.

## Perfil base

El perfil base ponderado se calcula como:

```text
P_u = alpha1*D1 + alpha2*D2 + alpha3*D3 + alpha4*D4 + alpha5*D5 + alpha6*D6
```

Interpretación:

- Un valor mayor indica que, bajo los pesos definidos, el perfil concentra más señales dimensionales.
- El resultado depende directamente de los pesos, por lo que estos deben documentarse.
- Si los pesos cambian, dos reportes sólo son comparables cuando explicitan su configuración.

## Influencia directa

La influencia directa incorpora centralidad:

```text
I_u = P_u * (1 + beta*C_b)
```

La centralidad representa la posición del perfil dentro de la red o una aproximación manual validada. `beta` controla cuánto pesa esa posición sobre el perfil base.

## Influencia multigrado

La influencia estimada para el grado `n` se calcula con decaimiento exponencial:

```text
I_u^(n) = I_u * e^(-lambda*n)
```

Esto refleja una intuición del TFM: la influencia puede extenderse más allá del contacto inmediato, pero pierde fuerza con la distancia.

## Impacto total

El impacto total suma influencia directa y propagación:

```text
T_u = I_u + I_u^(1) + I_u^(2) + ... + I_u^(N)
```

Donde `N` es `max_degree`. Por defecto se usa `3`, en coherencia con la discusión de influencia por grados presente en el TFM.

## Contrato de validación

El paquete aplica controles mínimos:

- Las dimensiones deben estar entre `0` y `1`.
- La centralidad debe estar entre `0` y `1`.
- Los pesos deben ser numéricos, no negativos y con suma mayor que cero.
- `beta` y `lambda_decay` no pueden ser negativos.
- `max_degree` debe ser entero y mayor o igual a `1`.

Estos controles no validan la verdad de los datos. Solo garantizan que el cálculo respete una forma coherente.

## Lectura de resultados

SDMC usa etiquetas cualitativas simples:

- `bajo`: menor a `0.34`.
- `medio`: desde `0.34` hasta antes de `0.67`.
- `alto`: `0.67` o superior.

Estas etiquetas son orientativas. Para uso operativo real, cada organización debería definir umbrales con base en validación empírica, contexto jurídico y tolerancia al riesgo.

## Decisiónes de diseño

- El núcleo no recolecta datos. Solo calcula sobre entradas declaradas.
- La CLI admite JSON para facilitar reproducibilidad.
- El reporte Markdown muestra fórmulas, entradas y controles.
- El script histórico se mantiene como wrapper para no romper usos previos.
