class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l , r = 0, 0
        sset = set()
        res = 0
        while r < len(s):
            if s[r] not in sset:
                sset.add(s[r])
                res = max(res, r- l +1)
            else:
                while s[l] != s[r]:
                    sset.remove(s[l])
                    l += 1
                l += 1
                res = max(res, r- l +1)
            
            r += 1
        return res