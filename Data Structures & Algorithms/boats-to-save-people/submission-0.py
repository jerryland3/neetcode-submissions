class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        minBoat = 0
        while left <= right:
            if left == right:
                left += 1
            elif people[left] + people[right] > limit:
                right -= 1
            else:
                left += 1
                right -= 1
            minBoat += 1

        return minBoat

"""
       r
 l  
(1 2 2 3 3)
limit = 3
result = 2


Strategy:
    - need to find the two people where their weight is as close to limit as possible
    - Can use two pointer to solve this

Complexity:
    - O(nlogn) time for sorting
    - O(n) aux space depending on the sorting algorithm
"""
        