# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution(object):
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) == 1:
			return len(nums)
		l, r = 0, 1
		while r < len(nums):
			# print(l,r,nums[l],nums[r])
			while r < len(nums) and nums[l] == nums[r]:
				r += 1
			if r < len(nums):
				nums[l + 1] = nums[r]
			l += 1
		return len(nums[:l])

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        for num in nums:
            if i<2 or num>nums[i-1]:
                nums[i] = num
                i+=1
        return i