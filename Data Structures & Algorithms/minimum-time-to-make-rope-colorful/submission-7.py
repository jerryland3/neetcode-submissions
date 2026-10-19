import heapq
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        minTime = 0
        minHeap = []
        for index in range(len(colors)):
            if index == len(colors) - 1:
                minHeap.append(neededTime[index])
            elif colors[index] == colors[index + 1]:
                minHeap.append(neededTime[index])
            else:
                minHeap.append(neededTime[index])
                heapq.heapify(minHeap)
                while len(minHeap) > 1:
                    minTime += heapq.heappop(minHeap)
                heapq.heappop(minHeap)
                
        heapq.heapify(minHeap)
        while len(minHeap) > 1:
            minTime += heapq.heappop(minHeap)
        
        return minTime





"""
minTime = 3
minHeap = [2 3 5 8]


a-a-b-b-c
4 1 2 7 3 

Given:
    - ballon sorted in order
    - ballon[i] takes neededTime[i] to remove
    - after removal, neighboring ballon are connected
    - Return min total removal time so no two remaining neighboring ballons have same coloe

Strategy:
    - for all same letter, remove the ones that takes the least amount of time until there is one color left
    - Do this for all letters until each letter only have a count of 1
        - loop through the list and keep pushing current tuple of (time, letter) into a MinHeap
        - once we see that the next letter is different than current, then run a while loop to pop from heap.
        - pop until the heap only have a single letter left, during pop, add time to total time
        - once the length of the heap is 1, then reset the heap so its empty and go on to next character

Data Structure:
    - Min heap to track the current smallest time letter to remove for all same letters

Edge Case:
    - at the end of the loop, the heap may not be empty, keeping poping the heap outside of the loop if its not empty
    - at the end of the loop, need to check index out of bound, otherwise get index out of bound error.

Complexity:
    - let say average size of the heap will be k, bulding the heap is O(k). pop is O(klog(k)). We need to do this at most
      26 times. Thus time complexity is O(26*klog(k)), where k = n/(number of unique letters)
    
    - space complexity of O(k) for the heap. output space of O(1)

        
"""
