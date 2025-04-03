# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array 
# except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].

def mult_except_self(lista):
    mult = 1
    for i in lista:
        mult *= i
    return [mult//i for i in lista]

def mult_except_self_without_division(lista): # O(n^2)
    result = []
    for i in range(len(lista)):
        result.append(1)
        for j in range(len(lista)):
            if i != j:
                result[i] *= lista[j]
    return result

def mult_except_self_without_division_optimized(lista): # O(n)
    n = len(lista)
    left = [1] * n
    right = [1] * n
    result = [1] * n
    for i in range(1, n):
        left[i] = left[i-1] * lista[i-1]
    for i in range(n-2, -1, -1):
        right[i] = right[i+1] * lista[i+1]
    for i in range(n):
        result[i] = left[i] * right[i]

print(mult_except_self_without_division_optimized([1, 2, 3, 4, 5]))