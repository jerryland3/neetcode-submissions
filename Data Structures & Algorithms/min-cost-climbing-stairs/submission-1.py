class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def dp(n: int) -> int:
            if n <= 1:
                return cost[n]
            if n in cache:
                return cache[n]
            
            previousStepCost = dp(n-1)
            previousTwoStepCost = dp(n-2)
            if n < len(cost):
                cache[n] = min(previousStepCost, previousTwoStepCost) + cost[n]
                return cache[n]
            else:
                return min(previousStepCost, previousTwoStepCost)
        
        return dp(len(cost))
            

"""
cost[i] - cost of taking a step from the ith floor. After paying, we can either take one or two steps.
We can start from floor 0 or 1.

Return the minimum cost to reach the top, just past last index of cost list.
------------------------------
0 1 2
1 2 3

                    3
                2       1
            1      0
cache will store minimum cost at each step except base case
{
    2: 1
}


0 1 2 3 4
1 2 1 2 1 

                              []
                    4                      3
             3              2        2             1
        2    1     1     0   1    0          0
    1       0   0
                            
Strategy:
    - we can use recursion and return the lowest cost. However this is not efficient O(2^n)
    - Recurrence relation dp(n) = min(dp(n-1), dp(n-2)) + cost[n]. Where dp(n) is the min cost to reach step(n)
    - Top down approach need to cache cost at each step, O(n) space
    - base case: if n <= 1, then return cost[n]
"""