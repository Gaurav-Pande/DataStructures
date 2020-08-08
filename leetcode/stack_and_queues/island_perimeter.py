#link: https://leetcode.com/problems/island-perimeter/submissions/


"""
Go through every cell on the grid and whenever you are at cell 1 (land cell), look for surrounding (UP, RIGHT, DOWN, LEFT) cells. A land cell without any surrounding land cell will have a perimeter of 4. Subtract 1 for each surrounding land cell.

"""
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols  = len(grid), len(grid[0])
        result = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if r==0:
                        up = 0
                    else:
                        up = grid[r-1][c]
                    
                    if c ==0:
                        left = 0
                    else:
                        left = grid[r][c-1]
                        
                    if r == rows-1:
                        down =0
                    else:
                        down =grid[r+1][c]
                        
                    if c == cols-1:
                        right = 0 
                    else:
                        right = grid[r][c+1]
                    
                    result += 4-(up+down+left+right)
                    
        return result
                    
        