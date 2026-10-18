import heapq
from collections import defaultdict, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        countDict = defaultdict(int)
        for task in tasks:
            countDict[task] += 1
        
        maxHeap = [-count for count in countDict.values()]

        heapq.heapify(maxHeap)
        queue = deque()
        time = 0
        while maxHeap or queue:
            time += 1
            if maxHeap:
                count = heapq.heappop(maxHeap) + 1
                if count != 0:
                    queue.append((count, time + n))
            
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
        
        return time


"""
A A A B C, n = 3

A: 3
B: 1
C: 1

time = 9
maxHeap = []
queue = []
count = 0


A A A B C, n = 3

A -> B -> C -> _ -> A -> _ -> _ -> _ -> A

- select most frequent task first results in less compute cycles

Strategy:
    1. need to get the count of each task type, use dictionary to do this
    2. can use maxHeap to keep track of the task with most count
    3. once a task is selected an processed, the task need to go into a cool down queue until it is ready
    4. loop until both heap and queue are empty, update time at each loop

Data Structure:
    1. simple default dict for getting count
    2. max heap of each task type
        - store just the count in the maxHeap
    3. queue is used to store the count and cool down time as tuple (count, cooldown time)
"""