class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left = 0
        right = len(tokens) - 1
        maxScore = 0
        curScore = 0
        while left <= right:
            if tokens[left] <= power:
                curScore += 1
                power -= tokens[left]
                maxScore = max(maxScore, curScore)
                left += 1
            elif curScore > 0:
                curScore -= 1
                power += tokens[right]
                right -= 1
            else:
                return maxScore
        
        return maxScore
"""
                  r
          l
tokens = 50 55 60 65 
power = 10
score = 0
maxS = 0

if power > sum(tokens), then just return len(tokens)

Greedy choice:
    - keep buying the cheapest if we can buy it
    - if not, then sell score to buy most expensive token

Complexity:
    - O(nlogn) time for sorting, O(n) time for two pointer
    - O(1) or O(n) aux space depending on sorting algorithm
"""