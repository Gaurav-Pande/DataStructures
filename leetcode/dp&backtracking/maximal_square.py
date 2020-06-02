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

     