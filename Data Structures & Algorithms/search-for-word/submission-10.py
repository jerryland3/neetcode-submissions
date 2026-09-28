class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        maxRow = len(board)
        maxCol = len(board[0])
        wordLength = len(word)
        seen = set()

        def DFS(row: int, col: int, index: int) -> bool:
            if index >= wordLength:
                return True
            if (
                min(row, col) < 0 or
                row >= maxRow or col >= maxCol or
                board[row][col] != word[index] or
                (row, col) in seen
            ):
                return False
            
            seen.add((row, col))
            for rowDiff, colDiff in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if DFS(row + rowDiff, col + colDiff, index + 1):
                    return True
            seen.remove((row, col))

            return False
        
        for row in range(maxRow):
            for col in range(maxCol):
                if DFS(row, col, 0):
                    return True
        
        return False

"""
[a b c a t e]
[s a a t i s]
[a c a e x x]

catesit

loop through every grid, if the grid start with starting char of word, then do DFS from
that starting grid.

DFS rule, if the grid char is not the same as the next char in word, then return

time complexity of O(n * 4^m) where n is the number of grid and m is the length of word.
space complexity of O(m) for recursion stack.
"""