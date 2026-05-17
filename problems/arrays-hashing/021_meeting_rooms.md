# 021 - Meeting Rooms

## Resumen

Dado un conjunto de intervalos de reuniones, calcular cuantas salas se necesitan para poder realizarlas sin solapamientos.

## Idea

El problema mide cuantos intervalos se solapan al mismo tiempo. Una forma clara es separar los horarios de inicio y fin, ordenarlos, y simular el paso del tiempo.

Cuando el proximo evento es un inicio, se ocupa una sala. Cuando el proximo evento es un fin, se libera una sala. El maximo de salas ocupadas durante el recorrido es la respuesta.

## Paso a paso

- Ordenar todos los comienzos.
- Ordenar todos los finales.
- Avanzar dos punteros sobre ambas listas.
- Si la proxima reunion empieza antes de que termine la actual mas temprana, sumar una sala.
- Si no, liberar una sala y avanzar el puntero de finales.

## Complejidad

- Tiempo: `O(n log n)` por el ordenamiento.
- Espacio: `O(n)`.

## Codigo

[Ver solucion](021_meeting_rooms.py)
