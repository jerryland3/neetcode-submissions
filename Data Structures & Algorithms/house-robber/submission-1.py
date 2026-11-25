class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def dp(index: int) -> int:
            if index == 2:
                return nums[0]
            if index < 2:
                return 0
            if index in cache:
                return cache[index]

            cache[index] = max(dp(index - 2) + nums[index - 2], dp(index - 3) + nums[index - 3])
            return cache[index]
        
        return dp(len(nums) + 1)

"""
nums[i] - the amount of money house i has
houses are adjacent by their index
cannont rob two adjacent houses

return the maximum amount of money we can rob
--------------------------------------------------

0 1 2 3 4 5 6 
1 2 3 1 5
max = 4


                       [6]
                  4           3      
                2  1        1   0      
                0

Base Case:
    - reached index 0 or 1 or 2. if n <= 2
    - dp(n) is the maximum money gained to reach house n
    - dp(n) = max(dp(n-2) + nums[n-2], dp(n-3) + nums[n-3])
    - start from dp(len(nums) + 1)

Complexity:
    - recursive solution is O(2^n) since we make two choices at each branch
    - space complexity of O(n) for recursion stack
"""