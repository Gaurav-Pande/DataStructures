#link: https://leetcode.com/problems/search-a-2d-matrix-ii/


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # best solution of reduced search
        if len(matrix) == 0:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        
        r,c = rows-1,0
        
        while c<cols and r >=0:
            if matrix[r][c]>target:
                r -=1
            elif matrix[r][c]<target:
                c +=1
            else:
                return True
            
        return False



class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # best solution of reduced search
        if len(matrix) == 0:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        
        for i in range(min(rows,cols)):
            vertical = self.bin(matrix,target,i,True)
            horizontal = self.bin(matrix, target, i, False)
            if vertical or horizontal:
                return True
            
        return False
    
    def bin(self, matrix, target, start, isvertical):
        l = start
        if isvertical:
            r = len(matrix[0])-1
        else:
            r = len(matrix)-1
            
        while l<=r:
            mid =(l+r)//2
            if isvertical:
                if matrix[start][mid] < target:
                    l = mid+1
                elif matrix[start][mid] > target:
                    r = mid-1
                else:
                    return True
            else:
                if matrix[mid][start] < target:
                    l = mid+1
                elif matrix[mid][start] > target:
                    r = mid-1
                else:
                    return True
        return False