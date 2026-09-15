class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        curList = []
        seen = []
        length = len(nums)
        for _ in nums:
            seen.append(False)
        
        def helper(index: int):
            if(index == length):
                output.append(curList[:])
                return
            
            for j in range(length):
                if seen[j]:
                    continue
                curList.append(nums[j])
                seen[j] = True
                helper(index + 1)
                curList.pop()
                seen[j] = False
        
        helper(0)
        return output

"""
first level have n choice
second level have n-1 choice
...
nth level have 1 choice

leaf node have O(n) cost since it and there are n! leaf nodes. Thus cost at leaf is O(n*n!).

2
[2 3 1]
[T T T]
output = [[1 2 3] [1 3 2] [2 1 3]]
"""