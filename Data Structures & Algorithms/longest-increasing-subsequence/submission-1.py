class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp = [1] * len(nums) # every element itself forms an increasing subsequence

        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], 1 + dp[j])

        # return max(dp)
        
        tails = []

        for num in nums:
            l = 0 
            r = len(tails) - 1
            while l <= r:
                mid = l + (r-l) // 2

                if tails[mid] < num:
                    l = mid + 1
                else: 
                    r = mid - 1

            if l == len(tails):
                tails.append(num)
            else:
                tails[l] = num

        return len(tails)
        