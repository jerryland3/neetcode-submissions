class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        curList = []
        length = len(nums)

        def helper(index: int, curSum: int):
            if curSum == target:
                output.append(curList[:])
                return
            if curSum > target:
                return
            
            for j in range(index, length):
                curList.append(nums[j])
                helper(j, curSum + nums[j])
                curList.pop()
        
        helper(0, 0)
        return output

"""
nums = [1,2,3,5]
target = 3

[[1,1,1], [3], [2,1]]

                            []
           1                                2             3          5
    1,1            1,2  1,3  1,5       2,2 2,3 2,5            
1,1,1  1,1,2 ...

base case:
    - current sum == target, add combination to output and return
    - current sum > target, just return

recursivly traverse down, index is always start at what parent pass down to prevent repeat

complexity:
    - depth is at most target/s, where s is the smallest number in nums. Branching factor is at most n. The work
      at each node is O(1) since we are just appending and poping. 
      Thus, a loose upper bound on time is O((t/s)*n^(t/s)) due to coping at the leaf of at most t/s numbers.

    - aux space is O(t/s) for recursion stack. The output space is at most O((t/s)*n^(t/s)) 

"""

