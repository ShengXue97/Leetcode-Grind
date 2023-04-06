class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1Map = Counter(s1)
        for i in range(len(s2) - len(s1) + 1):
            sub = s2[i:i + len(s1)]
            s2Map = Counter(sub)
            if s1Map == s2Map:
                return True
        
        return False