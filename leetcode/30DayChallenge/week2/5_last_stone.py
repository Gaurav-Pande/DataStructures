# link: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3297/

class Solution(object):
	def lastStoneWeight(self, stones):
		"""
		:type stones: List[int]
		:rtype: int
		"""
		if len(stones) == 1:
			return stones[0]
		if len(stones) == 2:
			stones = sorted(stones)
			return stones[1] - stones[0]
		nums = sorted(stones)
		while len(nums) != 1 or len(nums) != 2:
			# print(nums)
			s1 = nums.pop()
			s2 = nums.pop()
			# print(s2,s1)
			if s1 - s2 != 0:
				nums.append(s1 - s2)
				nums = sorted(nums)
			if len(nums) == 2 or len(nums) == 1:
				break
		# print(nums)
		if len(nums) == 1:
			return nums[0]
		else:
			return nums[1] - nums[0]
	#####
	##  using heap
	##
	####

	# def lastStoneWeight(self, stones):
	# 	"""
	# 	:type stones: List[int]
	# 	:rtype: int
	# 	"""
	# 	# min heap implementation using the python inbuilt library
	# 	for i in range(len(stones)):
	# 		stones[i] *= -1
	#
	# 	# heapify the list
	# 	heapq.heapify(stones)
	# 	while len(stones) > 1:
	# 		s1 = heapq.heappop(stones)
	# 		s2 = heapq.heappop(stones)
	# 		if s1 - s2 != 0:
	# 			heapq.heappush(stones, s1 - s2)
	#
	# 	if stones:
	# 		return -heapq.heappop(stones)
	# 	else:
	# 		return 0
# def binSearch(x, nums):
#     first = 0
#     last = len(nums)-1
#     while first < last:
#         mid = (first+last)//2
#         if x > nums[mid] and x < nums[mid+1]:
#             return mid
#         elif x <.nums[mid]:
#             last = mid-1
#         else:
#             first = mid+1
