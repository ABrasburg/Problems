import random

class Node:
    def __init__(self, value):
        self.value = value
        self.izq = None
        self.der = None
        self.cantidad = 1

class ABBA:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        insertado  = False
        actual = self.root
        while not insertado:
            p = (actual.cantidad+1)
            if random.randint(1, p) == 1:
                nuevo = Node(value)
                if value < actual.value:
                    nuevo.izq = actual.izq
                    actual.izq = nuevo
                else:
                    nuevo.der = actual.der
                    actual.der = nuevo
                insertado = True
                if actual.value == self.root.value:
                    self.root = nuevo
            else:
                actual.cantidad += 1
                if value < actual.value:
                    if actual.izq is None:
                        actual.izq = Node(value)
                        insertado = True
                    else:
                        actual = actual.izq
                else:
                    if actual.der is None:
                        actual.der = Node(value)
                        insertado = True
                    else:
                        actual = actual.der

    def search(self, value):
        return self._search(self.root, value)
    
    def _search(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self._search(node.izq, value)
        else:
            return self._search(node.der, value)
        
    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return None
        if node.value == value:
            if node.izq is None:
                return node.der
            if node.der is None:
                return node.izq
            if random.randint(0, node.cantidad) == 0:
                node.izq = self._delete(node.izq, value)
            else:
                node.der = self._delete(node.der, value)
            return node
        if value < node.value:
            node.izq = self._delete(node.izq, value)
        else:
            node.der = self._delete(node.der, value)