class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n= len(nums)
        minSum = float('inf')
        for i in range(n):
            currentSum = 0
            for j in range(i , n):
                
                currentSum += nums[j]
                if currentSum >= target:
                    minSum = min(minSum, j - i + 1)
                    break

        return 0 if minSum == float('inf') else minSum
                
        