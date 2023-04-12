class Solution:
    def countSubstrings(self, s: str) -> int:
        def countPalindromes(i, j):
            res = 0
            while i >= 0 and j <= len(s) - 1 and s[i] == s[j]:
                res += 1
                i -= 1
                j += 1
            return res
        
        res = 0
        for i in range(len(s)):
            # odd length palindromes
            res += countPalindromes(i, i)
            # even length palindromes
            res += countPalindromes(i, i + 1)

        return res
