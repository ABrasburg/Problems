# 002 - Product Array

## Resumen

Construir un arreglo donde cada posicion contenga el producto de todos los elementos excepto el de esa misma posicion.

## Idea

El patron usual es combinar productos acumulados desde la izquierda y desde la derecha. Asi cada posicion recibe el producto de lo que tiene antes y despues, sin necesitar division.

## Complejidad

- Tiempo: `O(n)`.
- Espacio: `O(n)` si se guardan ambos acumulados; puede bajarse a `O(1)` extra usando el arreglo de salida.

## Codigo

[Ver solucion](002_product_array.py)
