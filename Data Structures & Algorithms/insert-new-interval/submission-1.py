class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        mergeInterval = [newInterval[0], newInterval[1]]
        for index, interval in enumerate(intervals):
            # 1. interval[i] ends before the new one starts, no overlap, append it
            if interval[1] < mergeInterval[0]:
                result.append(interval)
            
            # 2. interval[i] starts after the new on ends, append new one, then the rest of the list and return it
            elif interval[0] > mergeInterval[1]:
                result.append(mergeInterval)
                result.extend(intervals[index:])
                return result

            # 3. otherwise it overlap: absorb it into the new interval, dont append yet
            else:
                mergeInterval = [min(mergeInterval[0], interval[0]), max(mergeInterval[1], interval[1])]
            
        result.append(mergeInterval)
        return result




"""
mergedI = [1 5]

I = [4, 6]


intervals[i] = [start_i, end_i], initially sorted in ascending order by start_i, no overlaps
newInterval = [start, end]

merge newInterval in intervals so that it is still sorted and no overlap
may merge overlapping intervals if needed
return intervals after merging


            -------------
-----                      ---------
1 2 3 4 5 6

newI = [2 5]
[[a b] [c d]] [[e f] [g h]]

    --
------ 

Strategy:


Complexity:
    - O(n) for loop, and O(n) for deletion or insertion in the intervals. O(n) total time
    - O(1) space since we just need to track interval index for overlap
"""