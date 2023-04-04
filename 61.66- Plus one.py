class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        hasCarryOver = True
        i = len(digits) - 1

        while hasCarryOver and i >= 0:
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                hasCarryOver = False
            i -= 1
        
        if hasCarryOver:
            digits.insert(0, 1)
        
        return digits