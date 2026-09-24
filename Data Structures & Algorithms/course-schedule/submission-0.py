from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        seen = set()
        complete = set()

        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        def DFS(courseNode: int) -> bool:
            if courseNode in complete:
                return True
            if courseNode in seen:
                return False
            
            noCycle = True
            seen.add(courseNode)
            for neighbor in graph.get(courseNode, []):
                noCycle = noCycle and DFS(neighbor)
            
            if noCycle:
                complete.add(courseNode)
                seen.discard(courseNode)
                return True
            seen.discard(courseNode)
            return False
            

        for course in range(numCourses):
            if not DFS(course):
                return False
        
        return True



"""
prerequisties = 
[
    [0, 1]
    [5, 10]
    [15, 20]
]
[course, prereq]

0 -> 1   5 -> 10   15 -> 20

numCourses = 2, means we are required to take courses 0 and 1
return true if its possible to finish the required courses (0, 1)

failure case: return False if there is a cycle for the course in prereq
[
    [0,1]
    [1,0]
]

strategy:
    - use DFS to traverse through all the courses.
    - use 3 state tracking. visited and not visited states can be tracked by a single hash set, this will track if the
      current path has been seen. Complete hash set will mark if a course can be completed, that is no cycle exist.
    - with DFS, as we traverse the path, if there are no cycle, then we will mark those courses as complete.
    - The base cases for DFS will be if the node has been seen, then we have a cycle and return False. The other
      base case would be if that course is in the Complete set, then we would return True since it means that
      required prereq course can be completed.
    - use DFS through all 0 to n-1 courses.
    - Graph will be represented with adjacency list, where the course will point toward its prereq.
    
Complexity:
    - DFS is O(V), where V is the number of nodes in the graph. Since with Complete hashset, we do not need to traverse
      already completed nodes. Thus time complexity is O(V + E)
    - Aux space is O(V + E) for the number of nodes and edges in prereq. The number of edges is length of prereq list.
      Output space is O(1).  
"""