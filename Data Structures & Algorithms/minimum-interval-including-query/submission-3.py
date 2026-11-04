import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        minHeap = []
        intervals.sort()
        index = 0
        answer = {}
        for query in sorted(set(queries)):
            while index < len(intervals) and intervals[index][0] <= query:
                intervalDistance = intervals[index][1] - intervals[index][0] + 1
                intervalTuple = (intervalDistance, intervals[index][0], intervals[index][1])
                heapq.heappush(minHeap, intervalTuple)
                index += 1
            
            while minHeap and minHeap[0][2] < query:
                heapq.heappop(minHeap)
            
            if minHeap:
                answer[query] = minHeap[0][0]
            else:
                answer[query] = -1

        return [answer[query] for query in queries]
            

"""
{
7: 0
9: []
3: 2
}

[1,6] [1,9] [4,5] [5,8] [8,10]
[3 3 7 9 9]

  ---
   --
    --------
          -

          -

minHeap = []
result = []

at query point q, we do not care about any interval that starts after q. Meaning we only care about intervals that
have a start before or at q.

Also, at query point q, we only care about interval that have a end at or after q.

Complexity:
    - O(nlogn + mlogm) time since we need to sort both the intervals and the queries.
    - O(n + m) or O(1) aux space depending on the sorting algorithm. O(m) output space due to query size.

"""