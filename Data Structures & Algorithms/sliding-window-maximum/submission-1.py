class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        output = []

        for i in range(len(nums)-k +1):
            maxNum = nums[i]
            for j in range(i, i +k):
                maxNum = max(maxNum, nums[j])
            output.append(maxNum)

        return output

        