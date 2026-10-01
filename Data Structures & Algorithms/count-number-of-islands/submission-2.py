class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        maxRow = len(grid)
        maxCol = len(grid[0])
        seen = set()
        count = 0

        def DFS(row: int, col: int):
            if (min(row, col) < 0 or row >= maxRow or col >= maxCol):
                return
            if (row, col) in seen or grid[row][col] == "0":
                return
            
            seen.add((row, col))
            for rowDiff, colDiff in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                DFS(row + rowDiff, col + colDiff)
        
        for row in range(maxRow):
            for col in range(maxCol):
                if (row, col) not in seen and grid[row][col] == "1":
                    DFS(row, col)
                    count += 1
        
        return count
            

"""

"""