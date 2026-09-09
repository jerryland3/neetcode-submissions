class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        curList = []
        length = len(s)

        def validPalindrome(left: int, right: int) -> bool:
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def helper(index: int):
            if index >= length:
                output.append(curList[:])
                return

            for j in range(index, length):
                # check if string from index to j is a valid palindrome
                if validPalindrome(index, j):
                    curList.append(s[index:j+1])
                    helper(j + 1)
                    curList.pop()

        helper(0)
        return output

"""
s = aab

A plaindrome is a string where reversing the string results in the same string.

                        aab
        a               aa              aab
    a      ab           b              
  b           

                        aaba
        a          aa             aab          aaba
  a    ab  aba                           
b  ba        
a           

base case:
    - if index is at the end of string, index >= len(s) - 1, then add curList to output and return

recursive case:
    - loop through all current parition of the string at this level, recursivly parition from index + 1 if
      current parition is a valid palindrome

"""
        