class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        maxRow = len(grid)
        maxCol = len(grid[0])
        seen = set()

        def DFS(row: int, col: int):
            if (min(row, col) < 0 or row >= maxRow or col >= maxCol or
               ((row, col) in seen or grid[row][col] == '0')
            ):
                return 0
            
            seen.add((row, col))
            for rowDelta, colDelta in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                DFS(row + rowDelta, col + colDelta)
            
            return 1

        for rowIndex in range(maxRow):
            for colIndex in range(maxCol):
                count += DFS(rowIndex, colIndex)

        return count 

"""
[
    [1 1 0 1]
    [1 1 0 0]
    [0 0 1 1]
]

strategy:
    - loop through every grid and use DFS. If we land on water or already seen land, then just return 0. If it is
      new land, use DFS and mark all connected land, then return 1 for count.
    
    - increment count after each DFS search.

Complexity:
    - time complexity of O(mxn) since we will visit each grid at most once and each visit is O(1)
    - Aux space is O(mxn) due to the set and recursion stack. Output space is O(1)
"""