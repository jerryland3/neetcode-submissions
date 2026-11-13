class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = nums[0]
        for index, num in enumerate(nums):
            maxReach = max(maxReach, num + index)
            if maxReach < len(nums) - 1 and maxReach == index:
                return False
        
        return True

"""
nums[i] - maximum jump length at position i

Return true if you can reach the last index starting from index 0. False otherwise
 r
i 
1 

Strategy:
    - maxReach = max(i + nums[i], maxReach)
    - check at end of loop if i == maxReach
        - if so, then return False
    - return true if we finish the for loop

Complexity:
    - O(n) time since we will loop through the list once
    - O(1) aux and output space
"""