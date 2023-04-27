class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)
        length = sum(matchsticks) // 4
        if sum(matchsticks) / 4 != length:
            return False
        res = False
        curArr = [0,0,0,0]

        def backtrack(i):
            nonlocal res
            if res:
                return
            if i == len(matchsticks):
                if curArr[0] == curArr[1] == curArr[2] == curArr[3]:
                    res = True
                return
            
            for j in range(4):
                if curArr[j] + matchsticks[i] <= length:
                    curArr[j] += matchsticks[i]
                    backtrack(i + 1)
                    curArr[j] -= matchsticks[i]
        
        backtrack(0)
        return res