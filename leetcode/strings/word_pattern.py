# https://leetcode.com/problems/word-pattern/submissions/
class Solution(object):
	def wordPattern(self, pattern, str):
		"""
		:type pattern: str
		:type str: str
		:rtype: bool
		"""
		s = set()
		str = str.split(" ")
		for elem in str:
			s.add(elem)

		# print(zip(pattern,str))
		if len(set(pattern)) == len(s) == len(set(zip(pattern, str))) and len(str) == len(pattern):
			return True
		else:
			return False
