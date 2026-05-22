# Programming Problems

Coleccion de problemas de programacion en Python, organizada por patrones de
resolucion. Cada problema combina una explicacion breve, pistas de enfoque y un
archivo ejecutable con asserts simples.

El objetivo es practicar con problemas chicos pero densos: estructuras de datos,
recursion, ventanas deslizantes, grafos, programacion dinamica, parsing y
razonamiento probabilistico.

## Como Leer

1. Elegi un tema en la tabla de temas.
2. Abri el `.md` del problema para leer el enunciado, la intuicion y las pistas.
3. Intentá resolverlo en el `.py`.
4. Ejecutá el archivo para correr los asserts.

## Convenciones

- `problems/<tema>/<numero>_<slug>.md`: explicacion, intuicion, pistas y complejidad.
- `problems/<tema>/<numero>_<slug>.py`: implementacion o archivo de trabajo.
- Los asserts al final de cada archivo sirven como verificacion rapida.
- Los problemas en progreso pueden tener `pass` hasta que la solucion este lista.

## Temas

| Tema | Problemas | Enfoque |
|---|---:|---|
| [Arrays y hashing](problems/arrays-hashing/README.md) | 6 | Arreglos, hashing, ventanas e intervalos |
| [Strings y parsing](problems/strings-parsing/README.md) | 9 | Strings, parsing, prefijos y expresiones |
| [Arboles y grafos](problems/trees-graphs/README.md) | 4 | Arboles, grafos, grillas y recorridos |
| [Programacion dinamica](problems/dynamic-programming/README.md) | 3 | Recurrencias y optimizacion |
| [Estructuras de datos](problems/data-structures/README.md) | 4 | Listas, pares y estructuras especificas |
| [Probabilidad y aleatoriedad](problems/probability-randomized/README.md) | 2 | Muestreo y algoritmos probabilisticos |
| [Sistemas y concurrencia](problems/systems-concurrency/README.md) | 1 | Scheduling, timers y concurrencia |

## Destacados

- [Sliding Window Maximum](problems/arrays-hashing/018_sliding_window_maximum.md): cola doble para mantener maximos en ventanas.
- [Locking Binary Tree](problems/trees-graphs/024_locking_binary_tree.md): estado agregado para bajar operaciones de `O(m + h)` a `O(h)`.
- [Regular Expression Matching](problems/strings-parsing/025_regular_expression_matching.md): recursion con memoizacion sobre string y patron.
- [Balanced Brackets](problems/strings-parsing/027_balanced_brackets.md): pila para validar cierres correctamente anidados.

## Indice

| # | Problema | Tema | Estado |
|---|---|---|---|
| 001 | [Two Sum](problems/arrays-hashing/001_two_sum.md) | Arrays y hashing | Resuelto |
| 002 | [Product Array](problems/arrays-hashing/002_product_array.md) | Arrays y hashing | Resuelto |
| 003 | [Serialize and Deserialize Tree](problems/trees-graphs/003_serialize_deserialize_tree.md) | Arboles y grafos | Resuelto |
| 004 | [First Missing Positive](problems/arrays-hashing/004_first_missing_positive.md) | Arrays y hashing | Resuelto |
| 005 | [Cons, Car and Cdr](problems/data-structures/005_cons_car_cdr.md) | Estructuras de datos | Resuelto |
| 006 | [XOR Linked List](problems/data-structures/006_xor_linked_list.md) | Estructuras de datos | Resuelto |
| 007 | [Decode Ways](problems/strings-parsing/007_decode_ways.md) | Strings y parsing | Resuelto |
| 008 | [Unival Tree Count](problems/trees-graphs/008_unival_tree_count.md) | Arboles y grafos | Resuelto |
| 009 | [Max Non-Adjacent Sum](problems/dynamic-programming/009_max_non_adjacent_sum.md) | Programacion dinamica | Resuelto |
| 010 | [Job Scheduler](problems/systems-concurrency/010_job_scheduler.md) | Sistemas y concurrencia | Resuelto |
| 011 | [Autocomplete](problems/strings-parsing/011_autocomplete.md) | Strings y parsing | Resuelto |
| 012 | [Staircase](problems/dynamic-programming/012_staircase.md) | Programacion dinamica | Resuelto |
| 013 | [Longest Substring With K Distinct](problems/strings-parsing/013_longest_substring_k_distinct.md) | Strings y parsing | Resuelto |
| 014 | [Estimate Pi](problems/probability-randomized/014_estimate_pi.md) | Probabilidad y aleatoriedad | Resuelto |
| 015 | [Reservoir Sampling](problems/probability-randomized/015_reservoir_sampling.md) | Probabilidad y aleatoriedad | Resuelto |
| 016 | [Order Log](problems/arrays-hashing/016_order_log.md) | Arrays y hashing | Resuelto |
| 017 | [Longest File Path](problems/strings-parsing/017_longest_file_path.md) | Strings y parsing | Resuelto |
| 018 | [Sliding Window Maximum](problems/arrays-hashing/018_sliding_window_maximum.md) | Arrays y hashing | Resuelto |
| 019 | [Paint House](problems/dynamic-programming/019_paint_house.md) | Programacion dinamica | Resuelto |
| 020 | [Linked List Intersection](problems/data-structures/020_linked_list_intersection.md) | Estructuras de datos | Resuelto |
| 021 | [Meeting Rooms](problems/arrays-hashing/021_meeting_rooms.md) | Arrays y hashing | Resuelto |
| 022 | [Word Break](problems/strings-parsing/022_word_break.md) | Strings y parsing | Resuelto |
| 023 | [Shortest Path Grid](problems/trees-graphs/023_shortest_path_grid.md) | Arboles y grafos | Resuelto |
| 024 | [Locking Binary Tree](problems/trees-graphs/024_locking_binary_tree.md) | Arboles y grafos | Resuelto |
| 025 | [Regular Expression Matching](problems/strings-parsing/025_regular_expression_matching.md) | Strings y parsing | Resuelto |
| 026 | [Remove Kth Last Linked List Node](problems/data-structures/026_remove_kth_last_linked_list.md) | Estructuras de datos | Resuelto |
| 027 | [Balanced Brackets](problems/strings-parsing/027_balanced_brackets.md) | Strings y parsing | Resuelto |
| 028 | [Text Justification](problems/strings-parsing/028_text_justification.md) | Strings y parsing | Resuelto |
| 029 | [Run-Length Encoding](problems/strings-parsing/029_run_length_encoding.md) | Strings y parsing | En progreso |
