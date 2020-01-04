# https://leetcode.com/problems/isomorphic-strings/submissions/
class Solution(object):
	def isIsomorphic(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		if len(set(s)) == len(set(t)) == len(set(zip(s, t))):
			return True
		else:
			return False

