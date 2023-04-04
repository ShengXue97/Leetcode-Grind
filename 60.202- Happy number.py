class Solution:
    def isHappy(self, n: int) -> bool:
        def sumSquareDigits(num):
            count = 0
            while num > 0:
                count += pow((num % 10), 2)
                num = num // 10
            return count
        
        slow, fast = n, sumSquareDigits(n)
        while slow != fast:
            slow = sumSquareDigits(slow)
            fast = sumSquareDigits(fast)
            fast = sumSquareDigits(fast)
        
        if slow == 1:
            return True
        return False