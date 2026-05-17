# 005 - Cons, Car and Cdr

## Resumen

Implementar `cons`, `car` y `cdr`, usando funciones para representar pares.

## Idea

El par se guarda como una clausura: `cons(a, b)` devuelve una funcion que recibe otra funcion y se la aplica a `a` y `b`. `car` y `cdr` pasan selectores distintos para recuperar el primer o segundo valor.

## Complejidad

- Tiempo: `O(1)` para construir y consultar.
- Espacio: `O(1)`.

## Codigo

[Ver solucion](005_cons_car_cdr.py)
