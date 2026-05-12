# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque([root] if root else [])
        while queue:
            level_len = len(queue)
            for i in range(level_len):
                node = queue.popleft()
                if i == 0:
                    res.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        
        return res



"""
[]
[1]

[3, 2]
[1, 3]

[4]
[1, 3, 4]

[5]
[1, 3, 4, 5]
"""
        