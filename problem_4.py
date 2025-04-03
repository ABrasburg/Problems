# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that 
# does not exist in the array. The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input  should give 3.

# You can modify the input array in-place.

def find_missing_positive(lst):
    if not lst:
        return -1
    first = 1
    hash = set()
    for i in lst:
        if i < 0:
            continue
        hash.add(i)
        if (first+1) in hash:
            number = first+1
            while number in hash:
                first = number
                number = number+1
    return first + 1

print(find_missing_positive([3,4,-1,1]))
print(find_missing_positive([1, 2, 0]))