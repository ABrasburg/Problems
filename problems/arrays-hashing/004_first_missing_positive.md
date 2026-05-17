# 004 - First Missing Positive

## Resumen

Encontrar el menor entero positivo que no aparece en el arreglo.

## Idea

El detalle importante es que solo importan valores entre `1` y `n + 1`. Una estrategia eficiente reubica cada numero valido en su posicion esperada, para luego recorrer el arreglo y detectar el primer hueco.

## Complejidad

- Tiempo: `O(n)`.
- Espacio: `O(1)` extra si se modifica el arreglo.

## Codigo

[Ver solucion](004_first_missing_positive.py)
