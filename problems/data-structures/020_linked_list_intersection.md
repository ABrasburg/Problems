# 020 - Linked List Intersection

## Resumen

Encontrar el nodo en el que dos listas enlazadas comienzan a compartir estructura.

## Idea

Si dos listas se intersectan, no solo comparten un valor: comparten exactamente el mismo nodo en memoria y todo lo que sigue desde ahi.

Una solucion con espacio extra guarda los nodos de una lista en un conjunto y busca el primer nodo de la otra que ya este en ese conjunto. La version con `O(1)` espacio primero iguala las distancias hasta el final.

## Paso a paso

- Calcular la longitud de ambas listas.
- Avanzar la cabeza de la lista mas larga por la diferencia de longitudes.
- Mover ambas cabezas al mismo ritmo.
- El primer nodo donde las referencias coinciden es la interseccion.
- Si llegan a `None`, no se cruzan.

## Complejidad

- Tiempo: `O(n + m)`.
- Espacio: `O(1)`.

## Codigo

[Ver solucion](020_linked_list_intersection.py)
