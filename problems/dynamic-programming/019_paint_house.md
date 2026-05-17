# 019 - Paint House

## Resumen

Pintar una fila de casas minimizando costo, con la restriccion de que casas vecinas no pueden usar el mismo color.

## Idea

La decision de color de una casa depende solo de la casa anterior. Para cada color posible en la casa actual, se suma su costo al mejor costo anterior que use un color distinto.

La version directa mira todos los colores anteriores para cada color actual. Una optimizacion guarda el menor y segundo menor costo de la fila anterior, para elegir rapido el mejor color permitido.

## Paso a paso

- Tomar la primera fila de costos como base.
- Para cada casa siguiente, calcular el costo acumulado por color.
- Si el color actual coincide con el color del minimo anterior, usar el segundo minimo.
- Si no coincide, usar el minimo anterior.
- Al final, tomar el menor costo de la ultima casa.

## Complejidad

- Tiempo: `O(n * k^2)` en la version directa, con `n` casas y `k` colores.
- Espacio: `O(k)` si solo se conserva la fila anterior.

## Codigo

[Ver solucion](019_paint_house.py)
