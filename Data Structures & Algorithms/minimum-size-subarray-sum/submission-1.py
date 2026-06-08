class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        minSum = 0
        window = float('inf')

        for right in range(len(nums)):
            minSum += nums[right]

            while minSum >= target:
                window = min(right- left +1, window)
                minSum -= nums[left]
                left += 1

        return 0 if window == float('inf') else window
            


                
        