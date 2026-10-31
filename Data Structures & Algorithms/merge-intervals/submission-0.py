class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        for interval in intervals:
            if result and result[-1][1] >= interval[0]:
                prev = result.pop()
                mergeInterval = [min(prev[0], interval[0]), max(prev[1], interval[1])]
                result.append(mergeInterval)
            else:
                result.append(interval)
        
        return result



"""
[1 3] [1 5] 

res = [[1 5] [6 7]]



Strategy:
- First, need to sort the interval so we do not need to search the list for the next interval
    - sort by start and end

- can use a stack
    - push into stack if stack is empty
    - if stack not empty, then check if stack top element overlap with current interval
        - if they overlap, then pop from stack, merge, and push into stack
        - if they do not overlap, then just push into the stack

Complexity:
    - O(n) time since we loop through the list once, and we at most pop once at each loop
    - O(1) aux space and O(n) output space
"""
        