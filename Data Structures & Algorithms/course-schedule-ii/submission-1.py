from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        output = []
        complete = set()
        seen = set()
        graph = defaultdict(list)

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        def DFS(course: int) -> bool:
            if course in seen:
                return False
            if course in complete:
                return True
            if course not in graph:
                output.append(course)
                complete.add(course)
                return True
            if not graph.get(course):
                output.append(course)
                complete.add(course)
                return True
            
            seen.add(course)
            canComplete = True
            for neighbor in graph.get(course):
                canComplete = DFS(neighbor) and canComplete

            if canComplete:
                complete.add(course)
                output.append(course)

            seen.remove(course)
            return canComplete

        
        for course in range(numCourses):
            if not DFS(course):
                return []
        
        return output
        
        

"""
[a, b] -> b is required for a
return a valid ordering of courses to finish ALL courses

1 -> 0

1
[0 1 2] - out
(0 1) - complete
[] - seen

representation:
course -> prereq

- if there are no loop in the graph, then all prereq are valid
- use DFS, mark node as complete if then can be finished with the given prereq
- also need seen set to ensure we are not seeing loops, seen need to be modified in place
- A node have no prereq will always be first

Complexity:
    - O(V + E) time since we visit each node once
    - O(V + E) for adj list, and O(numCourses) output space.
"""   