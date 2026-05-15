# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        counter = 0
        def find_smallest(root: Optional[TreeNode], k: int):
            nonlocal res, counter
            if not root:
                return

            find_smallest(root.left, k)

            counter += 1
            if counter == k:
                nonlocal res 
                res = root.val
            
            find_smallest(root.right, k)
        
        find_smallest(root, k)
        return res