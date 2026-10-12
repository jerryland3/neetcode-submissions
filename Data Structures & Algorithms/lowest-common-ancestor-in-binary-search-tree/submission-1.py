# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        out = []
        def DFS(root: TreeNode) -> bool:
            if not root:
                return False
            
            foundLeft = DFS(root.left)
            foundRight = DFS(root.right)

            if foundLeft and foundRight:
                out.append(root)
                return False
            elif (foundLeft or foundRight) and (root == p or root == q):
                out.append(root)
                return False
            
            if foundLeft or foundRight:
                return True
            
            return True if (root == p or root == q) else False 
        
        DFS(root)
        return out[0]

"""
Given a root of BST
and a p and q node

return lowest common ancestor of p and q, where a node can be a ancestor of itself

Use DFS to traverse the tree, visit left, right, then root.
DFS return true if it found either p or q node, otherwise false

if both left and right child return true, then we return current node
if either left or right child return true, and current node is either p or q node, then we also return current node

Complexity:
    - O(n) time where n is number of nodes
    - O(h) space for recursion stack, O(1) output.
"""
        