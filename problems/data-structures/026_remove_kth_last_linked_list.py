# This problem was asked by Google.
#
# Given a singly linked list and an integer k, remove the kth last element from
# the list in one pass and constant space.


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def to_list(self):
        values = []
        current = self
        while current:
            values.append(current.val)
            current = current.next
        return values


def from_list(values):
    head = None
    for value in reversed(values):
        head = Node(value, head)
    return head


def remove_kth_last(head, k):
    actual = head
    dist_k = head
    for i in range(k):
        dist_k = dist_k.next

    anterior = None
    while dist_k:
        anterior = actual
        actual = actual.next
        dist_k = dist_k.next
    anterior.next = actual.next
    return head


if __name__ == "__main__":
    head = from_list([1, 2, 3, 4, 5])
    head = remove_kth_last(head, 3)
    assert head.to_list() == [1, 2, 4, 5]

    head = from_list([1, 2, 3])
    head = remove_kth_last(head, 1)
    assert head.to_list() == [1, 2]
