class Solution:
    def solve(self, board: List[List[str]]) -> None:
        maxRow = len(board)
        maxCol = len(board[0])

        def DFS(row: int, col: int):
            if (min(row, col) < 0 or
                row >= maxRow or col >= maxCol or
                board[row][col] == "X" or 
                board[row][col] == "Z"
            ):
                return
            
            board[row][col] = "Z"
            for rowDiff, colDiff in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                DFS(row + rowDiff, col + colDiff)

        for col in range(maxCol):
            DFS(0, col)
            DFS(maxRow - 1, col)
        
        for row in range(maxRow):
            DFS(row, 0)
            DFS(row, maxCol - 1)
        
        for row in range(maxRow):
            for col in range(maxCol):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "Z":
                    board[row][col] = "O"

"""
[o]
[o]

[x x x x x]
[x o o o x]
[x x x x x]
[x o o x x]
[x o o o o]

[x x x x x]
[x o o o x]
[x x x x x]
[x z z x x]
[x z z z z]

[x x x x x]
[x x x x x]
[x x x x x]
[x o o x x]
[x o o o o]

Strategy:
    1. start from all border "o" cells and mark each "o" connected through border cell as "z"
    2. loop through all grid and mark "o" as "x" and all "z" as "o"
    3. use DFS for traversal
    - use DFS for traversal

Complexity:
    - O(mxn) time since we will visit each cell at most twice, once for DFS and another when we loop through the board.
    - O(mxn) aux space due to recursion and O(mxn) output space
"""
        