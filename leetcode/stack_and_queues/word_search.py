# link: https://leetcode.com/problems/word-search/


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows,cols = len(board), len(board[0])
        
        for r in range(rows):
            for c in range(cols):
                if self.backtrack(r, c, word, board):
                    return True
                
        return False
    
    
    
    def isvalid(self,r,c,board):
        rows, cols = len(board), len(board[0])
        if r< 0 or r>= rows or c<0 or c>=cols:
            return False
        return True
    
    def backtrack(self, r, c, word, board):
        if len(word) == 0:
            return True
        if self.isvalid(r,c,board) and board[r][c] == word[0]:
            board[r][c]= '#'
            res =  self.backtrack(r+1, c, word[1:], board)  or self.backtrack(r-1, c, word[1:], board) or self.backtrack(r, c+1, word[1:], board) or self.backtrack(r, c-1, word[1:], board)
            board[r][c] = word[0]
            return res
            
    
            
            
        
        
    
        
        
    
