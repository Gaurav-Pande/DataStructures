#link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r = 0, len(nums)-1
        
        while l<r:
            pivot = (l+r)//2
            if nums[pivot]<nums[r]:
                r=pivot
            elif nums[pivot]>nums[r]:
                l =pivot+1
        
        
        return nums[l]
