class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # 1,2,3,4,5,6
        # 4
        # T,T,T,T,F,F
        # Binary search
        res, arr = "", self.map.get(key, [])
        
        l, r = 0, len(arr) - 1
        while l <= r:
            m = l + (r - l) // 2
            if arr[m][0] <= timestamp:
                res = arr[m][1]
                l = m + 1
            else:
                r = m - 1
        
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)