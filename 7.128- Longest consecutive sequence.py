class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        s = set()
        for n in nums:
            s.add(n)
        
        for n in s:
            if (n -1) in s:
                continue
            
            # Start of a new sequence
            result = max(1, result)
            c = n + 1
            length = 1
            while c in s:
                length += 1
                result = max(length, result)
                c += 1
        
        return result