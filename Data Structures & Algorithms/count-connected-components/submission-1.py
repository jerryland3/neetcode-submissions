from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        currentSeen = set()
        graph = defaultdict(list)
        for source, des in edges:
            graph[source].append(des)
            graph[des].append(source)
        
        def DFS(node: int, prevNode: int) -> bool:
            if node in seen:
                return False
            if node not in graph or node in currentSeen:
                return True
            
            currentSeen.add(node)
            for neighbor in graph.get(node):
                if neighbor == prevNode:
                    continue
                DFS(neighbor, node)
            
            return True
        
        count = 0
        for node in range(n):
            currentSeen.clear()
            if DFS(node, -1):
                count += 1
            
            for currentSeenNode in currentSeen:
                seen.add(currentSeenNode)
        
        return count
"""
{
0: [1]
1: [0 2]
2: [1]
3: [4]
4: [3]
}
seen = (0 1 2 3 4)
current seen = ()

n = 6
node = 4
count = 2

"""


"""
- undirected graph with n nodes (0 - (n-1))
- edges: given is a 2-d list [[ai, bi]]

return the number of connected componenets

n = 4
edges = [[0, 1] [2, 3]]

Strategy:
    - create adj list representation of the graph
    - use DFS to traverse, if the nodes were never seen before, then its a new connected component
    - DFS return bool, indicating if the connected component is new or not

{
0: [1]
1: [0]
2: [3]
3: [2]
}

(0 1 2 3 4)
count = 2

Complexity:
    - O(V + E) time since we will visit each node at most once
    - O(V + E) space since adj list representation



"""
        