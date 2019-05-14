#https://leetcode.com/problems/3sum-closest/

import sys

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        nums = sorted(nums)
        dic ={}
        print(nums)
        for i in range(0,len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                s = nums[i]+nums[l]+nums[r]
                print(nums[i],nums[l],nums[r])
                if s-target<0:
                    dic[s-target]=s
                    l+=1
                elif s-target>0:
                    r-=1
                    dic[s-target]=s
                else:
                    return s
                    l+=1
                    r-=1
        # below code to get the closest number to 0
        zero_left = -sys.maxint-1
        zero_right = sys.maxint
        for k in dic.keys():
            if k < 0:
                zero_left = max(zero_left,k)
            else:
                zero_right = min(zero_right,k)
        if 0-zero_left > zero_right:
            final_key = zero_right
        else:
            final_key = zero_left
        return dic[final_key]