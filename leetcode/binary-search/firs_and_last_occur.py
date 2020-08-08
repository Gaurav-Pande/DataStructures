# find the first and last occurance of a number in  a sorted list
# link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
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

		
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r =0,len(nums)-1
        f,s=-1,-1
        if not nums:
            return [f,s]
        
        if nums[l]==nums[r]==target:
            return [l,r]
    
        while l <= r:
            mid = (l+r)//2
            # 8,8,8,8
            # 7,8,8,8
            # 8,8,8,9
            if nums[mid] == target:
                f = mid
                if mid == 0 or nums[mid-1]!=target :
                    break
                else:
                    r=mid-1
            elif nums[mid]>target:
                r = mid-1
            else:
                l= mid+1
                
        l,r = 0,len(nums)-1
        
        while l<=r:
            mid =(l+r)//2
            if nums[mid]==target:
                s=mid
                if  mid == len(nums)-1 or nums[mid+1]!=target:
                    break
                else:
                    l = mid+1
            elif nums[mid]<target:
                l=mid+1
            else:
                r = mid-1
                
                
                
                
            
            
            
        return [f,s]
            
            
        
        
        


if __name__ == '__main__':
	list=[2,4,10,10,10,10,18,20]
	ob = BinarySearch()
	print(ob.firstAndLastOccurance(list,10))