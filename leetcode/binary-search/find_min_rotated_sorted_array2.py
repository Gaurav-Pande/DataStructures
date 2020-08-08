# link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # this is the similar question to number of times an array is rotated
        
        # l,r = 0, len(nums)-1
        
        l,r = 0,len(nums)-1

        while l<r:
            pivot = (l+r)//2
            # case1: nums[pivot] < nums[r]
            if nums[pivot]<nums[r]:
                r = pivot
            elif nums[pivot]>nums[r]:
                l = pivot+1
            else:
                r-=1
        return nums[l]
        


class Solution:
    def findMin(self, nums: List[int]) -> int:    
        low = 0
        high = len(nums)-1
        while high > low:
            pivot = low + (high - low) // 2
            # risk of overflow: pivot = (low + high) // 2
            # Case 1):
            if nums[pivot] < nums[high]:
                high = pivot 
                # alternative: high = pivot - 1
                # too aggressive to move the `high` index,
                # it won't work for the test case of [3, 1, 3]
            # Case 2):
            elif nums[pivot] > nums[high]:
                low = pivot + 1
            # Case 3):
            else:
                high -= 1
        # the 'low' and 'high' index converge to the inflection point.
        return nums[low]