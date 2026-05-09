class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for row_index in range(9):
            for col_index in range(9):
                square_value = board[row_index][col_index]
                if square_value == ".":
                    continue
                elif (square_value in rows[row_index] or
                      square_value in cols[col_index] or
                      square_value in squares[(row_index // 3, col_index // 3)]):
                    return False

                rows[row_index].add(square_value)
                cols[col_index].add(square_value)
                squares[(row_index // 3, col_index // 3)].add(square_value)
        
        return True

"""
iterate through all rows
    iterate through all item in a row
        check if item is in hashset, if its in hash set return false
        else add to hashset

iterate through all columns
    ...

iterate through all 3x3 blocks
    iterate through every item in block
        ...

for row in range(3):
    for column in range(3):
        number = ...

for row in range(3):
    for column in range(4, 7)
        ...

for row in range(3):
    for column in range(7, 10):
        ...

for row in range(4, 7)



let n be the number of rows
time complexity O(n^2)
space complexity O(n)
"""
        