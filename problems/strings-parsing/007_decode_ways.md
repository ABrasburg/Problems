# 007 - Decode Ways

## Resumen

Contar cuantas formas hay de decodificar un string numerico donde cada numero valido representa una letra.

## Idea

Cada caracter puede decodificarse solo si representa un numero valido, y a veces tambien puede combinarse con el caracter anterior para formar un valor entre 10 y 26.

La recurrencia sobre prefijos suma dos posibilidades:

- usar el ultimo digito solo;
- usar los ultimos dos digitos juntos, si forman una letra valida.

## Paso a paso

- Definir una tabla donde `dp[i]` representa formas de decodificar el prefijo de largo `i`.
- Inicializar el prefijo vacio con una forma.
- Para cada posicion, sumar `dp[i - 1]` si el digito actual no es `0`.
- Sumar `dp[i - 2]` si los dos ultimos digitos forman un numero entre 10 y 26.
- El resultado queda en `dp[n]`.

## Complejidad

- Tiempo: `O(n)`.
- Espacio: `O(n)`, reducible a `O(1)`.

## Codigo

[Ver solucion](007_decode_ways.py)
