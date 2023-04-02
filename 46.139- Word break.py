class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # applepenapple
        bools = [False] * (len(s) + 1)
        bools[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) >= len(bools):
                    continue
                if bools[i + len(word)] and\
                    s[i:i + len(word)] == word:
                    bools[i] = True
        
        return bools[0]