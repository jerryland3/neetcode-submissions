class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0] * len(temperatures)

        for index in range(len(temperatures)):          
            if index == 0 or temperatures[index] <= temperatures[index - 1]:
                stack.append(index)
            else:
                while stack and temperatures[stack[-1]] < temperatures[index]:
                    stack_index = stack.pop()
                    results[stack_index] = index - stack_index
                stack.append(index)

        return results
        
"""
30 38 30 30 36 35 40 28
[0] - stack

[1] - stack
[1] - results

[]
[1 5 2 1 2 1 0 0]

[6 7]


"""