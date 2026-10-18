class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        seen = set()

        def DFS(row: int, col: int) -> int:
            if min(row, col) < 0 or row >= len(grid) or col >= len(grid[0]):
                return 0
            if (row, col) in seen or grid[row][col] == 0:
                return 0
            
            seen.add((row, col))
            area = 0
            for rowDiff, colDiff in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                area += DFS(row + rowDiff, col + colDiff)
            
            return area + 1
            
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                maxArea = max(maxArea, DFS(row, col))
        
        return maxArea


"""
  [0 1 1 1 1]
  [1 0 1 0 1]
  [0 1 1 1 1]
  [0 0 0 0 0]

Strategy:
    - loop through every cell
    - if the cell have not been seen and it is 1, then use DFS to find its area
    - DFS mark every cell it sees in seen, and return the area of the current island
    - update max area after DFS returns

Complexity:
    - O(mxn), we need to visit each cell only once. After each visit, we call DFS, but if the cell has already
      been seen with DFS, then we do not go through it again. Thus, time complexity is O(mxn)
    - Space complexity of O(mxn) for worst case with seen set. O(1) output space
"""
        