class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        curList = []
        
        def helper(index: int):
            if len(curList) == k:
                output.append(curList.copy())
                return
            if index > n:
                return
            
            curList.append(index)
            helper(index + 1)
            curList.pop()
            helper(index + 1)

        helper(1)
        return output

"""
n = 3
k = 2

range: 1 - 3

[1,2][1,3][2,3]

so n must be positive
n >= k

                      []                        1
            1                    []             2
      1,2        1           2       []         3
            1,3     1   2,3    2   3    []      4   

base case:
    - created a subset of size k, append to output list, return
    - index > n, return

recursive case:
    - append index to current list
    - traverse down to index + 1 for inclusive branch
    - pop from current list
    - traverse down to index + 1 for exclusive branch

complexity:
    - O(k*2^n) time complexity since we are bounded by all possible of subsets from 1-n, and we are at most adding k element per leaf node
    - O(n) since our recursion stack is at most n + 1
"""