from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        seen = set()
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        def hasCycleDFS(node: int, prevNode: int) -> bool:
            if node in seen:
                return True
            
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor != prevNode and hasCycleDFS(neighbor, node):
                    return True
            
            return False

        for node in range(n):
            if node == 0 and hasCycleDFS(node, -1):
                return False
            elif node > 0 and node not in seen:
                return False

        return True 

"""
{
1: [0 4]
2: [0]
3: [0]
4: [1]
}

seen = (0)



Given n nodes and labeled from 0 to n-1 and a list of undirected edges
Return true if the nodes and edges makes a valid tree, otherwise false

What is a valid tree:
    - no cycle
    - contains a single root node

Strategy:
    - create graph from the edges, adj list representation
    - use DFS to detect if there are any cycles, if not, return True, otherwise return False
    - it does not matter which node to start the search from, so we can start from node 0
    - we are given node 0 to n-1, so there are atleast n nodes in the graph
    - we may be given disjoint graph, so we may need to loop through from 0 to n-1, and only call DFS if we have not
      seen that node yet. But a disjoint graph should not be a valid tree

Complexity:
    - O(V + E) time since we will visit each node at most once
    - O(V + E) space for graph representation, recursion stack, and seen set. O(1) output

{
0: [1 2 3]
1: [0 4]
2: [0]
3: [0]
4: [1]
}

seen = (0 1 4 2 3)


"""