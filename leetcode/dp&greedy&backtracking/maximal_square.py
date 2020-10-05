# link: https://leetcode.com/problems/maximal-square/


# Backtracking Solution
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row = len(matrix)
        if row >0:
            col = len(matrix[0])
        else:
            col= 0
        res = 0
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == '1':
                    side =1
                    flag = True
                    while side+r<row and side+c<col and flag:
                        for k in range(r,side+r+1):
                            if matrix[k][c+side]=='0':
                                flag = False
                                break
                        for k in range(c, side+c+1):
                            if matrix[r+side][k] == '0':
                                flag = False
                                break
                        if flag:
                            side+=1
                            
                    res = max(res,side)
                    
        return res*res
        
     # Dp SOlution


"""
To appy DP, we define the state as the maximal size (square = size * size) of the square that can be formed till point (i, j), denoted as dp[i][j].

For the topmost row (i = 0) and the leftmost column (j = 0), we have dp[i][j] = matrix[i][j] - '0', meaning that it can at most form a square of size 1 when the matrix has a '1' in that cell.

When i > 0 and j > 0, if matrix[i][j] = '0', then dp[i][j] = 0 since no square will be able to contain the '0' at that cell. If matrix[i][j] = '1', we will have dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1, which means that the square will be limited by its left, upper and upper-left neighbors. 
"""
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        maxlen = 0
        rows = len(matrix)
        if rows>0:
            cols = len(matrix[0])
        else:
            cols = 0
        dp = [[0]*(cols+1) for _ in range(rows+1)]

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    dp[i][j]= min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
                    maxlen = max(maxlen,dp[i][j])
        return maxlen*maxlen