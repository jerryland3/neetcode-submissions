class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
"""
use a list, already have built in append, pop, 
and top can be acheived with indexing the list with -1

1 2 0

[1, 2]
[1, 1]



keep track of minimum value
every time item added to stack compare that with minimum value identified
so far, if this value is less, than set as new min

"""
