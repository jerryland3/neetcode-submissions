"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copyMapping = dict()

        def DFS(curNode):
            if not curNode:
                return
            if curNode in copyMapping:
                return copyMapping[curNode]
            
            copyCur = Node(curNode.val)
            copyMapping[curNode] = copyCur
            
            for neighbor in curNode.neighbors:
                copyPrev = DFS(neighbor)
                copyCur.neighbors.append(copyPrev)
            
            return copyCur

        return DFS(node)

"""
Given the first node in an undirected graph, make a deep copy of the graph

Strategy:
    - use a dictionary to keep mapping of original node to its copy
    - use DFS to traverse the graph, and make a copy at each visited node
    - DFS also need to pass the prev node into the next visited node, so the prev and current copy connection can be
      made
    - edge case of cycle require making the connection before returning from the cycle

Complexity:
    - O(V + E) time since we will visite each node once
    - O(V + E) space since we are making a deep copy
"""