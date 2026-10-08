class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        curList = []
        used = []
        inputLength = len(nums)

        for _ in range(inputLength):
            used.append(False)
        
        def helper(depth: int):
            if depth == inputLength:
                output.append(curList[:])
                return
            
            for index in range(inputLength):
                if used[index]:
                    continue
                
                curList.append(nums[index])
                used[index] = True
                helper(depth + 1)
                curList.pop()
                used[index] = False
        
        helper(0)
        return output


"""
nums = [1 2 3]
out = [[1 2 3] [1 3 2] ]
used = [F T F]
curList = [2]
depth = 0


                1             2              3
            2       3     1       3      1        2
            3       2     3       1      2        1

Complexity:
    - n(n-1)(n-2)...(1) = n! permutations. Copy at leaf is O(n). Thus time complexity is O(n*n!)
    - O(n) aux space for recursion stack and curList and used table. O(n*n!) output space. 

"""