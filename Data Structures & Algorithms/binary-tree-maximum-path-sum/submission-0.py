# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float("-inf")
        def solve(node):
            if not node:
                return 0 
            
            leftSum = solve(node.left)
            rightSum = solve(node.right)

            if leftSum < 0:
                leftSum = 0
            
            if rightSum < 0:
                rightSum = 0
            
            self.maxSum = max(self.maxSum, node.val + leftSum + rightSum)

            return node.val + max(rightSum, leftSum)
        solve(root)
        return self.maxSum
            
            
        