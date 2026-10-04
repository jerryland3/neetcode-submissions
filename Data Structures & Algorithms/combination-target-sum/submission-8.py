class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        curList = []
        inputLength = len(nums)

        def helper(index: int, curSum: int):
            if curSum == target:
                output.append(curList[:])
                return
            if curSum > target:
                return
            
            for j in range(index, inputLength):
                curList.append(nums[j])
                helper(j, curSum + nums[j])
                curList.pop()
        
        helper(0, 0)
        return output

"""
index = 2
curSum = 0
j = 2

curList = [3]
output = [[1 1 1] [1 2] []]

nums = [1 2 3 4]
target = 3

[[1 1 1] [1 2] [3]]


                    []
               1                           2              3          4
      1        2    3  4                  2   3   4        3   4        
 1 2 3 4

 complexity:
    - a loose upper bound for time is O(d*n^d), where d is the depth of the decision tree. The depth
      is at most target/min(nums) => t/s. Thus time complexity is O((t/s)*n^(t/s))
    - Aux space of O(t/s) for recursion stack and curList. A loose upper bound on output space is 
      O(t/s*n^(t/s)). The output space will depends on both the target value and the numbers in
      nums.     
"""

