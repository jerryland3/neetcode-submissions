class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        curList = []
        numsLength = len(nums)
        numsSorted = sorted(nums)

        def helper(index: int):
            if index >= numsLength:
                output.append(curList[:])
                return
            
            curList.append(numsSorted[index])
            helper(index + 1)
            curList.pop()
            
            while index < numsLength - 1 and numsSorted[index] == numsSorted[index + 1]:
                index += 1
            helper(index + 1)
    
        helper(0)
        return output

"""
index = 0

curList = []
output = [[1 1 2] [1 1] [1 2]]

first sort the subset

1 1 2

                     1                  []
               1 1       []        2         []
        1 1 2     1 1  1 2  1

[1 1 2] [1 1] [1 2] [1] [2] []

time complexity:
    - O(n*2^n) time since we have binary decision at each level and at the leaf we are copying at most n elements.
    - O(n) aux space for the recursion stack and curList. O(n*2^n) output space.

"""
        