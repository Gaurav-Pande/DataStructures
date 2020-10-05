#link: https://leetcode.com/problems/intersection-of-two-arrays/submissions/

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1,s2 = set(nums1), set(nums2)
        
        if len(s1)<len(s2):
            return self.set_intersection(s1,s2)
        else:
            return self.set_intersection(s2,s1)
        
        
    def set_intersection(self, s1, s2):
        res = []
        for x in s1:
            if x in s2:
                res.append(x)
                
        return res
        