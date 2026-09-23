from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        seen = set()
        maxRow = len(grid)
        maxCol = len(grid[0])
        fresh = 0
        time = -1

        for row in range(maxRow):
            for col in range(maxCol):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        
        while queue:
            time += 1
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for rowDiff, colDiff in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    newRow = row + rowDiff
                    newCol = col + colDiff

                    if (
                        min(newRow, newCol) < 0 or
                        newRow >= maxRow or 
                        newCol >= maxCol or
                        grid[newRow][newCol] != 1 or
                        (newRow, newCol) in seen
                    ):
                        continue

                    queue.append((newRow, newCol))
                    seen.add((newRow, newCol))
                    fresh -= 1
        
        if fresh != 0:
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
        