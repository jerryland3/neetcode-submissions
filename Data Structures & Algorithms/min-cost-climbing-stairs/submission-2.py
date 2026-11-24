class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def dp(n: int) -> int:
            if n <= 1:
                return 0
            if n in cache:
                return cache[n]
            
            cache[n] = min(dp(n-1) + cost[n-1], dp(n-2) + cost[n-2])
            return cache[n]

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
    - Top down approach need to cache cost at each step, O(n) space. Cache store min cost at each step
    - base case: if n <= 1, then return cost[n]

Complexity:
    - O(n) time since we need to visit each steps
    - O(n) aux space for the cache, O(1) output
"""