# 016 - Order Log

## Resumen

Disenar una estructura que registre ids de ordenes y permita consultar el ultimo `i`-esimo registro.

## Idea

Como solo hace falta recordar una cantidad fija de ordenes recientes, no conviene crecer una lista indefinidamente. Un buffer circular reutiliza las mismas posiciones: cada nueva orden se escribe en `current_index % capacity`.

La consulta del ultimo `i`-esimo elemento se transforma en una resta desde el indice actual, tambien usando modulo para envolver al principio del arreglo.

## Paso a paso

- Reservar un arreglo de tamano fijo.
- Guardar cada nueva orden en la posicion circular actual.
- Avanzar el contador global.
- Para consultar el ultimo `i`, calcular la posicion relativa desde el ultimo elemento insertado.

## Complejidad

- Agregar orden: `O(1)`.
- Consultar orden reciente: `O(1)`.
- Espacio: `O(n)`, donde `n` es la capacidad del log.

## Codigo

[Ver solucion](016_order_log.py)
