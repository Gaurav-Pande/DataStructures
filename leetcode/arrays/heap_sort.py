class Solution(object):
	def heapSort(self,nums):
		for i in range(len(nums)):
			self.heapify(nums,len(nums), i)  # O(Nlogn)
		for i in range(len(nums)-1,0,-1):
			nums[i],nums[0] = nums[0],nums[i]
			self.heapify(nums,i, 0) #O(N)

	def heapify(self,nums,l, i):
		largest = i
		left= 2*i+1
		right = 2*i+2
		if left < l and nums[left] > nums[largest]:
			#nums[left],nums[root]= nums[root],nums[left]
			#self.heapify(nums,left)
			largest = left

		if right < l and nums[right]>nums[largest]:
			#nums[right],nums[root]= nums[root], nums[right]
			#self.heapify(nums,right)
			largest = right

		if largest!=i:
			nums[largest],nums[i] = nums[i],nums[largest]
			self.heapify(nums,l,largest)

if __name__ == '__main__':
	ob = Solution()
	nums = [4,3,8,6,1,2,5]
	ob.heapSort(nums)
	print(nums)
