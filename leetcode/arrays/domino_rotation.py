# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

class Solution(object):
	def minDominoRotations(self, A, B):
		"""
		:type A: List[int]
		:type B: List[int]
		:rtype: int
		"""
		for x in range(1, 7):
			if all(x == a or x == b for a, b in zip(A, B)):
				count_a = A.count(x)
				count_b = B.count(x)
				dif_a = len(A) - count_a
				dif_b = len(B) - count_b
				return min(dif_a, dif_b)
		return -1

