class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gaps = defaultdict(int)
        gaps[0] = 0

        for r in range(len(wall)):
            cur = 0
            for c in range(len(wall[r]) - 1):
                cur += wall[r][c]
                gaps[cur] += 1
        
        return len(wall) - max(gaps.values())