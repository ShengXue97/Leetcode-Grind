class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def markSides(i, j):
            if i < 0 or i >= len(board) or\
                j < 0 or j >= len(board[0]) or\
                board[i][j] != "O":
                return
            board[i][j] = "-"
            markSides(i - 1, j)
            markSides(i + 1, j)
            markSides(i, j - 1)
            markSides(i, j + 1)
        
        # Mark the sides as "-"
        for i in range(len(board)):
            if board[i][0] == "O":
                markSides(i, 0)
            if board[i][len(board[0]) - 1] == "O":
                markSides(i, len(board[0]) - 1)
        for j in range(len(board[0])):
            if board[0][j] == "O":
                markSides(0, j)
            if board[len(board) - 1][j] == "O":
                markSides(len(board) - 1, j)

        # Set all non-sides as "X"
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
        
        # Set the sides back as "O"
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "-":
                    board[i][j] = "O"
