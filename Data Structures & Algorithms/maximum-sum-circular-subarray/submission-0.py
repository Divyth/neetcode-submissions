class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        minSum = maxSum = nums[0]

        currMin = 0
        currMax = 0

        for num in nums:
            total += num

            currMax = max(num, num + currMax)
            maxSum = max(maxSum, currMax)

            currMin = min(num, num + currMin)
            minSum = min(minSum, currMin)

        if maxSum < 0:
            return maxSum

        return max(maxSum , total - minSum)
