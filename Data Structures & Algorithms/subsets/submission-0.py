class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        length = len(nums)

        def helper(curList: List[int], index: int):
            if index == length:
                output.append(curList[:])
                return
            
            # curList + [nums[index]] creates a NEW list by value
            helper(curList + [nums[index]], index + 1)
            helper(curList, index + 1)

        helper([], 0)
        return output

"""
[1, 2]
         []
    
   [1]         []

[1, 2] [1]  [2]   []


each layer of decision tree is the index number of the array
traverse left subtree, we add index value of array into the set
traverse right subtree, we do not add that index value

only append the subset into our output list when we are at the last index of array
"""
        