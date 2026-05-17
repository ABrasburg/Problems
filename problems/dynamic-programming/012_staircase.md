# 012 - Staircase

## Resumen

Contar cuantas formas hay de subir una escalera de `n` escalones usando saltos permitidos.

## Idea

La cantidad de formas de llegar a un escalon depende de las formas de llegar a los escalones anteriores desde los cuales se puede saltar. Eso produce una recurrencia natural de programacion dinamica.

## Complejidad

- Tiempo: `O(n * k)`, donde `k` es la cantidad de saltos permitidos.
- Espacio: `O(n)`.

## Codigo

[Ver solucion](012_staircase.py)
