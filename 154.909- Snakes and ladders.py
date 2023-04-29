class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()
        visited = set()
        q = deque()
        q.append((1, 0)) # index, moves
        N = len(board)
        def posToInt(pos):
            r = (pos - 1) // N
            quotient = (pos - 1) % N
            c = 0
            if r % 2 == 0:
                c = quotient
            else:
                c = N - quotient - 1
            
            return r, c

        while q:
            index, moves = q.popleft()
            for i in range(1, 7):
                nextPos = index + i
                r, c = posToInt(nextPos)
                if nextPos in visited:
                    continue
                visited.add(nextPos)
                if board[r][c] != -1:
                    nextPos = board[r][c]
                
                if nextPos == N * N:
                    return moves + 1
                q.append((nextPos, moves + 1))
        
        return -1