#link: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3284/

class Solution(object):
	def isHappy(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		res = 0
		num = n
		s = set()
		while num != 1:
			num = self.square(n)
			if num in s: return False
			s.add(num)
			n = num
		return True

	def square(self, num):
		res = 0
		while num != 0:
			a = (num % 10)
			res += a * a
			num = num // 10
		return res


