#  link: https://leetcode.com/problems/max-area-of-island/

class Solution(object):
    def __init__(self):
        self.max_area = 0
        self.curr_area = 0
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        rows,cols = len(grid), len(grid[0]) 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    self.curr_area = 0 
                    self.dfs(grid, r, c, rows, cols)
                    # print(curr_area)
        return self.max_area
    
    def isValid(self, i, j, rows, cols):
        if i<0 or j<0 or i>=rows or j>=cols:
            return False
        return True
    
    def dfs(self, grid, r, c , rows, cols):
        if self.isValid(r, c, rows, cols) and grid[r][c]==1:
            grid[r][c]=0
            self.curr_area += 1
            self.dfs(grid, r+1, c, rows, cols)
            self.dfs(grid, r-1, c, rows, cols )
            self.dfs(grid, r, c+1, rows, cols )
            self.dfs(grid, r, c-1, rows, cols)
        # print(self.curr_area)
        self.max_area = max(self.curr_area, self.max_area)
