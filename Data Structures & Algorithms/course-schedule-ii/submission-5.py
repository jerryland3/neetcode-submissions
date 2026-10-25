from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        good = set()
        seen = set()
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        output = []
        def hasCycle(node: int) -> bool:
            if node in seen:
                return True
            if node in good:
                return False
            if node not in graph:
                output.append(node)
                good.add(node)
                return False
            
            seen.add(node)
            for neighbor in graph[node]:
                if hasCycle(neighbor):
                    return True
            
            output.append(node)
            good.add(node)
            seen.remove(node)
            return False
        
        for course in range(numCourses):
            if hasCycle(course):
                return []
        
        return output
        
"""
seen = (0 1 2)
good = (5 4 2 3 0)
out = [5 4 2 3 0 1]

prereq = [[1, 0]]
numCourses = 3 => require to take course 0 to 2

Return valid ordering of courses you can take to finish all courses.
If not possible, return an empty array

0, 1, 2

Graph representation:
    course -> prereq

Complexity:
    - O(V + E) since we will visit each node at most once
    - O(V + E) space for graph representation, and O(numCourses - 1) output for the nodes

{
0: [2, 3]
2: [4]
3: [5]
4: [5]
}
"""   