# https://leetcode.com/problems/unique-paths-ii/submissions/
class Solution(object):
	def uniquePathsWithObstacles(self, obstacleGrid):
		"""
		:type obstacleGrid: List[List[int]]
		:rtype: int
		"""
		if len(obstacleGrid) == 1 and obstacleGrid[0][0] == 1:
			return 0

		cl = len(obstacleGrid[0])
		rl = len(obstacleGrid)
		dp = [[0 for x in range(cl)] for y in range(rl)]
		for i in range(cl):
			if obstacleGrid[0][i] == 1:
				for elem in dp[0][i:]:
					elem = 0
				break
			else:
				dp[0][i] = 1
		for j in range(rl):
			if obstacleGrid[j][0] == 1:
				for elem in dp[j:][0]:
					elem = 0
				break
			else:
				dp[j][0] = 1
		print(dp)
		for r in range(1, rl):
			for c in range(1, cl):
				if obstacleGrid[r][c] == 1:
					dp[r][c] = 0
				else:
					dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
		return dp[rl - 1][cl - 1]