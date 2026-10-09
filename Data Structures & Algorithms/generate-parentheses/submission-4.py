class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        curList = []

        def helper(openCount:int, closeCount: int):
            if closeCount == n:
                output.append("".join(curList))
                return
            
            if openCount < n:
                curList.append("(")
                helper(openCount + 1, closeCount)
                curList.pop()
            
            if closeCount < openCount:
                curList.append(")")
                helper(openCount, closeCount + 1)
                curList.pop()
        
        helper(0, 0)
        return output

"""
n = 2
[()()] [(())]

n = 3
()()() (())() ()(()) ((())) (()()) 


                    (                                  
            ((            ()                      
            (()           ()(
            (())          ()()


decide between open or close bracket to append at each level

- if current open count < n, then we can always chose open
- if close < open, then we can always chose close

Complexity:
    - binary decison at each level and there are at most 2*n levels. Thus time complexity is
      O(n*4^(n))
    - O(n) aux space for recursion and curList, O(n*4^n) output space.
"""
        