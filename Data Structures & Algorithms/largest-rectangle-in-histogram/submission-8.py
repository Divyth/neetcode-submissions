class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #(index, height)
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                area = (i - idx) * height
                maxArea = max(maxArea, area)
                start = idx  # after popping from the stack, update the idx to the previously popped height
            
            stack.append((start, h))
        
        # remaining heights in stack: for them no smaller height found, so they can reach untill end of the heights array
        for i, h in stack:
            maxArea = max(maxArea, (len(heights) - i) * h)
        return maxArea
        