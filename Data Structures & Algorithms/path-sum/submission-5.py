# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(root: Optional[TreeNode], curSum: int):
            # check edge case of null node
            if not root:
                return False
            if isLeaf(root) and (curSum + root.val) == targetSum:
                return True
            
            if helper(root.left, curSum + root.val):
                return True
            if helper(root.right, curSum + root.val):
                return True
            
            return False

        def isLeaf(root: Optional[TreeNode]):
            if not root.left and not root.right:
                return True
            return False 

        return helper(root, 0)

"""
strategy:
    - DFS traversal through the tree and add node value to currentSum
    - once at a leaf node, check if currentSum == target sum. If it does, return true, if not, return.
    - at each level we recurse with node value added to currentSum, then recurse with updated currentSum

    - we can check if current node is a leaf or not by examining if it has any children. If no children, then it
      is a leaf.

Complexity:
    - O(n) time since at worst case we could visit all the nodes.
    - O(n) aux space worst since the tree nodes not need to be balanced in problem statement, the space
      come from the recursion stack. The output space is O(1) since output is a bool.
"""