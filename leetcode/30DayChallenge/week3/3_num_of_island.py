#link: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3302/

class Solution(object):
	def numIslands(self, grid):
		"""
		:type grid: List[List[str]]
		:rtype: int
		"""
		if not grid:
			return 0
		rows = len(grid)
		cols = len(grid[0])
		result = 0
		for r in range(rows):
			for c in range(cols):
				if grid[r][c] == '1':
					result += 1
					self.dfs(grid, r, c, rows, cols)
		return result

	def dfs(self, grid, r, c, rows, cols):
		if self.isValid(r, c, rows, cols, grid) and grid[r][c] == '1':
			grid[r][c] = '0'
			self.dfs(grid, r + 1, c, rows, cols)
			self.dfs(grid, r, c + 1, rows, cols)
			self.dfs(grid, r - 1, c, rows, cols)
			self.dfs(grid, r, c - 1, rows, cols)

	def isValid(self, r, c, rows, cols, grid):
		if r >= rows or c >= cols or r < 0 or c < 0:
			return False
		else:
			return True

