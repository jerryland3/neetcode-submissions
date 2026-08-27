class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        curList = []
        length = len(nums)

        def helper(index: int):
            if index >= length:
                output.append(curList[:])
                return
            
            curList.append(nums[index])
            helper(index + 1)
            curList.pop()
            helper(index + 1)
        
        helper(0)
        return output

"""
[1,2,3]
                []
        1                []       index = 0
   1,2        1       2      []   index = 1
1,2,3 1,2   1,3 1  2,3 2    3  [] index = 2

base case:
    - index >= len(nums), append our curList to output and return

recursive case:
    - append nums[index] to curList
    - call recursive function with index + 1
    - pop curList
    - call recursive function with index + 1

complexity:
    - total of 2^n subsets, where n is the number of elements in nums. Building each subset requires
      appending at most n elements. time complexity of O(n * 2^n)
    
    - our curList will hold at most n elements and there are at most n + 1 recursion stack.
      We will always have 1 curList, thus aux space is associated with recursion stack. 
      Thus, space complexity of O(n). Output space requires O(2^n) space for 2^n subsets.
"""
        