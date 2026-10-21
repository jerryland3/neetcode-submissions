import heapq
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        totalMin = 0
        curMax = 0
        curTotal = 0
        for index, letter in enumerate(colors):
            curMax = max(curMax, neededTime[index])
            curTotal += neededTime[index]
            if index == (len(colors) -  1) or letter != colors[index + 1]:
                totalMin += curTotal - curMax
                curTotal = 0
                curMax = 0
        
        return totalMin
            



"""
        p
a a b b c
4 1 2 7 3

curMax = 7
curTotal = 12
min = 1 + 5 = 6

m1 + m2 + m3 = total
max = m1
total - max = sum of smaller values


Strategy:
    - We need to sum the smallest needed times for a continous substring of the same letter
    - Loop through the string from 0 - n-1
        - update the current max for current substring of same letters
        - update the current sum for current substring of same letter
        - if current letter is same as next, then we continue the loop
        - if current letter is not the same as next
            - calculate total - max and add it to total minutes
            - reset total = 0 and max = 0

Edge Case:
    - at last index, we simply calculate total - max and add it to total minutes

Complexity:
    - O(n) time since we need to loop through every letter of the string
    - O(1) aux space and output space since we use no other data structure 
"""
