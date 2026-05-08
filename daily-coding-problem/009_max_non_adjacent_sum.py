# This problem was asked by Airbnb.
# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Follow-up: Can you do this in O(N) time and constant space?

def juan_el_vago(sueldos): # O(n) en espacio
    lista = [0] * (len(sueldos)+1)
    lista[1] = sueldos[0]
    for posicion, trabajo in enumerate(sueldos[1:], 2):
        if posicion == 1:
            lista[posicion] = trabajo
        trabajo_hoy = trabajo + lista[posicion-2]
        no_trabajo_hoy = lista[posicion-1]
        lista[posicion] = max(trabajo_hoy, no_trabajo_hoy)
    return  lista[len(lista)-1]

def juan_el_vago_mejorado(sueldos): # O(1) en espacio
    if len(sueldos) <= 2:
        return max(0, max(sueldos))

    max_excluding_last= max(0, sueldos[0])
    max_including_last = max(max_excluding_last, sueldos[1])

    for num in sueldos[2:]:
        prev_max_including_last = max_including_last

        max_including_last = max(max_including_last, max_excluding_last + num)
        max_excluding_last = prev_max_including_last

    return max(max_including_last, max_excluding_last)

print(juan_el_vago([1000, 500, 200, 700]))
print(juan_el_vago_mejorado([1000, 500, 200, 700]))