class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        curList = []
        inputLength = len(candidates)
        numsSorted = sorted(candidates)

        def helper(index: int, curSum: int):
            if curSum == target:
                output.append(curList[:])
                return
            if curSum > target:
                return
            
            for j in range(index, inputLength):
                if j > index and numsSorted[j] == numsSorted[j - 1]:
                    continue
                curList.append(numsSorted[j])
                helper(j + 1, curSum + numsSorted[j])
                curList.pop()
        
        helper(0, 0)
        return output






"""
nums = [9 2 2 4 6 1 5]
t = 8

[[2 2 4] [2 6] [2 1 5]]

sorted = [1 2 2 4 5 6 9]

                                []
                    1                                      2       2        4        5         6         9
        2          2*         4     5     6      9      2 3 5 6 9
    2 4 5 6 9   (4 5 6 9)*  5 6 9
 4 5 6 9
when encountering a dup, only use the first apperance of dup, and skip the rest in the decision tree.

Complexity:
    - worsts case is if target is larger than sum of all elements, then we need to build the whole tree.
      Depth is at most n deep, first level have n nodes, each of those spawn n - 1, n - 2, ... 0 nodes.
      An loose upper limit would be n*(n-1)*(n-2)...*1 nodes, thus O(n*n!).
    
    - Aux space of O(n) for curList and recursion stack. O(n*n!) output space
"""