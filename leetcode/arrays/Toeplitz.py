# Author: Gaurav Pande
#(766. Toeplitz Matrix)[https://leetcode.com/problems/toeplitz-matrix/description/]

class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        return all(r == 0 or c == 0 or matrix[r-1][c-1]== val
               for r, id in enumerate(matrix)
               for c, val in enumerate(id))
