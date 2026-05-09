# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        level = 0
        return self.depth_dfs(root, level)


    def depth_dfs(self, root: Optional[TreeNode], level: int) -> int:
        if not root:
            return level
        
        level += 1
        max_depth_left = self.depth_dfs(root.left, level)
        max_depth_right = self.depth_dfs(root.right, level)
        
        return max(max_depth_left, max_depth_right)