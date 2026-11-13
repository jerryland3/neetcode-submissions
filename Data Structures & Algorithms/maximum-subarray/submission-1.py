class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = nums[0]
        for num in nums:
            curSum = max(0, curSum)
            curSum += num
            maxSum = max(curSum, maxSum)
        
        return maxSum

"""                      
nums - int array given
Find the sublist with largest sum, return that sum
---------------------------------------------------
                 i
2 -3 4 -2 2 1 -1 4

curSum = 8
maxSum = 8

    i
-2 -1 -3

Strategy:
    - never add negative curSum since that just decrease the overall sum
    - Once our curSum becomes negative, it is just better to start over with curSum = 0. This is because if our curSum
      becomes negative, then future subarray that include curSum will be smaller than if its not included.

Complexity:
    - O(n) time since we loop through the list once
    - O(1) aux and output space
"""