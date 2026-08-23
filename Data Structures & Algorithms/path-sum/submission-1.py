# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def hasPathSumHelper(root: Optional[TreeNode], current_sum: int) -> bool:
            if not root:
                return False

            current_sum += root.val             
            if self.is_leaf(root):
                return current_sum == targetSum

            if hasPathSumHelper(root.left, current_sum):
                return True
            return hasPathSumHelper(root.right, current_sum)

        return hasPathSumHelper(root, 0)
    
    def is_leaf(self, root):
        if root.left is None and root.right is None:
            return True
            
        return False


"""
        1

    1         0

1
                
"""  
        