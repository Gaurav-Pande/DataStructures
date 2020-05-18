# link: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3300/

##
# TME solution
##
class Solution(object):
	def productExceptSelf(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		result = []
		for i, v in enumerate(nums):
			result.append(self.findProd(nums[0:i], nums[i + 1:]))
		return result

	def findProd(self, num1, num2):
		prod = 1
		for n in num1:
			prod *= n
		for m in num2:
			prod *= m
		return prod


##
# O(n) solution
##

class Solution(object):
	def productExceptSelf(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		l, r, result = [0] * len(nums), [0] * len(nums), [0] * len(nums)
		l[0], r[len(nums) - 1] = 1, 1
		for i in range(1, len(nums)):
			l[i] = l[i - 1] * nums[i - 1]
		for j in reversed(range(len(nums) - 1)):
			r[j] = r[j + 1] * nums[j + 1]
		# print(l)
		# print(r)
		for k in range(len(nums)):
			result[k] = l[k] * r[k]
		return result




