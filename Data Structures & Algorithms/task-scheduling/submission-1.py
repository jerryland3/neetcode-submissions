import heapq
from collections import defaultdict, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        countDict = defaultdict(int)
        for task in tasks:
            countDict[task] += 1
        maxHeap = []
        for task, count in countDict.items():
            heapq.heappush(maxHeap, -count)

        cpuCycle = 0
        queue = deque()
        while maxHeap or queue:
            cpuCycle += 1
            if maxHeap:
                count = heapq.heappop(maxHeap) + 1
                if count < 0:
                    queue.append((count, cpuCycle + n))
            if queue and queue[0][1] <= cpuCycle:
                heapq.heappush(maxHeap, queue.popleft()[0])

        return cpuCycle

"""
tasks = [X Y Y Y], n = 2

- each cpu cycle allow for completion of a single task
- task can be completed in any order, 
- identical task must be seperated by at least n cpu cycles

return min number of cpu cycles required to complete all tasks

x x y y, n = 2

x y - x y

a a a b c, n = 3
a c b - a - - - a

{
    a: 3
    b: 1
    c: 2
}
        (3)
    (1)     (2)
        
[(2, 1 + 3)] 4
(count, timeUntilReady)

a b c # a # # # a
cpuCycle = 9

We need to process the most frequent element first, thus use dict to track count of each element.
Make count into a tuple with it character (count, char) and push into a max heap so we can process the most freq element
Use a queue to track when a element can be used again, append n '#' ahead of the (count, char) tupled if a task is processed an its count is still > 0
Update the number of process every loop
use while loop until both queue and heap are empty

Complexity:
    - O(h) to get count, need to push at most 26 elements into the heap, creating the heap is O(26). Need to push and pop 
      from the heap at most O(h) times, thus heap push/pop is O(hlog(26)). Queue push and pop is at most n*h times. Thus
      queue is O(n*h). total time complexity in the worst case is thus O(nh). h is the size of the input.
    
    - Aux space of O(26) for dict and O(26) for heap, and O(26) for queue. O(1) output space
"""