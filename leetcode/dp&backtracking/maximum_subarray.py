# https://leetcode.com/problems/maximum-subarray/
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

class Solution(object):
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		# k = 0
		# m = -sys.maxsize-1

		# bruteforce solution
		# for i in range(len(nums)):
		#     k += 1
		#     for j in range(len(nums)):
		#         curr_wind_sum = sum(nums[j:j+k])
		#         if m< curr_wind_sum:
		#             m = curr_wind_sum
		#         else:
		#             continue
		# return m
		# current_sum= nums[0]
		# so_far = nums[0]
		# for i in range(1,len(nums)):
		#    # print(current_sum+nums[i],nums[i])
		#     current_sum = max(current_sum+nums[i],nums[i])
		#     #print("so far",so_far,current_sum)
		#     so_far = max(so_far,current_sum)
		# return so_far

		dp = []
		dp.append(nums[0])
		for i in range(1, len(nums)):
			# print(i,dp&backtracking)
			dp.append(max(dp[i - 1] + nums[i], nums[i]))

		# print(dp&backtracking)
		return max(dp)

