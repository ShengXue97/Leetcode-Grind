class Solution:
    def isValid(self, m, k):
        if len(m.values()) <= 1:
            return True

        return sum(m.values()) - max(m.values()) <= k

    def characterReplacement(self, s: str, k: int) -> int:
        # AABABBA
        # ACBDBD k = 1

        m = {}
        l = 0
        res = 0
        for r, c in enumerate(s):
            m[c] = 1 + m.get(c, 0)
            while not self.isValid(m, k):
                if m[s[l]] == 1:
                    del m[s[l]]
                else:
                    m[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res
