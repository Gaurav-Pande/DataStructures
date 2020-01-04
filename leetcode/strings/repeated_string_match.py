# https://leetcode.com/problems/repeated-string-match/
class Solution(object):
	def repeatedStringMatch(self, A, B):
		"""
		:type A: str
		:type B: str
		:rtype: int
		"""
		repeat = 0
		sr = A
		while len(A) <= 10000:
			if B in A:
				return repeat + 1
			else:
				A = A + sr
				repeat += 1

		return -1


