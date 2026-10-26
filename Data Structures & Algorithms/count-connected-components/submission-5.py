from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        def DFS(node: int):
            if node not in graph or node in seen:
                return
            
            seen.add(node)
            for neighbor in graph[node]:
                DFS(neighbor)
        
        seen = set()
        result = 0
        for node in range(n):
            if node not in seen:
                DFS(node)
                result += 1
        
        return result
"""
{
0: [1]
1: [0 2]
2: [1]
3: [4]
4: [3]
}

seen = (0 1 2 3 4)
out = 2
node = 0 


Given an undirected graph with n node (0 to n-1) and an array of edges [nodei, nodej].
Return the number of connected components in the graph.

Graph representation adj list:

{
0: [1]
1: [0 2]
2: [1]
3: [4]
4: [5]
}

seen = (0 1)
out = 2 

- Loop through every element from 0 to n-1
    - only call DFS if the node have not been seen, increment output by 1

DFS:
    - need to account for node not in graph

Complexity:
    - O(V+E) time since we will visite each node at most once
    - O(V+E) for graph representation
"""
        