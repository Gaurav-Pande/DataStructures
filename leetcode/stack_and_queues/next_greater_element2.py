#link:https://leetcode.com/problems/next-greater-element-ii/submissions/

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [-1]*len(nums)
        
        for i in range(len(nums))*2:
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)
            
        return res
        