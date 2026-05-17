# 006 - XOR Linked List

## Resumen

Representar una lista doblemente enlazada usando una sola referencia combinada por nodo.

## Idea

Una lista doble tradicional guarda dos referencias por nodo: anterior y siguiente. La variante XOR guarda una sola celda con `prev_address XOR next_address`.

Si durante el recorrido conocemos la direccion del nodo anterior, podemos recuperar la siguiente con:

`next = both XOR prev`

porque `prev XOR next XOR prev` cancela `prev` y deja `next`.

En Python esta estructura es mas conceptual que practica, porque el manejo de memoria queda abstraido por el runtime.

## Paso a paso

- Cada nodo guarda su valor y el XOR de vecinos.
- Para agregar al final, se actualiza el XOR del viejo ultimo nodo incorporando el nuevo.
- Para recorrer, se mantiene el par `(prev, current)`.
- El siguiente nodo se calcula usando la direccion previa y el campo combinado.

## Complejidad

- Insercion: `O(1)`.
- Acceso secuencial: `O(n)`.
- Espacio por nodo: `O(1)`.

## Codigo

[Ver solucion](006_xor_linked_list.py)
