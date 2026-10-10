import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = list(nums)
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)
    
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            return self.heap[0]

        if val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        
        return self.heap[0]
        
        
            



"""
nums = [1000 -1000]
[-1000 1000]
k = 3

            -1000
        1000     0   

Complexity:
    - init is O(n) for building the heap, n = size of nums. add is O(logk) since we are adding to the heap
    - aux space of O(k) for the heap
"""
        
