# 003 - Serialize and Deserialize Tree

## Resumen

Convertir un arbol binario a una representacion serializada y reconstruirlo luego desde esa representacion.

## Idea

Serializar solo los valores no alcanza, porque se pierde la forma del arbol. La solucion usa un recorrido en preorden y agrega un marcador para hijos vacios.

Al deserializar se consume la secuencia en el mismo orden: primero raiz, luego subarbol izquierdo, luego subarbol derecho. Los marcadores indican cuando cortar una rama.

## Paso a paso

- Si el nodo es vacio, escribir un marcador especial.
- Si no es vacio, escribir su valor.
- Serializar recursivamente el hijo izquierdo.
- Serializar recursivamente el hijo derecho.
- Para reconstruir, leer el proximo token y repetir la misma estructura recursiva.

## Complejidad

- Tiempo: `O(n)`.
- Espacio: `O(n)`.

## Codigo

[Ver solucion](003_serialize_deserialize_tree.py)
