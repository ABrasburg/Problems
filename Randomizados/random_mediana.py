# Elegir la mediana de un arreglo
import random

def _elegir_posicion_k_si_ordenado(S, k): # O(n) en promedio y O(n^2) en el peor caso pero es muy raro que pase
    pivot = elegir_pivot(S, k)
    menor =  []
    mayor = []
    for elem in S:
        if elem < pivot:
            menor.append(elem)
        elif elem > pivot:
            mayor.append(elem)
    if len(menor) == k-1:
        return pivot
    elif len(menor) >= k:
        return _elegir_posicion_k_si_ordenado(menor, k)
    else:
        return _elegir_posicion_k_si_ordenado(mayor, k-len(menor)-1)
    
def elegir_pivot(S, k):
    return random.choice(S)

def elegir_pivote_mejorado(S, k):
    uno = random.choice(S)
    dos = random.choice(S)
    tres = random.choice(S)
    return sorted([uno, dos, tres])[1]