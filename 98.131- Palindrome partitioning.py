class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def recurse(curArr, index):
            if index >= len(s):
                res.append(curArr[:])
            
            for i in range(index + 1, len(s) + 1):
                sub = s[index:i]
                if isPalindrome(sub):
                    curArr.append(sub)
                    recurse(curArr, i)
                    curArr.pop()
        
        recurse([], 0)
        return res