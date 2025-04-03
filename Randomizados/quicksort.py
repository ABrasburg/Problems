from random_mediana import elegir_pivote_mejorado

def quicksort(S):
    if len(S) <= 1:
        return S
    pivot = elegir_pivote_mejorado(S, len(S)//2)
    menores = []
    mayores = []
    buen_pivote = False
    while not buen_pivote:
        for elem in S:
            if elem < pivot:
                menores.append(elem)
            elif elem > pivot:
                mayores.append(elem)
        if len(menores) >= len(S)//4 and len(mayores) >= len(S)//4:
            buen_pivote = True
    return quicksort(menores) + [pivot] + quicksort(mayores)
    