# 005 - Cons, Car and Cdr

## Resumen

Implementar `cons`, `car` y `cdr`, usando funciones para representar pares.

## Idea

La gracia del ejercicio es representar datos usando funciones. `cons(a, b)` no necesita devolver una tupla: puede devolver una funcion que recibe otra funcion y se la aplica a los dos valores guardados.

Entonces `car` y `cdr` solo tienen que pasar un selector distinto:

- `car` pasa una funcion que elige el primer argumento.
- `cdr` pasa una funcion que elige el segundo argumento.

## Paso a paso

- `cons` captura `a` y `b` en una clausura.
- Al llamar esa clausura con un selector, se ejecuta `selector(a, b)`.
- `car(pair)` evalua el par con un selector que devuelve `a`.
- `cdr(pair)` evalua el par con un selector que devuelve `b`.

## Complejidad

- Tiempo: `O(1)` para construir y consultar.
- Espacio: `O(1)`.

## Codigo

[Ver solucion](005_cons_car_cdr.py)
