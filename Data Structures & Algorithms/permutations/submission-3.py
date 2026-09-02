class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        curList = []
        length = len(nums)
        seen = [False for _ in nums]

        def helper(index: int):
            if index >= length:
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
                                []
           1      TFF            2                       3                                   0
        2    3    TFT            1   3                   1   2                                1
      3 TTF     2   TTT         3       1                2      1                              2

so we have 3*2*1 choices as we go down the tree, thus we have at most 3! = 6 permutations. generalize to n! for n elements.

depth is at most n.
need to keep track what values have been taken at each depth so we do not pick that value for repeat. Can use boolean list here.


base case:
    - stop once index >= n, copy element from curList and return

recursive case:
    - loop through all index of nums
    - check if bool list index element is true, if so continue
    - if bool list index element is false, then append element, update bool list, recurse, pop, update bool list

complexity:
    - there is at most n! permutations, each permutation takes at most n append. Thus time complexity is 
      O(n*n!).
    
    - aux space is at most O(n) since there is at most n recursion layers. Output space is n! permutations and
      each permuatations is at most n elements, thus output space is at most O(n*n!)

"""