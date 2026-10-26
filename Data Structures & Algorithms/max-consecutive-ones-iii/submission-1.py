class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        result = 0
        left = 0
        zeroCount = 0
        for right, num in enumerate(nums):
            if num == 0:
                zeroCount += 1

            while zeroCount > k:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1
            
            result = max(result, right - left + 1)
        
        return result


"""      l
        r
nums = [01]
k = 0
zc = 0
res = 1

return maximum number of consecutive 1'ss in the array if you can flip at most k 0's

Strategy:
    - use sliding window to compute the longest sub array with 1's

Valid Window:
    - zeroCount <= k
    - once window is invalid, move left until window is valid

Algorithm:
    - each loop move right pointer, if current index value == 0, then increment zeroCount
    - once invalid, move left until winodw is valid (zoerCount <= k)
    - compute the window length each loop 

Complexity:
    - O(n) time for sliding window
    - O(1) aux space
"""