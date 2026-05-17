# 009 - Max Non-Adjacent Sum

## Resumen

Calcular la maxima suma posible eligiendo numeros del arreglo sin tomar elementos adyacentes.

## Idea

En cada posicion hay dos opciones: tomar el numero actual y sumar la mejor solucion hasta dos posiciones atras, o no tomarlo y conservar la mejor solucion anterior.

## Complejidad

- Tiempo: `O(n)`.
- Espacio: `O(1)` si solo se guardan los dos estados previos.

## Codigo

[Ver solucion](009_max_non_adjacent_sum.py)
