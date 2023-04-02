class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(i, j, prev, visited):
            if i < 0 or j < 0 or i >= len(heights) or j >= len(heights[0]):
                return
            if heights[i][j] < prev:
                return
            elif (i, j) in visited:
                return

            visited.add((i, j))
            prev = heights[i][j]

            dfs(i - 1, j, prev, visited)
            dfs(i + 1, j, prev, visited)
            dfs(i, j - 1, prev, visited)
            dfs(i, j + 1, prev, visited)
        
        res = []
        p_visited = set()
        a_visited = set()

        for i in range(len(heights)):
            dfs(i, 0, float('-inf'), p_visited)
            dfs(i, len(heights[0]) - 1, float('-inf'), a_visited)

        for j in range(len(heights[0])):
            dfs(0, j, float('-inf'), p_visited)
            dfs(len(heights) - 1, j, float('-inf'), a_visited)

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in p_visited and (i, j) in a_visited:
                    res.append((i, j))
        
        return res