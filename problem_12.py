# This problem was asked by Amazon.
# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways 
# ou can climb the staircase. The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:
# 1, 1, 1, 1
#2, 1, 1
#1, 2, 1
#1, 1, 2
#2, 2

#What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, 
# you could climb 1, 3, or 5 steps at a time.

def escalera_dos_pasos(n):
    if n <= 2:
        return n
    return escalera_dos_pasos(n-1) + escalera_dos_pasos(n-2)

def ecalera_dos_pasos_dinamica(n):
    if n <= 2:
        return n
    lista = [0] * (n+1)
    lista[1] = 1
    lista[2] = 2
    for i in range (3, n+1):
        lista[i] = lista[i-1] + lista[i-2]
    return lista[n]

def escalera_dos_pasos_poco_espacio(n):
    a, b = 1, 2
    for _ in range(n - 1):
        a, b = b, a + b
    return a

def escalera_muchos_pasos(n, pasos):
    if n <= 2:
        return n
    lista = [0] * (n+1)
    lista[1] = 1
    pasos.sort()
    for i in range (2, n+1):
        parcial = 0
        for paso in pasos:
            if paso <= i:
                parcial += lista[i-paso]
        if i in pasos:
            parcial += 1
        lista[i] = parcial
    return lista[n]

print(escalera_dos_pasos(5))
print(ecalera_dos_pasos_dinamica(5))
print(escalera_muchos_pasos(5, [1,2]))