import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stonesCopy = list(stones)
        for index in range(len(stonesCopy)):
            stonesCopy[index] = -stonesCopy[index]

        heapq.heapify(stonesCopy)

        while len(stonesCopy) > 1:
            stone1 = heapq.heappop(stonesCopy)
            stone2 = heapq.heappop(stonesCopy)
            smashed = abs(stone1 - stone2)

            heapq.heappush(stonesCopy, -smashed)
        
        return -stonesCopy[0]



"""
[2 3 6 2 4]

[1 1 2 2]
s1 = 2
s2 = 2

[0 1 1]
s1 = 1
s2 = 1

[0 0]
s1 = 0
s2 = 0

[0]

strategy:
    - use max heap, pop two top ones and smash them.
    - add the smashed result back into the heap

Complexity:
    - create heap, pop from heap, push into heap. Create is O(n) and only do once. Pop and push are logn time and
      we do this at most n times. Thus O(nlog(n)) time
    - aux space of O(n) for the heap and copy of stones. O(1) for the output.
"""   