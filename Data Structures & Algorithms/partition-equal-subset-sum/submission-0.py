class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)

        if totalSum % 2 != 0 :
            return False

        # now this becaomes normal subset, since 
        # sum // 2 subset exists ie, the remainig elements are part of other subset

        findSum = totalSum // 2

        dp = [[False] * (findSum + 1) for _ in range(len(nums)+1)]

        for i in range(len(nums)+1):
            dp[i][0] = True

        for i in range(1, len(nums)+1):
            for j in range(1, findSum+1):
                if nums[i-1] <= j:
                    dp[i][j] = (dp[i-1][j] or dp[i-1][j-nums[i-1]])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(nums)][findSum]