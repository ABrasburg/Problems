# 013 - Longest Substring With K Distinct

## Resumen

Encontrar la longitud de la subcadena mas larga que contiene como maximo `k` caracteres distintos.

## Idea

La ventana deslizante mantiene una subcadena valida mientras sea posible. Al expandir hacia la derecha, puede aparecer un nuevo caracter distinto. Si la ventana pasa a tener mas de `k` caracteres distintos, se contrae desde la izquierda.

Para saber cuando un caracter deja de estar en la ventana, se mantiene un contador por caracter.

## Paso a paso

- Avanzar `right` por el string y sumar el caracter al contador.
- Si la cantidad de caracteres distintos supera `k`, mover `left`.
- Al mover `left`, decrementar el contador y borrar el caracter si llega a cero.
- En cada estado valido, actualizar la longitud maxima.

## Complejidad

- Tiempo: `O(n)`.
- Espacio: `O(k)`.

## Codigo

[Ver solucion](013_longest_substring_k_distinct.py)
