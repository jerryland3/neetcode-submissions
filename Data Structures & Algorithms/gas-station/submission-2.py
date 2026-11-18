class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        startIndex = 0
        totalSum = 0
        curSum = 0
        for index, gas in enumerate(gas):
            diff = gas - cost[index]
            totalSum += diff
            curSum += diff
            if curSum < 0:
                curSum = 0
                startIndex = index + 1
        
        if totalSum < 0:
            return -1
        return startIndex

"""
gas[i] - the amount of gas at station i
cost[i] - the cost of moving from station i to i + 1

Return the starting index that allow us to travel the circuit once in clockwise direction. 
Return -1 if its not possible
----------------------------------

 1  2  3  4 - gas
 2  2  4  1 - cost
-1  0 -1  3 - gas - cost

      i
-2 -2 -2 3 3

sum = 0
index = 2

if sum < 0, then startIndex = i + 1
sum(gas - cost) >= 0 for a valid circuit

Complexity:
    - O(n) time since we loop though the list once
    - O(1) space since we do not need adititional data structure

"""