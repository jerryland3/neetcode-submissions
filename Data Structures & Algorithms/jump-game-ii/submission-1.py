class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        jumps = 0
        maxReach = 0
        for index, num in enumerate(nums):
            if index > end:
                end = maxReach
                jumps += 1
            maxReach = max(maxReach, num + index)
        
        return jumps


"""
nums[i] - maximum length of a jump toward the right from index i
start at i = 0

Return mininum number of jumps to reach the last position of the array. Always a valid answer exist
-----------------------------------------

i
1
-
  ---
      -----

end = 0
jumps = 0

maxReach = 1


Strategy:
    - every time we reach past teh end mark, increment jump and update start and end. Essentially, we are building the
      end mark for each level once we reach that level.

Complexity:
    - O(n) time since we are traversing the list once
    - O(1) aux and output space
"""