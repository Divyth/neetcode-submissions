class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i, currentSum):
            if i == len(nums):
                return 1 if currentSum == target else 0
            
            if (i, currentSum) in dp:
                return dp[(i, currentSum)]

            positive = dfs(i+1, currentSum + nums[i])
            negative = dfs(i+1, currentSum - nums[i])

            dp[(i, currentSum)] = positive + negative
            return dp[(i, currentSum)]

        return dfs(0,0)
        