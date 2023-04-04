class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        rotten = deque()
        fresh = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
                    
        while fresh > 0 and rotten:
            res += 1
            for i in range(len(rotten)):
                orange = rotten.popleft()
                for direction in directions:
                    row = orange[0] + direction[0]
                    col = orange[1] + direction[1]
                    if row < 0 or row >= len(grid) or\
                        col < 0 or col >= len(grid[0]) or\
                        grid[row][col] != 1:
                        continue
            
                    grid[row][col] = 2
                    fresh -= 1
                    rotten.append((row, col))

        if fresh == 0:
            return res
        return -1
        