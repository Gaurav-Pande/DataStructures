# link:


#########
# Approach1: find rotation index using BS and using BS search on left and
# right part of rotation index
#
########
class Solution(object):
	def search(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		if len(nums) == 0:
			return -1
		if len(nums) == 1:
			return 0 if nums[0] == target else -1
		rotation_index = self.finRotationIndex(nums, 0, len(nums) - 1)
		if nums[rotation_index] == target: return rotation_index

		if rotation_index == 0:
			return self.binarySearch(nums, 0, len(nums) - 1, target)

		if target < nums[0]:
			return self.binarySearch(nums, rotation_index, len(nums) - 1, target)

		return self.binarySearch(nums, 0, rotation_index, target)

	def finRotationIndex(self, nums, left, right):
		if nums[left] < nums[right]:
			return 0
		while left <= right:
			mid = (left + right) // 2
			if nums[mid] > nums[mid + 1]:
				return mid + 1
			else:
				if nums[mid] < nums[left]:
					right = mid - 1
				else:
					left = mid + 1

	def binarySearch(self, nums, left, right, target):
		# print(nums)
		while left <= right:
			mid = (left + right) // 2
			# print(mid)
			if nums[mid] == target:
				return mid
			else:
				if nums[mid] < target:
					left = mid + 1
				else:
					right = mid - 1
		return -1



#####
# Approach2: In single pass BS
#
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) -1
        
        while start <= end:
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:
                if target < nums[mid] and target >= nums[start]:
                    end = mid-1
                else:
                    start = mid+1
            else:
                if target > nums[mid] and target <= nums[end]:
                    start = mid+1
                else:
                    end=mid-1
        return -1
           
#
####