class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n1, n2 = 0, len(numbers) - 1
        while True:
            val = numbers[n1] + numbers[n2]
            if val == target:
                return (n1 + 1, n2 + 1)
            elif val < target:
                n1 += 1
            else:
                n2 -= 1
            