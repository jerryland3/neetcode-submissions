class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        curString = []

        def helper(openCount: int, closeCount: int):
            if openCount == closeCount == n:
                output.append("".join(curString))
            
            if openCount < n:
                curString.append("(")
                helper(openCount + 1, closeCount)
                curString.pop()

            if closeCount < openCount:
                curString.append(")")
                helper(openCount, closeCount + 1)
                curString.pop()
            
        helper(0, 0)
        return output


"""
n = 2

                    (()()(), ((())), (())(), ()(()), (()()))

what makes a string valid:
    - each open bracket have a corresponding closing bracket
    - The open bracket appear before its corresponding closing bracket

                            (
                    ((                      ()
             (((         (()              ()(       
        ((()         (()(   (())       ()((   ()() 
    ((())
((()))
rules for choosing bracket:
    - first choice must be open
    - if open == close, then must choose open
    - can have at most n open and n close

base case:
    - if open == close == n, then append to output and return

recursive case:
    - if open < n, choose open and recurse
    - if close < n, choose close and recurse

complexity:
    - 
    - aux space is at most O(2n) since the recursion stack is at most 2n deep. 

"""
        