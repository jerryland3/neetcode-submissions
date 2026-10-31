class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[0])
        resultIntervals = [intervals[0]]
        result = 0
        for start, end in intervals[1:]:
            if start < resultIntervals[-1][1]:
                resultIntervals[-1][1] = min(end, resultIntervals[-1][1])
                result += 1
            else:
                resultIntervals.append([start, end])
        
        return result


"""
[1 2] [1 4] [2 4] 
[[1 2] [2 4]]
s = 2
e = 4
result = 1

Strategy:
    - first sort intervals by start value
    - Loop through intervals
        - check interval in result overlap with current interval
        - if they overal, then keep the interval with the smaller end value and increment numDelete
        - if they do not overlap, then append interval to result and go to next iteration

Complexity:
    - O(nlogn) time for sorting, interating through the intervals is O(n)
    - O(n) aux space for result, O(1) output space
"""    