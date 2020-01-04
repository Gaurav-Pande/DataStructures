# https://leetcode.com/problems/longest-palindrome/
class Solution(object):
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		has = set()
		for i in range(len(s)):
			if s[i] not in has:
				has.add(s[i])
			else:
				has.remove(s[i])

		if len(has)>0:
			return len(s)-len(has)+1
		else:
			return len(s)


		