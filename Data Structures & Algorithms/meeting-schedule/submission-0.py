"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True

        intervals.sort(key=lambda i: i.start)
        prev = intervals[0]
        for interval in intervals[1:]:
            if prev.end > interval.start:
                return False
            prev = interval
        return True

"""
Given a list of interval objects, return true if no conflict and false otherwise
Conflict means two or more intervals overlap
(0 8)(8 10) is not a conflict

Strategy:
    - sort the list of intervals, then loop through them to see if there are any overlaps
        - if there are overlaps, then return false
        - return true at the end of the loop since we did not see any conflict
    - sort by start value or end value would work

Complexity:
    - O(nlogn) time since we need to sort
    - O(n) or O(1) aux space depending on sorting algorithm

(5,8),(9,15)

prev = (9 16)
interval = (9 16)
8 > 9
"""
