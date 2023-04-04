class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def isValid(row, col):
            if row < 0 or row >= len(matrix) or\
                col < 0 or col >= len(matrix[0]) or\
                matrix[row][col] == 999:
                return False
            return True

        curDir = "r"
        i, j = 0, -1
        res = []

        while len(res) < len(matrix) * len(matrix[0]):
            if curDir == "r":
                if isValid(i, j + 1):
                    j += 1
                    res.append(matrix[i][j])
                else:
                    curDir = "d"
            elif curDir == "d":
                if isValid(i + 1, j):
                    i += 1
                    res.append(matrix[i][j])
                else:
                    curDir = "l"
            elif curDir == "l":
                if isValid(i, j - 1):
                    j -= 1
                    res.append(matrix[i][j])
                else:
                    curDir = "u"
            elif curDir == "u":
                if isValid(i - 1, j):
                    i -= 1
                    res.append(matrix[i][j])
                else:
                    curDir = "r"
            else:
                continue
            matrix[i][j] = 999
        
        return res
        



