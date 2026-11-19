from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        hand.sort()
        for num in hand:
            if count[num] > 0:
                for i in range(num, num + groupSize):
                    if count[i] <= 0:
                        return False
                    count[i] -= 1
        
        return True




"""
hand[i] - vlaue written on the ith card
groupSize - int

rearrage the cards into groups where each group is size GroupSize and cards values consecutivly incresing by 1
Return true if its possible, otherwise false
-----------------------------------------------

[1 2 4 2 3 5 3 4]

  i 
1 2 2 3 3 4 6 7 8
groupSize = 4

[1 2 3 4]
[5 6 7 8]

len(hand) % groupSize == 0, this is a requirement for dividing the input into group size

{
    1: 1
    2: 2
    3: 2
    4: 1
    6: 1
    7: 1
    8: 1
}

Complexity:
    - O(nlog(n)) time since we loop through the list once and we need to sort
    - O(n) aux space for sorting and hashTable, O(1) otuput

"""