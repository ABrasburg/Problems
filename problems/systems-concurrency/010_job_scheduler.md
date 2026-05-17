# 010 - Job Scheduler

## Resumen

Implementar un scheduler que ejecute una funcion despues de una cantidad dada de milisegundos.

## Idea

La solucion crea una tarea diferida: espera `n / 1000` segundos y luego invoca la funcion. Usar un hilo separado evita bloquear al llamador mientras pasa el tiempo.

## Complejidad

- Programar tarea: `O(1)`.
- Espacio: `O(1)` por tarea programada, mas el costo del hilo.

## Codigo

[Ver solucion](010_job_scheduler.py)
