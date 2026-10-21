class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        def DFS(row: int, col: int, ocean: set):
            if (row, col) in ocean:
                return
            
            ocean.add((row, col))
            for rowDiff, colDiff in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                newRow = row + rowDiff
                newCol = col + colDiff
                if (min(newRow, newCol) < 0 or newRow >= len(heights) or newCol >= len(heights[0])):
                    continue
                if heights[newRow][newCol] >= heights[row][col]:
                    DFS(newRow, newCol, ocean)

        for row in range(len(heights)):
            DFS(row, 0, pacific)
        for col in range(len(heights[0])):
            DFS(0, col, pacific)
        
        for row in range(len(heights)):
            DFS(row, len(heights[0]) - 1, atlantic)
        for col in range(len(heights[0])):
            DFS(len(heights) - 1, col, atlantic)

        output = []
        for row, col in pacific:
            if (row, col) in atlantic:
                output.append([row, col])
        
        return output
        
"""
Given:
    - 2D matrix representing height of each cell at coordinate (r, c)
    - Water flow in four direction from higher cell to equal or lower cells
    - Find all cell that water can flow to both pacific and atlantic ocean
   p p p p p 
 p 4 2 7 3 4 a
 p 7 4 6 4 7 a
 p 6 3 5 3 6 a
   a a a a a 

[(0 0) (1 0) (0 1) (1 1) ()]

 Strategy:
    - Start from the end positions (pacific/atlantic) and mark each cell that can be visited from pacific ocean
      and then mark every cell that can be visited from atlantic ocean
    - at the end, find all cells that are marked by both pacific and atlantic
    - Marking can be done with a set, pacific set for all cells that can be traversed from pacific ocean
      atlantic set for atlantic ocean cells
    - Traversal is DFS

Traversal Rule:
    - from end points (top row and left col or bottom row and right col), only can traverse to cell with higher
      or equal numberic value
    - mark as we traverse

Complexity:
    - O(mxn) time since we will visit each cell at most twice
    - O(mxn) space for atlantic set, pacific set and DFS recursion. O(mxn) output space in worst case
"""