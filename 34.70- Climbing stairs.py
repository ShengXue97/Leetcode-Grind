class Solution:
    def climbStairs(self, n: int) -> int:
        # n[0] = 1
        # n[1] = 1
        # n[2] = 2
        # n[3] = 3

        if n < 2:
            return 1
        
        n1, n2 = 1, 1
        for i in range(n - 1):
            tmp = n2
            n2 = n1 + n2
            n1 = tmp
        
        return n2