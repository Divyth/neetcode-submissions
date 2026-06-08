class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nummap = {}

        for i, n in enumerate(nums):
            complement = target - n 

            if complement in nummap:
                return [nummap[complement],i]
            nummap[n] = i
        return []