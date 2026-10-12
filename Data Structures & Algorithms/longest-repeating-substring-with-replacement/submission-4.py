from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        output = 0
        left = 0
        charCount = defaultdict(int)

        for right, char in enumerate(s):
            charCount[char] += 1
            windowLength = right - left + 1
            
            while windowLength - self.mostFrequent(charCount) > k:
                charCount[s[left]] -= 1
                left += 1
                windowLength = right - left + 1
                
            output = max(output, windowLength)
        
        return output
    
    def mostFrequent(self, countDict: dict) -> int:
        maxCount = 0
        for _, count in countDict.items():
            maxCount = max(maxCount, count)
        
        return maxCount
            

"""
out = 5
left = 3
right = 6
char = A

charCount = {
    A: 1
    B: 3
}

4 - 3 <= 1

Performe K replacement, return length of longest substring which contain on distinct characters
s = AAABABB
K = 1

AAAB

valid window => windowLength - mostFreqCount <= k

{
A: 1
B: 2
X: 0
Y: 0
}

3 - 2 = 1 <= 1
result = 5

Complexity:
    - searching through the dictionary is O(26) since we have at most 26 characters. We need to do this at
      each window pointer move, thus time complexity (26*n), where n is the number of characters in s.
    
    - O(26) aux space needed for the dictionary. O(1) output space
"""