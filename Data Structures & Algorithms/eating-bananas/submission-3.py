class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2
            if self.feasibility(piles, h, mid):
                right = mid
            else:
                left = mid + 1
        
        return left
        
    def feasibility(self, piles: List[int], h: int, rate: int):
        total_hours = 0
        for bananas in piles:
            total_hours += (bananas + rate - 1) // rate

        if total_hours <= h:
            return True
        
        return False
"""
1 4 3 2
h = 9

search space = 1 2 3
left = 0
right = 0

mid = 0
rate = 1
total hour = 3
feasible = yes


1 4 3 2 5 6
h = 7

1 <= k <= max(piles)

as k increase, the number of hours taken should be less than or equal
to previous hours at k-1.

search space of k
1 2 3 ... max(piles)

max(piles) have o(n) complexity where n = piles.length

can we use binary search on this space?

1 4 3 2

search space
1 2 3 4 5 6

let max(piles) = m
time complexity O(log(m))
space complexity O(m)

total time compexity O(n) + O(log(m))


"""