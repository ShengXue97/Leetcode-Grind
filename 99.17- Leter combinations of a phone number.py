class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        if not digits:
            return []
            
        res = []
        def recurse(curArr, index):
            if index >= len(digits):
                res.append("".join(curArr))
                return
            
            for c in m[digits[index]]:
                curArr.append(c)
                recurse(curArr, index + 1)
                curArr.pop()
        
        recurse([], 0)
        return res