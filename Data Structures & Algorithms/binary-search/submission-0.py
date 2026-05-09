class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            index = left + (right - left)//2
            if target > nums[index]:
                left = index + 1
            elif target < nums[index]:
                right = index - 1
            else:
                return index
        
        return -1

"""
[-1 0 2 4 6 8]
target = 4
left = 0
right = 5
index = left + (right - left)/2 = 2
target > array[2] = 2

left = index + 1 = 3
right = 5

index = left + (right - left)/2 = 4
array[4] = 6
target < 6
right = index - 1 = 3
left = 3

index = left + 0 = 3

"""