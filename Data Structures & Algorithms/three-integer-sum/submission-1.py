class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        output = []
        
        while i < len(nums) - 2 and nums[i] <= 0:
            if i != 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if left != i + 1 and nums[left] == nums[left - 1]:
                    left += 1
                    continue
                elif right != len(nums) - 1 and nums[right] == nums[right + 1]:
                    right -= 1
                    continue
                
                if nums[left] + nums[right] == -nums[i]:
                    output.append([nums[left], nums[right], nums[i]])
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] > -nums[i]:
                    right -= 1
                else:
                    left += 1

            i += 1

        return output

"""
-4, -1, -1, 0, 1, 2, 3, 4, 5

-4, -2, 1, 1, 3

i, j, k
nums[i] + nums[j] + nums[k] = 0
-nums[i] = nums[j] + nums[k]

-4, -1, 5
-4, 0, 4
-4, 1, 3

-1, -1, 2
-1, 0, 1

nums[i] = -4
-1, 5
0, 4
1, 3



"""