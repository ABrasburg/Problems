# 022 - Word Break

## Resumen

Determinar si un string puede segmentarse en palabras pertenecientes a un diccionario.

## Idea

Se evalua cada prefijo del string. Si existe un punto de corte donde la parte izquierda es segmentable y la derecha es una palabra valida, entonces el prefijo completo tambien es segmentable.

## Complejidad

- Tiempo: `O(n^2)` considerando cortes de prefijos.
- Espacio: `O(n)`.

## Codigo

[Ver solucion](022_word_break.py)
