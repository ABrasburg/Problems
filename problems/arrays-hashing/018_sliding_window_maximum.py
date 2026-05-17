# This problem was asked by Google.

# Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.
#For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)
# Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results.
# You can simply print them out as you compute them.

def max_subarray(arr, k): # Fuerza bruta O(n*k)
    """
    Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.
    """
    if len(arr) == 0 or k == 0:
        return []
    if k > len(arr):
        return []
    
    max_values = []
    for i in range(len(arr) - k + 1): # O(n)
        max_values.append(max(arr[i:i+k])) # O(k)
    
    return max_values

print(max_subarray([10, 5, 2, 7, 8, 7], 3)) # [10, 7, 8, 8]

# Un deque es una estructura de datos que permite agregar y quitar elementos de ambos extremos.
# Agregar elementos a un deque es O(1) y quitar elementos de un deque es O(1).
from collections import deque

def max_of_subarrays(lst, k): # O(n)
    q = deque()
    for i in range(k): # O(k)
        while q and lst[i] >= lst[q[-1]]:
            q.pop()
        q.append(i)

    # Loop invariant: q is a list of indices where their corresponding values are in descending order.
    for i in range(k, len(lst)): # O(n)
        print(lst[q[0]])
        while q and q[0] <= i - k:
            q.popleft()
        while q and lst[i] >= lst[q[-1]]:
            q.pop()
        q.append(i)
    print(lst[q[0]])

max_of_subarrays([10, 5, 2, 7, 8, 7], 3) # [10, 7, 8, 8]