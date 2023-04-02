class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.backtrack(board, i, j, word):
                    return True
        return False
        
        
    
    def backtrack(self, board, i, j, word):
        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        
        board[i][j] = "#"
        res = self.backtrack(board, i+1,j,word[1:]) or self.backtrack(board, i-1,j,word[1:])\
            or self.backtrack(board, i,j+1,word[1:]) or self.backtrack(board, i,j-1,word[1:])
                
        board[i][j] = word[0]
        
        return res