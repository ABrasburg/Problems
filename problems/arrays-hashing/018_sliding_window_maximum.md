# 018 - Sliding Window Maximum

## Resumen

Para cada ventana contigua de tamano `k`, obtener el maximo de esa ventana.

## Idea

La estructura clave es una cola doble que mantiene candidatos al maximo en orden decreciente. Al avanzar la ventana, se eliminan indices fuera de rango y valores que ya no pueden ganar.

## Complejidad

- Tiempo: `O(n)`.
- Espacio: `O(k)`.

## Codigo

[Ver solucion](018_sliding_window_maximum.py)
