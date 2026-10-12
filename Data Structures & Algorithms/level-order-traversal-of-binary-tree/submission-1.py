# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        output = []
        queue = deque()
        queue.append(root)
        
        while queue:
            levelList = []
            for _ in range(len(queue)):
                node = queue.popleft()
                levelList.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.append(levelList)
        return output


        



"""
[]
node = 5
levelList = [4 5 6 7]
out = [[1] [2 3] [4 5 6 7]]

Use BFS to traverse the tree.
For each level order, add the node to a list, then add that list to output at the end of the level

Complexity:
    - O(n) time since we need to visit each node
    - O(h) aux space for the recursion stack, where h is height of tree. O(n) output space
"""