# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_pos = 0
        inorder_index = {}
        total_length = len(preorder)
        for index, item in enumerate(inorder):
            inorder_index[item] = index

        def tree_helper(left, right) -> TreeNode:
            nonlocal preorder_pos, inorder_index, total_length, preorder, inorder
            if left > right:
                return None

            cur_node = TreeNode(preorder[preorder_pos])
            preorder_pos += 1

            mid = inorder_index[cur_node.val]
            cur_node.left = tree_helper(left, mid - 1)
            cur_node.right = tree_helper(mid + 1, right)

            return cur_node

        return tree_helper(0, total_length - 1)
