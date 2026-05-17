# 016 - Order Log

## Resumen

Disenar una estructura que registre ids de ordenes y permita consultar el ultimo `i`-esimo registro.

## Idea

Como solo interesa una ventana fija de los ultimos eventos, alcanza con un buffer circular. Cada nueva orden pisa la posicion mas antigua cuando se supera la capacidad.

## Complejidad

- Agregar orden: `O(1)`.
- Consultar orden reciente: `O(1)`.
- Espacio: `O(n)`, donde `n` es la capacidad del log.

## Codigo

[Ver solucion](016_order_log.py)
