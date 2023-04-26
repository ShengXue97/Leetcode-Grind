class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 1,2,2,3
        people.sort()
        l = 0
        r = len(people) - 1
        res = 0

        while l < r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            res += 1
        
        if l == r:
            res += 1
        return res