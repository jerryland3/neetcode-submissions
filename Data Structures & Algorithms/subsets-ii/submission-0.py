class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        curList = []
        length = len(nums)
        nums.sort()

        def helper(index: int):
            if index >= length:
                output.append(curList.copy())
                return
            
            curList.append(nums[index])
            helper(index + 1)
            curList.pop()

            while (index < length-1) and (nums[index] == nums[index + 1]):
                index += 1
            helper(index + 1)
        
        helper(0)
        return output




"""
        [7,7]    
    [7]             []
[7,7]  [7]       []    []

subset = [7]
index = 3
output = [[7,7],[7],[]]

base case: index > len(nums), we reached the end, append curList into output

recursive case: append nums[index] into curList, recursivly traversed down tree with index + 1, pop from curList, 
recursively traversed down tree with index + 1

special condition for duplicates: if current index value is the same as previous index value, then skip by incrementing index.
This need to be done before 2nd recursive traversal. We also need to make sure our index is not bigger than len(nums).

Sorted order will be important here, so sort first with O(nlog(n)) time.

Time complexity: the number of subset is at most 2^n and we build at most a subset of size n. Time complexity is O(n*2^n)
Space complexity: O(h), where h is the height of the tree for the recursion stack.


[1,1,2]

index = 0
curList = []
output = []

            1                       []
    1,1          1,2           2          []
1,1,2  1,1                 2              []
      
"""
        