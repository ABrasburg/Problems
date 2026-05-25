# This problem was asked by Facebook.
#
# Given an array of non-negative integers representing an elevation map,
# compute how many units of water remain trapped after raining.
# The solution should run in O(n) time and O(1) space.

def trapped_water(heights):
    if not heights:
        return 0
    max_height = 0
    max_index = 0
    for i in range(len(heights)):
        if heights[i] > max_height:
            max_height = heights[i]
            max_index = i
    water = 0

    max_left = heights[0]
    for i in range(1, max_index):
        if heights[i] < max_left:
            water += max_left - heights[i]
        else:
            max_left = heights[i]

    max_right = heights[-1]
    for i in range(len(heights) - 2, max_index, -1):
        if heights[i] < max_right:
            water += max_right - heights[i]
        else:
            max_right = heights[i]

    return water


if __name__ == "__main__":
    assert trapped_water([2, 1, 2]) == 1
    assert trapped_water([3, 0, 1, 3, 0, 5]) == 8
    assert trapped_water([]) == 0
