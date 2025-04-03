import random

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.abajo = None

class SkipList:
    def __init__(self):
        self.heads = []
        self.altura = 0
        self.iniciar_heads()

    def iniciar_heads(self):
        self.altura = 1
        self.heads = [Node(-float('inf'))]
        self.heads[0].next = Node(float('inf'))

    def insert(self, value):
        current = self.heads[self.altura-1]
        lista_actual = self.altura-1
        while lista_actual >= 0:
            while current.next.value < value:
                current = current.next
            if current.abajo:
                current = current.abajo
                lista_actual -= 1
            else:
                break
        nuevo = Node(value)
        nuevo.next = current.next
        current.next = nuevo
        altura_actual = 1
        while random.random() < 0.5:
            nuevo_nodo = Node(value)
            nuevo_nodo.abajo = nuevo
            nuevo = nuevo_nodo
            if altura_actual == self.altura:
                self.altura += 1
                nuevo_head = Node(-float('inf'))
                nuevo_head.next = nuevo
                nuevo.next = Node(float('inf'))
                self.heads.append(nuevo_head)
            else:
                current = self.heads[self.altura-altura_actual-1]
                while current.next.value < value:
                    current = current.next
                nuevo.next = current.next
                current.next = nuevo

    def search(self, value):
        current = self.heads[self.altura-1]
        lista_actual = self.altura-1
        while lista_actual >= 0:
            while current.next.value < value:
                current = current.next
            if current.abajo:
                current = current.abajo
                lista_actual -= 1
            else:
                break
        return current.next.value == value
    
    def delete(self, value):
        current = self.heads[self.altura-1]
        lista_actual = self.altura-1
        while lista_actual >= 0:
            while current.next.value < value:
                current = current.next
            if current.abajo:
                current = current.abajo
                lista_actual -= 1
            else:
                break
        if current.next.value == value:
            current.next = current.next.next
            return True
        return False
    
# Tests
s = SkipList()
s.insert(3)
s.insert(6)
s.insert(7)
s.insert(9)
s.insert(12)
s.insert(19)
s.insert(17)
s.insert(26)
s.insert(21)
s.insert(25)
assert s.search(19)