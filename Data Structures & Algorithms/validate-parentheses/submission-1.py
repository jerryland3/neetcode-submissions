class Solution:
    def isValid(self, s: str) -> bool:
        matching = {')': '(',
                    '}' : '{', 
                    ']': '['}
        stack = []

        for char in s:
            # if char is closing bracket and stack is not empty
            if char in matching and stack:
                if not stack or matching[char] != stack.pop():
                    return False
            else:
                stack.append(char)

        if not stack:
            return True
        
        return False

"""
([{}])

()[]

]

[

"""