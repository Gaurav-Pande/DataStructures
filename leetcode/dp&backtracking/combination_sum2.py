#https://leetcode.com/problems/combination-sum-ii/
class Solution(object):
	def combinationSum(self, candidates, target):
		"""
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		result = []
		candidates.sort()
		self.backtrack(candidates, target, result, [], 0)
		return result

	def backtrack(self, nums, remaining, result, templist, index):
		if remaining == 0:
			if templist not in result:
				result.append(templist)
			return
		else:
			for i in range(index, len(nums)):
				# templist.append(nums[i])
				if remaining < 0:
					# no need to check we can return and look for next integer in the array
					break
				print(templist, remaining)
				self.backtrack(nums, remaining - nums[i], result, templist + [nums[i]], i+1)

