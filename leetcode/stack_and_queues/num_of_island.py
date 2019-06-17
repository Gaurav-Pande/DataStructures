# https://leetcode.com/problems/number-of-islands/

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        result = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    result += 1
                    self.bfs_search(grid, i, j)
        return result

    def bfs_search(self, grid, row, col):
        import collections
        q = collections.deque()
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q.append((row, col))
        while q:
            cr, cc = q.popleft()
            for elem in d:
                r, c = elem
                nr, nc = r + cr, c + cc
                if self.isvalid(grid, nr, nc):
                    if grid[nr][nc] == "1":
                        q.append((nr, nc))
                        grid[nr][nc] = "0"

    def isvalid(self, grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return False
        return True





