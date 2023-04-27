class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def isValid(start, end):
            sub = s[start:end + 1]
            if start > end:
                return False
            if sub[0] == "0" and len(sub) > 1:
                return False

            subInt = int(sub)
            return 0 <= subInt <= 255

        def backtrack(curStr, curIndex, numDots):
            if numDots == 3:
                if isValid(curIndex, len(s) - 1):
                    res.append(curStr)
                return
            if curIndex > len(s) - 1:
                return

            for i in range(1,4):
                if curIndex + i - 1 > len(s) - 1:
                    break
                if not isValid(curIndex, curIndex + i - 1):
                    continue

                backtrack(curStr[:curIndex + i + numDots] + "." + curStr[curIndex + i + numDots:], curIndex + i, numDots + 1)
            
        backtrack(s, 0, 0)
        return res