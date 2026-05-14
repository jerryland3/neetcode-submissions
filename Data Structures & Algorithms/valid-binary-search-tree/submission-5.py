# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res_list = []
        def DFS(root: Optional[TreeNode]) -> None:
            if not root:
                return

            nonlocal res_list
            DFS(root.left)
            res_list.append(root.val)
            DFS(root.right)

        def check_valid(result_list: list) -> bool:
            for index, value in enumerate(result_list):
                if index > 0 and value <= result_list[index - 1]:
                    return False
            
            return True
        
        DFS(root)
        return check_valid(res_list)
            


        