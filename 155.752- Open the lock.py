class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def getNext(c):
            if c == "0":
                return "9", "1"
            elif c == "9":
                return "8", "0"
            else:
                n = int(c)
                return str(n -1), str(n + 1)

        def getNeighbours(s):
            neighbours = []
            for i in range(4):
                for neighbour in getNext(s[i]):
                    neighbours.append(s[:i] + neighbour + s[i + 1:])
            return neighbours
        
        deadends = set(deadends)
        q = deque()
        q.append(("0000", 0)) # key, moves
        visited = set()

        while q:
            key, moves = q.popleft()
            if key in visited:
                continue
            visited.add(key)
            if key == target:
                return moves
            if key in deadends:
                continue

            for neighbour in getNeighbours(key):
                q.append((neighbour, moves + 1))
        return -1


