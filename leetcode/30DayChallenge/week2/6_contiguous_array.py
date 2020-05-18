# link: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3298/


class Solution(object):
	def findMaxLength(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		dic = {0: 0}
		result = 0
		count = 0
		for i, v in enumerate(nums, 1):
			# print(dic)
			if v == 0:
				count -= 1
			if v == 1:
				count += 1

			if count not in dic:
				dic[count] = i
			else:
				result = max(result, i - dic[count])

		return result




