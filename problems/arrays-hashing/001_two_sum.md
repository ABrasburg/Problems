# 001 - Two Sum

## Resumen

Dado un arreglo de numeros y un objetivo `k`, hay que determinar si existen dos elementos distintos que sumen `k`.

## Idea

Hay tres caminos naturales:

1. Probar todos los pares con dos bucles. Es simple, pero repite mucho trabajo.
2. Ordenar y buscar el complemento de cada valor con busqueda binaria, cuidando no usar dos veces la misma posicion.
3. Recorrer una sola vez con un `set` de valores ya vistos. Para cada numero `num`, el unico valor que falta para llegar a `k` es `k - num`.

La solucion del repo usa el tercer enfoque: si el complemento ya fue visto, existe un par valido; si no, agrega el numero actual y sigue.

## Paso a paso

- Crear un conjunto vacio `seen`.
- Para cada numero, calcular `k - num`.
- Si el complemento esta en `seen`, devolver `True`.
- Si no esta, guardar `num`.
- Si termina el recorrido sin encontrar par, devolver `False`.

## Complejidad

- Tiempo: `O(n)`.
- Espacio: `O(n)`.

## Codigo

[Ver solucion](001_two_sum.py)
