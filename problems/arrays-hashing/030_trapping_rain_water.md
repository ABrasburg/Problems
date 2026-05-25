# 030 - Trapping Rain Water

## Resumen

Dado un array de enteros no negativos que representa un mapa de elevacion, calcular cuantas unidades de agua quedan atrapadas despues de llover.

Cada posicion del array representa una pared de ancho `1`, y el valor representa su altura.

Ejemplos:

```text
[2, 1, 2] -> 1
[3, 0, 1, 3, 0, 5] -> 8
```

En el segundo caso se acumulan:

- `3` unidades sobre la posicion con altura `0`;
- `2` unidades sobre la posicion con altura `1`;
- `3` unidades sobre la otra posicion con altura `0`.

Total: `8`.

## Objetivo

Completar `trapped_water(heights)` en el archivo de Python.

La solucion esperada debe ser:

- Tiempo: `O(n)`.
- Espacio extra: `O(1)`.

## Pistas

- En una posicion `i`, el agua que puede quedar atrapada depende de la pared mas alta a la izquierda y la pared mas alta a la derecha.
- La cantidad de agua sobre `i` esta limitada por la menor de esas dos paredes.
- Una solucion con arrays auxiliares de maximos izquierda/derecha es mas directa, pero usa `O(n)` espacio.
- Para lograr `O(1)` espacio, podes usar el maximo global como punto de separacion o usar dos punteros.

## Explicacion

La intuicion central es que el agua en una posicion necesita estar contenida por ambos lados. Si a la izquierda la mejor pared tiene altura `L` y a la derecha la mejor pared tiene altura `R`, entonces el nivel maximo de agua sobre esa posicion es:

```text
min(L, R)
```

La cantidad que realmente se suma es:

```text
min(L, R) - heights[i]
```

siempre que ese valor sea positivo.

Una primera forma de pensarlo es construir dos listas:

- `left_max[i]`: la pared mas alta vista desde la izquierda hasta `i`;
- `right_max[i]`: la pared mas alta vista desde la derecha hasta `i`.

Despues se recorre cada posicion y se suma `min(left_max[i], right_max[i]) - heights[i]`.

Esa idea es `O(n)` en tiempo, pero usa `O(n)` espacio. Sirve para entender el problema, aunque no cumple la restriccion final.

Para bajar a `O(1)` espacio, hay que evitar guardar todos los maximos. Una manera es ubicar la pared mas alta del array. Esa pared funciona como limite seguro:

- A su izquierda, siempre existe una pared suficientemente alta a la derecha.
- A su derecha, siempre existe una pared suficientemente alta a la izquierda.

Entonces se puede recorrer desde la izquierda hasta el maximo manteniendo solo `left_max`, y desde la derecha hasta el maximo manteniendo solo `right_max`.

En cada paso:

```text
agua += maximo_actual - altura_actual
```

y luego se actualiza el maximo actual si la pared presente es mas alta.

## Casos de prueba incluidos

- Un valle simple: `[2, 1, 2]`.
- Varios huecos con distintas alturas: `[3, 0, 1, 3, 0, 5]`.
- Array vacio.

## Codigo

[Resolver aca](030_trapping_rain_water.py)
