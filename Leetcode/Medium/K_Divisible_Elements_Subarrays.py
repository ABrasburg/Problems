class Solution(object):
    def countDistinct(self, nums, k, p):
        """
        :type nums: List[int]
        :type k: int
        :type p: int
        :rtype: int
        """
        seen = set()
        n = len(nums)
        
        for i in range(n):
            count = 0
            current = []
            for j in range(i, n):
                if nums[j] % p == 0:
                    count += 1
                if count > k:
                    break
                current.append(nums[j])
                seen.add(tuple(current))
        
        return len(seen)