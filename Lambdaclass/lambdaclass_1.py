#  Deserializar puntos
# Dada una secuencia de puntos expresada como una tira de números de la forma x0y0x1y1x2y2..., implementar una función que reciba esa tira de números y devuelva
# una lista de puntos de la forma [(x0, y0), (x1, y1), (x2, y2), ...]. Cada coordenada xi e yi está expresada en la tira de números como un número de 8 dígitos.

# Ejemplo
# Dada la tira de números 12345678000000010234321242424242, la función debería devolver los puntos (12345678, 1) y (2343212, 42424242).

def deserializar(puntos):
    puntos_aux =  puntos
    lista = []
    while len(puntos_aux) > 0:
        primero = int(puntos_aux[0:8])
        segundo = int(puntos_aux[8:16])
        lista.append((primero, segundo))
        puntos_aux = puntos_aux[16:]
    return lista

print(deserializar("12345678000000010234321242424242"))