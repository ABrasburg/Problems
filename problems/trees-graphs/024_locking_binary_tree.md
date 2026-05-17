# 024 - Locking Binary Tree

## Resumen

Permitir bloquear y desbloquear nodos de un arbol binario solo si no hay ancestros ni descendientes bloqueados.

## Idea

La validacion requiere mirar dos direcciones:

- no puede haber ancestros bloqueados;
- no puede haber descendientes bloqueados.

Revisar todos los descendientes en cada operacion seria caro. La optimizacion es guardar en cada nodo un contador de descendientes bloqueados. Asi, detectar si hay algun descendiente bloqueado cuesta `O(1)`.

## Paso a paso

- Cada nodo guarda `locked`, `parent` y `locked_descendants_count`.
- Para bloquear o desbloquear, primero revisar si `locked_descendants_count > 0`.
- Luego subir por `parent` para verificar que no haya ancestros bloqueados.
- Al bloquear, marcar el nodo y sumar uno al contador de todos sus ancestros.
- Al desbloquear, desmarcar el nodo y restar uno a esos contadores.

## Complejidad

- `is_locked`: `O(1)`.
- `lock` y `unlock`: `O(h)`, donde `h` es la altura del arbol.
- Espacio extra por nodo: `O(1)`.

## Codigo

[Ver solucion](024_locking_binary_tree.py)
