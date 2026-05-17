# 027 - Balanced Brackets

## Resumen

Dado un string con brackets redondos, cuadrados y llaves, determinar si estan balanceados y bien formados.

Ejemplos:

- `"([])[]({})"` debe devolver `True`.
- `"([)]"` debe devolver `False`.
- `"((()"` debe devolver `False`.

## Objetivo

Completar `is_balanced(brackets)` en el archivo de Python.

## Idea

Un string de brackets esta balanceado cuando cada cierre corresponde al ultimo bracket abierto que todavia no fue cerrado.

Eso sugiere usar una pila:

- Cuando aparece un bracket de apertura, se guarda en la pila.
- Cuando aparece un bracket de cierre, debe coincidir con el ultimo bracket abierto.
- Si no coincide, el string no esta bien formado.

La razon por la que una pila funciona es que los brackets se cierran en orden inverso al que se abren. Por ejemplo:

```text
([])[]({})
```

Dentro del primer par de parentesis se abre `[`, y ese `[` debe cerrarse antes de poder cerrar `(`.

## Paso a paso

1. Crear una pila vacia.
2. Recorrer el string caracter por caracter.
3. Si el caracter es de apertura (`(`, `[`, `{`), apilarlo.
4. Si el caracter es de cierre (`)`, `]`, `}`):
   - si la pila esta vacia, devolver `False`;
   - sacar el ultimo elemento de la pila;
   - verificar que sea la apertura correspondiente.
5. Al terminar, devolver `True` solo si la pila quedo vacia.

## Pistas

- Conviene tener un diccionario que relacione cierres con aperturas, por ejemplo `")": "("`.
- `"([)]"` falla porque `]` intenta cerrar `[` pero arriba de la pila queda `(`.
- `"((()"` falla porque quedan aperturas sin cerrar.
- Un string vacio suele considerarse balanceado.

## Casos de prueba incluidos

- Brackets anidados y consecutivos validos.
- Cierre en orden incorrecto.
- Aperturas sin cierre suficiente.

## Complejidad esperada

- Tiempo: `O(n)`.
- Espacio: `O(n)` en el peor caso, si todos los caracteres son aperturas.

## Codigo

[Resolver aca](027_balanced_brackets.py)
