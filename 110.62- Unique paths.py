class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        curRow = [1] * n
        prev = 1

        for i in range(m - 2, -1, -1):
            nextRow = [0] * n
            prev = 0
            for j in range(n - 1, -1, -1):
                nextRow[j] = curRow[j] + prev
                prev = nextRow[j]
            curRow = nextRow

        return prev