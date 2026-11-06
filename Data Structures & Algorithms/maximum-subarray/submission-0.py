class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        for num in nums:
            curSum = max(curSum, 0) + num
            maxSum = max(curSum, maxSum)
        
        return maxSum


"""                      n
nums = [2 -3 4 -2 2 1 -1 4]
curSum = 8
maxSum = 8

4 -5 1 1 1 1 1

find the subarray with the largest sum and return that sum

Strategy:
    - make a greedy choice at each index
    - if current sum is negative, then start over at zero at the next index. This is because if a find a larger
      subarray at later indicies, including the previous negative results would not result in largest subarray
    - if current sum is positive, then keep going with the current subarray

Complexity:
    - O(n) time since we loop through the list once
    - O(1) aux and output space since we are not using any data structure
"""