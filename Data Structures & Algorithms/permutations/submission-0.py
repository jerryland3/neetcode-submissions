class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        length = len(nums)

        def helper(index: int):
            if index >= length - 1:
                return [[nums[index]]]
            
            output = []
            perLists = helper(index + 1)
            for permList in perLists:
                for j in range(len(permList) + 1):
                    permListCopy = permList.copy()
                    permListCopy.insert(j, nums[index])
                    output.append(permListCopy)
            return output

        return helper(0)


"""
nums = [1,2,3]

[[1,2,3] [2,1,3] [2,3,1] [1,3,2][3,1,2][3,2,1]]  index = 0
                  [[2,3] [3,2]]                  index = 1
                      [[3]]                      index = 2

base case:
    - index >= len(nums), append nums[index] into curList

recursive case:
    - create all possible combinations with curList by appending current index
      element at all possible location of curList. done by appending from index = 0 to 
      index = len(curList)

complexity:
    - there are n! permutations. For each (n-1)! permutation we perform n insertion into a list,
      each insertion is O(n). Thus, time complexity = O((n-1)! * n^2)
    - we need O(n) recursion stack, thus O(n) aux space.
"""
        