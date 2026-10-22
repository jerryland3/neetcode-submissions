class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def DFS(row, col):
            if (min(row, col) < 0 or row >= len(board) or col >= len(board[0])):
                return
            if board[row][col] != "O":
                return
            
            board[row][col] = "Z"
            for rowDiff, colDiff in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                DFS(row + rowDiff, col + colDiff)
        
        lastCol = len(board[0]) - 1
        for row in range(len(board)):
            DFS(row, 0)
            DFS(row, lastCol)
        
        lastRow = len(board) - 1
        for col in range(len(board[0])):
            DFS(0, col)
            DFS(lastRow, col)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "Z":
                    board[row][col] = "O"
"""
x x x x x
x x x x x
o o x x x 
x o x x x 

x


capture regions (o's) that are surrounded
a region is surrounded if none of the o's in that region are on the edge of the board

Strategy:
    - use DFS on all edge cells
    - if the edge cell is an O, then we can call DFS and mark all connected o's with z
    - After this, all non marked o's are not connected to edge, this means they can be surronded
    - After DFS, we change all remaining o's to x and all marked o's remain o

Time Complexity:
    - O(mxn) time since we will visit each cell at most once in DFS
    - O(mxn) aux space due to DFS recursion. No output space since we return nothing
"""
        