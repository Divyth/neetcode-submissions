# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def height(node):
            nonlocal res
            if not node:
                return 0

            leftHeight = height(node.left)
            rightHeight = height(node.right)
        
            diameter = leftHeight + rightHeight
            res = max(res, diameter)
            return 1 + max(leftHeight, rightHeight)
        height(root)
        return res