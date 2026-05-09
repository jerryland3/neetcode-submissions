# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, max_dia = self.dfs_max_diameter(root)
        return max_dia

    def dfs_max_diameter(self, root: Optional[TreeNode]) -> tuple[int, int]:
        if not root:
            return 0, 0
        
        left_depth, left_dia = self.dfs_max_diameter(root.left)
        right_depth, right_dia = self.dfs_max_diameter(root.right)
        cur_dia = left_depth + right_depth
        
        return max(left_depth + 1, right_depth + 1), max(cur_dia, left_dia, right_dia)
