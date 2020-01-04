# https://leetcode.com/problems/split-array-largest-sum/
# backtracking
class Solution(object):
	def splitArray(self, nums, m):
		"""
		:type nums: List[int]
		:type m: int
		:rtype: int
		"""
		if not nums:
			return 0
		if m == 1:
			return sum(nums)
		else:
			result = sys.maxsize
			for i in range(len(nums)):
				left, right = sum(nums[:i]), self.splitArray(nums[i:], m - 1)
				curr_max = max(left, right)
				result = min(result, curr_max)
			return result

# memoization
import collections
class Solution(object):
	def __init__(self):
		self.dic = collections.defaultdict()

	def splitArray(self, nums, m):
		"""
		:type nums: List[int]
		:type m: int
		:rtype: int
		"""
		return self.helper(0, nums, m)

	def helper(self, i, nums, m):
		if not nums:
			return 0
		if m == 1:
			return sum(nums[i:])
		else:
			if (i, m) in self.dic.keys():
				return self.dic[(i, m)]
			else:
				result = sys.maxsize
				for j in range(len(nums)):

					left, right = sum(nums[i:i + j]), self.helper(j + i, nums, m - 1)
					curr_max = max(left, right)
					result = min(result, curr_max)
					self.dic[(i, m)] = result
					if left > right:
						break
				return self.dic[(i, m)]


# binary search
class Solution(object):
	def is_valid(self, nums, m, mid):
		# assume mid is < max(nums)
		cuts, curr_sum = 0, 0
		for x in nums:
			curr_sum += x
			if curr_sum > mid:
				cuts, curr_sum = cuts + 1, x
		subs = cuts + 1
		return (subs <= m)

	def splitArray(self, nums, m):
		"""
		:type nums: List[int]
		:type m: int
		:rtype: int
		"""
		low, high, ans = max(nums), sum(nums), -1
		while low <= high:
			mid = (low + high) // 2
			if self.is_valid(nums, m, mid):  # can you make at-most m sub-arrays with maximum sum atmost mid
				ans, high = mid, mid - 1
			else:
				low = mid + 1
		return ans