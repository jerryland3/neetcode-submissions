class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        curList = []
        length = len(candidates)
        candidates.sort()

        def helper(index: int, curSum: int):
            if curSum == target:
                output.append(curList[:])
                return
            elif curSum > target or index >= length:
                return
            
            for j in range(index, length):
                if j > index and candidates[j] == candidates[j-1]:
                    continue
                curList.append(candidates[j])
                helper(j + 1, curSum + candidates[j])
                curList.pop()

        helper(0, 0)
        return output

"""
nums = [2,2,4,6,1,5] target = 8
nums = [1,2,2,4,5,6]

                            []
        2                        4                    6              1          5          
    2      4 6 1 5             6 1 5                 1 5             5
  4 6 1 5 
      5
need to sort the original list to skip repeats. O(logn) time once

base case:
    - curList sums to target, add curList[:] to output and return
    - curList > target or index >= len(nums), return

recursive case:
    - loop j from current index to len(nums) - 1
    - check if nums[j] = nums[j-1] if j != 0
    - append nums[j] to curList
    - recurse with input j + 1
    - pop from curList

complexity:
    - top layer have n nodes, next layer have at most (n-1)^2 nodes, next layer have at most (n-2)^3 nodes,
      at layer n, we will have at most n^n nodes. Time complexity is O(n^n)
    
    - aux space is at most O(n) due to the n recursion stack.
"""