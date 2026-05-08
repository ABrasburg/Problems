class Solution(object):
    def _twoSum(self, nums, target): # O(N)
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i):
                if (nums[i] + nums[j]) == target:
                    return [i, j]
                
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dicc = {}
        for i in range(len(nums)):
            if target - nums[i] in dicc:
                return [i, dicc[target - nums[i]]]
            dicc[nums[i]] = i
        