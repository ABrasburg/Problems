# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Si se  puede sumar de cualquier manera
def add_up_to_k(lst, obj):
    # Filtro los elementos que son mayores a k
    lst = list(filter(lambda x: x <= obj, lst))
    matriz = []
    # ordeno de menor a mayor
    lst.sort()
    # Tiene x=k  y  y=len(lst) e inicialmente va un 0 en todas las posiciones
    for x in range(obj+1):
        matriz.append([0]*len(lst))
    for index, peso_numero in list(enumerate(lst)):
        if peso_numero == obj:
            return True
        for peso in range(obj+1):
            if peso_numero > peso:
                matriz[peso][index] = matriz[peso][index-1]
                continue
            if index == 0:
                matriz[peso][index] = peso_numero
            else:
                sin_elemento = matriz[peso][index-1]
                con_elemento = matriz[peso-peso_numero][index-1] + peso_numero
                if con_elemento == obj:
                    return True
                if con_elemento > peso:
                    matriz[peso][index] = sin_elemento
                else:
                    matriz[peso][index] = max(con_elemento, sin_elemento)
    return False

# Solo c on 2 numeros
def find_pair_sum(numbers, k): # Hashing
    seen = set()
    for num in numbers:
        complement = k - num
        if complement in seen:
            return True
        seen.add(num)
    return False