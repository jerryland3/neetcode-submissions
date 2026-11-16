from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charCount = Counter(s)
        charSet = set()
        left = 0
        output = []

        for right, char in enumerate(s):
            charCount[char] -= 1
            charSet.add(char)
            if charCount[char] == 0:
                charSet.discard(char)
                if len(charSet) == 0:
                    output.append(right - left + 1)
                    left = right + 1
        
        return output
            
"""
l
r
a

set = ()
output = [1]
{
    a: 0
}
"""