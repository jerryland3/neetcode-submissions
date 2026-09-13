class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        curList = []
        length = len(nums)
        nums.sort()

        def helper(index: int):
            if index == length:
                output.append(curList[:])
                return
            
            curList.append(nums[index])
            helper(index + 1)
            curList.pop()

            while index + 1 < length and nums[index] == nums[index + 1]:
                index += 1
            helper(index + 1)

        helper(0)
        return output

"""
nums = [1,1,2]

[
    []
    1
    2
    1,2
    1,1
    1,2,3
]

                        []
            1                         []                index = 0
    1,1           1             2           []          index = 1 or 2 depending on condition
1,1,2  1,1     1,2  1        

skip after coming out of first recursive call if current number is equal to next number

complexity:
    - The worst case is when the input does not cotain duplicates, then there are O(2^n) subsets. Building
      each subset is O(n) since we need to append at most n elements and then add those to ouput list. Thus,
      time complexity is O(n*2^n).
    - The aux space complexity is O(n) due to recursion stack of at most n layers. The output space is at most
      O(n*2^n) since there is at most 2^n subsets and a subset have a most n elements. 
"""
        