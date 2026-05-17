# 017 - Longest File Path

## Resumen

Calcular la longitud del path absoluto mas largo hacia un archivo dentro de una representacion textual de un filesystem.

## Idea

Cada linea indica un nivel por su indentacion. Una pila o diccionario de longitudes acumuladas por nivel permite saber la longitud del path actual y actualizar el maximo cuando aparece un archivo.

## Complejidad

- Tiempo: `O(n)`, donde `n` es el largo del string.
- Espacio: `O(d)`, donde `d` es la profundidad maxima.

## Codigo

[Ver solucion](017_longest_file_path.py)
