class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        area = 0
        maxRow = len(grid)
        maxCol = len(grid[0])
        seen = set()

        def DFS(row: int, col: int):
            if(
                min(row, col) < 0 or row >= maxRow or col >= maxCol or
                (row, col) in seen or grid[row][col] == 0
            ):
                return
            
            nonlocal area
            seen.add((row, col))
            area += 1
            for rowDelta, colDelta in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                DFS(row + rowDelta, col + colDelta)
        
        for rowIndex in range(maxRow):
            for colIndex in range(maxCol):
                area = 0
                DFS(rowIndex, colIndex)
                maxArea = max(maxArea, area)
        
        return maxArea
        