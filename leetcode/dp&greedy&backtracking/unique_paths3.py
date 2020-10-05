#link: https://leetcode.com/problems/unique-paths-iii


class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        A = grid
        self.res = 0
        m, n, empty = len(A), len(A[0]), 1
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    x, y = (i, j)
                elif A[i][j] == 0:
                    empty += 1

        def dfs(x, y, empty):
            if not (0 <= x < m and 0 <= y < n and A[x][y] >= 0): return
            if A[x][y] == 2:
                self.res += empty == 0
                return
            A[x][y] = -2
            dfs(x + 1, y, empty - 1)
            dfs(x - 1, y, empty - 1)
            dfs(x, y + 1, empty - 1)
            dfs(x, y - 1, empty - 1)
            A[x][y] = 0
        dfs(x, y, empty)
        return self.res
        