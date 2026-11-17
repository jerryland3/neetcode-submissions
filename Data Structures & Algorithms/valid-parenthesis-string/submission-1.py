class Solution:
    def checkValidString(self, s: str) -> bool:
        lowCount = 0
        highCount = 0

        for char in s:
            if char == "(":
                lowCount += 1
                highCount += 1
            elif char == ")":
                lowCount -= 1
                highCount -= 1
            else:
                lowCount -= 1
                lowCount = max(0, lowCount)
                highCount += 1
            
            if highCount < 0:
                return False
        
        return lowCount <= 0 <= highCount

"""
*

Given string s, the strin only contain "(", ")", or "*"
* can be left paren, right paren, or empty string

Return true if s is valid, otherwise false
------------------------------------------------------

Strategy:

    can brute force this by creating a list for every combination where "*" is replaced with all possible cases, then
    check with a stack to see if string is valid. though this is likly exponential time n*3^(num of *)

    i
    )))(

    lowCount = 1: If we take all right bracket, then we end up with an extra right bracket
    highCount = 3: If we take all left bracket, then we end up with 3 extra left bracket

    This tell us that if both low and high count never gets negative and zero is between them at the end of the loop,
    then the string is valid.

Complexity:
    - O(n) time since we loop through the string once
    - O(1) aux and output space

"""