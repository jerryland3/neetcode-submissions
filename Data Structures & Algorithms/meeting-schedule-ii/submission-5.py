"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda i : i.start)
        result = 0
        minHeap = []
        for interval in intervals:
            while minHeap and interval.start >= minHeap[0]:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, interval.end)
            result = max(len(minHeap), result)
        return result


"""
Intervals = [(0,40) (5,10) (10, 12) (15,20)]

minHeap = (12 40)
cur = (10, 12)
res = 2



--------------------------
  --------     ---------
         -----

Goal: Find the largest number of overlapping intervals

Min-heap will keep all the overlapping intervals, with the heap ordered by smallest end.

- Sort intervals by start
- loop through interval and add end value to min heap
- check if cur interval overlap with smallest min heap end
- if it does, then push into min heap. Otherwise, pop min heap until find an end that overlap or min heap have no element
- update result with min heap length i.e. result = max(len(minHeap), result)

Complexity:
    - O(nlogn) time for sorting and pushing into minHeap
    - O(n) aux space depending on sorting algorithm
"""
        