from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        seen = set()
        maxRow = len(grid)
        maxCol = len(grid[0])
        gridCopy = grid[:]

        def freshCount(board: list[list[int]]):
            fresh = 0
            for row in range(maxRow):
                for col in range(maxCol):
                    if board[row][col] == 1:
                        fresh += 1
            return fresh

        def initalSearch():
            for row in range(maxRow):
                for col in range(maxCol):
                    if grid[row][col] == 2:
                        queue.append((row, col))
        
        def BFS():
            length = 0
            while queue:
                lengthQueue = len(queue)
                length += 1
                for _ in range(lengthQueue):
                    row, col = queue.popleft()
                    for rowDiff, colDiff in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        newRow = row + rowDiff
                        newCol = col + colDiff
                        if (min(newRow, newCol) < 0 or newRow >= maxRow or newCol >= maxCol or
                            gridCopy[newRow][newCol] == 0 or gridCopy[newRow][newCol] == 2 or (newRow, newCol) in seen):
                            continue
                        seen.add((newRow, newCol))
                        queue.append((newRow, newCol))
                        gridCopy[newRow][newCol] = 2
            return length - 1
        
        if freshCount(grid) == 0:
            return 0
        
        initalSearch()
        time = BFS()

        if freshCount(gridCopy) > 0:
            return -1
        
        return time
                        



"""
Strategy:
    - inital search of all grid to find rotten orange and place it in BFS queue
    - use BFS search and return the length of the search
    - finial search of all grid to see if there are anymore fresh organge
        if there are, return -1, else return length from BFS

Complexity:
    - O(mxn) time since inital search, final search, and BFS are O(mxn)
    - O(mxn) aux space for BFS queue, and O(1) for output space 

5
[(0,1)]
"""
        