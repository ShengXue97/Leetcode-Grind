class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        longest_length = 0
        def getLongestPalindrome(l, r):
            nonlocal res
            nonlocal longest_length

            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                length = r - l + 1
                if length > longest_length:
                    longest_length = length
                    res = s[l:r + 1]
                l -= 1
                r += 1

        for i in range(len(s)):
            # odd length palindrome
            getLongestPalindrome(i, i)

            # even length palindrome
            getLongestPalindrome(i, i + 1)
        
        return res
            