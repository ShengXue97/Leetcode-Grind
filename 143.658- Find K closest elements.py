class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = deque()
        l, r = 0, len(arr) - 1
        # num <= x? TTTTFFF Find last T
        while True:
            m = l + (r - l + 1) // 2
            if arr[m] <= x:
                l = m
            else:
                r = m - 1
            
            if l >= r:
                break
        prev = l
        
        if prev == -1:
            return arr[:k]
        elif prev == len(arr) - 1:
            return arr[len(arr) - k:]
        
        l, r = prev, prev
        if r < len(arr) - 1:
            r += 1

        while l >= 0 or r <= len(arr) - 1:
            if k == 0:
                break
            if l < 0:
                res.append(arr[r])
                r += 1
            elif r >= len(arr):
                res.appendleft(arr[l])
                l -= 1
            elif abs(arr[l] - x) <= abs(arr[r] - x):
                res.appendleft(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1
            k -= 1
        
        return res

