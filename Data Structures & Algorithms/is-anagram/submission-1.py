from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = defaultdict(int)
        for char in s:
            count[char] += 1
        
        for char in t:
            if char not in count or count.get(char) == 0:
                return False
            
            count[char] -= 1
        
        return True
            
        

"""
jar
jam

{
j:0
a: 0
r: 1
}

Strategy:
    first check if lenth of both string are the same
    create a dictionary for first string containing count of each char
    loop through second string and subtract from the dictionary.
        if none of the char are less than zero during subtraction or if the char exist, then it is an anagram

Complexity:
    - O(n) time where n is the number of char in both string. Need to loop though both string.
    - O(26) space for the dictionary, O(1) output space
"""
        
        