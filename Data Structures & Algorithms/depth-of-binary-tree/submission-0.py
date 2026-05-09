# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.find_depth(root, 0)

    def find_depth(self, root: Optional[TreeNode], depth) -> int:
        if root is None:
            return depth
        depth += 1
        depth_left = self.find_depth(root.left, depth)
        depth_right = self.find_depth(root.right, depth)
        depth = max(depth_left, depth_right)
        return depth
"""
     1
  2      3
       4

"""

        