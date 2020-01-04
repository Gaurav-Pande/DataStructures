# https://leetcode.com/problems/min-cost-climbing-stairs/

# DP solution
class Solution(object):
	def minCostClimbingStairs(self, cost):
		"""
		:type cost: List[int]
		:rtype: int
		"""
		dp = [0] * len(cost)
		dp[0] = cost[0]
		dp[1] = cost[1]

		for i in range(2, len(cost)):
			dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

		return min(dp[len(cost) - 1], dp[len(cost) - 2])



# Recursive solution with memoization
class Solution(object):
	def __init__(self):
		self.dic = {}

	def minCostClimbingStairs(self, cost):
		"""
		:type cost: List[int]
		:rtype: int
		"""
		return self.recursion(cost, len(cost) - 1)

	def recursion(self, cost, index):
		if index in self.dic:
			return self.dic[index]
		else:
			if index in (0, 1):
				self.dic[index] = cost[index]
				return self.dic[index]
			else:
				self.dic[index] = cost[index] + min(self.recursion(cost, index - 1), self.recursion(cost, index - 2))

				return min(self.dic[len(self.dic) - 1], self.dic[len(self.dic) - 2])
