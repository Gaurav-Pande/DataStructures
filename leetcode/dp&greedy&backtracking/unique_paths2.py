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



class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows, columns = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for i in range(columns)] for j in range(rows)]
        # print(dp)
        for r in range(rows):
            for c in range(columns):
                if r ==0 or c==0:
                    dp[r][c] = 1
                    
        for r in range(rows):
            for c in range(columns):
                if r==0:
                    if obstacleGrid[r][c] == 1:
                        for i in range(c,columns):
                            dp[r][i] = 0
                if c ==0:
                    if obstacleGrid[r][c] ==1:
                        for j in range(r, rows):
                            dp[j][c] = 0
        # print(dp)            
        for r in range(1,rows):
            for c in range(1,columns):
                if obstacleGrid[r][c] ==1:
                    dp[r][c]=0
                else:
                    dp[r][c] = dp[r-1][c]+dp[r][c-1]
                                     
        return dp[-1][-1]


# optimized
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        dp = [[0]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i-1>=0:
                        dp[i][j] += dp[i-1][j]
                    if j-1>=0:
                         dp[i][j] += dp[i][j-1]
        return dp[-1][-1]