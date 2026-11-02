import heapq
class MedianFinder:

    def __init__(self):
        self.arr = []
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if not self.maxHeap or num < -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        
        if len(self.maxHeap) > len(self.minHeap) + 1:
            number = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, number)
        elif len(self.minHeap) > len(self.maxHeap):
            number = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -number)

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        else:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2



"""
3 1 2


maxHeap = [-2 -1] - keep bottom half of the numbers
minHeap = [3] - keep top half of the numbers

Strategy:
    - use a minHeap and a maxHeap
        - if maxHeap is empty, then just inset into it
        - elif current value is less than maxHeap top value, then inset into maxHeap
        - else inset into minHeap
    
    - check if len(maxHeap) > len(minHeap + 1)
        - is so, then pop from maxHeap and inset into minHeap
    - elif check if len(minHeap) > len(maxHeap)
        - if so, then pop from minheap and insert into maxHeap

Complexity:
    - O(1) time for find median. O(logn) for addNum.
    - O(n) aux space for the heap.
"""
