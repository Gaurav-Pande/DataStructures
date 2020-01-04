# find number of times an array is rotated

class BinarySearch(object):
	def numberOfTimes(self,list):
		l,r = 0,len(list)-1

		while l<r:
			mid = (l+r)/2
			if list[mid] < list[mid+1]:
				r  = mid
			else:
				l = mid+1
		return l



if __name__ == '__main__':
	ob = BinarySearch()
	list = [10,15,17,1,2,3,4]
	print(ob.numberOfTimes(list))