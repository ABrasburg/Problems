# 023 - Shortest Path Grid

## Resumen

Encontrar la cantidad minima de pasos entre dos celdas de una grilla con paredes.

## Idea

Como todos los movimientos tienen el mismo costo, BFS es el enfoque natural. Se exploran celdas por distancia creciente desde el inicio; la primera vez que se alcanza el destino, esa distancia es minima.

## Complejidad

- Tiempo: `O(m * n)`.
- Espacio: `O(m * n)`.

## Codigo

[Ver solucion](023_shortest_path_grid.py)
