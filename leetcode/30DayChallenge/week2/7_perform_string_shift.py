# link:https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3299/

class Solution(object):
	def stringShift(self, s, shift):
		"""
		:type s: str
		:type shift: List[List[int]]
		:rtype: str
		"""
		final_times = 0
		final_direction = -1
		for sh in shift:
			# print(s)
			direction, times = sh
			times = times % len(s)
			if direction == 0:
				# left shift
				# print(s[times:],s[0:times])
				s = s[times:] + s[0:times]
			if direction == 1:
				# print(s[len(s)-times:],s[0:times])
				s = s[len(s) - times:] + s[0:len(s) - times]

		return s

