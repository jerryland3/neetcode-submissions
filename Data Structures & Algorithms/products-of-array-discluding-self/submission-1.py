class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array_1 = []
        number_1 = 1
        for element in nums:
            number_1 *= element
            array_1.append(number_1)

        array_2 = []
        number_2 = 1
        for element in reversed(nums):
            number_2 *= element
            array_2.append(number_2)
        
        array_2 = array_2[::-1]
        
        res = []
        for index in range(len(nums)):
            if index == 0:
                res.append(array_2[index + 1])
                continue
            elif index == len(nums) - 1:
                res.append(array_1[index - 1])
                break
            
            product = array_1[index - 1] * array_2[index + 1]
            res.append(product)
        
        return res


"""
[1, 2, 3, 4]
---------------------
[1, 2, 6, 24]
[24, 24, 12, 4]

[24, 1*12, 2*4,  6]

space complexity O(n)
time complexity O(n)
"""