#link: 


# link: https://leetcode.com/problems/candy-crush/submissions/

class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(board), len(board[0])
        tocrush = False
        
        for r in range(rows):
            for c in range(cols-2):
                if abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) != 0:
                    board[r][c] = board[r][c+1] = board[r][c+2] = - abs(board[r][c])
                    tocrush = True
                    
        for r in range(rows-2):
            for c in range(cols):
                if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:
                    board[r][c] = board[r+1][c] = board[r+2][c] = - abs(board[r][c])
                    tocrush = True
                    
        for c in range(cols):
            tr = rows-1
            for r in range(rows-1,-1,-1):
                if board[r][c]>0:
                    board[tr][c] = board[r][c]
                    tr-=1
                    
            for tr in range(tr, -1, -1):
                board[tr][c] = 0
                
        if tocrush:
            return self.candyCrush(board)
        else:
            return board
                    
