class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        maxRow = len(grid)
        maxCol = len(grid[0])
        seen = set()

        def DFS(row: int, col: int):
            if(
                min(row, col) < 0 or row >= maxRow or col >= maxCol or
                (row, col) in seen or grid[row][col] == 0
            ):
                return 0
            
            seen.add((row, col))
            totalArea = 1
            for rowDelta, colDelta in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                totalArea += DFS(row + rowDelta, col + colDelta)
            
            return totalArea
            
        for rowIndex in range(maxRow):
            for colIndex in range(maxCol):
                area = DFS(rowIndex, colIndex)
                maxArea = max(maxArea, area)
        
        return maxArea

"""
Strategy:
    - use DFS to traverse each grid elements. During DFS, mark island in seen so we do not traverse it again.
    - Once a island is marked, increment area.
    - Outer loop update max area and reset area to 0 at the beginning of each loop

Complexity:
    - O(mxn) time since we visit each grid element at most once. Each visit is O(1) since we just update area and add
      island to seen
    - O(mxn) aux space due to recursion stack and seen set. Output space of O(1)

    [0 0 0 0 0]
    [0 0 1 1 1]
    [1 1 1 0 0]
"""
        