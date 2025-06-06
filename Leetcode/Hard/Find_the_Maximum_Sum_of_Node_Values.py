from typing import List

class Solution:
    def maxSumOfNodes(self, index, isEven, nums, k, memo):
        if index == len(nums):
            # If the operation is performed on an odd number of elements return INT_MIN
            return 0 if isEven == 1 else -float("inf")
        if memo[index][isEven] != -1:
            print(f"  Memoized value: {memo[index][isEven]}")
            return memo[index][isEven]
        print(f"Index: {index}, isEven: {isEven}, nums[index]: {nums[index]}")

        # No operation performed on the element
        noXorDone = nums[index] + self.maxSumOfNodes(index + 1, isEven, nums, k, memo)
        # XOR operation is performed on the element
        xorDone = (nums[index] ^ k) + self.maxSumOfNodes(
            index + 1, isEven ^ 1, nums, k, memo
        )
        print(f"Index: {index}")
        print(f"  No XOR: {noXorDone}, XOR: {xorDone}")

        # Memoize and return the result
        memo[index][isEven] = max(xorDone, noXorDone)
        return memo[index][isEven]

    def maximumValueSum_Dynamic_Memoization(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        memo = [[-1] * 2 for _ in range(len(nums))]
        return self.maxSumOfNodes(0, 1, nums, k, memo)
    
    def maximumValueSum_Dynamic_Tabulation(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[n][1] = 0
        dp[n][0] = -float('inf')
        
        for index in range(n - 1, -1, -1):
            for isEven in range(2):
                # Case 1: we perform an operation on this element.
                performOperation = dp[index + 1][isEven ^ 1] + (nums[index] ^ k)
                # Case 2: we don't perform operation on this element.
                dontPerformOperation = dp[index + 1][isEven] + nums[index]

                dp[index][isEven] = max(performOperation, dontPerformOperation)
        
        return dp[0][1]
    
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # Se puede hacer XOR a cualquier cantidad par de nodos sin necesidad de que sean adyacentes
        suma = 0
        cant_xor = 0
        minimoPositivo = 1 << 30
        maximoNegativo = -1 * (1 << 30)

        for nodo in nums:
            xor = nodo ^ k
            suma += nodo
            cambio = xor - nodo
            if cambio > 0:
                cant_xor += 1
                minimoPositivo = min(minimoPositivo, cambio)
                suma += cambio
            else:
                maximoNegativo = max(maximoNegativo, cambio)

        if (cant_xor % 2) == 0:
            return suma
        return max(suma-minimoPositivo, suma+maximoNegativo)

sol = Solution()
nums = [1, 2, 1]
k = 3
edges = [[0, 1], [0, 2]]
print(sol.maximumValueSum(nums, k, edges))
