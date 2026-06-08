class Solution:
    
    # Function to check if subRoot is a subtree of root
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Case 1: If subRoot is None, it is considered a subtree by default
        if not subRoot:
            return True
        # Case 2: If root is None and subRoot is not, subRoot can't be a subtree
        if not root:
            return False

        # Case 3: If the trees are the same at the current root and subRoot, return True
        if self.sameTree(root, subRoot):
            return True
        
        # Case 4: Recursively check the left and right subtrees of root
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))

    # Helper function to check if two trees are the same
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Case 1: Both trees are None, they are the same
        if not root and not subRoot:
            return True
        
        # Case 2: Both trees are not None and have the same value, check their left and right subtrees
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and 
                    self.sameTree(root.right, subRoot.right))
        
        # Case 3: Trees don't match (either one is None, or values are different)
        return False
