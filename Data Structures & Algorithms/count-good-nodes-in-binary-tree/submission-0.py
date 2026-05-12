# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def goodNodeCount(root: TreeNode, prevNodes: list) -> None:
            nonlocal count
            if not root:
                return
            
            if not prevNodes or prevNodes[-1].val <= root.val:
                count += 1
                prevNodes.append(root)
            
            goodNodeCount(root.left, prevNodes.copy())
            goodNodeCount(root.right, prevNodes.copy())
        
        goodNodeCount(root, [])
        return count



"""

[2 5]
3

"""
        