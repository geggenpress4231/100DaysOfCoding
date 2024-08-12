

# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         indexList = []
        
#         # First pass: find all the zero positions
#         for i in range(len(matrix)):
#             for j in range(len(matrix[i])):
#                 if matrix[i][j] == 0:
#                     indexList.append((i, j))
        
#         # Second pass: set rows and columns to zero
#         for (i, j) in indexList:
#             # Set all elements in the i-th row to zero
#             for col in range(len(matrix[0])):
#                 matrix[i][col] = 0
            
#             # Set all elements in the j-th column to zero
#             for row in range(len(matrix)):
#                 matrix[row][j] = 0



                    
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return

        rows = len(matrix)
        cols = len(matrix[0])

        # Determine if the first row or first column needs to be zeroed
        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

        # Use first row and column as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero out cells based on markers in the first row and column
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero out the first row if needed
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Zero out the first column if needed
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0
