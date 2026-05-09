class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = 9
        column = 9
        number_of_blocks = 9
        item_per_block = 9
        seen = set()

        for row in board:
            for item in row:
                if item == ".":
                    continue
                elif item in seen:
                    return False
                seen.add(item)
            seen.clear()

        for column_index in range(9):
            for row_index in range(9):
                item = board[row_index][column_index] 
                if item == ".":
                    continue
                elif item in seen:
                    return False
                seen.add(item)
            seen.clear()

        for block in range(9):
            for i in range(3):
                for j in range(3):
                    row_index = (block // 3) * 3 + i
                    column_index = (block % 3) * 3 + j
                    item = board[row_index][column_index]
                    if item == ".":
                        continue
                    elif item in seen:
                        return False
                    seen.add(item)
            seen.clear()

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
        