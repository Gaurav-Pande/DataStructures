#link: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3306/

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row, col):
#        """
#        :type row : int, col : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        r,c = binaryMatrix.dimensions()
        # print(r,c)
        ans = c
        for i in range(r):
            index = self.binarySearch(i, c, binaryMatrix)
            ans = min(ans,index)
        if ans == c:
            return -1
        else:
            return ans
        
    
    def binarySearch(self, i, c, binaryMatrix):
        start = 0
        end = c-1
        while start < end:
            mid = (start+end)//2
            # print("mid",mid)
            elem = binaryMatrix.get(i,mid)
            if elem == 0:
                start = mid+1
            else:
                end = mid
        if binaryMatrix.get(i,start) == 1:
            return start
        else:
            return c
                
    
            
                
                
                
                
                
                
                
                