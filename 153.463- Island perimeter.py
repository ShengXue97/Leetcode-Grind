class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()
        def dfs(i, j):
            nonlocal res
            # Returns boolean whether current cell is water or not
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return True
            if (i, j) in visited:
                return False
            visited.add((i, j))
            
            if dfs(i - 1, j):
                res += 1
            if dfs(i + 1, j):
                res += 1
            if dfs(i, j - 1):
                res += 1
            if dfs(i, j + 1):
                res += 1
            return False
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    break
        
        return res