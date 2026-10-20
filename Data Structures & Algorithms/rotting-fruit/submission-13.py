from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshCount = 0
        seen = set()
        queue = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col))
                    seen.add((row, col))
                elif grid[row][col] == 1:
                    freshCount += 1
        
        minute = 0
        while queue and freshCount > 0:
            minute += 1
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for rowDiff, colDiff in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    newRow = row + rowDiff
                    newCol = col + colDiff
                    if min(newRow, newCol) < 0 or newRow >= len(grid) or newCol >= len(grid[0]):
                        continue
                    if (newRow, newCol) in seen or grid[newRow][newCol] != 1:
                        continue
                    seen.add((newRow, newCol))
                    queue.append((newRow, newCol))
                    freshCount -= 1
        
        if freshCount != 0:
            return -1
        return minute
            


"""
2 2 0
0 2 2
0 2 2

seen = [(2, 2) (1, 2) (2, 1) (1, 1) (0, 1) (0, 0)]
queue = []
fresh = 0
min = 4


horizontal or vertical can be infected every min
return min elapse minutes until on fresh fruit. If impossible to infect all, then return -1

Strategy:
    - use BFS where the starting queue contain all the infected fruits coordiante
    - each traversal we will infect negiboring banana
    - use a seen set so we do not revisit already visited coordinates
    - determine how many fresh fruit there are when initalizing the queue
    - subtract fresh fruit count as we infect so we can check if that count becomes zero

Edge Case:
    - timer need to start at -1 because BFS will increment timer on the final infected fruits even when there
      are not other fruit to infect
    - However, if there are no fresh fruit (just empty cells or cells with only rotten fruit). Then we need to
      return 0 since there are no fresh fruit to infect

Complexity
    - O(mxn) time since we visit each cell at most once
    - O(mxn) for queue and seen set. O(1) output space
"""
        