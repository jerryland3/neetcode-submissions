class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashTable = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
            }
        output = []
        curList = []
        length = len(digits)

        def helper(index: int):
            if index > (length - 1):
                output.append("".join(curList))
                return
            
            for char in hashTable[digits[index]]:
                curList.append(char)
                helper(index + 1)
                curList.pop()

        if length == 0:
            return output
        helper(0)
        return output

"""
s = 34952
s = 23456789
s = 234567892348579

2 -> a, b, or c
s =    3      4      5
    [d,e,f][g,h,i][j,k,l]

curList = [d,g,j] [d,h,i] [f,g,l]

so for s = 345, we would have 3*3*3 = 3^3 = 27 combinations.
In general, we would have 4^(len(s)) combinations if 7 and 9 are repeatedly choosen.

lets use a simple example
s =    3     4
    [d,e,f][g,h,i]


                     []
          d           e            f            index = 0
      g   h   i    g  h  i      g  h   i        index = 1

base case:
    - reaching the end of s -> index > len(s) - 1
    - append curList to output, then return

recursive case:
    - loop through all character mapping of current number
    - append character to curList, recursive call, pop from curList

complexity:
    - O(4^n) combinations, each combination requires appending n element to the cur list, thus time complexity
      is O(n*4^n). n is number of numbers in s.
    - aux space is O(n) for the recursion layers. output space will have 4^n combinations and each combinations
      will have n elements, thus output space of O(n*4^n)
"""
