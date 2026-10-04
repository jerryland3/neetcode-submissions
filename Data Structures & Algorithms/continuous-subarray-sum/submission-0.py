class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        inputLength = len(nums)
        for i in range(inputLength - 1):
            curSum = nums[i]
            for j in range(i + 1, inputLength):
                curSum += nums[j]
                if curSum % k == 0:
                    return True
        
        return False


"""
23 2 4 6 7

i = 3
j = 4

curSum = 2

   0   1  2  3  4
  [23  2  4  6  7]
[0 23 25 29 35 42]

k = 6

sum[i:j] = prefix[j] - prefix[i-1]
sum[i:j] = n*k

"""
        