class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        curList = []
        length = len(nums)
        used = [False for _ in range(length)]

        def helper(index: int):
            if index >= length:
                output.append(curList[:])
                return
            
            for j in range(length):
                if used[j]:
                    continue
                curList.append(nums[j])
                used[j] = True
                helper(index + 1)
                curList.pop()
                used[j] = False
        
        helper(0)
        return output
    

"""
nums = [1,2,3]

                        []
             1          2           3          0
          2    3      1   3       1   2        1
          3    2      3   1       2   1        2

    [T,F,F]   [T,F,F]
    [T,T,F]   [T,F,T]
    [T,T,T]   [T,T,T]

base case:
    - index >= len(nums), append copy of curList to output and return

recursive case:
    - loop through j from 0 to len(nums)-1
    - check if index j of truth table is False. If so, append nums[j] into curList and set truth table to True. If not, continue
    - recursivly go into next level with truth list and index + 1
    - pop from curList and restore truth list by setting index j to False

complexity:
    - n! choices and each permutation requires n list append. Time complexity of O(n*n!)
    - curList appending happen in place. Recursion stack is at most n levels. Thus need O(n) aux space and O(n*n!) output space.
"""
        