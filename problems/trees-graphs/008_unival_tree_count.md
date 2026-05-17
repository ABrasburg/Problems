# 008 - Unival Tree Count

## Resumen

Contar cuantos subarboles son unival, es decir, todos sus nodos tienen el mismo valor.

## Idea

La recursion devuelve si cada subarbol es unival y acumula el conteo. Un nodo forma un subarbol unival si sus hijos tambien lo son y, cuando existen, tienen el mismo valor que el nodo.

## Complejidad

- Tiempo: `O(n)`.
- Espacio: `O(h)`, donde `h` es la altura del arbol.

## Codigo

[Ver solucion](008_unival_tree_count.py)
