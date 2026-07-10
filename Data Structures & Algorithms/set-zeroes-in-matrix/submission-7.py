class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_col , first_row = 0, 0 
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row = 1
                    if j == 0:
                        first_col = 1
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] ==0:
                    matrix[i][j] = 0
        for i in range(0, len(matrix)):
            if first_row == 1:
                matrix[0] = [0]*len(matrix[0])
        for j in range(0, len(matrix)):
            if first_col == 1:
                matrix[j][0] = 0
        
        