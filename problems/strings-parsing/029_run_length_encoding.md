# 029 - Run-Length Encoding

## Resumen

Dado un string, implementar dos operaciones:

- `encode(value)`: comprime caracteres repetidos consecutivos usando cantidad + caracter.
- `decode(value)`: reconstruye el string original desde esa representacion.
- El string a codificar no tiene digitos y solo contiene caracteres alfabeticos.
- El string a decodificar se puede asumir valido.

Ejemplo:

```text
"AAAABBBCCDAA" -> "4A3B2C1D2A"
"4A3B2C1D2A" -> "AAAABBBCCDAA"
```

## Objetivo

Completar `encode(value)` y `decode(value)` en el archivo de Python.

## Pistas

- Para codificar, recorri el string agrupando caracteres iguales consecutivos.
- Para decodificar, acumula los digitos hasta encontrar el caracter al que aplican.
- El numero puede tener mas de un digito, por ejemplo `12A`.

## Explicacion

El problema tiene dos partes simetricas: comprimir grupos consecutivos y despues expandirlos.

Para `encode(value)`, la idea es mantener dos datos mientras se recorre el string:

- el caracter actual del grupo;
- cuantas veces aparecio seguido.

Mientras el siguiente caracter sea igual al actual, se incrementa el contador. Cuando aparece un caracter distinto, el grupo anterior ya termino: se agrega a la respuesta el contador seguido del caracter, y se empieza un nuevo grupo.

Al terminar el recorrido, todavia queda pendiente agregar el ultimo grupo, porque no va a aparecer un caracter distinto que fuerce su cierre.

Ejemplo:

```text
AAAABBBCCDAA
AAAA -> 4A
BBB  -> 3B
CC   -> 2C
D    -> 1D
AA   -> 2A
```

Resultado:

```text
4A3B2C1D2A
```

Para `decode(value)`, el proceso se invierte. Se recorre el string codificado acumulando digitos en un contador. Cuando aparece una letra, esa letra se repite tantas veces como indique el contador, se agrega a la respuesta y el contador vuelve a cero.

La parte importante es que el contador puede tener mas de un digito. Por eso no alcanza con leer un solo numero antes de cada letra: si aparece `12A`, hay que construir `12`, no interpretar `1` y `2` por separado.

Una forma de construir ese contador es:

```text
count = count * 10 + digito
```

Entonces:

```text
1  -> count = 1
2  -> count = 12
A  -> agregar "A" 12 veces
```

## Complejidad esperada

- Tiempo: `O(n)`, porque se recorre cada string una vez.
- Espacio: `O(n)`, por el string de salida.

## Codigo

[Resolver aca](029_run_length_encoding.py)
