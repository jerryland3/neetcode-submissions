class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        chars_seen = set()

        for right, char in enumerate(s):
            while char in chars_seen:
                chars_seen.remove(s[left])
                left += 1

            chars_seen.add(char)
            length = (right - left) + 1
            longest = max(length, longest)

        
        return longest
                
        

"""
left = 4
longest = 5

index = 7
substring_length = 4
new_left = 4

0 1 2 3 4 5 6 7 8 9 
z j x y z w y x j a

left = 0
longest_substring = 0
use dict to keep track of the char seen along with its index

loop through the string char by char
    add char into dict if dict does not already contain it

    if dict already contain char, move left pointer to the previous location where
    that char was seen and add 1

    calculate substring length, if its longer than longest, update longest substring

care need to be taken when returning longest_substring, we should add 1 to longest_substring
if its not 0    
"""