class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            hashTable = {}
            for index, num in enumerate(nums):
                complment = target - num
                if complment in hashTable:
                    return [hashTable[complment], index]
                hashTable[num] = index
        