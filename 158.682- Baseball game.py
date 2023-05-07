class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                s1, s2 = stack[-1], stack[-2]
                stack.append(s1 + s2)
            elif op == "D":
                s = stack[-1]
                stack.append(s * 2)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)