#prefix postfix in two pass without taking extra space for each 
# prefix and postfix, either doing in two passes in the same output
# saving the space

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        left = [0] * n
        right = [0] * n

        left[0] = 1
        for i in range(1,n):
            left[i] = left[i-1] * nums[i-1]
        
        right[-1] = 1
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        for i in range(n):
            res[i] = left[i] * right[i]

        return res