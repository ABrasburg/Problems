# This problem was asked by Google.

# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
# In this example, assume nodes with the same value are the exact same node objects.
# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def length(head):
    if not head:
        return 0
    return 1 + length(head.next)
    
def find_intersection(list1, list2):
    m,n = length(list1), length(list2)
    if m > n:
        for _ in range(m - n):
            list1 = list1.next
    else:
        for _ in range(n - m):
            list2 = list2.next
    while list1 and list2:
        if list1 == list2:
            return list1
        list1 = list1.next
        list2 = list2.next
    return None