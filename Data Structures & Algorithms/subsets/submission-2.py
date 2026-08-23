class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        currentSubset = []

        def helper(index: int):
            if index == len(nums):
                output.append(currentSubset.copy())
                return
            
            currentSubset.append(nums[index]) # add
            helper(index + 1)
            currentSubset.pop() # remove
            helper(index + 1)

        helper(0)
        return output
"""
[1, 2]
         []
    
   [1]         []

[1, 2] [1]  [2]   []

[]
2
[[1, 2], [1], [2], []]

each layer of decision tree is the index number of the array
traverse left subtree, we add index value of array into the set
traverse right subtree, we do not add that index value

only append the subset into our output list when we are at the last index of array

time complexity O(2^n * n) because there can be 2^n subset and the worst subset takes n time to build
space complexity O(h) where h is the number of subsets or O(2^n *n) where n is the number of elements in input array
"""
        