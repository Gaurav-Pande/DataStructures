#link: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3301/
####
## it is a greedy approach. See the solution in the leetcode to understand it.
##
#####
class Solution(object):
	def checkValidString(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		cmin, cmax = 0, 0
		for c in s:
			if c == '(':
				cmin += 1
				cmax += 1
			if c == ')':
				cmax -= 1
				cmin = max(cmin - 1, 0)
			if c == '*':
				cmax += 1
				cmin = max(cmin - 1, 0)
			if cmax < 0:
				return False
		return cmin == 0
