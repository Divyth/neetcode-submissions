class Solution:
    def splitArray(self, nums: List[int], k: int):

        def canSplit(limit):
            currentSum = 0
            splits = 1

            for num in nums:

                if currentSum + num > limit:
                    splits += 1
                    currentSum = num

                else:
                    currentSum += num

            return splits <= k

        l = max(nums)
        r = sum(nums)

        while l <= r:

            mid = l + (r - l) // 2

            if canSplit(mid):
                r = mid - 1      # try smaller answer

            else:
                l = mid + 1      # need larger answer

        return l