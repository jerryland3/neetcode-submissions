# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def goodNodeCount(root: TreeNode, prevMax: Optional[TreeNode]) -> None:
            nonlocal count
            if not root:
                return
            
            if not prevMax or prevMax.val <= root.val:
                count += 1
                prevMax = root
            
            goodNodeCount(root.left, prevMax)
            goodNodeCount(root.right, prevMax)
        
        goodNodeCount(root, None)
        return count



"""

[2 5]
3

"""
        