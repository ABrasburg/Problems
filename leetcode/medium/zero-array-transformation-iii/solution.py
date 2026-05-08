import heapq

class Solution(object):
    def maxRemoval(self, nums, queries):
        queries.sort(key=lambda x: x[0])
        available = []
        assigned = []
        count = 0
        k = 0
        for time in range(len(nums)):
            while assigned and assigned[0] < time:
                heapq.heappop(assigned)
            while k < len(queries) and queries[k][0] <= time:
                heapq.heappush(available, -queries[k][1])
                k += 1
            while len(assigned) < nums[time] and available and -available[0] >= time:
                heapq.heappush(assigned, -heapq.heappop(available))
                count += 1
            if len(assigned) < nums[time]:
                return -1
        return len(queries) - count
    
sol = Solution()
# nums = [2,0,2]
# queries = [[0,2],[0,2],[1,1]]
# print(sol.maxRemoval(nums, queries))  # Output: 1
# nums = [1,1,1,1]
# queries = [[0,1],[1,2],[2,3],[0,3]]
# print(sol.maxRemoval(nums, queries))  # Output: 2
# nums = [1,2,3,4]
# queries = [[0,3]]
# print(sol.maxRemoval(nums, queries))  # Output: -1
# nums = [0,0,1,1,0,0]
# queries = [[2,3],[0,2],[3,5]]
# print(sol.maxRemoval(nums, queries))  # Output: 2
nums = [1,1,0]
queries = [[0,2],[1,2],[1,2],[1,1],[2,2],[2,2],[0,2],[0,2],[0,0]]
print(sol.maxRemoval(nums, queries))  # Output: 4