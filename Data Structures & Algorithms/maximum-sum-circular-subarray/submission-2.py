class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = nums[0]
        minSum = nums[0]
        curMax = 0
        curMin = 0
        total = 0

        for num in nums:
            total += num
            curMax = max(0, curMax) + num
            maxSum = max(curMax, maxSum)
            curMin = min(0, curMin) + num
            minSum = min(curMin, minSum)
        
        if maxSum < 0:
            return maxSum
        elif (total - minSum) < maxSum:
            return maxSum
        return total - minSum
"""
           
5 -3 -2 4 -2 -4 3  5
maxSum = 8
curSum = 8

minSum = -7
curMin = 0
total = 6

total - minSum = 13

-2 3 1 2 -5

3 -5 -2 2

maxSum = 15
curSum = 9

Strategy:
    - if the array do not wrap, then the max sum is the standard kadane algorithm
    - if the max sum do require array warp, then "maxSum = total - min subarray"
        - the min sub-array can be computed similar to regular kadane for min-sum

Loop:
    - for the loop, we want to compute the regular maxSum with kadane
    - we also want to compute the min sum and the total
    - at the end we compare the regular kadane maxSum aginst total - minSum and output the larger value

Complexity:
    - O(n) time since we will loop through the list at most 2x
    - O(1) aux space and O(1) output space
"""