# 023 - Shortest Path Grid

## Resumen

Encontrar la cantidad minima de pasos entre dos celdas de una grilla con paredes.

## Idea

Como cada movimiento cuesta lo mismo, BFS es el algoritmo adecuado: explora primero todas las celdas a distancia 1, luego distancia 2, y asi sucesivamente. Por eso, la primera vez que se alcanza el destino, esa distancia ya es minima.

DFS puede encontrar un camino, pero no garantiza que sea el mas corto sin explorar combinaciones innecesarias.

## Paso a paso

- Iniciar una cola con `(start, 0)`.
- Mantener un conjunto de celdas vistas.
- Sacar una celda de la cola.
- Si es el destino, devolver su distancia.
- Agregar vecinos caminables no vistos con distancia `+ 1`.
- Si la cola se vacia, no hay camino.

## Complejidad

- Tiempo: `O(m * n)`.
- Espacio: `O(m * n)`.

## Codigo

[Ver solucion](023_shortest_path_grid.py)
