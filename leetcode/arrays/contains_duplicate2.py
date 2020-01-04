# https://leetcode.com/problems/contains-duplicate-ii/

class Solution(object):
	def containsNearbyDuplicate(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: bool
		"""
		dic = {}
		for i, v in enumerate(nums):
			if v in dic and abs(dic[v] - i) <= k:
				return True
			else:
				dic[v] = i
		return False

