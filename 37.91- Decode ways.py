class Solution:
    def numDecodings(self, s: str) -> int:
        n1 = 1
        n2 = 0
        if int(s[-1]) > 0:
            n2 = 1

        if len(s) == 1:
            return n2

        for i in range(len(s) - 2, -1, -1):
            num_big = int(s[i:i + 2])
            num_small = int(s[i])

            tmp = 0
            if num_small > 0:
                tmp = n2
                if 10 <= num_big <= 26:
                    tmp += n1
            
            n1 = n2
            n2 = tmp
        
        return n2
