class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        visited = set()
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            if grid[i][j] == 0 or (i, j) in visited:
                return
            visited.add((i, j))
            for di, dj in dirs:
                dfs(i + di, j + dj)
        
        def bfs():
            q = deque()
            for i, j in visited:
                q.append((i, j, 0))
            
            while q:
                i, j, moves = q.popleft()
                for di, dj in dirs:
                    curi, curj = i + di, j + dj
                    if curi < 0 or curi >= len(grid) or curj < 0 or curj >= len(grid[0]):
                        continue
                    if (curi, curj) in visited:
                        continue
                    if grid[curi][curj] == 1:
                        return moves
                    visited.add((curi, curj))
                    q.append((curi, curj, moves + 1))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i,j)
                    return bfs()