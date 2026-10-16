import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, num)
                continue
            
            if num > minHeap[0]:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, num)
        
        return minHeap[0]

"""
[2,3,1,5,4]
k = 2

return kth largest in the array | input unsorted


       min                  
        4
      5                  

Complexity:
    - loop through every element and add to min heap. pop and push into head is log(n). Thus time
      complexity is O(nlog(k)).
    - Space Complexity of O(k) since we need to store k values in the min heap. O(1) output
"""
        