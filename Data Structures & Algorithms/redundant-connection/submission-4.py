from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        def inCycleDFS(node: int, prevNode: int):
            if node in seen:
                cycle.add(node)
                return True
            
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor != prevNode and inCycleDFS(neighbor, node):
                    if node not in cycle:
                        cycle.add(node)
                        return True
                    else:
                        return False
            
            seen.remove(node)
            return False
        
        seen = set()
        cycle = set()
        inCycleDFS(1, -1)
        for node1, node2 in reversed(edges):
            if node1 in cycle and node2 in cycle:
                return [node1, node2]

"""
{
1: [2 3 4]
2: [1]
3: [1 4]
4: [1 3 5]
5: [4]
}

seen = (2 1 3 4)
cycle = (1 4 3)

- Given undirected graph with n nodes (1-n), and contain no cycles
- An edge is added to make a cycle in the graph
- Return an edge that can be removed so the graph have no cycle, return edge that appear last in the input

edges = [[1,2],[1,3],[3,4],[2,4]]

Strategy:
    - use DFS to detect which edges forms the cycle, add those edges to the cycle set
    - reverse backward from edges list until we find an edge in the cycle set

Graph Representation:
    - adj list

DFS:
    - start from any node (use node 1 arbitraily)
    - undirected graph, pass prevNode into each recusive layer to prevent
    - DFS return True if cycle has been detected, False otherwise
    - seen need to be poped if current node is an end path with no cycle
    - end result should be seen containing all the nodes that form a cycle
    - outside loop do not need to bool, its only needed for internal loop

Complexity:
    - O(V+E) time since we visite each node at most once and O(E) for back looping through edges
    - O(V+E) for graph representation, O(V) for recursion stack, O(1) output.
"""