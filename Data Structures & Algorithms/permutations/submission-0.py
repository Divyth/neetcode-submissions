class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        visited = [False]* len(nums)

        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if visited[i]:
                    continue

                visited[i] = True
                path.append(nums[i])

                backtrack()

                path.pop()
                visited[i] = False

        backtrack()
        return res


        