class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        for index in range(len(gas)):
            diff.append(gas[index] - cost[index])

        lastStart = 0
        total = 0
        curSum = 0
        for index, costDiff in enumerate(diff):
            curSum += costDiff
            total += costDiff
            if curSum < 0:
                lastStart = index + 1
                curSum = 0
        
        if total < 0:
            return -1
        return lastStart


"""
given gas array, where gas[i] is the amount of gas at station i
given cost, where cost[i] is the amount of gas needed to move from i to i+1

Return the starting gas station index so that we can travel around the circuit once in clockwise direction.
Return -1 if its impossible
At most one soluiton exists
----------------------------------------------------

     i
gas  1  2  3  4
cost 2  2  4  1
    -1  0 -1  3


1  2  3
2  3  2
-1 -1 1

1 -2 2 2 3 -5


issue is when cost > gas

Strat:
    - calculate diff array, where diff[i] = gas[i] - cost[i]
    - if sum(diff) < 0, then its impossible.
    - if sum(diff) >= 0, then its possible to finish the circuit
"""