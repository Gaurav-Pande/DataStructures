# https://leetcode.com/problems/k-diff-pairs-in-an-array

class Solution(object):
	def findPairs(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""
		# [ 3,1,4,1, 5 ]
		import collections
		a = collections.Counter(nums)
		result = 0
		for c in a:
			if c + k in a and k > 0:
				result += 1
			if k == 0 and a[c] > 1:
				result += 1
		return result
	# return len(b)

