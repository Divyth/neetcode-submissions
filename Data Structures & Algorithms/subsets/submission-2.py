class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def getAllSubsets(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i]) # include
            getAllSubsets(i+1)

            subset.pop() # exclude ie backtract 
            getAllSubsets(i+1)

        getAllSubsets(0)

        return res
        
