# 019 - Paint House

## Resumen

Pintar una fila de casas minimizando costo, con la restriccion de que casas vecinas no pueden usar el mismo color.

## Idea

Para cada casa y color, se suma el costo actual al minimo costo acumulado de la casa anterior usando un color distinto. La respuesta es el menor costo de la ultima fila.

## Complejidad

- Tiempo: `O(n * k^2)` en la version directa, con `n` casas y `k` colores.
- Espacio: `O(k)` si solo se conserva la fila anterior.

## Codigo

[Ver solucion](019_paint_house.py)
