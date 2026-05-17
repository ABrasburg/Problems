# 006 - XOR Linked List

## Resumen

Representar una lista doblemente enlazada usando una sola referencia combinada por nodo.

## Idea

La tecnica clasica guarda el XOR entre la direccion del nodo anterior y la del siguiente. Para avanzar, se combina el nodo previo con el valor guardado y se obtiene el siguiente.

En Python esta estructura es mas conceptual que practica, porque el manejo de memoria queda abstraido por el runtime.

## Complejidad

- Insercion: `O(1)`.
- Acceso secuencial: `O(n)`.
- Espacio por nodo: `O(1)`.

## Codigo

[Ver solucion](006_xor_linked_list.py)
