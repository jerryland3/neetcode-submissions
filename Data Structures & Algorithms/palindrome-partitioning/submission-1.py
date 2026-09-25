class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        curList = []
        length = len(s)

        def isPalindrome(left: int, right: int):
            while left < right:
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
                if isPalindrome(index, j):
                    curList.append(s[index:(j + 1)])
                    helper(j + 1)
                    curList.pop()
        
        helper(0)
        return output
"""
s = aab
[[a,a,b] [aa,b]]
aab
a, ab
aa, b
a a b
                        aab
        a                aa             aab              
    a         ab          b
    b      

curList = ["a", ...]
base case:
    - index > len(s), append curList to output and return
    - if current substring is not a palidrome, return. (can use two pointer to check for palindrome)

recursive case:
    - append current substring to curList, recurse with index + 1, pop from curList

Complexity:
    - each cut is a binary choice, and there are n-1 cuts. Thus, there are at most 2^(n-1) cuts to try. If each cut
      is a valid palindrome, then copying it from curList to output is O(n) for each. Thus time is O(n*2^(n-1)).
    - aux space is O(n) due to recursion stack and curList. Output space is O(n*2^(n-1)) in worst case.

    cut1       cut2 
     no         no
     yes        no
     no         yes
     yes        yes
"""
        