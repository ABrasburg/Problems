# 001 - Two Sum

## Resumen

Dado un arreglo de numeros y un objetivo `k`, hay que determinar si existen dos elementos distintos que sumen `k`.

## Idea

La solucion directa con hashing guarda los numeros ya vistos. Para cada numero, calcula su complemento `k - num`; si ese complemento ya aparecio, la respuesta es verdadera.

## Complejidad

- Tiempo: `O(n)`.
- Espacio: `O(n)`.

## Codigo

[Ver solucion](001_two_sum.py)
