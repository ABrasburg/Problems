# 010 - Job Scheduler

## Resumen

Implementar un scheduler que ejecute una funcion despues de una cantidad dada de milisegundos.

## Idea

La parte importante es que programar el trabajo no deberia bloquear al llamador. Por eso la funcion diferida corre en otro hilo: ese hilo duerme el tiempo indicado y despues ejecuta el callback.

Para una version productiva, tambien habria que manejar cancelacion, errores del callback y reutilizacion de threads, pero para el ejercicio alcanza con crear una tarea independiente.

## Paso a paso

- `delay(f, n)` recibe la funcion y milisegundos.
- Crear una funcion interna que duerma `n / 1000` segundos.
- Luego llamar a `f`.
- Ejecutar esa funcion interna en un thread separado.

## Complejidad

- Programar tarea: `O(1)`.
- Espacio: `O(1)` por tarea programada, mas el costo del hilo.

## Codigo

[Ver solucion](010_job_scheduler.py)
