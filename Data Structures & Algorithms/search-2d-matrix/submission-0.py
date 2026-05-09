class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = (len(matrix) * len(matrix[0])) - 1

        while left <= right:
            mid = left + ((right - left) // 2)
            mid_row = mid // len(matrix[0])
            mid_col = mid % len(matrix[0])

            if target < matrix[mid_row][mid_col]:
                right = mid - 1
            elif target > matrix[mid_row][mid_col]:
                left = mid + 1
            else:
                return True
        
        return False


"""
[[1 2 4 8], 
 [10 11 12 13], 
 [14 20 30 40]]
 target = 15

left = 9
right = 8

mid = 9
mid_row = 2
mid_col = 1
value = 20




"""