# 004 - First Missing Positive

## Resumen

Encontrar el menor entero positivo que no aparece en el arreglo.

## Idea

El menor positivo faltante siempre esta entre `1` y `n + 1`, donde `n` es el largo del arreglo. Los numeros negativos, cero y valores mayores a `n` no ayudan a decidir las primeras posiciones.

Hay varias formas de resolverlo: ordenar, usar un set, o modificar el arreglo para usar sus indices como marcas. La version eficiente intenta colocar cada valor `x` valido en la posicion `x - 1`.

## Paso a paso

- Recorrer el arreglo y, mientras el valor actual pueda ocupar una posicion valida, intercambiarlo con su posicion esperada.
- Despues de ordenar parcialmente por posicion, recorrer desde el inicio.
- La primera posicion `i` que no contiene `i + 1` revela el positivo faltante.
- Si todas coinciden, la respuesta es `n + 1`.

## Complejidad

- Tiempo: `O(n)`.
- Espacio: `O(1)` extra si se modifica el arreglo.

## Codigo

[Ver solucion](004_first_missing_positive.py)
