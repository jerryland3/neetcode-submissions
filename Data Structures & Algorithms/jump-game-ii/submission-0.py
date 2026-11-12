class Solution:
    def jump(self, nums: List[int]) -> int:
        jumpCount = 0
        index = 0

        while index < len(nums) - 1:
            if index + nums[index] >= len(nums) - 1:
                jumpCount += 1
                return jumpCount
            index = self.searchNext(nums, index)
            jumpCount += 1
        
        return jumpCount
            
    def searchNext(self, nums: List[int], index: int) -> int:
        maxReach = 0
        nextIndex = 0
        start = index + 1
        end = index + nums[index] + 1
        for j in range(start, end):
            if nums[j] + j > maxReach:
                maxReach = nums[j] + j
                nextIndex = j
        return nextIndex


"""
i
3 3 4 2 1 0 1 3 5

count = 3

Strategy:
    While at index i, always select the next index that allow us to jump farthest to the right.
    We do need to check if our current index value allow us to jump to the end, if so we can break the loop
    Update count on each jump

Complexity:
    - O(n) time since we loop through the list at most once, though we do have inner for loop to search for next
      index to jump to
    - O(1) aux space and output space
"""