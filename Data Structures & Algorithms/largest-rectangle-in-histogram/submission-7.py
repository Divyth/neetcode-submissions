class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        
        for i in range(n):
            min_height = float('inf')
            for j in range(i, n):
                min_height = min(min_height, heights[j])
                width = j -i+1
                area = width * min_height
                max_area = max(max_area, area)
        
        return max_area