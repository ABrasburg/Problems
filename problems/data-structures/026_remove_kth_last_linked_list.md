# 026 - Remove Kth Last Linked List Node

## Resumen

Dada una lista simplemente enlazada y un entero `k`, eliminar el k-esimo nodo contando desde el final.

La lista puede ser muy larga, asi que la solucion debe hacer una sola pasada y usar espacio constante.

## Objetivo

Completar `remove_kth_last(head, k)` en el archivo de Python.

## Idea

Hay que borrar el k-esimo nodo contando desde el final, no desde el principio. Si la lista fuera corta o si se permitieran dos pasadas, se podria calcular primero el largo `n` y despues borrar el nodo en la posicion `n - k`.

La restriccion pide una sola pasada. Para lograrlo, se usan dos punteros separados por una distancia de `k` nodos:

- `dist_k` o `fast` avanza primero `k` posiciones.
- `actual` o `slow` empieza en la cabeza.
- Cuando ambos avanzan juntos, `fast` llega al final justo cuando `slow` esta en el nodo que hay que borrar.

Como la lista es simplemente enlazada, para borrar un nodo tambien hace falta guardar el nodo anterior. El borrado se hace saltando el nodo:

```python
anterior.next = actual.next
```

## Paso a paso

1. Crear dos punteros que arranquen en `head`.
2. Adelantar uno de ellos `k` nodos.
3. Crear `anterior = None`.
4. Avanzar los dos punteros al mismo ritmo hasta que el puntero adelantado llegue al final.
5. En cada avance, actualizar `anterior` para que quede justo antes de `actual`.
6. Cuando termina el recorrido, `actual` es el nodo a eliminar.
7. Reasignar `anterior.next` para saltear `actual`.
8. Devolver `head`, porque la cabeza no cambia bajo la condicion `k < len(lista)`.

## Pistas

- El enunciado garantiza que `k` es menor que el largo de la lista, asi que no hace falta resolver el caso de borrar la cabeza.
- Si `k = 1`, se borra el ultimo nodo.
- Si `k = 2`, se borra el anteultimo nodo.
- El punto delicado es no perder el `anterior`, porque sin ese nodo no podes modificar el enlace que apunta al nodo borrado.

## Casos de prueba incluidos

- Eliminar un nodo del medio.
- Eliminar el ultimo nodo.

## Complejidad esperada

- Tiempo: `O(n)`.
- Espacio: `O(1)`.

## Codigo

[Resolver aca](026_remove_kth_last_linked_list.py)
