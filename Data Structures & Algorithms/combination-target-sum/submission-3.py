class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        curList = []
        length = len(nums)

        def helper(index: int, curSum: int):
            if curSum == target:
                output.append(curList[:])
                return
            if curSum > target or index == length:
                return
            
            for j in range(index, length):
                curSum += nums[j]
                curList.append(nums[j])
                helper(j, curSum)
                curSum -= nums[j]
                curList.pop()
        
        helper(0, 0)
        return output

"""
nums = [2,5,6], target = 6
                                                []
        2                                 5           6        
    2       5      6             
  2 5 6    5 6     6          

[5]

base case:
    - if path sum == target, then add to output list
    - if path sum > target, then just return

recursive case:
    - loop through every index, starting from current index and onward
    - update path sum
    - add element of current index into curList
    - recursivly traverse down the tree
    - pop element from curList

complexity:
    - 
"""

