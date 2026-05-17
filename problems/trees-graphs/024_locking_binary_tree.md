# 024 - Locking Binary Tree

## Resumen

Permitir bloquear y desbloquear nodos de un arbol binario solo si no hay ancestros ni descendientes bloqueados.

## Idea

Cada nodo guarda si esta bloqueado y cuantos descendientes bloqueados tiene. Asi se puede detectar descendientes bloqueados en `O(1)` y revisar ancestros subiendo por punteros `parent`.

## Complejidad

- `is_locked`: `O(1)`.
- `lock` y `unlock`: `O(h)`, donde `h` es la altura del arbol.
- Espacio extra por nodo: `O(1)`.

## Codigo

[Ver solucion](024_locking_binary_tree.py)
