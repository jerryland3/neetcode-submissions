# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter, _ = self.find_diameter(root, 0)
        return max_diameter

    def find_diameter(self, root: Optional[TreeNode], depth:int=0):
        if not root:
            return (0, depth)
        depth += 1
        left_max_dia, left_max_depth = self.find_diameter(root.left, depth)
        right_max_dia, right_max_depth = self.find_diameter(root.right, depth)

        current_dia = left_max_depth + right_max_depth - 2 * depth
        max_dia = max(right_max_dia, left_max_dia, current_dia)
        max_depth = max(right_max_depth, left_max_depth)
        return (max_dia, max_depth)

"""
The largest diameter at a node is the sum of left and right child depth

use depth first search to visit each node and store depth of that node
calculate the max depth for both left and right child nodes
calculate the diameter at that node
compare the diameter at that node with max_diameter seen so far from subtree
compare left and right subtree depth
return max_diameter seen so far and the max_depth seen so far

diameter at a subtree is max_depth_left + max_depth_right - 2cur_depth
"""

