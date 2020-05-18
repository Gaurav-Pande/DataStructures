# link: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3285/


class Solution(object):
	def __init__(self):
		self.result = -1000

	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		# greedy solution
		# dp = [nums[0]]
		# for i in range(1,len(nums)):
		#     dp.append(max(dp[i-1]+nums[i],nums[i]))
		# return max(dp)

		return self.mergeMethod(nums, 0, len(nums) - 1)

	def mergeMethod(self, nums, first, last):
		if first == last:
			return nums[first]
		mid = (first + last) // 2
		leftsum = self.mergeMethod(nums, first, mid)
		rightsum = self.mergeMethod(nums, mid + 1, last)
		cross_sum = self.cross_sum(nums, first, last, mid)
		return max(leftsum, rightsum, cross_sum)

	def cross_sum(self, nums, first, last, mid):
		if first == last:
			return nums[first]

		left_subsum = float('-inf')
		curr_sum = 0
		for i in range(mid, first - 1, -1):
			curr_sum += nums[i]
			left_subsum = max(left_subsum, curr_sum)

		right_subsum = float('-inf')
		curr_sum = 0
		for i in range(mid + 1, last + 1):
			curr_sum += nums[i]
			right_subsum = max(right_subsum, curr_sum)

		return left_subsum + right_subsum

	# first = 0
	# last = len(nums)-1
	# res = 0
	# nums = sorted(nums)
	# self.recursion(first,last,nums)
	# return self.result

# def recursion(self,first,last,nums):
#     print(first,last,nums[first:last])
#     if first>=last-1:
#         return nums[first]
#     else:
#         curr = sum(nums[first:last+1])
#         if curr > self.result:
#             self.result = curr
#         self.recursion(first+1,last, nums)
#         self.recursion(first, last-1, nums)





