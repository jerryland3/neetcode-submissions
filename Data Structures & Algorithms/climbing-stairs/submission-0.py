from collections import deque
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        queue = deque([1, 2])
        for _ in range(3, n + 1):
            steps = queue[0] + queue[1]
            queue.popleft()
            queue.append(steps)
        
        return queue[1]




"""
n = 4
queue = [3 5]

i = 4
steps = 5


n - number of steps to reach top
can climb with 1 or 2 step at a time

return number of distinct way to climb to the top
-----------------------------------------------------

steps = 1, return 1
1

steps = 2, return 2
1 1
2

steps = 3, return 3
1 1 1
2 1
1 2

steps = 4, return 5
1 1 1 1
2 2
2 1 1
1 2 1
1 1 2

Strategy:
    - step(1) and step(2) are base cases, because we can take at most 1 or 2 steps
    - step(1) = 1, step(2) = 2
    - From step 1 to reach step 3, there is only one way to reach step 3. From step 2 to reach step 3, there is also
      only 1 way to reach step 3. This means step(3) = step(1) + step(2)
    - In general, step(n) = step(n-1) + step(n-2)
    - Given this, we can use a bottom up appraoch of dp, setting the two base state can calculate from there

Complexity:
    - O(n) time since we need to compute each state starting from state 3
    - O(1) aux and output space with bottom up approach since we only keep previous two states in memory.

"""
        