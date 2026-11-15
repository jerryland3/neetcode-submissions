from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        countDict = defaultdict(int)
        for num in hand:
            countDict[num] += 1
        
        for num in hand:
            if countDict[num] <= 0:
                continue
            for groupNum in range(num, num + groupSize):
                if countDict[groupNum] <= 0:
                    return False
                countDict[groupNum] -= 1
        
        return True


"""
i    
1 2 3 3 4 5 6 7


1 2 4 2 3 5 3 4
groupSize = 4


numGroups = len(n) / groupSize = 8/4 = 2

prev = nums[i]
nums[i] = -1

{
1: 0
2: 0
3: 0
4: 0
5: 1
6: 1
7: 1
}

Complexity:
    - O(nlog(n)) time due to sorting, 2nd phase is linear time
    - O(n) aux space due to sorting and hashmap and O(1) output space
"""