from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        seen = set()
        good = set()
        def DFS(courseNumber) -> bool:
            if courseNumber in seen:
                return True
            elif courseNumber in good or courseNumber not in graph:
                return False

            seen.add(courseNumber)
            for course in graph[courseNumber]:
                if DFS(course):
                    return True
            
            seen.remove(courseNumber)
            good.add(courseNumber)
            return False
        
        for course in range(numCourses):
            if DFS(course):
                return False
        
        return True
            
        

        



"""
1 -> 2 -> 3 -> 1

0 -> 1

seen (0 1 2 3 1)
good (4 2 1 0 3)

pre[i] = [a, b] => b is prereq for a
numCourses means required to take course 0 to numCourses - 1
Return True if its possible to take all courses, otherwise false

if a course we are required to take is not in prereq, then that mean it does not have a prereq.
As long as the prereq list do not have cycle, then we can take all the courses

0 -> 1 -> 0: Fail due to cycle

Modeling:
    - directed graph where course -> prerequsite
    - build the graph with list representation
    e.g.
    {
    course 0: [course 1]
    course 1: [course 0]    
    }

Algorithm:
    - The goal is to detect cycles, since cycle indicate that we cannot complete prereq
    - DFS is used for cycle detection
    - DFS return true if there is a cycle, otherwise false
    - loop though every course from course 0 to numCourses - 1, only call DFS if that course number is in graph and not
      good set.

Data Structure:
    - dictionary for graph representation
    - seen set for detecting cycles

Complexity:
    - O(V + E) time since DFS need to visit each node at most once
    - O(V + E) aux space for the graph representation and O(1) output space
"""