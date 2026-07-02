class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # i will change late but j will change so col will change fast we are traversing vertically
        for i  in range(9):
            row_list= set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row_list:
                        return False
                    else:
                        row_list.add(board[i][j])

        for col in range(9):
            col_list = set()
            for row in range(9):
                if board[row][col]!=".":
                    if board[row][col] in col_list:
                        return False
                    else:
                        col_list.add(board[row][col])
        
        for square in range(9):
            # divide the suduko in three parts 
            # we have three parts.
            square_list = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3)*3+ i
                    col = (square%3)*3 + j
                    if board[row][col]!=".":
                        if board[row][col] in square_list:
                            return False
                        else:
                            square_list.add(board[row][col])
        return True                        
