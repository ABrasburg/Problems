# 008 - Unival Tree Count

## Resumen

Contar cuantos subarboles son unival, es decir, todos sus nodos tienen el mismo valor.

## Idea

Un subarbol es unival si todos sus nodos tienen el mismo valor. La forma comoda de resolverlo es hacer una recursion postorden: primero se evalua cada hijo y despues se decide si el nodo actual tambien forma un subarbol unival.

La funcion auxiliar puede devolver dos cosas: si el subarbol actual es unival y cuantos subarboles unival hay debajo.

## Paso a paso

- Un nodo vacio se considera compatible.
- Resolver recursivamente izquierda y derecha.
- Si algun hijo no es unival, el nodo actual tampoco lo es.
- Si un hijo existe y su valor difiere del nodo actual, tampoco lo es.
- Si pasa ambas condiciones, sumar uno al conteo.

## Complejidad

- Tiempo: `O(n)`.
- Espacio: `O(h)`, donde `h` es la altura del arbol.

## Codigo

[Ver solucion](008_unival_tree_count.py)
