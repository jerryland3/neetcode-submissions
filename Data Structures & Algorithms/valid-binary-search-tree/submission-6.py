# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def DFS(root: Optional[TreeNode], left, right) -> bool:
            if not root:
                return True
            
            if not (left < root.val < right):
                return False
            
            left_valid = DFS(root.left, left, root.val)
            right_valid = DFS(root.right, root.val, right)

            return left_valid and right_valid
        
        return DFS(root, float("-inf"), float("inf"))
            


        