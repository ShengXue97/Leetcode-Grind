class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        curDp = triangle[len(triangle) - 1]
        for i in range(len(triangle) - 2, -1, -1):
            newDp = []
            for j in range(len(triangle[i])):
                newDp.append(triangle[i][j] + min(curDp[j], curDp[j + 1]))
            curDp = newDp

        return curDp[0]