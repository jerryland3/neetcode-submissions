from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges and n == 1:
            return True

        graph = defaultdict(list)
        seen = set()
        for source, des in edges:
            graph[source].append(des)
            graph[des].append(source)
        
        def DFS(node: int, prevNode: int) -> bool:
            if node in seen:
                return False
            if node not in graph:
                return False
            
            seen.add(node)
            isValidTree = True
            for neighbor in graph.get(node):
                if prevNode is not None and neighbor == prevNode:
                    continue
                isValidTree = DFS(neighbor, node) and isValidTree

            return isValidTree
        
        for curNode in range(n):
            seen.clear()
            noCycle = DFS(curNode, None)
            seenAllNodes = True
            for node, _ in graph.items():
                if node not in seen:
                    seenAllNodes = False
                    break
            
            if not seenAllNodes or not noCycle:
                return False

        return True

"""
{
0: [1 2 3]
1: [0 4]
2: [0]
3: [0]
4: [1]
}
seen - [0 1]
node = 1 prev = 0

n = 5
edges = [[0 1] [0 2] [0 3] [1 4]]

                0
        1       2       3
        4

What is a valid tree?
- The tree must have a single root node, the root node have no children
- Each node must have a single parent, except for the root node
- No cycle exist


Strategy:
    - build adj list representation of graph
    - start traversing from any node, if no cycle is detected, then it is a valid tree
    - seen set is used to detect cycle, also need to pass previous node into the recursive function
      since the graph is undirected. So if we see the previous node, this does not invalidate the tree
    - use DFS for traversal

Complexity:
    - O(V + E) time for DFS traversal, this traversal only need to be done once
    - O(V + E) space for adj list representaion

"""