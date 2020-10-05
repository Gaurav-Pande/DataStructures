# https://leetcode.com/problems/unique-paths/submissions/

# Recursion


class Solution(object):
	def uniquePaths(self, m, n):
		"""
		:type m: int
		:type n: int
		:rtype: int
		"""
		return self.dfs(1, 1, m, n)

	def dfs(self, c, r, m, n):
		if c == m or r == n:
			return 1
		else:
			return self.dfs(c+1,r,m,n) + self.dfs(c,r+1,m,n)




# Memoization
class Solution(object):
	def __init__(self):
		self.dic = {}

	def uniquePaths(self, m, n):
		"""
		:type m: int
		:type n: int
		:rtype: int
		"""
		return self.dfs(1, 1, m, n)

	def dfs(self, c, r, m, n):
		if (c, r) in self.dic:
			return self.dic[(c, r)]
		elif c == m or r == n:
			self.dic[(c, r)] = 1
			return 1
		else:
			self.dic[(c, r)] = self.dfs(c + 1, r, m, n) + self.dfs(c, r + 1, m, n)
			return self.dic[(c, r)]



# DP
class Solution(object):
	def uniquePaths(self, m, n):
		"""
		:type m: int
		:type n: int
		:rtype: int
		"""
		dp = [[0 for x in range(n)] for y in range(m)]
		# print(dp)
		for i in range(n):
			dp[0][i] = 1

		for i in range(m):
			dp[i][0] = 1

		for r in range(1, m):
			for c in range(1, n):
				# print(r,c)
				dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
		return dp[m - 1][n - 1]







