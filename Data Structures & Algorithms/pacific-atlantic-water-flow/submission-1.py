class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        alantic = set()
        output = []
        maxRow = len(heights)
        maxCol = len(heights[0])

        def DFS(row: int, col: int, visited: set):
            if (row, col) in visited:
                return
            
            visited.add((row, col))
            for rowDiff, colDiff in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                newRow = row + rowDiff
                newCol = col + colDiff
                if (
                    min(newRow, newCol) < 0 or
                    newRow >= maxRow or newCol >= maxCol or
                    heights[newRow][newCol] < heights[row][col]
                ):
                    continue
                DFS(newRow, newCol, visited)

        # loop through all boarders
        for col in range(maxCol):
            DFS(0, col, pacific)
            DFS(maxRow - 1, col, alantic)
        for row in range(maxRow):
            DFS(row, 0, pacific)
            DFS(row, maxCol - 1, alantic)
            
        # final check and append to output
        for row, col in pacific:
            if (row, col) in alantic:
                output.append([row, col])

        return output 
        
"""
pppppppppppp
p[4 2 7 3 4]a
p[7 4 6 4 7]a
p[6 3 5 3 6]a
aaaaaaaaaaaaa

if we can traverse to first row and first column -> we can flow to pacific
if we can traverse to last row and last column -> we can flow to alantic

Can brute force with DFS through every grid, however this is O((mxn)^2)

Strategy:
    - start from the border cells of pacific (first row, first col) and use DFS to traverse. If a visiting cell can be reached, we add it to the
      pacific set
    - run DFS again starting from the alantic border (last row, last col), if a visiting cell can be reached, add it to the alantic set
    - find all common cells in both pacific and alantic set and return them
    - traversal rule: not in set (pacific or alantic) or nextHeight >= currentHeight

complexity:
    - O(mxn) time since we mark the cells in the set, so we will not see the same node twice. Two traversal total.
    - O(mxn) space for the pacific and alantic set and recursion stack. O(mxn) output space for the returned list
"""