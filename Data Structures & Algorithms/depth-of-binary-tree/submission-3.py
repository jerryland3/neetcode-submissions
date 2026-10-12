# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def DFS(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            leftDepth = DFS(root.left)
            rightDepth = DFS(root.right)
            return max(leftDepth, rightDepth) + 1
        
        return DFS(root)


"""
use DFS to traverse the tree
DFS return the max depth at current level

                1
            2       3
                 4      6
                       5

Complexity:
    - O(n) time since we need to visit each node
    - O(h) aux space for the recursion stack, where h is depth of tree.
"""
