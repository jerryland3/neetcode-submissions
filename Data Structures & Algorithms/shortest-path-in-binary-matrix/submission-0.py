from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        seen = set()
        queue = deque()
        queue.append((0, 0))
        seen.add((0, 0))
        length = 0

        if grid[0][0] == 1:
            return -1

        while queue:
            queueLength = len(queue)
            length += 1
            for index in range(queueLength):
                row, col = queue.popleft()
                if row == n - 1 and col == n - 1:
                    return length
                
                for rowDelta, colDelta in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    if (min(row + rowDelta, col + colDelta) < 0 or max(row + rowDelta, col + colDelta) >= n or
                        grid[row + rowDelta][col + colDelta] == 1 or (row + rowDelta, col + colDelta) in seen
                    ):
                        continue
                    queue.append((row + rowDelta, col + colDelta))
                    seen.add((row + rowDelta, col + colDelta))

        
        return -1


"""
[0 0 1]
[1 1 1]
[1 1 0]

use BFS to travers from (0, 0) to (n-1, n-1).
Return the number of visited cells along the way

Complexity:
    - O(mxn) time since we visit each cell at most once and each operation at the cell is O(1)
    - O(mxn) aux space due to the seen set, output space O(1) 
"""