import random

class Node:
    def __init__(self, value):
        self.value = value
        self.izq = None
        self.der = None

class Treap:
    def __init__(self):
        self.root = None

    def insert(self, value):
        priority = random.random()
        self.root = self._insert(self.root, value, priority)

    def _insert(self, node, value, priority):
        if node is None:
            return Node(value)
        if value < node.value:
            node.izq = self._insert(node.izq, value, priority)
            if node.izq.priority > node.priority:
                node = self._rotate_der(node)
        else:
            node.der = self._insert(node.der, value, priority)
            if node.der.priority > node.priority:
                node = self._rotate_izq(node)
        return node

    def _rotate_der(self, node):
        temp = node.izq
        node.izq = temp.der
        temp.der = node
        return temp

    def _rotate_izq(self, node):
        temp = node.der
        node.der = temp.izq
        temp.izq = node
        return temp

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
            if node.izq is None and node.der is None:
                return None
            if node.izq is None:
                node = self._rotate_izq(node)
            elif node.der is None:
                node = self._rotate_der(node)
            else:
                if node.izq.priority > node.der.priority:
                    node = self._rotate_der(node)
                else:
                    node = self._rotate_izq(node)
            return self._delete(node, value)
        if value < node.value:
            node.izq = self._delete(node.izq, value)
        else:
            node.der = self._delete(node.der, value)
        return node
