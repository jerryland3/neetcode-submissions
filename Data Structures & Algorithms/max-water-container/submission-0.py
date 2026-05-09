class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            if area > max_area:
                max_area = area

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

"""
1,7,2,5,4,7,3,6

water_height = min(heights[a], heights[b]) * abs(b-a)

1 1 2 1 1
"""