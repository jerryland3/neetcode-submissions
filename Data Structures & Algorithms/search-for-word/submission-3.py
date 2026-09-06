class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        length = len(word)
        boardRows = len(board)
        boardCols = len(board[0])

        def helper(row: int, col: int, index: int):
            if (row < 0 or col < 0) or (row >= boardRows or col >= boardCols) or board[row][col] == "#" :
                return False
            if index >= length or board[row][col] != word[index]:
                return False
            if index == length - 1 and board[row][col] == word[index]:
                return True



            temp = board[row][col]
            board[row][col] = "#"
            if helper(row - 1, col, index + 1):
                return True
            if helper(row + 1, col, index + 1):
                return True
            if helper(row, col - 1, index + 1):
                return True
            if helper(row, col + 1, index + 1):
                return True
            board[row][col] = temp
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
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
    
    - can use a hash table to keep track of index we already visited O(n) space, O(1) lookup, O(n) construction
    - worst time should be O(n^2) since we may do the search at every chracter when the grid does not contain
      the 'word'.

recursion strategy for helper:
    base case:
        - if index == length - 1 and 
"""