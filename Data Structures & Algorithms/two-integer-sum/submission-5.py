from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # Dictionary to store value and its index
        
        for i, num in enumerate(nums):
            complement = target - num  # Find the required pair
            
            if complement in num_map:
                return [num_map[complement], i]  # Return indices of the pair
            
            num_map[num] = i  # Store current number with its index
        
        return []  # No solution found
