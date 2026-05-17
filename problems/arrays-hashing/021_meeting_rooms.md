# 021 - Meeting Rooms

## Resumen

Dado un conjunto de intervalos de reuniones, calcular cuantas salas se necesitan para poder realizarlas sin solapamientos.

## Idea

Ordenar comienzos y finales permite recorrer la linea de tiempo. Cuando empieza una reunion se ocupa una sala; cuando termina una reunion se libera. El maximo de salas ocupadas es la respuesta.

## Complejidad

- Tiempo: `O(n log n)` por el ordenamiento.
- Espacio: `O(n)`.

## Codigo

[Ver solucion](021_meeting_rooms.py)
