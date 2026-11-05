class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for index, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                result.append(newInterval)
                result.extend(intervals[index:])
                return result
            elif newInterval[0] > interval[1]:
                result.append(interval)
            else:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
        
        result.append(newInterval)
        return result

"""

    --
        ---    
          --
(2 3) (4 6)
newInterval = (0 1)

[[0 1] [2 3] [4 6]]

Interval insert rules:
- if newInterval.end < curInterval.start, then we would insert new interval into results and append the rest of intervals
- if newInterval.start > curInterval.end, then we would insert curInterval into the result
- else newInterval must overlap with current interval, so we merge them

Edge case:
    - need to insert merged interval after the loop

Complexity:
    - O(n) time since we need to loop through the entire intervals list
    - O(n) output space for storing results (insertedIntervals), O(1) aux space.
"""