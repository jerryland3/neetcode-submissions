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
        
        found_left_sub = self.isSubtree(root.left, subRoot)
        found_right_sub = self.isSubtree(root.right, subRoot)
        return found_left_sub or found_right_sub
    
    def isSubTreeSame(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            left_sub_same = self.isSubTreeSame(root.left, subRoot.left)
            right_sub_same = self.isSubTreeSame(root.right, subRoot.right)
            return left_sub_same and right_sub_same
        else:
            return False        