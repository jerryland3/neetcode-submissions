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
    - longest path is t/m, where m is the smallest number in nums.
      let d = t/m. At layer 1 we will have n^1 elements, at layer two we will have n^2 elements, at layer d, we will have at most n^d elements.
      Each operation is O(1) since we just append, recurse, and pop. On leaf node, we copy at most O(d) elements over.
      Thus time complexity is O(d*n^d).

    - aux space complexity of O(d) = O(t/m) since we have at most t/m layers. Output space is at most O(d*n^d) since output leaf have at most d elements and there
      are at most n^d leaf nodes.
"""

