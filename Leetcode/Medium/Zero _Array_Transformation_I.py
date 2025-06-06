class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        diff = [0] * (len(nums) + 1)
        for start, end in queries:
            diff[start] += 1
            diff[end + 1] -= 1
        decrement = 0
        for i in range(len(nums)):
            decrement += diff[i]
            if decrement < nums[i]:
                return False
        return True