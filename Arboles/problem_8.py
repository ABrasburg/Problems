# This problem was asked by Google.
# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees:

#   0
#  / \
# 1   0
#    / \
#   1   0
#  / \
# 1   1

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_uval(nodo, valor):
    if nodo.left == None and nodo.right == None:
        return nodo.val == valor
    derecha = True
    if nodo.right is not None:
        derecha = is_uval(nodo.right, valor)
    izquierda = True
    if nodo.left is not None:
        izquierda = is_uval(nodo.left, valor) 
    return derecha and izquierda

def cant_uval_subtree(nodo):
    cant = 0
    if is_uval(nodo, nodo.val):
        cant = 1
    izq = 0
    if nodo.left is not None:
        izq = cant_uval_subtree(nodo.left)
    der = 0
    if nodo.right is not None:
        der = cant_uval_subtree(nodo.right)
    return cant + izq + der

arbol = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
print(cant_uval_subtree(arbol)) # 5 y es O(n^2) porque se recorre el arbol y se revisa si es unival

# Otra forma de hacerlo es con un diccionario que guarde si es unival o no y la cantidad de unival subtrees
def helper(nodo):
        if nodo is None:
            return True, 0
        izq, cant_izq = helper(nodo.left)
        der, cant_der = helper(nodo.right)
        if izq and der:
            if nodo.left is not None and nodo.left.val != nodo.val:
                return False, cant_izq + cant_der
            if nodo.right is not None and nodo.right.val != nodo.val:
                return False, cant_izq + cant_der
            return True, cant_izq + cant_der + 1
        return False, cant_izq + cant_der

def cant_uval_subtree(nodo):
    _, cant = helper(nodo)
    return cant

print(cant_uval_subtree(arbol)) # 5 y es O(n) porque se recorre el arbol una sola vez