# 009 - Max Non-Adjacent Sum

## Resumen

Calcular la maxima suma posible eligiendo numeros del arreglo sin tomar elementos adyacentes.

## Idea

En cada numero hay una decision local con efecto sobre el siguiente: si se toma el valor actual, no se puede tomar el anterior; si no se toma, se conserva la mejor suma acumulada hasta ahora.

La recurrencia es:

`best[i] = max(best[i - 1], best[i - 2] + array[i])`

No hace falta guardar toda la tabla; alcanza con los dos mejores estados previos.

## Paso a paso

- Mantener `incluyendo_actual` y `excluyendo_actual`, o equivalentes.
- Al procesar un numero, calcular la mejor suma si se lo toma.
- Compararla contra la mejor suma si se lo saltea.
- Actualizar los dos acumuladores.

## Complejidad

- Tiempo: `O(n)`.
- Espacio: `O(1)` si solo se guardan los dos estados previos.

## Codigo

[Ver solucion](009_max_non_adjacent_sum.py)
