# https://leetcode.com/problems/contains-duplicate/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        b = set(nums)
        if len(b) < len(nums):
			return True
        else:
			return False
