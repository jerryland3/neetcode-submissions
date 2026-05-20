import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k

        for item in nums:
            self.add(item)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
            return self.min_heap[0]
        
        if val > self.min_heap[0]:
            heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, val)
        
        return self.min_heap[0]




"""
Find the kth largest integer in a stream
[1 2 3 3] k = 2, then 2nd largest is 3

given: int k and nums -> initalize object in constructor

add(int val) -> this method adds the int val to the stream and return the kth largest integer in the stream


[1 2 3 3 3 5] [6 7 8]

[5 3 3 3 2 1]
min heap = [6 7 8]

- min heap to always keep 3 items
- all items in min heap must be larger than all values in the max heap

let stream length = h
time complexity should be h*log(h) 
"""
        
