class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, res = set(), set()

        for i in range(len(s) - 10 + 1):
            sub = s[i: i + 10]
            if sub in seen:
                res.add(sub)
            seen.add(sub)
        return res