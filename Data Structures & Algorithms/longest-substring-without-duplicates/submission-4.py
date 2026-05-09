class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        left = 0
        longest = 0
        char_seen = {}

        for index, char in enumerate(s):
            substring_length = index - left
            longest = max(longest, substring_length)
            if char not in char_seen:
                char_seen[char] = index
            else:
                new_left = char_seen[char] + 1
                for previous_index in range (left, new_left):
                    char_seen.pop(s[previous_index])

                char_seen[char] = index
                left = new_left

        if (index - left) == longest:
            return longest + 1
        
        return longest
                
        

"""
zxyzxyz

left = 4
longest = 5
char_seen = {z: 4, w: 5, y: 6, x: 7, j: 8, a: 9}

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