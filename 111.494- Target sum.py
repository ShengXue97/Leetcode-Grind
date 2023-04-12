class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        m = defaultdict(int)
        m[0] = 1

        for num in nums:
            next_m = m.copy()
            for k, v in m.items():
                if v > 0:
                    next_m[k - num] += v
                    next_m[k + num] += v
                    next_m[k] -= v
            m = next_m
        
        return m[target]