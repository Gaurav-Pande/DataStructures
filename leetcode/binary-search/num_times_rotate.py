#link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/solution/
# find number of times an array is rotated

class BinarySearch(object):
	def numberOfTimes(self,list):
		l,r = 0,len(list)-1

		while l<r:
			mid = (l+r)/2
			if list[mid] < list[r]:
				r  = mid
			else:
				l = mid+1
		return l

		# while l<r:
		# 	mid = (l+r)/2
		# 	if list[mid-1] < list[mid]:
		# 		l = mid+1
		# 	else:
		# 		r = mid
		#
		# return l


if __name__ == '__main__':
	ob = BinarySearch()
	list = [10,15,17,19,2,3,4]
	# [2,3,4,10,15,17,19]
	print(ob.numberOfTimes(list))