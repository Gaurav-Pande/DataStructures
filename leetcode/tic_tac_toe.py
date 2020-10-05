#link: https://leetcode.com/problems/design-tic-tac-toe/submissions/



"""
Initially, I had not read the Hint in the question and came up with an O(n) solution. After reading the extremely helpful hint; a much easier approach became apparent. The key observation is that in order to win Tic-Tac-Toe you must have the entire row or column. Thus, we don't need to keep track of an entire n^2 board. We only need to keep a count for each row and column. If at any time a row or column matches the size of the board then that player has won.

To keep track of which player, I add one for Player1 and -1 for Player2. There are two additional variables to keep track of the count of the diagonals. Each time a player places a piece we just need to check the count of that row, column, diagonal and anti-diagonal.

Also see a very similar answer that I believe had beaten me to the punch. We came up with our solutions independently but they are very similar in principle.
"""
class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.rows = [0]*n
        self.cols = [0]*n
        self.diag = 0
        self.anti_diag =0
        self.n = n
        

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        toadd =None
        if player == 1:
            toadd = 1
        else:
            toadd = -1
        self.rows[row] += toadd
        self.cols[col] += toadd
        
        if row == col:
            self.diag+=toadd
            
        if row+col == self.n-1:
            self.anti_diag += toadd
            
        print(self.rows)
        print(self.cols)
        print(self.diag)
        print(self.anti_diag)
        if abs(self.rows[row]) == self.n  or abs(self.cols[col]) == self.n  or abs(self.diag) == self.n or abs(self.anti_diag) == self.n:
            return player
        
        return 0
            
        
            
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)