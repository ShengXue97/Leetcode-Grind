class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        res = float('inf')
        N = len(grid[0])

        firstRowPrefix, secondRowPrefix = grid[0][:], grid[1][:]
        for i in range(1, N):
            firstRowPrefix[i] += firstRowPrefix[i - 1]
            secondRowPrefix[i] += secondRowPrefix[i - 1]

        for i in range(N):
            firstRowSum = firstRowPrefix[-1] - firstRowPrefix[i]
            secondRowSum = secondRowPrefix[i - 1] if i > 0 else 0
            secondRobotPoints = max(firstRowSum, secondRowSum)
            res = min(res, secondRobotPoints)
        
        return res

