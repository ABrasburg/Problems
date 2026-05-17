# 007 - Decode Ways

## Resumen

Contar cuantas formas hay de decodificar un string numerico donde cada numero valido representa una letra.

## Idea

Cada posicion puede depender de una decodificacion de un digito o de dos digitos, siempre que formen valores validos. La solucion se modela con una recurrencia sobre prefijos del string.

## Complejidad

- Tiempo: `O(n)`.
- Espacio: `O(n)`, reducible a `O(1)`.

## Codigo

[Ver solucion](007_decode_ways.py)
