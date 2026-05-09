class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while True:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
            
        
"""
1, 2, 3, 4, 9, 10
target = 7

index1 = 1
index2 = 2

reutrn [index1, index2]

index1 < index2 and numbers[index1] + numbers[index2] == target

"""