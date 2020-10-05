#Link:https://leetcode.com/problems/next-greater-element-i/

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # use stack and dictionary
        stack= []
        dic = {}
        for num in nums2:
            while stack and stack[-1] < num:
                dic[stack.pop()] = num
            stack.append(num)
        result = []
        for num in nums1:
            if num in dic:
                result.append(dic[num])
            else:
                result.append(-1)
                
        return result