# link:
# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3303/

class Solution(object):
	def minPathSum(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		# TLE solution
		return self.recursion(0, 0, grid)

	def recursion(self, r, c, grid):
		if r == len(grid) or c == len(grid[0]):
			return 100000
		if r == len(grid) - 1 and c == len(grid[0]) - 1:
			# when reached last cell, return that grid value and from there build the stack.
			return grid[r][c]
		return grid[r][c] + min(self.recursion(r + 1, c, grid), self.recursion(r, c + 1, grid))



####
##
## DP solution much simpler
####

class Solution(object):
	def minPathSum(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		# TLE solution
		rows = len(grid)
		cols = len(grid[0])
		dp = grid

		for r in reversed(range(rows)):
			for c in reversed(range(cols)):
				# print(r,c)
				if r == rows - 1 and c != cols - 1:
					dp[r][c] = grid[r][c] + dp[r][c + 1]
				elif r != rows - 1 and c == cols - 1:
					dp[r][c] = grid[r][c] + dp[r + 1][c]
				elif r != rows - 1 and c != cols - 1:
					dp[r][c] = grid[r][c] + min(dp[r + 1][c], dp[r][c + 1])
				else:
					dp[r][c] = grid[r][c]
			# print(dp)

		# print(dp)
		return dp[0][0]