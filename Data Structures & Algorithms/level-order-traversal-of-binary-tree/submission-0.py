# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []
        queue = deque([root] if root else [])
        while queue:
            level_nodes = []
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                level_nodes.append(node.val)
            
            out.append(level_nodes)
        
        return out


"""
[1]

1
[2, 3]

2, 3
[4, 5, 6, 7]

4, 5, 6, 7

"""