from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        countDict = defaultdict(int)
        for num in hand:
            countDict[num] += 1
        
        for num in hand:
            if num in countDict and countDict[num] > 0:
                countDict[num] -= 1
                nextNum = num
                for _ in range(groupSize - 1):
                    nextNum += 1
                    if nextNum in countDict and countDict[nextNum] > 0:
                        countDict[nextNum] -= 1
                    else:
                        return False
        
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