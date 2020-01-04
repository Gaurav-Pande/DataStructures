# https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution(object):
	def peakIndexInMountainArray(self, A):
		"""
		:type A: List[int]
		:rtype: int
		"""
		# Simple linear search
		# for i in range(1,len(A)-1):
		#     if A[i-1]<A[i]>A[i+1]:
		#         return i
		# return -1

		# Binary Search
		l, r = 0, len(A) - 1
		while l < r:
			mid = (l + r) / 2
			if A[mid] < A[mid + 1]:
				l = mid + 1
			else:
				r = mid

		return l






