class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        currentList = []

        def helper(index: int, total: int):          
            if total == target:
                output.append(currentList.copy())
                return
            elif total > target or index == len(nums):
                return
            
            for i in range(index, len(nums)):
                currentList.append(nums[i])
                helper(i, total + nums[i])
                currentList.pop()

        helper(0, 0)
        return output

"""
Decision tree with n decisions. Base condition is when our leaf node value exceed or equal target.

nums = [3,4,5], target = 16

                            []
                    [3]    [4]     [5]

            [3,3] [3,4] [3,5]           [3,3]

    [3,3,3]     [1,1,3]

[3,3,3,3] [1,1,1,3]

[1,3]
[[1,1,1,1], []]


same pattern of add, recurse, remove of currentSubset.
Need to check for unique combinations.

Use index to track path, right subtree use index + 1 while left use index. Once we go to index + 1, we do not want to go back to index 0 again since this could cause repeat.

time complexity is O(2^(t/m)) where t is the target value and m is the smallest value in nums
Space complexity is O(t/m) since recursion stack is at most t/m
"""