# link: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3291/

class Solution(object):
	def backspaceCompare(self, S, T):
		"""
		:type S: str
		:type T: str
		:rtype: bool
		"""
		result1, result2 = [], []
		for s in S:
			if s != '#':
				result1.append(s)
			elif result1:
				result1.pop()

		for t in T:
			if t != "#":
				result2.append(t)
			elif result2:
				result2.pop()
		print(result1, result2)
		return "".join(result1) == "".join(result2)
