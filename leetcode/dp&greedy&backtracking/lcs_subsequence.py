# https://leetcode.com/problems/longest-palindromic-subsequence
# print longest pallindrom subsequence in a string
# or print longest common subsequence in a string and the reverse of its string
# 

class Solution(object):
	def __init__(self):
		self.result = ""

	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		return self.lcs(s, s[::-1])

	def lcs(self, X, Y):
		result = ""
		l1 = len(X)
		l2 = len(Y)
		dp = [[0] * (l2 + 1)] * (l1w + 1)
		for i in range(l1 + 1):
			for j in range(l2 + 1):
				if i == 0 or j == 0:
					dp[i][j] = 0

				elif X[i - 1] == Y[j - 1]:
					dp[i][j] = dp[i - 1][j - 1] + 1
				else:
					dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

		i, j = l1, l2

		while i > 0 and j > 0:
			if X[i - 1] == Y[j - 1]:
				result += X[i - 1]
				i -= 1
				j -= 1
			elif dp[i - 1][j] > dp[i][j - 1]:
				i -= 1
			else:
				j -= 1

		print(dp)
		return len(result)






