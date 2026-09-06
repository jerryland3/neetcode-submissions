class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        length = len(word)
        boardRows = len(board)
        boardCols = len(board[0])

        def helper(row: int, col: int, index: int):
            if(
                (row < 0 or col < 0) or
                (row >= boardRows or col >= boardCols) or 
                board[row][col] != word[index]
            ):
                return False
            if index == length - 1 and board[row][col] == word[index]:
                return True

            temp = board[row][col]
            board[row][col] = "#"
            found = False
            for deltaRow, deltaCol in [(1,0), (0, 1), (-1, 0), (0, -1)]:
                if helper(row + deltaRow, col + deltaCol, index + 1):
                    found = True
                    break
            board[row][col] = temp
            return found

        for row in range(boardRows):
            for col in range(boardCols):
                if helper(row, col, 0):
                    return True
        return False
        


"""
strategy:
    - loop through every element of the grid and stop on element that matches the first char or 'word'
    - once found first character, search left, up, right, down elements to see if it matches second char
        - need to keep track path so we do not reuse previous char
        - if we found last char by doing this, then return true
        - if we do not find all char, then continue looping through grid
    
    - with recursion solution, can use '#' to keep track where we visited so far and reset when returning
      when completed recursive calls

Complexity:
    - each recursive calls visit at most 4 path, thus O(4^n) time for recursive calls, where n is length 
      of 'word'. We will call recursive function at most m times when looping through grid, where m is 
      the number of cells in grid. Thus, time complexity of O(m*4^n).
    - O(n) aux space since the recursion stack is at most n deep.
"""