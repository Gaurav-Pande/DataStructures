#link:https://leetcode.com/problems/find-all-duplicates-in-an-array/


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums:
            # print(nums)
            if nums[abs(num)-1]<0:
                res.append(abs(num))
            else:
                nums[abs(num)-1] *= -1
            
        return res
                