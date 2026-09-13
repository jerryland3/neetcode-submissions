class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startColor = image[sr][sc]
        maxRow = len(image)
        maxCol = len(image[0])
        visited = set()

        def DFS(row: int, col: int):
            if (
                min(row, col) < 0 or 
                (row >= maxRow or col >= maxCol) or 
                image[row][col] != startColor or 
                (row, col) in visited
            ):
                return

            image[row][col] = color
            visited.add((row, col))
            for rowDiff, colDiff in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                DFS(row + rowDiff, col + colDiff)
            
        DFS(sr, sc)
        return image


"""
given:
    - mxn grid of integers called image
    - sr and sc which represent starting row and column respectivly
    - color, is an integer representing a color
    - perform flood fill starting from image[sr][sc]

Return:
    - modified image with flood filled color

grid = [
        [1, 1, 1],
        [1, 2, 0],
        [1, 0, 1],
       ]

sr = 1, sc = 1
color = 2

strategy:
    - start at the sr and sc, store the current color in a temp then change its value to color
    - visit up, down, left, and right recursivly, need to check if its color is equal to temp, if so update its
      value to color, if not, then just return

complexity:
    - worst case all grid have the same value, then we need to visit each pixel. There are at most (m x n) pixels.
      At each pixel, we have 4 directions to visit. The cost of visiting each node is O(1) since we are either updating
      or not updating its value. Thus, time complexity is O(4^(mxn)).
    
    - aux space of O(mxn) for the recursion stack. The output space is O(mxn) since we are returning the same grid.
"""