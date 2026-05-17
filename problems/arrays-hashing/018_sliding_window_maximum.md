# 018 - Sliding Window Maximum

## Resumen

Para cada ventana contigua de tamano `k`, obtener el maximo de esa ventana.

## Idea

La solucion ingenua recalcula el maximo para cada ventana y cuesta `O(n * k)`. La optimizacion usa una cola doble con indices de candidatos al maximo.

La cola se mantiene en orden decreciente de valores. Si entra un numero mayor que los candidatos del fondo, esos candidatos ya no pueden ser maximo en ninguna ventana futura y se eliminan.

## Paso a paso

- Antes de agregar el nuevo indice, quitar del frente los indices que salieron de la ventana.
- Quitar del fondo los indices cuyos valores son menores o iguales al nuevo valor.
- Agregar el indice actual.
- Cuando ya se completo la primera ventana, el frente de la cola apunta al maximo.

## Complejidad

- Tiempo: `O(n)`.
- Espacio: `O(k)`.

## Codigo

[Ver solucion](018_sliding_window_maximum.py)
