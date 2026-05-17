# 022 - Word Break

## Resumen

Determinar si un string puede segmentarse en palabras pertenecientes a un diccionario.

## Idea

El problema pregunta si existe una secuencia de cortes que convierta el string completo en palabras del diccionario.

Una recursion prueba prefijos validos y llama al resto del string. Para evitar repetir los mismos sufijos muchas veces, se memoiza si cada indice puede llegar a una segmentacion valida.

## Paso a paso

- Convertir el diccionario en `set` para busqueda `O(1)`.
- Definir una funcion `can_break(start)` sobre el indice actual.
- Probar todos los finales posibles desde `start + 1` hasta `n`.
- Si `s[start:end]` es palabra y `can_break(end)` es verdadero, guardar `True`.
- Si ningun corte funciona, guardar `False`.

## Complejidad

- Tiempo: `O(n^2)` considerando cortes de prefijos.
- Espacio: `O(n)`.

## Codigo

[Ver solucion](022_word_break.py)
