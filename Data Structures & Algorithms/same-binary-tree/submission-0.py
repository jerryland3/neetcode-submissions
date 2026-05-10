# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and not q:
            return False
        elif q and not p:
            return False
        elif not p and not q:
            return True

        if p.val == q.val:
            sub_tree_left_same = self.isSameTree(p.left, q.left)
            sub_tree_right_same = self.isSameTree(p.right, q.right)
        else:
            return False
        
        if sub_tree_left_same and sub_tree_right_same:
             return True 
        else:
             return False