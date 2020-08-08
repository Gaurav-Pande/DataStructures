class BinarySearch(object):
	def binarySearch(self,list,val):
		l=0
		r=len(list)-1
		while l<r:
			mid = (l+r)//2
			print(list[mid])
			if list[mid]==val:
				return mid
			# if mid value is greater then the search value then we need to search on the left side
			elif list[mid] >= val:
				r = mid-1
			else:
				l = mid
		return -1

	def binarySearchRecursive(self,list,l,r,val):
		mid = (l+r)//2
		if list[mid] == val:
			return mid
		if list[mid]>= val:
			return self.binarySearchRecursive(list,l,mid-1,val)
		else:
			return self.binarySearchRecursive(list,mid+1,r,val)
		return -1

if __name__ == '__main__':
	l = [1,2,3,4,5,6,7,8,9]
	ob = BinarySearch()
	print("result:",ob.binarySearch(l,7))
	# print(ob.binarySearchRecursive(l,0,len(l)-1,4))
