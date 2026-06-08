class Solution:
    def combinationSum(self, nums, target):
        res = []

        def dfs(i, path, remaining):

            # found valid combination
            if remaining == 0:
                res.append(path.copy())
                return

            # invalid case
            if i >= len(nums) or remaining < 0:
                return

            # include current number (allow multiple use)
            path.append(nums[i])
            dfs(i, path, remaining - nums[i])

            # backtrack
            path.pop()

            #  exclude current number
            dfs(i + 1, path, remaining)

        dfs(0, [], target)
        return res