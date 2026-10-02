from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        cycle = set()
        seen = set()
        graph = defaultdict(list)

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        def DFS(node: int, prev: int) -> bool:
            if node in seen and node not in cycle:
                cycle.add(node)
                return True
            if node in cycle:
                return False
            
            seen.add(node)
            for neighbor in graph.get(node, []):
                if neighbor == prev:
                    continue
                if DFS(neighbor, node) and node not in cycle:
                    cycle.add(node)
                    return True
            
            return False
                

        DFS(1, -1)

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
seen = (1 2 3 4)
cycle = (1 4 3)


n = 3
edges = [[1 2] [2 3] [1 3]]

1 - 2 - 3

we are always given a cyclic graph, remove the last edge that results in an acyclic graph

Given:
    our input is n and a list of edges, the number of edges is always equal to n
    initally there are no cycle, a single edge is added to create a cycle

Find: 
    Find the edge closes to the end of the list that we can remove so there are no cycles.

strategy:
    - Use DFS to traverse the graph, once we visit a node already in seen, then we know we are at the 
      end of a cycle, and we add that node to the cycle set

    - DFS return true if we are currently in a cycle

    - if we are currently in a cycle, we can break out of the neighbor loop, and if the current node
      is not in the cycle set, then add to the cycle set.

    - if current node is in the cycle set, then we have reached that same head/end cycle node, and 
      the DFS return False

    - backward scan the edges list until we find an edge where both nodes are in the cycle set

Complexity:
    - O(V + E) time since we need DFS once and we traverse the edge list once
    - O(V + E) space for the graph, cycle set, and recursion stack



"""
        