# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if root.val == subRoot.val:
            if self.isSubTreeSame(root, subRoot):
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSubTreeSame(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return self.isSubTreeSame(root.left, subRoot.left) and self.isSubTreeSame(root.right, subRoot.right)
        else:
            return False        