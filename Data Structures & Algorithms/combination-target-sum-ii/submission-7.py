class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        curList = []
        inputLength = len(candidates)
        sortedInput = sorted(candidates)

        def helper(index: int, curSum: int):
            if curSum == target:
                output.append(curList[:])
                return
            if index >= inputLength or curSum > target:
                return
            
            curList.append(sortedInput[index])
            helper(index + 1, curSum + sortedInput[index])
            curList.pop()

            while index < inputLength - 1 and sortedInput[index] == sortedInput[index + 1]:
                index += 1
            helper(index + 1, curSum)
        
        helper(0, 0)
        return output


"""
index = 2
curSum = 1

curList = [1]
output = [[1 1]]

sort input first
[1 1 2]
target = 2

                        
                1            []
            1      []      1    []
                2     []       2  []

The key is determine how to skip the duplicate
criteria for skip:
    current index number is same as previous index number, then skip
    But only do this is we are not under parent node of the same number

base case:
    curSum > target or index >= len(input) => return
    if curSum == target, append to output, then return

recursive case:
    append input[index] to curList
    recurse with index + 1 and updated curSum
    pop from curList

    check if current index value is same as previous, if so, skip
    recurse with index + 1 and curSum

"""