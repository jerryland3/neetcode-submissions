class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index = 0
        while (index < len(nums) - 1) and (nums[index] != 0):
            start = index + 1
            end = index + nums[index] + 1

            maxJumpIndex = start
            maxJump = 0
            for j in range(start, end):
                if j == len(nums) - 1:
                    maxJumpIndex = j
                    break
                if nums[j] + j >= maxJump:
                    maxJumpIndex = j
                    maxJump = nums[j] + j

            index = maxJumpIndex
        
        if index >= len(nums) - 1:
            return True
        return False 
            

            
"""
Given:
    nums - int array
    nums[i] indicate max jump length

    Return true if we can reach last index starting from index 0, otherwise return false

       i
nums = 1 2 1 0 1

Greedy:
    - the greedy choice at each index is to select the next index that allow us to jump the farthest. This is because
      The jump that allow us to make the farthest gain will include all possible position that smaller jump gets us.

Complexity:
    - O(n) time in worst case when the nums array is all "1"
    - O(1) aux and output space

"""