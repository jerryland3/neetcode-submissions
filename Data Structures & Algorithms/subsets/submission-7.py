class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        curList = []
        inputLength = len(nums)

        def helper(index: int):
            if index >= inputLength:
                output.append(curList[:])
                return
            
            curList.append(nums[index])
            helper(index + 1)
            curList.pop()
            helper(index + 1)
        
        helper(0)
        return output

"""                  
            1                    []
     1 2         1          2       []
1 2 3   1 2  1 3   1    2 3   2   3    [] 

Complexity:
    - O(n*2^n) time since at each index, we have a binary decision. n is the size of the input array
    - O(n) aux space for the current list and recursion stack, 
      O(n*2^(n)) output space because we  have 2^n subset and each. subset can have at most n items,
      the average subset size is n/2.
"""
        