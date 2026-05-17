# 015 - Reservoir Sampling

## Resumen

Elegir un elemento al azar de un flujo de datos cuyo tamano total no se conoce de antemano.

## Idea

Al procesar el elemento numero `i`, se reemplaza la muestra actual con probabilidad `1 / i`. Esa regla mantiene la misma probabilidad final para todos los elementos vistos.

## Complejidad

- Tiempo: `O(n)`.
- Espacio: `O(1)`.

## Codigo

[Ver solucion](015_reservoir_sampling.py)
