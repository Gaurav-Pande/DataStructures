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




	######
	##
	## Below is based on mergesort strategy
	##
	#####
	# def maxSubArray(self, nums):
	# 	"""
	# 	:type nums: List[int]
	# 	:rtype: int
	# 	"""
	# 	# greedy solution
	# 	# dp = [nums[0]]
	# 	# for i in range(1,len(nums)):
	# 	#     dp.append(max(dp[i-1]+nums[i],nums[i]))
	# 	# return max(dp)
	#
	# 	return self.mergeMethod(nums, 0, len(nums) - 1)

	# def mergeMethod(self, nums, first, last):
	# 	if first == last:
	# 		return nums[first]
	# 	mid = (first + last) // 2
	# 	leftsum = self.mergeMethod(nums, first, mid)
	# 	rightsum = self.mergeMethod(nums, mid + 1, last)
	# 	cross_sum = self.cross_sum(nums, first, last, mid)
	# 	return max(leftsum, rightsum, cross_sum)
	#
	# def cross_sum(self, nums, first, last, mid):
	# 	if first == last:
	# 		return nums[first]
	#
	# 	left_subsum = float('-inf')
	# 	curr_sum = 0
	# 	for i in range(mid, first - 1, -1):
	# 		curr_sum += nums[i]
	# 		left_subsum = max(left_subsum, curr_sum)
	#
	# 	right_subsum = float('-inf')
	# 	curr_sum = 0
	# 	for i in range(mid + 1, last + 1):
	# 		curr_sum += nums[i]
	# 		right_subsum = max(right_subsum, curr_sum)
	#
	# 	return left_subsum + right_subsum




#####
#####
#####

# Below solution finds maximum possible sum in a array.
# Note that it is not contiguous

	# def maxSubArray(self, nums):
	# 	"""
	# 	:type nums: List[int]
	# 	:rtype: int
	# 	"""
	# 	first = 0
	# 	last = len(nums) - 1
	# 	res = 0
	# 	nums = sorted(nums)
	# 	self.recursion(first, last, nums)
	# 	return self.result

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

#####
#####
#####