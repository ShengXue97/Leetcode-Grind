class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        isSub = True
        res = 0

        def dfs(i, j):
            nonlocal isSub
            if i < 0 or i >= len(grid2) or j < 0 or j >= len(grid2[0]):
                return
            if grid2[i][j] == 0:
                return
            grid2[i][j] = 0
            if grid1[i][j] == 0:
                isSub = False
            
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
        
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    isSub = True
                    dfs(i, j)
                    if isSub:
                        res += 1
        
        return res
            
