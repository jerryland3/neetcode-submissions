# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def postOrder(root: Optional[TreeNode]):
            if not root:
                return
            
            postOrder(root.left)
            postOrder(root.right)

            leftChild = root.left
            root.left = root.right
            root.right = leftChild
        
        postOrder(root)
        return root

"""
            1
    2               3

4               6      7

Strategy:
    - recursivly traverse in post order form, and swap child if children exist

Complexity:
    - O(n) time since we need to visit each node once, where n is the number of nodes in the tree
    - O(log(n)) aux space for recursion stack if tree is balanced, O(n) worst case aux space if tree is not balanced.
      O(n) output space since we will return the same tree that is inverted.


"""


        