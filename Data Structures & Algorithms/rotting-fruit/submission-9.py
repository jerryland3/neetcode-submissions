from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        maxRow = len(grid)
        maxCol = len(grid[0])
        queue = deque()
        seen = set()
        fresh = 0
        time = -1

        for row in range(maxRow):
            for col in range(maxCol):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        while queue:
            time += 1
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for rowDiff, colDiff in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    newRow = row + rowDiff
                    newCol = col + colDiff
                    if (min(newRow, newCol) < 0 or
                        newRow >= maxRow or newCol >= maxCol or
                        (newRow, newCol) in seen or grid[newRow][newCol] != 1):
                        continue
                    seen.add((newRow, newCol))
                    queue.append((newRow, newCol))
                    fresh -= 1
        
        if fresh == 0:
            if time > -1:
                return time
            return 0
        return -1



"""
[0 0 0]
[0 0 1]
[0 0 2]

queue = [(0, 0)]
time = 4



- if cell does not contain any fresh fruit, then return 0
- if cell contain fresh fruit after search, then return -1
- if after serach, cell do not contain fresh fruit, then reuturn number of minutes

- count number of fresh fruit and put rotting fruit in a queue
- use BFS with the queue and increment minutes and count donw the number of fresh fruit during
  infection.

Complexity:
    - O(mxn) time since we are using BFS once
    - O(mxn) space for seen set of BFS
"""
        