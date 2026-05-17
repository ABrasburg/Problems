# 014 - Estimate Pi

## Resumen

Estimar el valor de pi usando puntos generados aleatoriamente.

## Idea

El metodo usa una simulacion Monte Carlo. Se generan puntos aleatorios dentro de un cuadrado de lado 2 centrado en el origen, y se cuenta cuantos caen dentro del circulo unitario.

La razon entre puntos dentro del circulo y puntos totales aproxima la razon entre areas. Como el area del circulo unitario es `pi` y el cuadrado tiene area `4`, se estima:

`pi ~= 4 * puntos_dentro / puntos_totales`

## Paso a paso

- Generar pares `(x, y)` aleatorios.
- Evaluar si `x^2 + y^2 < 1`.
- Contar aciertos.
- Multiplicar la proporcion por `4`.

## Complejidad

- Tiempo: `O(n)` para `n` muestras.
- Espacio: `O(1)`.

## Codigo

[Ver solucion](014_estimate_pi.py)
