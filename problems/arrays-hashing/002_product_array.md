# 002 - Product Array

## Resumen

Construir un arreglo donde cada posicion contenga el producto de todos los elementos excepto el de esa misma posicion.

## Idea

Con division, se podria multiplicar todo el arreglo y dividir por el valor de cada posicion. El seguimiento pide resolverlo sin division, asi que la idea es separar el producto en dos partes:

- producto de todos los elementos a la izquierda de `i`;
- producto de todos los elementos a la derecha de `i`.

Multiplicando esos dos acumulados se obtiene el producto de todos excepto `array[i]`.

## Paso a paso

- Construir un arreglo `prefix` donde `prefix[i]` es el producto previo a `i`.
- Construir un arreglo `suffix` donde `suffix[i]` es el producto posterior a `i`.
- Para cada posicion, devolver `prefix[i] * suffix[i]`.
- La misma idea puede optimizarse usando el arreglo de salida y un acumulador de derecha.

## Complejidad

- Tiempo: `O(n)`.
- Espacio: `O(n)` si se guardan ambos acumulados; puede bajarse a `O(1)` extra usando el arreglo de salida.

## Codigo

[Ver solucion](002_product_array.py)
