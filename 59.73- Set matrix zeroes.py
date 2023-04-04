class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        isTopRowZero = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0:
                        isTopRowZero = True
                        continue

                    if j == 0:
                        matrix[0][0] = 0
                        continue

                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        
        if isTopRowZero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0