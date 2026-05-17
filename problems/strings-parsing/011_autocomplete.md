# 011 - Autocomplete

## Resumen

Dado un prefijo y un conjunto de palabras, devolver las palabras que comienzan con ese prefijo.

## Idea

La solucion mas directa revisa todas las palabras y conserva las que empiezan con el prefijo. Es suficiente para listas chicas.

Para un sistema real de autocompletado conviene un trie. Cada nodo representa un prefijo; buscar el prefijo cuesta recorrer sus caracteres, y luego se listan las palabras en el subarbol.

## Paso a paso

- Insertar cada palabra caracter por caracter en el trie.
- Marcar los nodos donde termina una palabra.
- Para consultar, avanzar por el trie siguiendo el prefijo.
- Si el prefijo no existe, devolver lista vacia.
- Si existe, recorrer desde ese nodo para recolectar completions.

## Complejidad

- Busqueda simple: `O(n * p)`, con `n` palabras y prefijo de largo `p`.
- Con trie: `O(p + r)`, donde `r` es el tamano de la salida.

## Codigo

[Ver solucion](011_autocomplete.py)
