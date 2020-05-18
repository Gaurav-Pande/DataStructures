# link: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3286/


class Solution(object):
	def moveZeroes(self, nums):
		"""
		:type nums: List[int]
		:rtype: None Do not return anything, modify nums in-place instead.
		"""

		## hint: 2 pointer solution.
		# one pointer to track the array and another to track the non zero elements
		
		i, j = 0, 0
		while j <= len(nums) - 1:
			if nums[j] != 0:
				nums[i] = nums[j]
				j += 1
				i += 1
			else:
				j += 1
		while i < len(nums):
			nums[i] = 0
			i += 1

		return None