# 011 - Autocomplete

## Resumen

Dado un prefijo y un conjunto de palabras, devolver las palabras que comienzan con ese prefijo.

## Idea

La version simple recorre todas las palabras y filtra por prefijo. Para escalar, el patron natural es un trie, que permite bajar por los caracteres del prefijo y listar solo el subarbol relevante.

## Complejidad

- Busqueda simple: `O(n * p)`, con `n` palabras y prefijo de largo `p`.
- Con trie: `O(p + r)`, donde `r` es el tamano de la salida.

## Codigo

[Ver solucion](011_autocomplete.py)
