class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack = []
        for index in range(len(s) - 1, -1, -1):
            if index == len(s) - 1:
                stack.append(0)
            elif s[index + 1] == "a":
                stack.append(stack[-1] + 1)
            else:
                stack.append(stack[-1])
        
        aRight = []
        while stack:
            aRight.append(stack.pop())
        
        bLeft = 0
        result = aRight[index]
        for index, char in enumerate(s):
            if index > 0 and s[index - 1] == "b":
                bLeft += 1
            result = min(bLeft + aRight[index], result)

        return result



"""
aaabbbaa
43222210
00001233




make a decision at each split point between each character:
    - the split require every letter to the left to be a
    - the split also require every letter to the right to be b
    - require building list where value is the number of a to the right of current index

Complexity:
    - O(n) time since we need to build the list of number of a's to the right of each index and looping through each
      char again
    - O(n) aux space for the list and O(1) output space.
"""