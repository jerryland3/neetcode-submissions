class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        total_pair = n
        solution = []
        result = []

        def backtrack(open_n, close_n):
            # base case
            if open_n == total_pair == close_n:
                result.append("".join(solution))
                
            # recursive case when open_n < n
            if open_n < total_pair:
                solution.append("(")
                backtrack(open_n + 1, close_n)
                solution.pop()
            
            # recursive case when close_n < n
            if close_n < open_n:
                solution.append(")")
                backtrack(open_n, close_n + 1)
                solution.pop()


        backtrack(0, 0)
        return result

"""
n = 3
[((())), (()()), (())(), ()(()), ()()()]

              (
        
        ((         ()   

    (((   (()       ()(   

((()     (()(  (())    ()((   ()()

((())  (()()  (())(    ()(()   ()()(

((()))  (()())  (())()  ()(())  ()()()


     close <= open
     open and close must equal to n

"""
        