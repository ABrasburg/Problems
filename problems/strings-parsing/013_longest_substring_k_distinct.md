# 013 - Longest Substring With K Distinct

## Resumen

Encontrar la longitud de la subcadena mas larga que contiene como maximo `k` caracteres distintos.

## Idea

Se usa una ventana deslizante con conteo de caracteres. El extremo derecho expande la ventana; cuando hay mas de `k` caracteres distintos, el extremo izquierdo avanza hasta restaurar la condicion.

## Complejidad

- Tiempo: `O(n)`.
- Espacio: `O(k)`.

## Codigo

[Ver solucion](013_longest_substring_k_distinct.py)
