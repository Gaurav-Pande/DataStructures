# link: https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)+1
        j=0
        for i in range(len(nums)):
            s-=nums[i]
            while s<=0:
                res = min(res,i-j+1)
                s+=nums[j]
                j+=1
        return res%(len(nums)+1)
        
