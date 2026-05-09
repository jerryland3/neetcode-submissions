class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[left]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

"""
0 1 2 3 4

4 0 1 2 3
3 4 0 1 2

2 3 4 0 1
1 2 3 4 0
"""
        