class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 3,2,1
        # 2,3,1
        # 2,1,3
        # 1,3,2
        # 1,2,3

        res = []
        stack = []

        def dfs(num_open, num_close):
            if num_open == n and num_close == n:
                res.append("".join(stack))
                return
            
            if num_open < n:
                stack.append("(")
                dfs(num_open + 1, num_close)
                stack.pop()
            if num_close < num_open:
                stack.append(")")
                dfs(num_open, num_close + 1)
                stack.pop()
        
        dfs(0, 0)
        return res