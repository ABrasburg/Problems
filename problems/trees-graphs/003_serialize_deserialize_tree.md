# 003 - Serialize and Deserialize Tree

## Resumen

Convertir un arbol binario a una representacion serializada y reconstruirlo luego desde esa representacion.

## Idea

Un recorrido en preorden funciona si tambien se registran nodos vacios. Al deserializar, se consume la secuencia en el mismo orden para reconstruir raiz, subarbol izquierdo y subarbol derecho.

## Complejidad

- Tiempo: `O(n)`.
- Espacio: `O(n)`.

## Codigo

[Ver solucion](003_serialize_deserialize_tree.py)
