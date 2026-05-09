class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[right] and (nums[mid] < target <= nums[right]):
                left = mid + 1
            elif nums[mid] > nums[right] and (target > nums[mid] or target <= nums[right]):
                left = mid + 1
            else:
                right = mid - 1
        
        return -1

"""
0 1 2 3 4 5

5 0 1 2 3 4
4 5 0 1 2 3

3 4 5 0 1 2
2 3 4 5 0 1
1 2 3 4 5 0


if target = mid
    found target
if mid < right and  mid < target <= right
    then target must be between mid+1 and right
if mid > right and mid < target <= right
    then target must be between mid+1 and right
else
    target must be between mid-1 and left
"""
        