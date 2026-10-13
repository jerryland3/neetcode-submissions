class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        minLen = 0
        total = 0

        for right, num in enumerate(nums):
            total += num
            while total >= target:
                windowLen = right - left + 1
                minLen = windowLen if minLen == 0 else min(minLen, windowLen)
                total -= nums[left]
                left += 1

        return minLen

"""
2 1 5 1 5 3
target = 10

min length: where sum >= target

2 1 5 1 5 3
l
          r

target = 1000

minLen = 3
total = 9
target = 10

1. what is a valid window:
    sum < target - keep growing window to the right
    sum >= target - update minLength, then move left window until sum < target

2. Edge case:
    initally set minLen = 0. Check if minLen == 0 when sum >= target, update minLen to the actual minLen
    if minLen != 0, then just use min(minLen, currentLength)

Complexity:
    - O(n) time since left and right pointer will loop through the input at most once
    - O(1) aux space, and O(1) output space

"""