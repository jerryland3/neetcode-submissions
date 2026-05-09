import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator_dict = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a/b)}

        for item in tokens:
            if item not in operator_dict:
                stack.append(int(item))
            else: # else operator encountered
                num2 = stack.pop()
                num1 = stack.pop()
                result = operator_dict[item](num1, num2)
                stack.append(result)

        return stack.pop()
        
"""
[1, 2, +, 3, *, 4, -]
((1 + 2) * 3) - 4 = 5

stack = [-, 4, *, 3, +, 2, 1]

stack_operand = [1, 2]
1 + 2 = 3
[3]

[3, 3]
3 * 3 = 9
[9]

[9, 4]
9 - 4 = 5
[5]

[1, 2, 3, *]




"""