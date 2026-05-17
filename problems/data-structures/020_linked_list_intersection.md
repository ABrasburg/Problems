# 020 - Linked List Intersection

## Resumen

Encontrar el nodo en el que dos listas enlazadas comienzan a compartir estructura.

## Idea

Si dos listas se cruzan, comparten todos los nodos desde el punto de interseccion. Una forma robusta es igualar longitudes avanzando primero la lista mas larga y luego mover ambas al mismo ritmo hasta coincidir.

## Complejidad

- Tiempo: `O(n + m)`.
- Espacio: `O(1)`.

## Codigo

[Ver solucion](020_linked_list_intersection.py)
