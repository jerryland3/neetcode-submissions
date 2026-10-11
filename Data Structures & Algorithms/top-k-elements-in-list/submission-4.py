from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = defaultdict(int)
        for num in nums:
            countDict[num] += 1
        
        minHeap = []
        for num, count in countDict.items():
            heapq.heappush(minHeap, (count, num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        output = []
        while len(minHeap) > 0:
            count, num = heapq.heappop(minHeap)
            output.append(num)
        
        return output
        



        
"""
nums = [1 1 2 2 2 3 3 3]
k = 2

out = [2 3]

dict = {
        1: 2
        2: 3
        3: 3
    }

maintain a min heap of size k. Loop through dict and add to heap, if heap size if over k, then we pop.
         (3, 3)
    (3, 2)    

(count, number)

loop though heap at the end, and extrat the number from it

Complexity:
    - dict building is O(n), loop though dict is at most O(n), building heap is O(klog(k)). Thus time complexity is
      O(n + klog(k))
    - aux space of O(n) at worst for dict and O(k) for dict. Thus aux space is O(n) and output space is O(k). 
"""
        