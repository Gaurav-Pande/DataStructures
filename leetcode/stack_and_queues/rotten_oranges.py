# link:  https://leetcode.com/problems/rotting-oranges/
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # this problem can be solved using BFS search
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        q = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh +=1
                    
        q.append((-1,-1))
        result = -1
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while q:
            cr,cc = q.popleft()
            if cr == -1:
                result +=1
                if q:
                    q.append((-1,-1))
            else:
                for mr, mc in moves:
                    nr,nc = cr + mr, cc + mc
                    if self.isvalid(grid, nr ,nc) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -=1
                        q.append((nr,nc))
                    
            
        if fresh == 0:
            return result
        else:
            return -1
        
    def isvalid(self,grid,r,c):
        rows, cols=len(grid), len(grid[0])
        if r<0 or c<0 or r>=rows or c>=cols:
            return False
        return True
        
        
            
            
        
                
