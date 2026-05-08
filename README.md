# Problemas de Programacion y Estructuras de Datos

Coleccion de ejercicios de programacion, soluciones de plataformas online,
estructuras de datos e implementaciones de algoritmos.

## Estructura

```text
daily-coding-problem/
  001_two_sum.py
  002_product_array.py
  ...
  024_locking_binary_tree.py

leetcode/
  easy/
    two-sum/
      solution.py
  medium/
  hard/

hackerrank/
  sql/
    easy/

data-structures/
  randomized_binary_search_tree.py
  skip_list.py
  treap.py

algorithms/
  randomized/
    quicksort.py
    random_median.py
```

## Convenciones

- `daily-coding-problem/`: problemas numerados con formato `NNN_slug.py`.
- `leetcode/`: problemas separados por dificultad. Cada problema vive en una carpeta propia y sus archivos se llaman `solution.<extension>`.
- `hackerrank/`: ejercicios separados por dominio, dificultad y nombre del problema.
- `data-structures/`: implementaciones reutilizables de estructuras de datos.
- `algorithms/`: algoritmos sueltos agrupados por tecnica o familia.

## Ejecucion

Los archivos de Python se pueden ejecutar directamente cuando incluyen casos de
prueba o ejemplos:

```bash
python3 daily-coding-problem/024_locking_binary_tree.py
python3 leetcode/easy/two-sum/solution.py
python3 algorithms/randomized/quicksort.py
```
