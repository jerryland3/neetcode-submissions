import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for index, (x, y) in enumerate(points):
            distance = math.sqrt(x*x + y*y)

            if len(maxHeap):
                topDistance, _ = maxHeap[0]

            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (-distance, index))
            elif distance < -topDistance:
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap, (-distance, index))
        
        out = []
        while len(maxHeap) > 0:
            _, index = heapq.heappop(maxHeap)
            out.append(points[index])
        
        return out



"""
[[0, 1] [0, 3] [0, 2]]
k = 2

max heap size k

            
    (-1, 0)
        
topD = -3
index = 2
dis = 2

out = [[0, 2] [0, 1]]

Complexity:
    - heap push is O(log(n)), we push it at most n times in worst case where k = n. Thus it is O(nlog(n)) time
    - aux space is O(n) if k = n due to the heap. Output space is at worst O(n)
"""