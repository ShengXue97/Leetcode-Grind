class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            isBroken = False
            if a > 0:
                stack.append(a)
                continue
            while stack:
                if stack[-1] == abs(a):
                    isBroken = True
                    stack.pop()
                    break
                if stack[-1] < 0:
                   break 
                if stack[-1] > abs(a):
                    isBroken = True
                    break
            
                stack.pop()
            
            if not isBroken:
                stack.append(a)
        return stack