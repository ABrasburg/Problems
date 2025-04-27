# This problem was asked by Google.
# Suppose we represent our file system by a string in the following manner:
# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

#dir
#    subdir1
#    subdir2
#        file.ext
# The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

#dir
#    subdir1
#        file1.ext
#        subsubdir1
#    subdir2
#        subsubdir2
#            file2.ext
# The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1.
# subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

# We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above,
# the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

# Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If 
# there is no file in the system, return 0.

class Node:
    def __init__(self, nombre, padre=None):
        self.nombre = nombre
        self.largo = len(nombre)
        self.padre = padre
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def __str__(self):
        return self.nombre

def texto_a_arbol(texto): # O(n)
    """
    Convierte un texto en un árbol de directorios.
    """
    partes = texto.split('\n')
    padre = Node(partes[0])
    actual = padre
    cant_t_actual = 0
    partes.pop(0)
    for directorio in partes:
        cant_t = 0
        while '\t' in directorio:
            cant_t += 1
            directorio = directorio[1:]
        while cant_t <= cant_t_actual:
            cant_t_actual -= 1
            actual = actual.padre
        nuevo_nodo = Node(directorio)
        nuevo_nodo.padre = actual
        actual.hijos.append(nuevo_nodo)
        if '.' not in  nuevo_nodo.nombre:
            actual = nuevo_nodo
            cant_t_actual += 1
    return padre

def longest_path_to_file(texto): # O(n)
    def dfs(nodo, path_length):
        nonlocal max_length
        if '.' in nodo.nombre:
            max_length = max(max_length, path_length + len(nodo.nombre))
        for hijo in nodo.hijos:
            dfs(hijo, path_length + len(nodo.nombre) + 1)  # +1 para incluir el separador '/'

    arbol = texto_a_arbol(texto)
    max_length = 0
    dfs(arbol, 0)
    return max_length

texto = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'
print(longest_path_to_file(texto))
