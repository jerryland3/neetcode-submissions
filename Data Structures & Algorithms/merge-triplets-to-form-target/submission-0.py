class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        workingTriplets = []
        for a, b, c in triplets:
            if target[0] < a or target[1] < b or target[2] < c:
                continue
            workingTriplets.append([a, b, c])
        
        resultingTriplet = [-1, -1, -1]
        for a, b, c in workingTriplets:
            ra = resultingTriplet[0]
            rb = resultingTriplet[1]
            rc = resultingTriplet[2]
            resultingTriplet = [max(a, ra), max(b, rb), max(c, rc)]
        
        targetSet = set(target)
        resultingTripSet = set(resultingTriplet)
        if targetSet == resultingTripSet:
            return True
        return False

"""

1 2 3
7 1 1

work =
1 2 3
7 1 1

resultingTrip = 7 2 3

target = 7 2 3

Strategy:
    - we have to find a triplet that have 1 or more value that match the target value and the non
      matching values are smaller than target
    - Only triplets where its value is not greater than the matching target value can be used

    - go trough the triplet list and find all triplet that works, meaning its value does not exceed matching target
      value
    - merge all working triplet and see if resulting triplet match target

Complexity:
    - O(n) time since we need to loop through triplet at most twice. n is the number of triplets
    - O(n) aux space for storing working triplets, O(1) output space
"""