# link:https://leetcode.com/problems/valid-triangle-number/submissions/


class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        nums.sort()
        for i in range(len(nums)-2):
            l,k = i+1, i+2
            
            while l<len(nums)-1 and nums[i] != 0:
                while k < len(nums) and nums[i] + nums[l] > nums[k]:
                    k+=1
                result += k-l-1
                l+=1
                    
        return result
                    
                