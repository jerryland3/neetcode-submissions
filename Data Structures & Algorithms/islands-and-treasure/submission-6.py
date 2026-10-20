from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        seen = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    queue.append((row, col))
                    seen.add((row, col))
        
        distance = 0
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                grid[row][col] = distance
                for rowDiff, colDiff in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    newRow = row + rowDiff
                    newCol = col + colDiff
                    if (min(newRow, newCol) < 0 or newRow >= len(grid) or newCol >= len(grid[0])):
                        continue
                    if grid[newRow][newCol] != 2147483647 or (newRow, newCol) in seen:
                        continue
                    
                    queue.append((newRow, newCol))
                    seen.add((newRow, newCol))
            distance += 1

"""
seen = ((0, 0) (1, 0) (1 1))
queue = [(1 1)]
row = 1 col = 0
dis = 2

3 x 0 1
2 2 1 x
1 x 2 x
0 x 3 4


-1 (x): Water cell
0: treasure chest
INF (1): land cell

fill each land cell with its distance to its nearest treasure chest. Keep it at INF if it cannot reach a treasure chest.
modify grid in place

3 x 0 1
2 2 1 x
1 x 2 x
0 x 3 4

0 -1
1 2

Strategy:
    - start BFS at each treasure chest. Update each land visited with the distance so far.
    - Once a land is visited in BFS, store it in seen so it will not be traversed again

Data Structure:
    - a set for storing cells already seen

Complexity:
    - O(mxn) time since we will visit each cell once
    - O(mxn) space for storing already visited cells. O(1) output space.
"""
