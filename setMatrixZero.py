

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        indexList = []
        
        # First pass: find all the zero positions
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    indexList.append((i, j))
        
        # Second pass: set rows and columns to zero
        for (i, j) in indexList:
            # Set all elements in the i-th row to zero
            for col in range(len(matrix[0])):
                matrix[i][col] = 0
            
            # Set all elements in the j-th column to zero
            for row in range(len(matrix)):
                matrix[row][j] = 0



                    