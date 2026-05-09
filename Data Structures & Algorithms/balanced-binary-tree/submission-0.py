# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced, _ = self.check_balance(root)
        return balanced
    
    def check_balance(self, root: Optional[TreeNode]) -> tuple[bool, int]:
        if not root:
            return True, 0
        
        is_left_balanced, left_depth = self.check_balance(root.left)
        is_right_balanced, right_depth = self.check_balance(root.right)

        if not is_left_balanced or not is_right_balanced:
            return False, 0
        
        return abs(left_depth - right_depth) <= 1, max(left_depth + 1, right_depth + 1)
