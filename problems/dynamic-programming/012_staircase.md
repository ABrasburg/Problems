# 012 - Staircase

## Resumen

Contar cuantas formas hay de subir una escalera de `n` escalones usando saltos permitidos.

## Idea

Si solo se permiten saltos de 1 o 2 escalones, el problema se parece a Fibonacci: para llegar al escalon `n`, el ultimo salto vino desde `n - 1` o desde `n - 2`.

La version general acepta un conjunto de saltos. Entonces las formas de llegar a `n` son la suma de las formas de llegar a `n - step` para cada salto permitido.

## Paso a paso

- Definir `ways[0] = 1`: hay una forma de no subir ningun escalon.
- Para cada altura de `1` a `n`, probar todos los saltos permitidos.
- Si `height - step >= 0`, sumar `ways[height - step]`.
- El resultado queda en `ways[n]`.

## Complejidad

- Tiempo: `O(n * k)`, donde `k` es la cantidad de saltos permitidos.
- Espacio: `O(n)`.

## Codigo

[Ver solucion](012_staircase.py)
