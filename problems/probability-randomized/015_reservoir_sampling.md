# 015 - Reservoir Sampling

## Resumen

Elegir un elemento al azar de un flujo de datos cuyo tamano total no se conoce de antemano.

## Idea

El objetivo es que cada elemento del stream tenga la misma probabilidad final de quedar elegido, aunque no sepamos cuantos elementos habra.

La regla es: cuando llega el elemento numero `i`, reemplazar la muestra actual con probabilidad `1 / i`. Los elementos tempranos tienen mas oportunidades de ser reemplazados, y eso compensa que hayan aparecido antes.

## Intuicion de probabilidad

Para que el primer elemento sobreviva hasta el final, debe no ser reemplazado en cada paso posterior. Esa probabilidad termina siendo `1 / n`. Lo mismo ocurre con cualquier elemento `i`: entra con probabilidad `1 / i` y sobrevive los reemplazos posteriores hasta quedar tambien con `1 / n`.

## Complejidad

- Tiempo: `O(n)`.
- Espacio: `O(1)`.

## Codigo

[Ver solucion](015_reservoir_sampling.py)
