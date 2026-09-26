"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashTable = {}
        seen = set()

        def DFS1(node: Node):
            if not node or node in seen:
                return
            
            seen.add(node)
            nodeCopy = Node(node.val)
            hashTable[node] = nodeCopy
            for neighbor in node.neighbors:
                DFS1(neighbor)
        
        def DFS2(node: Node):
            if not node or node in seen:
                return
            
            seen.add(node)
            nodeCopy = hashTable[node]
            for neighbor in node.neighbors:
                nodeCopy.neighbors.append(hashTable[neighbor])
                DFS2(neighbor)
        
        DFS1(node)
        seen.clear()
        DFS2(node)

        return hashTable[node] if node else None


"""
{
    2: 2
    1: 1
    3: 3
}
seen (2, 1, 3)
2 - [1, 3]
1 - [2]
3 - [2]

{
    1: [2]
    2: [1, 3]
    3: [2]
}

Strategy:
    - use BFS or DFS to visit each node from input node, make a copy of each visited node, and use hash table to map
      original node to copy node
    - make a 2nd pass with BFS starting from input node, take copy from hash table and add its negibor base on hash map
      and original node negibors
    - return the copy of the original input node

complexity:
    - O(V + E) for BFS
    - O(V) aux space since we are storing all nodes in seen with BFS and O(V + E) output space since we are making a copy.
"""