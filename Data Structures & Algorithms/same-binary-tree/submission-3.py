# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not q or not p:
            return False

        if p.val == q.val:
            sub_tree_left_same = self.isSameTree(p.left, q.left)
            sub_tree_right_same = self.isSameTree(p.right, q.right)
            return sub_tree_left_same and sub_tree_right_same
        else:
            return False
        



"""
None None -> True
O None -> false
None O -> false

O O -> do nothing

p or q
"""