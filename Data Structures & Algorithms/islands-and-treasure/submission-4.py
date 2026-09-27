from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        maxRow = len(grid)
        maxCol = len(grid[0])

        for row in range(maxRow):
            for col in range(maxCol):
                if grid[row][col] == 0:
                    queue.append((row, col))

        length = 0
        while queue:
            length += 1
            queueLength = len(queue)
            for _ in range(queueLength):
                row, col = queue.popleft()
                for rowDiff, colDiff in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    newRow = row + rowDiff
                    newCol = col + colDiff
                    if(
                        min(newRow, newCol) < 0 or
                        newRow >= maxRow or newCol >= maxCol or
                        grid[newRow][newCol] != 2147483647
                    ):
                        continue
                    
                    grid[newRow][newCol] = length
                    queue.append((newRow, newCol))

        


"""
[
 [x,-1,0, 1]
 [2, 2,1,-1]
 [1,-1,2,-1]
 [0,-1,x, x]
]

[0 x 0]
[x x x]

[0   1 2]
[-1 -1 1]
[x  -1 0]

queue = []
length = 3
(0, 2)


-1: cannot be traversed
0: Treasure
X: A land that can be traversed. (2147483647 representation)

[
[0   x x]
[-1 -1 x]
[x  -1 0]
]

[
[0   1 2]
[-1 -1 1]
[x  -1 0]
]

[]
(2,2)
update x with current length and put x in seen and queue

as we go through the grid, update x with distance to nearest 0.

complexity:
    - O(mxn) time since we visit each cell once.
    - aux space is O(1) since we are just modifying in place. Output space is O(mxn). 

"""
