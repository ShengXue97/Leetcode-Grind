class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        counts = defaultdict(int) # max index of the characters
        for i in range(len(s)):
            counts[s[i]] = i

        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, counts[c])
            if i == end:
                res.append(size)
                size = 0

        return res