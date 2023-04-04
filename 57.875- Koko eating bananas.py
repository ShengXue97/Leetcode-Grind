class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # l0, r11, m5, h8
        # l0, r4, m2, h15
        # l3, r4, m3, h10
        # l4, r4

        # [2,2]
        # l1, r2, m1, h4
        # l2, r2, 

        # [312884470, h 312884469]
        # l1, r312884470, m

        l, r = 1, max(piles)

        while l < r:
            hours = 0
            mid = l + ((r - l) // 2)
            for pile in piles:
                hours += math.ceil(pile / mid)
            
            if hours <= h:
                r = mid
            else:
                l = mid + 1

        return int(l)