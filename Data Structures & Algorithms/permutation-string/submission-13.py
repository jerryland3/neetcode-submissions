from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charCount = defaultdict(int)
        for char in s1:
            charCount[char] += 1
        
        left = 0
        for right, char in enumerate(s2):
            if char not in charCount:
                while left < right:
                    charCount[s2[left]] += 1
                    left += 1
                left += 1
                continue
            
            charCount[char] -= 1
            while charCount.get(char) < 0:
                charCount[s2[left]] += 1
                left += 1
            
            if (right - left + 1 == len(s1)):
                return True
        
        return False
"""
{
    a: 1
    b: 1
}

s1 = ab
s2 = eidboaoo
         l
         r

does s2 contain a permutation of s1?

Condition for permuation, does s2 contain a substring where its count matches exactly s1 count of characters

lecaabcee
    l
    r

{
    a: 0
    b: 1
    c: 1
}

A valid window:
    - the character in the window is in s1 and its count is not more than s1 count for each character

return true if we encounter a valid winodw where window length == len(s1)

Complexity:
    - O(n) time since we need to traverse the string once
    - O(26) aux space for dictionary, O(1) output
"""