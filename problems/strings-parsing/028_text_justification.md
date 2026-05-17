# 028 - Text Justification

## Resumen

Dada una lista de palabras y un ancho de linea `k`, devolver una lista de strings donde cada linea quede justificada y tenga exactamente largo `k`.

Reglas importantes:

- En cada linea debe entrar la mayor cantidad posible de palabras.
- Debe haber al menos un espacio entre palabras.
- Si sobran espacios, se distribuyen de la forma mas pareja posible.
- Si hay espacios extra que no se pueden repartir parejo, se agregan empezando desde la izquierda.
- Si una linea tiene una sola palabra, se rellena con espacios a la derecha.
- Ninguna palabra es mas larga que `k`.

## Objetivo

Completar `justify_text(words, k)` en el archivo de Python.

## Idea

El problema se puede separar en dos etapas:

1. Agrupar palabras en lineas, metiendo tantas como entren sin superar `k`.
2. Para cada grupo de palabras, calcular cuantos espacios hacen falta y distribuirlos.

Para saber si una palabra entra en la linea actual, hay que considerar:

- la suma de largos de las palabras;
- al menos un espacio entre cada par de palabras.

Una vez elegida una linea, si tiene varias palabras, los espacios se reparten entre los huecos. Si hay `gaps` huecos y `spaces` espacios totales a distribuir:

- cada hueco recibe `spaces // gaps`;
- los primeros `spaces % gaps` huecos reciben un espacio extra.

## Paso a paso

1. Recorrer `words` acumulando una linea candidata.
2. Agregar palabras mientras el largo minimo de la linea no supere `k`.
3. Cuando una palabra ya no entra, justificar la linea acumulada.
4. Para justificar:
   - si hay una sola palabra, usar `ljust(k)`;
   - si hay varias, repartir los espacios entre huecos.
5. Empezar una nueva linea con la palabra que no entro.
6. Al final, justificar la ultima linea pendiente con las mismas reglas del enunciado.

## Pistas

- No confundas cantidad de palabras con cantidad de huecos: si hay `n` palabras, hay `n - 1` huecos.
- El largo de una linea final debe ser siempre exactamente `k`.
- Para el ejemplo, `"the  quick brown"` tiene dos huecos: uno recibe dos espacios y el otro uno.
- Proba primero construir bien las lineas; despues ocupate del reparto exacto de espacios.

## Casos de prueba incluidos

- El ejemplo del enunciado.
- Una linea con una sola palabra.

## Complejidad esperada

- Tiempo: `O(n)`, sin contar el costo de construir los strings finales.
- Espacio: `O(n)` para la salida.

## Codigo

[Resolver aca](028_text_justification.py)
