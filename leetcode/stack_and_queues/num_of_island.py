# https://leetcode.com/problems/number-of-islands/

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        row, col = 0, 0
        col_len = len(grid[0])
        row_len = len(grid)
        result = 0
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == "1":
                    result += 1
                    self.dfs_traversal(i, j, row_len, col_len, grid)
        return result

    def bfs_traversal(self, row, col, row_len, col_len, grid):
        import collections

        q = collections.deque()
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q.append((row, col))
        while q:
            cr, cc = q.popleft()
            for m in moves:
                tr, tc = m
                nr = cr + tr
                nc = cc + tc
                if self.isvalid(nr, nc, row_len, col_len) and grid[nr][nc] == '1':
                    q.append((nr, nc))
                    grid[nr][nc] = '0'

    def isvalid(self, row, col, row_len, col_len):
        if row >= row_len or row < 0 or col >= col_len or col < 0:
            return False
        else:
            return True

    def dfs_traversal(self, row, col, row_len, col_len, grid):
        if self.isvalid(row, col, row_len, col_len) and grid[row][col] == '1':
            grid[row][col] = '0'
            self.dfs_traversal(row + 1, col, row_len, col_len, grid)
            self.dfs_traversal(row, col + 1, row_len, col_len, grid)
            self.dfs_traversal(row - 1, col, row_len, col_len, grid)
            self.dfs_traversal(row, col - 1, row_len, col_len, grid)












