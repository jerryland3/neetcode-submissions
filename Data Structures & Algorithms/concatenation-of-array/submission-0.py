class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums.copy()
        for num in nums:
            ans.append(num)
        
        return ans

"""
[1 4 1 2 1 4 1 2]

nums = [1 4 1 2]
n = 4

2n = 8
ans = [1 4 1 2 1 4 1 2]

strategy:
    make a copy of nums, then loop through nums and append each element to the copy.

complexity:
    O(n) time since we need to loop through every element twice
    O(n) output space since ans is of length 2n
"""