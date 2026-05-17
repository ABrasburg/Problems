# 025 - Regular Expression Matching

## Resumen

Implementar un matcher completo entre un string y una expresion regular valida con dos operadores:

- `.`: coincide con cualquier caracter individual.
- `*`: coincide con cero o mas repeticiones del elemento anterior.

El patron debe cubrir todo el string, no solo una parte.

## Idea

La estructura del problema es recursiva. Si el primer caracter del patron coincide con el primer caracter del string, entonces queda por resolver el resto del string contra el resto del patron.

El caso especial es `*`, tambien conocido como Kleene star. Cuando el segundo caracter del patron es `*`, hay dos posibilidades:

1. Usar cero apariciones del elemento anterior y saltar `x*` en el patron.
2. Si el primer caracter coincide, consumir un caracter del string y mantener el mismo patron, porque `*` todavia podria consumir mas.

La solucion usa memoizacion sobre los indices `(i, j)` para no recalcular el mismo sufijo del string contra el mismo sufijo del patron.

## Paso a paso

- Definir `matches(i, j)` como si `string[i:]` matchea `regex[j:]`.
- Si `j` llego al final del patron, solo hay match si `i` tambien llego al final del string.
- Calcular si el primer caracter actual coincide: mismo caracter o `.`.
- Si el proximo caracter del patron es `*`, probar:
  - saltear el par `caracter + *`;
  - consumir un caracter del string si habia coincidencia.
- Si no hay `*`, avanzar ambos indices cuando el primer caracter coincide.
- Guardar cada estado `(i, j)` para evitar recomputaciones.

## Complejidad

- Tiempo: `O(n * m)`, con `n = len(string)` y `m = len(regex)`.
- Espacio: `O(n * m)` por la cache de memoizacion.

## Codigo

[Ver solucion](025_regular_expression_matching.py)
