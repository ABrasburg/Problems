# 017 - Longest File Path

## Resumen

Calcular la longitud del path absoluto mas largo hacia un archivo dentro de una representacion textual de un filesystem.

## Idea

Cada entrada del string representa un archivo o directorio, y la cantidad de tabulaciones indica la profundidad. El problema se reduce a mantener la longitud acumulada del path para cada nivel.

Cuando aparece un directorio, se guarda la longitud acumulada para su nivel. Cuando aparece un archivo, se calcula la longitud completa usando la longitud del padre y se actualiza el maximo.

## Paso a paso

- Separar la entrada por lineas.
- Para cada linea, contar tabs para obtener el nivel.
- Quitar tabs para obtener el nombre real.
- Mantener `path_len[level]` como longitud acumulada hasta ese nivel.
- Si la linea es archivo, actualizar el maximo.
- Si es directorio, guardar longitud para que sus hijos la usen.

## Complejidad

- Tiempo: `O(n)`, donde `n` es el largo del string.
- Espacio: `O(d)`, donde `d` es la profundidad maxima.

## Codigo

[Ver solucion](017_longest_file_path.py)
