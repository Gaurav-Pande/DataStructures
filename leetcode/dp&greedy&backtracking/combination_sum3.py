# https://leetcode.com/problems/combination-sum-iii/

class Solution(object):
	def combinationSum3(self, k, n):
		"""
		:type k: int
		:type n: int
		:rtype: List[List[int]]
		"""
		nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		result = []
		self.backtrack(nums, n, result, [], 0, k)
		return result

	def backtrack(self, nums, remaining, result, templist, index, k):
		if remaining == 0 and len(templist) == k:
			if templist not in result:
				result.append(templist)
		else:
			for i in range(index, len(nums)):
				if remaining < 0:
					break
				if i - 1 >= index and nums[i] == nums[i - 1]:
					continue
				self.backtrack(nums, remaining - nums[i], result, templist + [nums[i]], i + 1, k)
