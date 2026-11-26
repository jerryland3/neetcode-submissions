from collections import deque
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        queue = deque([cost[0], cost[1]])
        for index in range(2, len(cost)):
            minCost = min(queue[0], queue[1]) + cost[index]
            queue.popleft()
            queue.append(minCost)
        
        return min(queue[0], queue[1])


"""
cost[i] - the cost of taking a step on floor i
        - can take either 1 or 2 steps after paying cost

can start on floor 0 or 1

return the minimum cost to reach the top of the stairs, at index = len(cost)
--------------------------
              i
1 2 1 2 1 1 1

[4 4]
minCost = 4


                        7
                    6       5
                 5             4
               4     3
             3   2  2  1
           2   1
        1    0

dp(n) - The minimum cost to arrive at state n (floor n)
dp(n) = min(dp(n-1) + cost[n-1], dp(n-2) + cost[n-2])

We can use bottom up approach by starting from basecase
we only need min cost at n-1 and n-2 to determine the min cost to arrive at step n.
With bottom up approach, we track what is the minimum cost to arrive at step n plus the cost of step n

[4 3]

Complexity:
    - Bottom up approach is O(n) time since we need to go through the cost list once
    - O(1) aux space since we only keep previous two step's minimum cost

"""