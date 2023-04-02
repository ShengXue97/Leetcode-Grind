class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                    
                top = stack.pop()
                if not ((top == "(" and c == ")") or\
                        (top == "[" and c == "]") or\
                        (top == "{" and c == "}")):
                    return False
        
        return len(stack) == 0