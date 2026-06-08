class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur = 0
        maxone = 0

        for i in nums:
            if i == 1:
                cur += 1
                maxone = max(maxone, cur)
            else:
                cur = 0
        return maxone
        