# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        self.invertTree(root.left)
        self.invertTree(root.right)
        left_child = root.left
        right_child = root.right
        root.right = left_child
        root.left = right_child
        return root
        