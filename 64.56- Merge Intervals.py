class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        res = []
        curInterval = intervals[0]

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if curInterval[1] < interval[0]:
                res.append(curInterval[:])
                curInterval = interval
            else:
                curInterval = [curInterval[0], max(curInterval[1], interval[1])]
        
        res.append(curInterval)
        return res