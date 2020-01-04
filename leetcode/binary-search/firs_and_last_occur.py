# find the first and last occurance of a number in  a sorted list
class BinarySearch(object):
	def firstAndLastOccurance(self,list,val):
		left = 0
		right = len(list)-1
		first = -1
		last = -1
		while left<=right:
			mid= (left+right)/2
			if list[mid] ==val:
				first = mid
				if list[mid-1] != val:
					break
				else:
					right = mid-1
			elif list[mid] >= val:
				right = mid-1
			else:
				left = mid+1
		left = 0
		right = len(list) - 1
		
		while left<=right:
			mid= (left+right)/2
			if list[mid] ==val:
				last = mid
				if list[mid+1] != val:
					break
				else:
					left = mid+1

			elif list[mid] >= val:
				right = mid-1
			else:
				left = mid+1

		return first,last


if __name__ == '__main__':
	list=[2,4,10,10,10,10,18,20]
	ob = BinarySearch()
	print(ob.firstAndLastOccurance(list,10))