class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xorOg = len(nums)
        for i in range(len(nums)):
            xorOg ^= i
        xor =  0
        for i in range(len(nums)):
            xor ^= nums[i]

        return xorOg ^ xor
        